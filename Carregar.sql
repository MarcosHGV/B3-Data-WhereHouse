CREATE TABLE dados(
    data_do_pregao DATE,
    codigo_de_negociacao VARCHAR(20),
    nome_da_empresa VARCHAR(100),
    moeda_de_referencia VARCHAR(10),
    preco_de_abertura NUMERIC,
    preco_maximo NUMERIC,
    preco_minimo NUMERIC,
    preco_medio NUMERIC,
    preco_de_fechamento NUMERIC,
    preco_de_fechamento_anterior NUMERIC,
    quantidade_de_negocios numeric,
    volume_total_dos_negocios NUMERIC
);

COPY dados FROM 'D:\B3 data\ETL\dados_limpos.csv' DELIMITER ','
CSV HEADER
ENCODING 'LATIN1';

select * from dados;

COPY dados FROM 'D:\B3 data\ETL\dados_limpos.csv' DELIMITER ','
CSV HEADER
ENCODING 'LATIN1';

select * from dados;