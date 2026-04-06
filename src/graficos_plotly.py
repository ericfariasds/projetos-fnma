import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Lê o arquivo
df = pd.read_csv('projetos-fnma-1990-a-2024-dados-abertos-2025.csv', sep=None, engine='python')
df.columns = df.columns.str.strip()
df = df.rename(columns={df.columns[0]: 'Ano'})
df['Região Geográfica'] = df['Região Geográfica'].str.strip()

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
fig1.update_layout(
    plot_bgcolor='#f8f8f8',
    paper_bgcolor='#f8f8f8',
    coloraxis_showscale=False
)
fig1.write_html('grafico_por_ano.html')
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
    color='Projetos',
    color_continuous_scale='Teal',
    text='Projetos'
)
fig2.update_traces(textposition='outside')
fig2.update_layout(
    plot_bgcolor='#f8f8f8',
    paper_bgcolor='#f8f8f8',
    coloraxis_showscale=False,
    height=500
)
fig2.write_html('grafico_por_tema.html')
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
    color_discrete_sequence=px.colors.qualitative.Set2
)
fig3.update_traces(textposition='inside', textinfo='percent+label')
fig3.update_layout(
    paper_bgcolor='#f8f8f8'
)
fig3.write_html('grafico_por_regiao.html')
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
    marker_color='#3266ad',
    name='Ano'
), row=1, col=1)

# Painel 2 - por região (pizza)
fig4.add_trace(go.Pie(
    labels=por_regiao['Região'],
    values=por_regiao['Projetos'],
    name='Região'
), row=1, col=2)

# Painel 3 - por tema
por_tema_top = por_tema.tail(8)
fig4.add_trace(go.Bar(
    x=por_tema_top['Projetos'],
    y=por_tema_top['Tema'],
    orientation='h',
    marker_color='#1D9E75',
    name='Tema'
), row=2, col=1)

# Painel 4 - por estado
por_uf = df['UF'].value_counts().head(10).reset_index()
por_uf.columns = ['UF', 'Projetos']
fig4.add_trace(go.Bar(
    x=por_uf['UF'],
    y=por_uf['Projetos'],
    marker_color='#D85A30',
    name='Estado'
), row=2, col=2)

fig4.update_layout(
    title_text='Dashboard FNMA: Projetos 1990-2024',
    title_font_size=20,
    plot_bgcolor='#f8f8f8',
    paper_bgcolor='#f8f8f8',
    showlegend=False,
    height=800
)
fig4.write_html('dashboard.html')
print("Salvo: dashboard.html")

print("\nTodos os gráficos gerados com sucesso!")
