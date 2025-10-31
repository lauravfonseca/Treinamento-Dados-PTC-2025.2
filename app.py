import pandas as pd
import numpy as np

df = pd.read_csv('Base_Membros_Desempenho.csv', encoding='latin1')

mapa_senioridade = {
    'Jr': 'Júnior', 'JR': 'Júnior',
    'P': 'Pleno', 'pleno': 'Pleno',
    'sênior': 'Sênior', 'senior': 'Sênior',
    'N/D': np.nan
}

df['Nivel_Senioridade'] = df['Nivel_Senioridade'].replace(mapa_senioridade)

df['Nivel_Senioridade'] = df['Nivel_Senioridade'].fillna(df['Nivel_Senioridade'].mode()[0])


for coluna in ['Avaliacao_Tecnica', 'Avaliacao_Comportamental']:
    df[coluna] = (df[coluna]
                    .astype(str) #convertendo para string
                    .str.replace(',', '.')        
                    .pipe(pd.to_numeric, errors='coerce')) #convertendo para numérico
    df[coluna] = df[coluna].fillna(df[coluna].mean()).round(1)

col_eng = 'Engajamento_PIGS'
df[col_eng] = (df[col_eng]
                .astype(str)
                .str.replace('%', '', regex=False)
                .replace(['N/A', 'n/a', '-', 'NA', 'N/D', '$N/A^{\prime})$'], np.nan)
                .astype(float) / 100)

df[col_eng] = df[col_eng].fillna(df[col_eng].mean()).round(2)

df['Score_Desempenho'] = ((df['Avaliacao_Tecnica'] + df['Avaliacao_Comportamental']) / 2).round(1)

df['Status_Membro'] = np.where(
    (df['Score_Desempenho'] >= 7.0) & (df[col_eng] >= 0.8),
    'Em Destaque',
    'Padrão'
)

df.to_csv('Base_Membros_Tratada.csv', index=False, sep=';', decimal=',', encoding='utf-8-sig')
df.to_excel('Base_Membros_Tratada.xlsx', index=False)


print("Bases tratadas salvas com sucesso!")
print(df.head())