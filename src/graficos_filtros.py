import pandas as pd
import matplotlib.pyplot as plt

# Estilo global
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.size': 12,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.grid': True,
    'grid.alpha': 0.3,
    'grid.linestyle': '--',
    'figure.dpi': 150,
    'figure.facecolor': '#f8f8f8',
    'axes.facecolor': '#f8f8f8'
})

# Lê o arquivo
df = pd.read_csv('projetos-fnma-1990-a-2024-dados-abertos-2025.csv', sep=None, engine='python')
df.columns = df.columns.str.strip()
df = df.rename(columns={df.columns[0]: 'Ano'})
df['Região Geográfica'] = df['Região Geográfica'].str.strip()

# -----------------------------------------------
# Filtro 1 — Projetos de uma região específica
# -----------------------------------------------
regiao = 'Sul'  # ← mude aqui para explorar outras regiões
df_regiao = df[df['Região Geográfica'] == regiao]

por_ano_regiao = df_regiao.groupby('Ano').size()

fig, ax = plt.subplots(figsize=(14, 5))
ax.bar(por_ano_regiao.index, por_ano_regiao.values, color='#1D9E75', width=0.7, zorder=3)

for bar in ax.patches:
    h = bar.get_height()
    if h > 0:
        ax.text(bar.get_x() + bar.get_width()/2, h + 0.3,
                str(int(h)), ha='center', va='bottom', fontsize=8, color='#444')

ax.set_title(f'Projetos por ano — Região {regiao}', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Ano')
ax.set_ylabel('Quantidade de projetos')
ax.set_xticks(por_ano_regiao.index)
ax.set_xticklabels(por_ano_regiao.index, rotation=45, ha='right', fontsize=9)
plt.tight_layout()
plt.savefig(f'projetos_{regiao.lower()}_por_ano.png', bbox_inches='tight')
print(f"Salvo: projetos_{regiao.lower()}_por_ano.png")
plt.close()

# -----------------------------------------------
# Filtro 2 — Projetos de um período específico
# -----------------------------------------------
ano_inicio = 2000  # ← mude aqui
ano_fim = 2009     # ← mude aqui

df_periodo = df[(df['Ano'] >= ano_inicio) & (df['Ano'] <= ano_fim)]

por_tema_periodo = df_periodo['Tema'].value_counts().head(8).sort_values()

fig, ax = plt.subplots(figsize=(12, 7))
cores = ['#c6dbef','#9ecae1','#6baed6','#4292c6','#2171b5','#08519c','#08306b','#041f4a']
bars = ax.barh(por_tema_periodo.index, por_tema_periodo.values, color=cores, zorder=3)

for bar in bars:
    w = bar.get_width()
    ax.text(w + 1, bar.get_y() + bar.get_height()/2,
            str(int(w)), va='center', fontsize=10, color='#444')

ax.set_title(f'Principais temas — {ano_inicio} a {ano_fim}', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Quantidade de projetos')
ax.set_xlim(0, por_tema_periodo.max() + 30)
plt.tight_layout()
plt.savefig(f'temas_{ano_inicio}_{ano_fim}.png', bbox_inches='tight')
print(f"Salvo: temas_{ano_inicio}_{ano_fim}.png")
plt.close()

# -----------------------------------------------
# Filtro 3 — Comparar regiões lado a lado
# -----------------------------------------------
regioes = ['Norte', 'Nordeste', 'Sul', 'Sudeste', 'Centro-Oeste']
cores_regioes = ['#7F77DD', '#D85A30', '#1D9E75', '#3266ad', '#BA7517']
contagens = [len(df[df['Região Geográfica'] == r]) for r in regioes]

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(regioes, contagens, color=cores_regioes, width=0.6, zorder=3)

for bar in bars:
    h = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, h + 3,
            str(int(h)), ha='center', va='bottom', fontsize=11, fontweight='bold', color='#444')

ax.set_title('Comparação de projetos por região', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Região')
ax.set_ylabel('Total de projetos')
plt.tight_layout()
plt.savefig('comparacao_regioes.png', bbox_inches='tight')
print("Salvo: comparacao_regioes.png")
plt.close()

print("\nTodos os gráficos gerados com sucesso!")
