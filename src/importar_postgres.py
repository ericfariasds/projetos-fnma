import pandas as pd
from sqlalchemy import create_engine

# Lê o CSV
df = pd.read_csv('projetos-fnma-1990-a-2024-dados-abertos-2025.csv', sep=None, engine='python')
df.columns = df.columns.str.strip()
df = df.rename(columns={df.columns[0]: 'Ano'})
df['Região Geográfica'] = df['Região Geográfica'].str.strip()

# Renomeia colunas
df = df.rename(columns={
    'Nº do Instrumento de Repasse': 'num_instrumento',
    'Nº  Interno': 'num_interno',
    'Tema': 'tema',
    'Instituição Executora': 'instituicao',
    'Título do Projeto': 'titulo',
    'UF': 'uf',
    'Região Geográfica': 'regiao',
    'Cidade da Instituição Executora': 'cidade',
    'Bioma': 'bioma',
    'Esfera Institucional': 'esfera',
    'Data Assinatura': 'data_assinatura',
    'Data de Publicação no DOU': 'data_dou',
    'Data de Fim da Vigência': 'data_fim',
    'Recursos do FNMA (R$)': 'valor_fnma',
    'Recursos de CP (R$)': 'valor_cp',
    'Valor Total do Projeto (R$)': 'valor_total',
    'Tipo de Seleção do Projeto': 'tipo_selecao',
    'Edital ou Termo de Referência de Origem do Projeto': 'edital'
})

# Conecta ao PostgreSQL — troque 'sua_senha' pela senha que você criou
engine = create_engine('postgresql://postgres:fnma1234@localhost:5432/fnma')

# Importa os dados
df.to_sql('projetos', engine, if_exists='replace', index=False)

print(f"{len(df)} projetos importados com sucesso!")
print("Banco de dados PostgreSQL atualizado: fnma")
