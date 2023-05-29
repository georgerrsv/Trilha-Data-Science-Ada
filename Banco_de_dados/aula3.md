## Disciplina de Banco de dados

### Aula 3 - Normalização 

#### Introdução

- `Normalização` é o processo de organização de um banco de dados por meio da eliminação de redundâncias e da redução de anomalias de atualização.

- `Redundância` é a repetição de dados em uma tabela.

- `Anomalias de atualização` são problemas que ocorrem quando os dados são atualizados em uma tabela, mas não em outra. Podem deixar dados inconsistentes, que são dados que não correspondem entre si, ou dados incorretos, que são dados que não correspondem à realidade.

- `Anomalias de inserção` são problemas que ocorrem quando os dados são inseridos em uma tabela, mas não em outra. Acontecem quando os dados a serem inseridos em uma tabela violam a integridade da tabela, ou quando os dados a serem inseridos em uma tabela não podem ser inseridos em outra tabela.

- `Anomalias de exclusão` são problemas que ocorrem quando os dados são excluídos de uma tabela, mas não de outra. As anomalias de exclusão podem resultar na perda de informações. Podem deixar dados órfãos, que são dados que não têm correspondência em outra tabela.

- `Dependência funcional parcial` é uma relação entre dois atributos de uma tabela em que um atributo determina outro atributo, mas não determina um conjunto de atributos.

- `Dependência funcional transitiva` é uma relação entre dois atributos de uma tabela em que um atributo determina outro atributo, que por sua vez determina um terceiro atributo.

- `Dependência funcional total` é uma relação entre dois atributos de uma tabela em que um atributo determina outro atributo e não determina nenhum outro atributo.

#### Tipos de formas normais

- `Primeira forma normal (1FN)` é uma forma normal que não permite a existência de atributos multivalorados, de atributos compostos e de atributos que dependem de outros atributos. Nessa forma também não podem haver aninhamentos de tabelas.

- `Segunda forma normal (2FN)` é uma forma normal que não permite a existência de dependências funcionais parciais. Na 2FN, todos os atributos que não são chave, devem depender completamente da chave primária da tabela.

- `Terceira forma normal (3FN)` é uma forma normal que não permite a existência de dependências funcionais transitivas. Ou seja, todos os atributos de uma tabela devem depender apenas da chave primária da tabela e não podem ser determinados por outro atributo não chave.

- `Forma normal de Boyce-Codd (FNBC)` é uma forma normal que não permite a existência de dependências funcionais parciais. Na FNBC, todos os atributos de uma tabela devem depender de toda a chave primária da tabela. A chave primária determina todos os outros atributos da tabela. A FNBC é uma forma normal mais restritiva que a 3FN.

- `Quarta forma normal (4FN)` é uma forma normal que não permite a existência de dependências multivaloradas. Nesse modelo, as tabelas são projetadas de forma a não permitir que um conjunto de atributos determine a existêcia de outro conjunto de atributos, o que significa que as informações multivaloradas devem ser tratadas separadamente e armazenadas em outras tabelas.

- `Quinta forma normal (5FN)` é uma forma normal que não permite a existência de dependências de junção. A ideia da 5FN é evitar redundância de dados que possam surgir quando tabelas são unidas. Esse modelo visa eliminar dependências que só podem ser obtidas através de operações de junção entre tabelas. Dessa forma os dados são armazenados de forma mais eficiente e as operações de junção são realizadas apenas quando necessárias.