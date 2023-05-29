## Disciplina de SQL e Power BI

### Aula 1 - Introdução ao SQL

#### Introdução

- SQL é uma linguagem de consulta estruturada, usada para manipular dados em bancos de dados relacionais. É uma linguagem declarativa, ou seja, o usuário diz o que quer e o banco de dados faz a consulta. É padronizada e sendo assim, é possível usar em qualquer banco de dados relacional.

- O SQL é dividido em 3 partes:

  - DDL (Data Definition Language): Usada para criar e alterar estruturas de dados, como tabelas, índices, etc.

  - DML (Data Manipulation Language): Usada para manipular dados, como inserir, alterar e excluir dados.

  - DQL (Data Query Language): Usada para consultar dados, como selecionar dados de uma tabela.

- O SQL é uma linguagem não procedural, ou seja, o usuário não precisa dizer como o banco de dados deve fazer a consulta. O usuário apenas diz o que quer e o banco de dados faz a consulta.

- É uma linguagem case insensitive, ou seja, não diferencia letras maiúsculas de minúsculas.

- O SQL é uma linguagem de alto nível, ou seja, o usuário não precisa saber como o banco de dados funciona internamente para fazer consultas.

#### Exemplos de comandos em SQL

##### 1. Criar um banco de dados:

```sql
CREATE DATABASE nome_do_banco_de_dados;
```
A função `CREATE DATABASE` cria um banco de dados.

##### 2. Criar uma tabela:

```sql
CREATE TABLE nome_da_tabela (
  nome_da_coluna tipo_de_dado,
  nome_da_coluna tipo_de_dado,
  nome_da_coluna tipo_de_dado
);
```

A função `CREATE TABLE` cria uma tabela.

##### 3. Inserir dados em uma tabela:

```sql
INSERT INTO nome_da_tabela (nome_da_coluna, nome_da_coluna, nome_da_coluna)
VALUES (valor, valor, valor);
```

A função `INSERT INTO` insere dados em uma tabela.

##### 4. Selecionar dados de uma tabela:

```sql
SELECT nome_da_coluna, nome_da_coluna, nome_da_coluna
FROM nome_da_tabela;
```

A função `SELECT` seleciona dados de uma tabela.

##### 5. Alterar dados de uma tabela:

```sql
UPDATE nome_da_tabela
SET nome_da_coluna = valor, nome_da_coluna = valor, nome_da_coluna = valor
WHERE nome_da_coluna = valor;
```

A função `UPDATE` altera dados de uma tabela.

##### 6. Excluir dados de uma tabela:

```sql
DELETE FROM nome_da_tabela
WHERE nome_da_coluna = valor;
```

A função `DELETE FROM` exclui dados de uma tabela.

##### 7. Excluir uma tabela:

```sql
DROP TABLE nome_da_tabela;
```

A função `DROP TABLE` exclui uma tabela.

##### 8. Excluir um banco de dados:

```sql
DROP DATABASE nome_do_banco_de_dados;
```

A função `DROP DATABASE` exclui um banco de dados.

##### 9. Criar um índice:

```sql
CREATE INDEX nome_do_indice
ON nome_da_tabela (nome_da_coluna);
```

A função `CREATE INDEX` cria um índice.

##### 10. Criar uma visão:

```sql
CREATE VIEW nome_da_visao
AS
SELECT nome_da_coluna, nome_da_coluna, nome_da_coluna
FROM nome_da_tabela;
```

A função `CREATE VIEW` cria uma visão de uma tabela ou de uma consulta SQL.

##### 11. Criar uma função:

```sql
CREATE FUNCTION nome_da_funcao (parametro tipo_de_dado)
RETURNS tipo_de_dado
AS
BEGIN
  DECLARE variavel tipo_de_dado;
  SET variavel = valor;
  RETURN variavel;
END;
```

A função `CREATE FUNCTION` cria uma função em SQL.