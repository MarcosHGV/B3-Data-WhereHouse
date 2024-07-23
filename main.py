import pandas as pd
from tabulate import tabulate

file_path = 'D:\\B3 data\\COTAHIST_A2023.TXT'

# Especificar as larguras das colunas
colspecs = [
    (0, 2),      # Tipo de registro
    (2, 10),     # Data do pregão
    (10, 12),    # Código BDI
    (12, 24),    # Código de negociação do papel
    (24, 27),    # Tipo de mercado
    (27, 39),    # Nome da empresa
    (39, 49),    # Especificação do papel (ON/PN)
    (49, 52),    # Prazo em dias do mercado a termo
    (52, 56),    # Moeda de referência
    (56, 69),    # Preço de abertura
    (69, 82),    # Preço máximo
    (82, 95),    # Preço mínimo
    (95, 108),   # Preço médio
    (108, 121),  # Preço de fechamento
    (121, 134),  # Preço do melhor negócio do dia
    (134, 147),  # Preço de fechamento anterior
    (147, 152),  # Preço de abertura de exercício de opções de compra
    (152, 170),  # Quantidade de negócios
    (170, 188),  # Volume total dos negócios
    (188, 200),  # ISIN do ativo
]

# Nomes das colunas correspondentes
colnames = [
    'Tipo de Registro',
    'Data do Pregão',
    'Código BDI',
    'Código de Negociação',
    'Tipo de Mercado',
    'Nome da Empresa',
    'Especificação do Papel',
    'Prazo em Dias do Mercado a Termo',
    'Moeda de Referência',
    'Preço de Abertura',
    'Preço Máximo',
    'Preço Mínimo',
    'Preço Médio',
    'Preço de Fechamento',
    'Preço do Melhor Negócio do Dia',
    'Preço de Fechamento Anterior',
    'Preço de Abertura de Exercício de Opções de Compra',
    'Quantidade de Negócios',
    'Volume Total dos Negócios',
    'ISIN do Ativo'
]

# Ler o arquivo .txt com larguras fixas
df = pd.read_fwf(file_path, colspecs=colspecs, names=colnames)

# Exibir apenas a primeira linha do DataFrame de forma formatada
print(tabulate(df.head(2), headers='keys', tablefmt='pretty'))

