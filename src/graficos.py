import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Configuração global de estilo
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.size': 12,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.grid': True,
    'grid.alpha': 0.3,
    'grid.linestyle': '--',
    'figure.dpi': 300,
    'figure.facecolor': '#f8f8f8',
    'axes.facecolor': '#f8f8f8'
})

# Lê o arquivo
df = pd.read_csv('data/projetos-fnma-1990-a-2024-dados-abertos-2025.csv', sep=None, engine='python')
df.columns = df.columns.str.strip()
df = df.rename(columns={df.columns[0]: 'Ano'})

# -----------------------------------------------
# Gráfico 1 — Projetos por ano
# -----------------------------------------------
por_ano = df.groupby('Ano').size()

fig, ax = plt.subplots(figsize=(16, 6))

bars = ax.bar(por_ano.index, por_ano.values, color='#3266ad', width=0.7, zorder=3)

z = np.polyfit(range(len(por_ano)), por_ano.values, 3)
p = np.poly1d(z)
ax.plot(por_ano.index, p(range(len(por_ano))),
        color='#e74c3c', linewidth=2, linestyle='--', label='Tendência')
ax.legend()

# Adiciona o número em cima de cada barra
for bar in bars:
    h = bar.get_height()
    if h > 0:
        ax.text(bar.get_x() + bar.get_width()/2, h + 1.5,
                str(int(h)), ha='center', va='bottom', fontsize=8, color='#444')

ax.set_title('Projetos por ano (1990–2024)', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Ano', fontsize=12)
ax.set_ylabel('Quantidade de projetos', fontsize=12)
ax.set_xticks(por_ano.index)
ax.set_xticklabels(por_ano.index, rotation=45, ha='right', fontsize=9)

plt.tight_layout()
plt.savefig('projetos_por_ano.png', bbox_inches='tight')
print("Salvo: projetos_por_ano.png")
plt.close()

# -----------------------------------------------
# Gráfico 2 — Projetos por tema
# -----------------------------------------------
por_tema = df['Tema'].value_counts().head(8).sort_values()

CORES = ['#c6dbef','#9ecae1','#6baed6','#4292c6','#2171b5','#08519c','#08306b','#041f4a']

fig, ax = plt.subplots(figsize=(12, 7))

bars = ax.barh(por_tema.index, por_tema.values, color=CORES, zorder=3)

# Adiciona o número no final de cada barra
for bar in bars:
    w = bar.get_width()
    ax.text(w + 2, bar.get_y() + bar.get_height()/2,
            str(int(w)), va='center', fontsize=10, color='#444')

ax.set_title('Principais temas do FNMA', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Quantidade de projetos', fontsize=12)
ax.set_xlim(0, por_tema.max() + 40)

plt.tight_layout()
plt.savefig('projetos_por_tema.png', bbox_inches='tight')
print("Salvo: projetos_por_tema.png")
plt.close()

# -----------------------------------------------
# Gráfico 3 — Projetos por região
# -----------------------------------------------
por_regiao = df['Região Geográfica'].str.strip().value_counts()

CORES_REGIAO = ['#3266ad','#1D9E75','#D85A30','#7F77DD','#BA7517']

fig, ax = plt.subplots(figsize=(8, 8))

wedges, texts, autotexts = ax.pie(
    por_regiao.values,
    labels=por_regiao.index,
    autopct='%1.1f%%',
    colors=CORES_REGIAO,
    startangle=140,
    pctdistance=0.75,
    wedgeprops={'edgecolor': 'white', 'linewidth': 2}
)

# Ajusta o tamanho das fontes
for text in texts:
    text.set_fontsize(12)
for autotext in autotexts:
    autotext.set_fontsize(11)
    autotext.set_color('white')
    autotext.set_fontweight('bold')

ax.set_title('Projetos por região geográfica', fontsize=16, fontweight='bold', pad=20)

plt.tight_layout()
plt.savefig('projetos_por_regiao.png', bbox_inches='tight')
print("Salvo: projetos_por_regiao.png")
plt.close()

print("\nTodos os gráficos gerados com sucesso!")
