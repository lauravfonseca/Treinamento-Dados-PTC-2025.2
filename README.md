# Treinamento-Dados-PTC-2025.2

Desafio de tratamento de dados
Aspirante: Laura Fonseca | lvnf@cin.ufpe.br - laura.vfonseca@ufpe.br

## 📌 Descrição do Projeto

Este projeto tem como objetivo aplicar técnicas de tratamento e análise de dados para classificar membros com base em desempenho técnico, comportamental e engajamento em atividades.

## Documentação do Código

1. **Carregamento da Base**  
   Leitura da base `Base_Membros_Desempenho.csv` com codificação UTF-8.

2. **Padronização de Senioridade**  
   Mapeamento de diferentes formas de escrita para os níveis Júnior, Pleno e Sênior.

3. **Tratamento das Avaliações**  
   Conversão de notas técnicas e comportamentais para formato numérico, com preenchimento de valores ausentes.

4. **Normalização do Engajamento**  
   Conversão de porcentagens para proporções decimais e imputação de valores ausentes.

5. **Cálculo do Score de Desempenho**  
   Média entre avaliação técnica e comportamental.

6. **Classificação dos Membros**  
   Membros com Score ≥ 7.0 e Engajamento ≥ 80% são classificados como "Em Destaque"; os demais como "Padrão".

7. **Exportação das Bases Tratadas**  
   Geração dos arquivos `Base_Membros_Tratada.csv` e `Base_Membros_Tratada.xlsx`.

8. **Saída Final**  
   Impressão das 10 primeiras linhas da base tratada para conferência.


## Saídas Esperadas

- `Base_Membros_Tratada.csv`: base tratada em formato CSV.
- `Base_Membros_Tratada.xlsx`: base tratada em formato Excel.
- Impressão das 10 primeiras linhas no terminal.