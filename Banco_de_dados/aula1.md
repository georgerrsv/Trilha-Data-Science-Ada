## Disciplina de Banco de Dados

### Aula 1 - Introdução ao banco de dados, conceitos e arquitetura

#### Introdução

- `Dados`: são fatos que podem ser gravados e que possuem um significado implícito. Os dados podem ser armazenados em diferentes tipos de mídia, como papel, fita magnética, disco magnético e memória principal.

- `Banco de dados`: é uma coleção de dados relacionados. Um banco de dados é projetado, construído e povoado com dados para um propósito específico. Tem uma variedade de aplicações diferentes e também é às vezes chamado de banco de dados orientado a objetos.

- `Sistema de gerenciamento de banco de dados (SGBD)`: é um software que permite aos usuários definir, criar e manter um banco de dados e fornece acesso controlado aos dados. O SGBD é um software de interface entre os dados e os programas de aplicação.

- `Sistema de banco de dados`: é composto por um SGBD, um conjunto de aplicativos de usuários finais e um banco de dados físico.

- `Banco de dados físico`: é um conjunto de arquivos que contém dados.

- `Banco de dados lógico`: é uma coleção de tabelas, relacionamentos ou associações, restrições e autorizações.

- Um banco de dados é chamado de `banco de dados autocontido` ou `autodescrito` porque contém uma descrição completa de seus dados. O catálogo do banco de dados contém a descrição dos dados e é chamado de `metadados`.

- `Metadados`: são informações sobre os dados. Os metadados descrevem o conteúdo e a estrutura dos dados e o modo como os dados estão armazenados no banco de dados.

- `Catálogo do banco de dados`: é uma coleção de metadados. O catálogo do banco de dados contém informações como o nome de cada tabela, o nome de cada coluna em cada tabela e os tipos de dados de cada coluna.

#### Vantagens e desvantagens do uso de banco de dados

- ##### Vantagens:

    - `Controle de redundância`: a redundância é a duplicação desnecessária de dados em um banco de dados. O controle de redundância significa que cada item de dado é armazenado apenas uma vez no banco de dados. Isso reduz a quantidade de espaço de armazenamento necessário para o banco de dados e, portanto, reduz os custos de armazenamento.

    - `Compartilhamento de dados`: o compartilhamento de dados significa que os usuários autorizados podem acessar os mesmos dados. Isso significa que os usuários não precisam criar seus próprios arquivos de dados pessoais, o que reduz a redundância e a inconsistência.

    - `Consistência dos dados`: a consistência dos dados significa que cada item de dado tem apenas um valor armazenado no banco de dados. Isso significa que todos os usuários veem os mesmos valores para os mesmos dados.

    - `Integridade dos dados`: a integridade dos dados significa que os dados atendem a certas restrições de integridade. Por exemplo, um número de telefone não pode ter menos de 10 dígitos.

    - `Segurança dos dados`: a segurança dos dados significa que o acesso aos dados é controlado. Isso significa que os usuários não autorizados não podem acessar os dados.

    - `Privacidade dos dados`: a privacidade dos dados significa que os dados pessoais são protegidos contra o acesso e uso não autorizados.

    - `Backup e recuperação`: o backup e a recuperação significam que os dados são copiados periodicamente para evitar perda de dados. Se ocorrer uma falha no sistema, os dados podem ser restaurados a partir de uma cópia de backup.

    - `Acesso simultâneo`: o acesso simultâneo significa que vários usuários podem acessar o banco de dados ao mesmo tempo. Isso significa que os usuários podem compartilhar dados e que o banco de dados pode ser usado por vários usuários simultaneamente.

    - `Acesso rápido aos dados`: o acesso rápido aos dados significa que os dados podem ser acessados rapidamente e que os usuários podem executar consultas complexas com eficiência.

- ##### Desvantagens:

    - `Complexidade do sistema de gerenciamento de banco de dados`: o sistema de gerenciamento de banco de dados é um software complexo que deve ser adquirido, instalado e administrado. Isso significa que os custos de hardware e software são maiores do que os custos de um sistema de arquivos.

    - `Custo de conversão`: os dados existentes devem ser convertidos para o novo formato. Isso significa que os custos de conversão são altos.

    - `Desempenho`: o desempenho é o tempo de resposta do sistema para uma solicitação do usuário. O desempenho é afetado pelo número de usuários, pelo tamanho do banco de dados e pela complexidade das consultas. Isso significa que o desempenho pode ser lento.

    - `Falha do sistema`: a falha do sistema significa que o sistema de gerenciamento de banco de dados pode falhar e que os dados podem ser perdidos. Isso significa que os dados podem ser perdidos.

    - `Custo de treinamento`: os usuários e administradores do sistema devem ser treinados para usar o sistema de gerenciamento de banco de dados. Isso significa que os custos de treinamento são altos.

#### Usuários de banco de dados

- `Administrador do banco de dados (DBA)`: é responsável por autorizar o acesso ao banco de dados, por coordenar e monitorar seu uso e por adquirir software e hardware. O DBA também é responsável por responder a perguntas dos usuários e por monitorar o desempenho do sistema.

- `Projetista de banco de dados`: é responsável por identificar os dados a serem armazenados no banco de dados e por escolher estruturas de armazenamento e métodos de acesso para esses dados.

- `Usuário final`: é uma pessoa que usa o banco de dados ocasionalmente ou que executa consultas simples. Os usuários finais incluem gerentes, analistas de sistemas e funcionários de escritório.

- `Programador de aplicativos`: é uma pessoa que escreve programas de aplicativos que usam o banco de dados, como programas de processamento de pedidos e programas de folha de pagamento.

#### Arquitetura de banco de dados

- `Arquitetura de três níveis`: é uma arquitetura de banco de dados que consiste em três níveis: nível externo, nível conceitual e nível interno.

- `Nível externo`: é o nível mais alto de abstração e é o nível mais próximo do usuário final. O nível externo descreve as partes do banco de dados que são relevantes para cada usuário final. O nível externo é às vezes chamado de nível de visão.

- `Nível conceitual`: é o nível intermediário de abstração e descreve o que os dados são armazenados no banco de dados e os relacionamentos entre os dados. O nível conceitual é às vezes chamado de nível de integração.

- `Nível interno`: é o nível mais baixo de abstração e descreve como os dados são armazenados no banco de dados. O nível interno é às vezes chamado de nível físico.

- `Independência de dados`: é a capacidade de alterar o esquema em um nível de um banco de dados sem afetar o esquema em um nível superior. A independência de dados é importante porque significa que os usuários finais e os programas de aplicativos não precisam ser alterados quando o esquema é alterado.

#### Definição do conceito ACID

- O conceito ACID é um conjunto de propriedades que garantem que as transações sejam processadas de forma confiável. O conceito ACID é importante para garantir que os dados permaneçam consistentes mesmo em caso de falha do sistema.

- `Transação` é uma unidade lógica de trabalho que acessa e possivelmente modifica os dados. As transações são usadas para garantir que os dados permaneçam consistentes mesmo em caso de falha do sistema.

- As quatro propriedades do ACID são: atomicidade, consistência, isolamento e durabilidade.

- `Atomicidade` significa que uma transação é tratada como uma unidade lógica de trabalho e que todas as operações da transação são concluídas com sucesso ou a transação é abortada.

- `Consistência` significa que uma transação deve transformar um banco de dados de um estado consistente para outro estado consistente. Se uma transação violar as restrições de integridade, o banco de dados deve ser restaurado ao estado consistente anterior.

- `Isolamento` significa que o resultado de uma transação não é visível para outras transações até que a transação seja concluída.

- `Durabilidade` significa que, após a conclusão de uma transação, os resultados da transação são armazenados permanentemente no banco de dados e não podem ser perdidos devido a uma falha do sistema.