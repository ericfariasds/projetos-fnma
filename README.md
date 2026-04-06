# Análise de Projetos do FNMA (1990–2024)

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Pandas](https://img.shields.io/badge/Pandas-data%20analysis-150458)
![Plotly](https://img.shields.io/badge/Plotly-interactive-3D4DB7)
![License](https://img.shields.io/badge/license-MIT-green)
[![Dashboard](https://img.shields.io/badge/Dashboard-GitHub%20Pages-brightgreen)](https://ericfariasds.github.io/projetos-fnma/)

## 🔗 Dashboard interativo

[Clique aqui para visualizar o dashboard](https://ericfariasds.github.io/projetos-fnma/)

Projeto de análise e visualização de dados dos projetos financiados pelo **Fundo Nacional do Meio Ambiente (FNMA)** entre 1990 e 2024, desenvolvido como parte da minha jornada de aprendizado em Python e análise de dados.

---

## Sobre os dados

Os dados são públicos e disponibilizados pelo governo federal, contendo **1.495 projetos** com informações como tema, região geográfica, bioma, estado, instituição executora e valores investidos.

---

## O que esse projeto faz

- Lê e processa o arquivo CSV com pandas
- Gera gráficos estáticos com matplotlib
- Filtra os dados por região, período e tema
- Cria dashboards interativos com Plotly
- Analisa os dados em Jupyter Notebook

---

## Tecnologias utilizadas

- Python 3.12
- pandas
- matplotlib
- seaborn
- Plotly
- Jupyter Notebook
- SQLite
- Git

---

## Estrutura do projeto

```
projetos-fnma/
├── graficos.py              # gráficos estáticos com matplotlib
├── graficos_filtros.py      # filtros por região e período
├── graficos_plotly.py       # dashboard interativo com Plotly
├── importar.py              # importa o CSV para banco de dados SQLite
├── fnma.db                  # banco de dados SQLite
├── projetos-fnma-...csv     # dados originais do FNMA
└── venv/                    # ambiente virtual Python
```

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
pip install pandas matplotlib seaborn plotly jupyter
```

**4. Rode os gráficos:**
```bash
python3 graficos.py
```

**5. Abra o dashboard interativo:**
```bash
python3 graficos_plotly.py
xdg-open dashboard.html
```

**6. Abra o Jupyter Notebook:**
```bash
jupyter notebook
```

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
- Uso de ambiente virtual e gerenciamento de dependências
- Versionamento de código com Git e GitHub
- Análise exploratória de dados com Jupyter Notebook

---

## Fonte dos dados

[Dados Abertos — Ministério do Meio Ambiente](https://www.gov.br/mma/pt-br)

---

## Autor

**Eric Farias**  
GitHub: [@ericfariasds](https://github.com/ericfariasds)
