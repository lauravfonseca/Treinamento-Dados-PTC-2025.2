import pandas as pd
import numpy as np

#primeiro passo: carregar a base de dados
df = pd.read_csv('Base_Membros_Desempenho.csv', encoding='utf-8-sig')

#segundo passo: tratar os dados
mapa_senioridade = {
    'Jr': 'Júnior', 'JR': 'Júnior', 'junior': 'Júnior',
    'P': 'Pleno', 'pleno': 'Pleno',
    'sênior': 'Sênior', 'senior': 'Sênior', 'SENIOR': 'Sênior',
    'N/D': np.nan, 'ND': np.nan
}

if 'Nivel_Senioridade' in df.columns:
    df['Nivel_Senioridade'] = df['Nivel_Senioridade'].replace(mapa_senioridade)
    if df['Nivel_Senioridade'].isna().any():
        df['Nivel_Senioridade'] = df['Nivel_Senioridade'].fillna(df['Nivel_Senioridade'].mode()[0])
else:
    raise KeyError("A coluna 'Nivel_Senioridade' não foi encontrada na base de dados.")

#terceiro passo: tratar as avaliações técnica e comportamental
for coluna in ['Avaliacao_Tecnica', 'Avaliacao_Comportamental']:
    if coluna in df.columns:
        df[coluna] = (df[coluna]
                        .astype(str)
                        .str.replace(',', '.', regex=False)
                        .pipe(pd.to_numeric, errors='coerce'))
        df[coluna] = df[coluna].fillna(df[coluna].mean()).round(1)
    else:
        raise KeyError(f"A coluna '{coluna}' não foi encontrada na base.")

#quarto passo: tratar o engajamento em PIGs
col_eng = 'Engajamento_PIGs'
if col_eng in df.columns:
    df[col_eng] = (df[col_eng]
                    .astype(str)
                    .str.replace('%', '', regex=False)
                    .replace(['N/A', 'n/a', '-', 'NA', 'N/D', 'nan'], np.nan)
                    .pipe(pd.to_numeric, errors='coerce') / 100)
    df[col_eng] = df[col_eng].fillna(df[col_eng].mean()).round(2)
else:
    raise KeyError(f"A coluna '{col_eng}' não foi encontrada na base.")

#quinto passo: cálculo do score de desempenho
df['Score_Desempenho'] = ((df['Avaliacao_Tecnica'] + df['Avaliacao_Comportamental']) / 2).round(1)

#sexto passo: classificação dos membros
df['Status_Membro'] = np.where(
    (df['Score_Desempenho'] >= 7.0) & (df[col_eng] >= 0.8),
    'Em Destaque',
    'Padrão'
)

#setimo passo: salvar as bases tratadas
df.to_csv('Base_Membros_Tratada.csv', index=False, sep=';', decimal=',', encoding='utf-8-sig')
df.to_excel('Base_Membros_Tratada.xlsx', index=False, engine='openpyxl')

#oitavo passo: saidas finais
print("✅ Bases tratadas salvas com sucesso!\n")
print(df.head(10).to_string(index=False))