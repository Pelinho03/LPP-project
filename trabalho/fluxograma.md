**Início do Programa**

```
Início
    Carregar interface de login
    Esperar ação do utilizador
```

**Login**

```
Se o utilizador introduzir um email válido:
    Carregar lista de utilizadores do ficheiro JSON
    Procurar utilizador com o email fornecido
    Se utilizador encontrado:
        Se grupo == "admin":
            Abrir interface de administração (GestorTarefas)
        Senão:
            Abrir interface de utilizador (UserUI)
    Senão:
        Apresentar mensagem de erro "Utilizador não encontrado"
```

**Interface de Administração (GestorTarefas)**

```
Ao abrir:
    Carregar lista de utilizadores e tarefas dos ficheiros JSON
    Apresentar painel com:
        - Formulário para criar tarefas
        - Lista de tarefas existentes
        - Opções para editar, remover, concluir, ordenar e pesquisar tarefas

Ao criar tarefa:
    Ler dados do formulário
    Validar dados (ex: título não vazio, prazo válido)
    Associar tarefa a um utilizador
    Adicionar tarefa à lista
    Guardar lista de tarefas no ficheiro JSON
    Atualizar lista apresentada

Ao editar/remover/concluir tarefa:
    Identificar tarefa selecionada
    Aplicar alteração
    Guardar lista de tarefas no ficheiro JSON
    Atualizar lista apresentada

Ao criar utilizador:
    Ler dados do formulário
    Validar dados
    Adicionar utilizador à lista
    Guardar lista de utilizadores no ficheiro JSON
    Atualizar lista apresentada
```

**Interface de Utilizador (UserUI)**

```
Ao abrir:
    Carregar lista de tarefas associadas ao utilizador autenticado
    Apresentar lista de tarefas, visor de detalhes e opções de ordenação/conclusão

Ao marcar/desmarcar tarefa como concluída:
    Identificar tarefa selecionada
    Alterar estado de conclusão
    Guardar lista de tarefas no ficheiro JSON
    Atualizar lista apresentada

Ao pesquisar ou ordenar tarefas:
    Filtrar ou ordenar lista de tarefas conforme critério selecionado
    Atualizar lista apresentada
```

**Persistência**

```
Sempre que há alteração em utilizadores ou tarefas:
    Converter objetos para dicionários
    Guardar em ficheiros JSON respetivos
```

**Notificações**

```
Ao criar tarefa de prioridade "Alta":
    Enviar notificação ao utilizador responsável
```

**Fim do Programa**

```
Ao fechar a interface principal:
    Terminar execução
```
