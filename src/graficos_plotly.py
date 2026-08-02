import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
from plotly.subplots import make_subplots

# Lê o arquivo
df = pd.read_csv('data/fnma_1990_2024.csv', sep=None, engine='python')
df.columns = [c.strip().replace('\ufeff', '') for c in df.columns]
df['Região Geográfica'] = df['Região Geográfica'].str.strip()

# -----------------------------------------------
# Tema visual único (identidade FNMA) - evita repetir
# cor/fonte/margem em cada gráfico separadamente
# -----------------------------------------------
pio.templates["fnma"] = go.layout.Template(
    layout=go.Layout(
        font=dict(family="Inter, -apple-system, sans-serif", size=13, color="#1a2e2a"),
        title=dict(font=dict(size=16, color="#0d2818", family="Inter, sans-serif"), x=0.5, xanchor="center"),
        colorway=["#0d3b2e", "#1f6b4f", "#3d9970", "#6fb98f", "#a3d4b5", "#d1e9d9"],
        plot_bgcolor="white",
        paper_bgcolor="white",
        margin=dict(l=40, r=30, t=60, b=40),
        xaxis=dict(showgrid=False, showline=True, linecolor="#e0e0e0"),
        yaxis=dict(showgrid=True, gridcolor="#f0f0f0", zeroline=False),
        hoverlabel=dict(bgcolor="white", font_size=12, font_family="Inter"),
    )
)
pio.templates.default = "fnma"

ALTURA_PADRAO = 380  # altura fixa para os gráficos individuais alinharem no grid do site

# paleta de verdes usada nas barras por categoria (temas, estados)
VERDES = ['#0d3b2e', '#163d29', '#1b4332', '#2d6a4f', '#40916c',
          '#52b788', '#74c69d', '#95d5b2', '#b7e4c7', '#d8f3dc']

# -----------------------------------------------
# Gráfico 1 - Projetos por ano (interativo)
# -----------------------------------------------
por_ano = df.groupby('Ano').size().reset_index(name='Projetos')
media = por_ano['Projetos'].mean()

fig1 = px.bar(
    por_ano,
    x='Ano',
    y='Projetos',
    title=f'Projetos por ano · {int(por_ano["Projetos"].sum())} projetos, 1990–2024',
    color='Projetos',
    color_continuous_scale=[[0, '#d1e9d9'], [1, '#0d3b2e']],
    text='Projetos'
)
fig1.update_traces(textposition='outside', textfont_size=10)
fig1.update_coloraxes(showscale=False)

fig1.add_hline(
    y=media,
    line_dash='dash',
    line_color='#8a8a8a',  # cinza neutro em vez de vermelho - não compete com a paleta verde
    annotation_text=f'Média: {media:.1f}',
    annotation_position='top right',
    annotation_font_color='#666'
)

fig1.update_layout(height=ALTURA_PADRAO)
fig1.update_xaxes(title_text='Ano')
fig1.update_yaxes(title_text='Número de Projetos')

fig1.write_html('docs/grafico_por_ano.html')
print("Salvo: grafico_por_ano.html")

# -----------------------------------------------
# Gráfico 2 - Temas (interativo)
# -----------------------------------------------
por_tema = df['Tema'].value_counts().reset_index()
por_tema.columns = ['Tema', 'Projetos']
por_tema = por_tema.sort_values('Projetos')

fig2 = px.bar(
    por_tema,
    x='Projetos',
    y='Tema',
    orientation='h',
    title=f'Principais temas · {por_tema.shape[0]} categorias, {int(por_tema["Projetos"].sum())} projetos',
    color='Projetos',
    color_continuous_scale=[[0, '#d1e9d9'], [1, '#0d3b2e']],
    text='Projetos'
)

fig2.update_traces(textposition='outside', textfont_size=10)
fig2.update_coloraxes(showscale=False)
fig2.update_layout(height=500, showlegend=False)
fig2.update_yaxes(title_text='')
fig2.update_xaxes(title_text='Projetos')

fig2.write_html('docs/grafico_por_tema.html')
print("Salvo: grafico_por_tema.html")

# -----------------------------------------------
# Gráfico 3 - Regiões (donut interativo)
# -----------------------------------------------
por_regiao = df['Região Geográfica'].value_counts().reset_index()
por_regiao.columns = ['Região', 'Projetos']
por_regiao = por_regiao.sort_values('Projetos', ascending=False)  # maior fatia primeiro, começando às 12h

fig3 = px.pie(
    por_regiao,
    names='Região',
    values='Projetos',
    title=f'Projetos por região geográfica · {int(por_regiao["Projetos"].sum())} projetos',
    color_discrete_sequence=['#0d3b2e', '#1f6b4f', '#3d9970', '#6fb98f', '#a3d4b5'],
    hole=0.45,
)

fig3.update_traces(
    textposition='outside',
    textinfo='percent+label',
    sort=False,
)
fig3.add_annotation(
    text=f"<b>{int(por_regiao['Projetos'].sum())}</b><br>projetos",
    x=0.5, y=0.5, showarrow=False, font=dict(size=14, color="#0d2818")
)
fig3.update_layout(height=ALTURA_PADRAO, showlegend=False)
fig3.write_html('docs/grafico_por_regiao.html')
print("Salvo: grafico_por_regiao.html")

# -----------------------------------------------
# Gráfico 4 - Dashboard com tudo junto
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
    line_color='#8a8a8a',
    annotation_text=f'Média: {media:.1f}',
    annotation_position='top right',
    annotation_font_color='#666',
    row=1, col=1
)

# Painel 2 - por região (donut)
fig4.add_trace(go.Pie(
    labels=por_regiao['Região'],
    values=por_regiao['Projetos'],
    name='Região',
    hole=0.45,
    sort=False,
    marker=dict(colors=['#0d3b2e', '#1f6b4f', '#3d9970', '#6fb98f', '#a3d4b5']),
    textinfo='percent',
), row=1, col=2)

# Painel 3 - por tema
por_tema_top = por_tema.tail(8)
fig4.add_trace(go.Bar(
    x=por_tema_top['Projetos'],
    y=por_tema_top['Tema'],
    orientation='h',
    marker_color=VERDES[:8],
    name='Tema'
), row=2, col=1)

# Painel 4 - por estado (SP destacado por ser líder isolado)
por_uf = df['UF'].value_counts().head(10).reset_index()
por_uf.columns = ['UF', 'Projetos']
cores_uf = ['#0d3b2e' if uf == por_uf.iloc[0]['UF'] else '#95d5b2' for uf in por_uf['UF']]
fig4.add_trace(go.Bar(
    x=por_uf['UF'],
    y=por_uf['Projetos'],
    marker_color=cores_uf,
    text=por_uf['Projetos'],
    textposition='outside',
    name='Estado'
), row=2, col=2)

fig4.update_layout(
    title=dict(
        text='Dashboard FNMA: Projetos 1990-2024',
        font=dict(size=20, color="#0d2818"),
        x=0.02, xanchor='left', 
        y=0.98, yanchor='top',
    ),
    showlegend=False,
    height=850,
    margin=dict(l=160, r=40, t=110, b=40),
)
fig4.update_yaxes(tickfont=dict(size=10), row=2, col=1)

fig4.write_html('docs/dashboard.html')
print("Salvo: dashboard.html")

print("\nTodos os gráficos gerados com sucesso!")