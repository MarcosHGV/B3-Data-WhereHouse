-- Cria a tabela principal que será particionada
CREATE TABLE DW (
    data_pregao DATE NOT NULL,
    codigo_negociacao VARCHAR(20) NOT NULL,
    nome_empresa VARCHAR(100),
    moeda_referencia VARCHAR(10),
    preco_abertura NUMERIC,
    preco_maximo NUMERIC,
    preco_minimo NUMERIC,
    preco_medio NUMERIC,
    preco_fechamento NUMERIC,
    preco_fechamento_anterior NUMERIC,
    quantidade_negocios NUMERIC,
    volume_total_dos_negocios NUMERIC
) PARTITION BY RANGE (data_pregao);

-- Cria partições para os anos 2021 e 2022
CREATE TABLE dw_2021 PARTITION OF DW
    FOR VALUES FROM ('2021-01-01') TO ('2022-01-01');

CREATE TABLE dw_2022 PARTITION OF DW
    FOR VALUES FROM ('2022-01-01') TO ('2023-01-01');

CREATE TABLE dw_2023 PARTITION OF DW
    FOR VALUES FROM ('2023-01-01') TO ('2023-12-29');

-- Cria índices nas partições
CREATE INDEX idx_codigo_de_negociacao_2021 ON dw_2021 (codigo_negociacao);
CREATE INDEX idx_data_do_pregao_2021 ON dw_2021 (data_pregao);

CREATE INDEX idx_codigo_de_negociacao_2022 ON dw_2022 (codigo_negociacao);
CREATE INDEX idx_data_do_pregao_2022 ON dw_2022 (data_pregao);

CREATE INDEX idx_codigo_de_negociacao_2023 ON dw_2023 (codigo_negociacao);
CREATE INDEX idx_data_do_pregao_2023 ON dw_2023 (data_pregao);

-- Carregar dados na tabela particionada
COPY DW FROM 'dados_limpos.csv' DELIMITER ','
CSV HEADER
ENCODING 'LATIN1';

-- Criar view para obter o preço de fechamento de cada empresa em uma data específica
CREATE VIEW fechamento_diario AS
SELECT
    data_pregao,
    codigo_negociacao,
    nome_empresa,
    preco_fechamento
FROM
    DW;

-- Criar view para obter o maior valor no ano de cada empresa
CREATE VIEW maior_valor_anual AS
SELECT
    codigo_negociacao,
    nome_empresa,
    EXTRACT(YEAR FROM data_pregao) AS ano,
    MAX(preco_maximo) AS maior_valor_no_ano
FROM
    DW
GROUP BY
    codigo_negociacao,
    nome_empresa,
    EXTRACT(YEAR FROM data_pregao);

-- Consultar as views
SELECT * FROM fechamento_diario;
SELECT * FROM maior_valor_anual;

-- Testar índices
EXPLAIN ANALYZE SELECT * FROM DW WHERE codigo_negociacao = 'PETR3';
EXPLAIN ANALYZE SELECT * FROM DW WHERE data_pregao = '2021-10-27';

-- Consulta de exemplo
SELECT data_pregao, preco_fechamento, volume_total_dos_negocios
FROM DW
WHERE codigo_negociacao = 'PETR3';

select * from dw_2021;