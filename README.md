# Análise de Projetos do FNMA (1990–2024)

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Pandas](https://img.shields.io/badge/Pandas-data%20analysis-150458)
![Plotly](https://img.shields.io/badge/Plotly-interactive-3D4DB7)
![SQLite](https://img.shields.io/badge/SQLite-database-003B57)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-database-336791)
![License](https://img.shields.io/badge/license-MIT-green)
[![Site](https://img.shields.io/badge/Site-GitHub%20Pages-brightgreen)](https://ericfariasds.github.io/projetos-fnma/)

## Site do projeto

[Clique aqui para visualizar](https://ericfariasds.github.io/projetos-fnma/)

Landing page editorial com contexto, metodologia e o dashboard interativo embutido.

---

Projeto de análise e visualização de dados dos projetos financiados pelo **Fundo Nacional do Meio Ambiente (FNMA)** entre 1990 e 2024, desenvolvido como parte da minha jornada de aprendizado em Python e análise de dados.

---

## O que esse projeto faz

- Lê e processa o arquivo CSV com pandas
- Gera gráficos estáticos com matplotlib
- Filtra os dados por região, período e tema
- Cria dashboards interativos com Plotly (exportados como HTML)
- Analisa os dados em Jupyter Notebook
- Importa os dados para banco relacional (SQLite ou PostgreSQL)

---

## Tecnologias utilizadas

- Python 3.12
- pandas
- matplotlib
- seaborn
- Plotly
- Jupyter Notebook
- SQLite
- PostgreSQL + SQLAlchemy
- Git

---

## Estrutura do projeto

```
projetos-fnma/
├── data/
│   └── projetos-fnma-1990-a-2024-dados-abertos-2025.csv
├── docs/                        # GitHub Pages — site público
│   ├── index.html               # Landing page (página principal)
│   ├── dashboard.html
│   ├── grafico_por_ano.html
│   ├── grafico_por_regiao.html
│   └── grafico_por_tema.html
├── notebooks/
│   └── analise_fnma.ipynb       # análise exploratória completa
├── src/
│   ├── graficos.py              # gráficos estáticos com matplotlib
│   ├── graficos_filtros.py      # filtragem por região e período
│   ├── graficos_plotly.py       # dashboard interativo com Plotly
│   ├── importar.py              # importação do CSV para SQLite
│   └── importar_postgres.py     # importação do CSV para PostgreSQL
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```
> **Nota:** o arquivo `fnma.db` não está versionado. Ele é gerado localmente ao rodar `importar.py` (no passo 4 abaixo).

---

## Como rodar o projeto

**1. Clone o repositório:**

```bash
git clone https://github.com/ericfariasds/projetos-fnma.git
cd projetos-fnma
```

**2. Crie o ambiente virtual:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Instale as dependências:**

```bash
pip install -r requirements.txt
```

**4. Importe os dados para o banco de dados:**

Escolha uma das opções abaixo conforme o banco que deseja usar:

```bash
# Opção A — SQLite (sem instalação adicional)
python3 src/importar.py

# Opção B — PostgreSQL (requer servidor PostgreSQL rodando localmente)
# Edite a connection string em src/importar_postgres.py antes de rodar
python3 src/importar_postgres.py
```

**5. Gere os gráficos:**

```bash
# Gráficos estáticos com matplotlib
python3 src/graficos.py

# Filtros por região e período
python3 src/graficos_filtros.py

# Dashboard interativo (gera dashboard.html e gráficos em docs/)
python3 src/graficos_plotly.py
```
> **Nota:** o `docs/index.html` (landing page) é editado manualmente e não é sobrescrito por esse script.

**6. Abra o Jupyter Notebook:**

```bash
jupyter notebook notebooks/analise_fnma.ipynb
```

---

## Banco de dados

O projeto suporta dois bancos relacionais para consulta dos dados via SQL:

| Script | Banco | Observação |
|---|---|---|
| `src/importar.py` | SQLite | Gera `data/fnma.db` localmente, sem configuração |
| `src/importar_postgres.py` | PostgreSQL | Requer servidor local; edite a connection string antes de rodar |

---

## Alguns insights dos dados

- **Educação Ambiental** é o tema mais financiado, com 319 projetos
- **Mata Atlântica** é o bioma com mais projetos (751), mais que Amazônia e Cerrado juntos
- O **Sudeste** lidera em número de projetos por região
- Houve um pico de atividade entre **1993 e 2006**, com retomada em 2024
- **São Paulo** é o estado com mais projetos (180)

---

## Aprendizados

Este projeto foi desenvolvido do zero como parte do meu aprendizado em:

- Leitura e manipulação de dados com pandas
- Criação de visualizações com matplotlib e Plotly
- Importação de dados para bancos relacionais (SQLite e PostgreSQL)
- Uso de ambiente virtual e gerenciamento de dependências
- Versionamento de código com Git e GitHub
- Publicação de sites com GitHub Pages
- Análise exploratória de dados com Jupyter Notebook

---

## Fonte dos dados

[Dados Abertos — Ministério do Meio Ambiente](https://www.gov.br/mma/pt-br)

---

## Autor

**Eric Farias**
GitHub: [@ericfariasds](https://github.com/ericfariasds)