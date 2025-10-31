# Treinamento-Dados-PTC-2025.2

Desafio de tratamento de dados: Aspirante - Laura Fonseca

## Documentação do código
 
1. Carregamento da Base
Primeiramente, realizei a leitura do arquivo csv que estava com os dados despadronizados

2. Padronização da Senioridade
Mapeamento de diferentes formas de escrita para os níveis de senioridade (Júnior, Pleno, Sênior).
Preenchimento de valores ausentes com a moda (valor mais frequente).

3. Tratamento das Avaliações
Conversão das colunas Avaliacao_Tecnica e Avaliacao_Comportamental para formato numérico.
Substituição de vírgulas por pontos decimais.
Imputação de valores ausentes com a média da coluna.
Arredondamento para uma casa decimal.

4. Normalização do Engajamento em PIGs
Remoção de símbolos de porcentagem e valores inválidos.
Conversão para proporção decimal (ex: 80% → 0.80).
Imputação de valores ausentes com a média da coluna.
Arredondamento para duas casas decimais.

5. Cálculo do Score de Desempenho
Média entre as avaliações técnica e comportamental.
Arredondamento para uma casa decimal.

6. Classificação dos Membros
Membros com Score_Desempenho ≥ 7.0 e Engajamento_PIGs ≥ 0.80 são classificados como "Em Destaque".
Os demais são classificados como "Padrão".

7. Exportação das Bases Tratadas
Salvamento da base tratada em dois formatos:
CSV (Base_Membros_Tratada.csv) com separador ; e decimal ,.
Excel (Base_Membros_Tratada.xlsx) com suporte ao openpyxl.

8. Saída Final
Impressão das 10 primeiras linhas da base tratada para conferência.