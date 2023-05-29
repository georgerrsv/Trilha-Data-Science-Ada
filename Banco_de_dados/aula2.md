## Disciplina de banco de dados

### Aula 2 - Modelagem de dados, modelo entidade-relacionamento, modelo relacional, definição de entidades, atributos, relacionamentos, chaves primárias e chaves estrangeiras.

#### Introdução

- `Modelagem de dados`: processo de criação de um modelo de dados para um sistema de informação por meio de um modelo de dados bem estruturado, usando notação formal que habilita a representação e a manipulação dos dados, e que permite a comunicação entre os usuários e os projetistas do sistema.

- `Modelo de dados`: é uma coleção de conceitos que podem ser usados para descrever a estrutura de um banco de dados. Um modelo de dados é constituído de três componentes: uma coleção de estruturas de dados que permite a representação de dados, um conjunto de operações que podem ser especificadas sobre essas estruturas e uma coleção de restrições que devem ser satisfeitas pelos dados.

- `Modelo de dados conceitual`: é uma descrição de alto nível de uma estrutura de dados, independente de considerações de software e hardware. O modelo conceitual deve ser fácil de entender para os usuários, que não precisam ter conhecimento de detalhes de software e hardware.

- `Modelo de dados lógico`: é uma descrição de nível intermediário, que descreve o que os dados são, e não como serão armazenados no banco de dados. O modelo lógico é independente de software e hardware, mas depende do modelo de dados conceitual.

- `Modelo de dados físico`: é uma descrição de baixo nível, que descreve como os dados são armazenados no banco de dados. O modelo físico depende do modelo de dados lógico e do software e hardware.


#### Tipos de dados

- `Dados alfanuméricos`: são dados que podem ser representados por letras do alfabeto, números e outros caracteres, como sinais de pontuação e caracteres especiais.

- `Dados numéricos`: são dados que podem ser representados por números.

- `Dados lógicos`: são dados que podem ser representados por valores lógicos, como verdadeiro e falso.

- `Dados de data e hora`: são dados que podem ser representados por datas e horas.

- `Dados de imagem`: são dados que podem ser representados por imagens.

- `Dados de áudio`: são dados que podem ser representados por sons.

- `Dados de vídeo`: são dados que podem ser representados por vídeos.

- `Dados de objetos`: são dados que podem ser representados por objetos.

#### Entidades e atributos

- `Entidade` é um objeto do mundo real que pode ser identificado por meio de seus dados. Uma entidade é representada por um conjunto de atributos.

- `Atributo` é uma propriedade ou característica de uma entidade que descreve o tipo de informação que é armazenada. Um atributo é representado por um nome e um domínio.

- Uma entidade se relaciona com outra entidade por meio de um relacionamento.

- `Relacionamento` é uma associação entre entidades. Um relacionamento é representado por um nome e um conjunto de entidades participantes.

- `Domínio` é um conjunto de valores que podem ser atribuídos a um atributo.

- `Chave primária` é um atributo ou conjunto de atributos que identifica unicamente uma entidade. A chave primária pode ser representada por um sublinhado abaixo do nome do atributo. Não podem ter valores nulos ou duplicados.

- `Chave estrangeira` é um atributo ou conjunto de atributos que identifica unicamente uma entidade em outra tabela. Chave estrangeira referencia uma chave primária de outra tabela. 

- `Chave candidata` é um atributo ou conjunto de atributos que identifica unicamente uma entidade. Uma chave candidata é uma chave primária em potencial.

#### Modelo entidade-relacionamento

- `Modelo entidade-relacionamento` é um modelo de dados conceitual que descreve a estrutura de um banco de dados por meio de um diagrama entidade-relacionamento. O modelo entidade-relacionamento é constituído de entidades, atributos e relacionamentos.

- `Cardinalidade` é o número de entidades que podem participar de um relacionamento. A cardinalidade é representada por um número mínimo e um número máximo de entidades participantes.

- `Cardinalidade mínima` é o número mínimo de entidades que podem participar de um relacionamento. A cardinalidade mínima é representada por um número inteiro maior ou igual a zero.

- `Cardinalidade máxima` é o número máximo de entidades que podem participar de um relacionamento. A cardinalidade máxima é representada por um número inteiro maior ou igual a um.

#### Modelo relacional

- `Modelo relacional` é um modelo de dados lógico que descreve a estrutura de um banco de dados por meio de um conjunto de tabelas e restrições. O modelo relacional é constituído de tabelas, atributos e restrições.

- `Tabela` é uma estrutura de dados que armazena dados em linhas e colunas. Uma tabela é representada por um nome e um conjunto de atributos.

- `Restrição` é uma condição que deve ser satisfeita pelos dados. Uma restrição é representada por um nome e uma condição.

##### Tipos de restrições

- `Restrição de domínio` é uma restrição que limita os valores que podem ser atribuídos a um atributo. A restrição de domínio é representada por um nome e um domínio.

- `Restrição de chave primária` é uma restrição que limita os valores que podem ser atribuídos a um atributo ou conjunto de atributos que identifica unicamente uma entidade. A restrição de chave primária é representada por um nome e um conjunto de atributos.

- `Restrição de integridade referencial` é uma restrição que limita os valores que podem ser atribuídos a um atributo ou conjunto de atributos que identifica unicamente uma entidade em outra tabela. A restrição de integridade referencial é representada por um nome e um conjunto de atributos.

- `Restrição de integridade` é uma restrição que limita os valores que podem ser atribuídos a um atributo ou conjunto de atributos. A restrição de integridade é representada por um nome e uma condição.