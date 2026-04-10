import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Lê o arquivo
df = pd.read_csv('data/projetos-fnma-1990-a-2024-dados-abertos-2025.csv', sep=None, engine='python')
df.columns = df.columns.str.strip()
df = df.rename(columns={df.columns[0]: 'Ano'})
df['Região Geográfica'] = df['Região Geográfica'].str.strip()

LAYOUT = dict(
    template='plotly_white',
    plot_bgcolor='white',
    paper_bgcolor='white',
    coloraxis_showscale=False
)

# -----------------------------------------------
# Gráfico 1 — Projetos por ano (interativo)
# -----------------------------------------------
por_ano = df.groupby('Ano').size().reset_index(name='Projetos')

fig1 = px.bar(
    por_ano,
    x='Ano',
    y='Projetos',
    title='Projetos por ano (1990–2024)',
    color='Projetos',
    color_continuous_scale='Blues',
    text='Projetos'
)
fig1.update_traces(textposition='outside')
media = por_ano['Projetos'].mean()

fig1.add_hline(
    y=media,
    line_dash='dash',
    line_color='red',
    annotation_text=f'Média: {media:.1f}',
    annotation_position='top right'
)

fig1.update_layout(**LAYOUT)

fig1.update_xaxes(title_text='Ano')
fig1.update_yaxes(title_text='Número de Projetos')

fig1.write_html('outputs/grafico_por_ano.html')
print("Salvo: grafico_por_ano.html")

# -----------------------------------------------
# Gráfico 2 — Temas (interativo)
# -----------------------------------------------
por_tema = df['Tema'].value_counts().reset_index()
por_tema.columns = ['Tema', 'Projetos']
por_tema = por_tema.sort_values('Projetos')

fig2 = px.bar(
    por_tema,
    x='Projetos',
    y='Tema',
    orientation='h',
    title='Projetos por tema',
    color='Tema',
    color_discrete_sequence=[
        '#d8f3dc','#b7e4c7','#95d5b2','#74c69d',
        '#52b788','#40916c','#2d6a4f','#1b4332',
        '#163d29','#0f2d1e','#52b788','#40916c',
        '#2d6a4f','#1b4332','#163d29','#0f2d1e'
    ],
    text='Projetos'
)

fig2.update_traces(textposition='outside')
fig2.update_layout(**LAYOUT, height=500)

fig2.write_html('outputs/grafico_por_tema.html')
print("Salvo: grafico_por_tema.html")

# -----------------------------------------------
# Gráfico 3 — Regiões (pizza interativa)
# -----------------------------------------------
por_regiao = df['Região Geográfica'].value_counts().reset_index()
por_regiao.columns = ['Região', 'Projetos']

fig3 = px.pie(
    por_regiao,
    names='Região',
    values='Projetos',
    title='Projetos por região geográfica',
    color_discrete_sequence=['#1b4332','#2d6a4f','#40916c','#52b788','#74c69d']
)

fig3.update_traces(textposition='inside', textinfo='percent+label')
fig3.update_layout(**LAYOUT)
fig3.write_html('outputs/grafico_por_regiao.html')
print("Salvo: grafico_por_regiao.html")

# -----------------------------------------------
# Gráfico 4 — Dashboard com tudo junto
# -----------------------------------------------
fig4 = make_subplots(
    rows=2, cols=2,
    subplot_titles=(
        'Projetos por ano',
        'Projetos por região',
        'Principais temas',
        'Top 10 estados'
    ),
    specs=[[{"type": "bar"}, {"type": "pie"}],
           [{"type": "bar"}, {"type": "bar"}]]
)

# Painel 1 - por ano
fig4.add_trace(go.Bar(
    x=por_ano['Ano'],
    y=por_ano['Projetos'],
    marker_color='#2d6a4f',
    name='Ano'
), row=1, col=1)

fig4.add_hline(
    y=media,
    line_dash='dash',
    line_color='red',
    annotation_text=f'Média: {media:.1f}',
    annotation_position='top right',
    row=1, col=1
)

# Painel 2 - por região (pizza)
fig4.add_trace(go.Pie(
    labels=por_regiao['Região'],
    values=por_regiao['Projetos'],
    name='Região',
    marker=dict(colors=['#1b4332','#2d6a4f','#40916c','#52b788','#74c69d'])
), row=1, col=2)

# Painel 3 - por tema
por_tema_top = por_tema.tail(8)
cores_tema = [
    '#d8f3dc','#b7e4c7','#95d5b2','#74c69d',
    '#52b788','#40916c','#2d6a4f','#1b4332'
]
fig4.add_trace(go.Bar(
    x=por_tema_top['Projetos'],
    y=por_tema_top['Tema'],
    orientation='h',
    marker_color=cores_tema,
    name='Tema'
), row=2, col=1)

# Painel 4 - por estado
por_uf = df['UF'].value_counts().head(10).reset_index()
por_uf.columns = ['UF', 'Projetos']
fig4.add_trace(go.Bar(
    x=por_uf['UF'],
    y=por_uf['Projetos'],
    marker_color='#95d5b2',
    name='Estado'
), row=2, col=2)

fig4.update_layout(
    **LAYOUT,
    title_text='Dashboard FNMA: Projetos 1990-2024',
    title_font_size=20,
    title_x=0.5,
    showlegend=False,
    height=800
)

fig4.write_html('outputs/dashboard.html')
print("Salvo: dashboard.html")

print("\nTodos os gráficos gerados com sucesso!")
