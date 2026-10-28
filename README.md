1. Nome do projeto:
- 67GAMES - Plataforma de Jogos Online

2. Tema escolhido:
- Plataforma de jogos online

3. Integrantes do grupo e responsabilidade:
- Michel Jackson: Model
- Rafael Fernandes: Controller
- Valessia Juliany: View

4. Descrição do sistema:
- O 67GAMES é uma aplicação desenvolvida com Flask, com o objetivo de reunir e organizar jogos online em uma plataforma. O sistema permite visualizar os jogos cadastrados, consultar suas informações, conhecer seus criadores e identificar suas categorias. Os jogos podem ser acessados por meio de links para plataformas externas que os hospedam. A aplicação utiliza um banco de dados para armazenar as informações dos usuários, jogos, criadores e categorias.

5. Entidades:
- Usuario: armazena as informações dos usuários cadastrados na plataforma.
- Jogo: armazena informações sobre os jogos, como nome, descrição, ano de lançamento, criador e categoria.
- Criador: representa os criadores ou desenvolvedores dos jogos.
- Categoria: representa as categorias utilizadas para organizar e filtrar os jogos.

6. Relacionamentos entre as entidades:
- Relacionamento 1:N - É o relacionamento entre "Criador" e "Jogo". Isso significa que um criador pode estar associado a vários jogos, enquanto cada jogo possui um único criador. Esse relacionamento é feito por meio da chave estrangeira na tabela de jogos, que referencia o id do criador.

- Relacionamento N:N - É o relacionamento entre "Usuario" e "Jogo". Isso significa que um usuário pode estar associado a vários jogos, enquanto um mesmo jogo pode estar associado a vários usuários. Esse relacionamento pode representar os jogos favoritos de cada usuário. Para implementá-lo, é utilizada uma tabela associativa que armazena as chaves estrangeiras de "Usuario" e "Jogo", permitindo registrar as associações entre eles.

7. Instalação das dependências:
- tenha o Python
- ative um ambiente virtual
- instale Flask e Flask-SQLAlchemy
- pip install flask e pip install flask_sqlalchemy
- veja melhor no requirements.txt

8. Criação e população do banco de dados:
- O projeto utiliza SQLAlchemy para interagir com o banco. A criação das tabelas é realizada pela função "criar_tabelas()", enquanto a função "cadastrar_dados()" insere os dados iniciais, como categorias, criadores e jogos, quando necessário.

9. Execução do sistema:
- Baixe a pasta do projeto pelo Github, e descompacte ela
- Ative o ambiente virtual
- Instale as dependências
- Rode o código pelo terminal com flask run --debug
- Coloque o caminho em seu navegador

10. Principais dificuldades encontradas:
- Criação dos modelos do banco utilizando SQLAlchemy
- A definição dos relacionamentos entre jogos, criadores e categorias
- A resolução de incompatibilidades entre a estrutura das tabelas e os modelos atualizados
- A implementação de rotas Flask e a integração entre páginas HTML e os dados do banco
- A integração de jogos hospedados em plataformas externas

11. Declaração de autoria

Declaro que desenvolvi este projeto compreendendo o código entregue e que sou capaz de explicar e modificar suas partes principais.

- [x] Não utilizei IA generativa.
- [ ] Utilizei IA generativa e descrevo abaixo onde e como foi utilizada.
