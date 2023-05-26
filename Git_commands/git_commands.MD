## Lista de comandos Git

### 1. Configuração inicial
- `git config --global user.name "Seu Nome"`: configura o nome do usuário
- `git config --global user.email "Seu Email"`: configura o email do usuário

### 2. Inicializando um repositório
- `git init`: inicializa um repositório git em um diretório
- `git clone <url>`: clona um repositório remoto para o diretório local

### 3. Comandos básicos
- `git status`: mostra o status do repositório
- `git add <arquivo>`: adiciona um arquivo ao stage
- `git add .`: adiciona todos os arquivos ao stage
- `git commit -m "mensagem"`: cria um commit com os arquivos do stage e a mensagem
- `git log`: mostra o histórico de commits

### 4. Branches
- `git branch`: mostra as branches existentes
- `git branch <nome>`: cria uma nova branch
- `git checkout <nome>`: muda para a branch especificada
- `git merge <nome>`: faz o merge da branch especificada com a branch atual
- `git branch -D <nome>`: deleta a branch especificada

### 5. Repositório remoto
- `git remote add origin <url>`: adiciona um repositório remoto
- `git push -u origin <branch>`: envia os commits para o repositório remoto
- `git pull`: puxa as alterações do repositório remoto diretamente para a branch atual
- `git clone <url>`: clona um repositório remoto para o diretório local
- `git remote -v`: mostra os repositórios remotos
- `git remote rm <nome>`: remove o repositório remoto especificado

### 6. Resolvendo conflitos
- `git fetch`: puxa as alterações do repositório remoto para o repositório local
- `git diff <branch> <branch>`: mostra as diferenças entre duas branches
- `git diff <branch> <arquivo>`: mostra as diferenças entre um arquivo e uma branch
- `git diff <branch> <arquivo>`: mostra as diferenças entre um arquivo e uma branch
- `git diff --name-only <branch> <branch>`: mostra os nomes dos arquivos diferentes entre duas branches
- `git diff --name-only <branch> <arquivo>`: mostra os nomes dos arquivos diferentes entre um arquivo e uma branch
- `git merge <branch>`: faz o merge da branch especificada com a branch atual

### 7. Desfazendo coisas
- `git restore --staged <arquivo>`: tira o arquivo do stage
- `git restore <arquivo>`: desfaz as alterações do arquivo especificado
- `git reset HEAD <arquivo>`: tira o arquivo do stage
- `git reset --soft <commit>`: volta para o commit especificado
- `git reset --mixed <commit>`: volta para o commit especificado e tira os arquivos do stage
- `git reset --hard <commit>`: volta para o commit especificado e apaga os arquivos do stage
- `git revert <commit>`: cria um commit revertendo as alterações do commit especificado
- `git checkout -- <arquivo>`: desfaz as alterações do arquivo especificado
- `git clean -f`: apaga os arquivos não rastreados
- `git clean -f -d`: apaga os arquivos não rastreados e os diretórios vazios