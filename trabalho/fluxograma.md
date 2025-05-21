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

**Notificações**

```
Ao criar tarefa de prioridade "Alta":
    Enviar notificação ao utilizador responsável

Ao abrir a interface de administração (GestorTarefas):
    Para cada tarefa com prazo a expirar em 1 dia:
        Se a tarefa não está concluída:
            Enviar email de aviso ao utilizador responsável
```

**Interface de Administração (GestorTarefas)**

```
Ao abrir:
    Carregar lista de utilizadores e tarefas dos ficheiros JSON
    Apresentar painel com:
        - Formulário para criar tarefas
        - Lista de tarefas existentes
        - Opções para editar, remover, concluir, bloquear/desbloquear, ordenar e pesquisar tarefas
    Verificar prazos de tarefas:
        Para cada tarefa com prazo a expirar em 1 dia:
            Se não está concluída:
                Enviar email de aviso ao utilizador responsável

Ao criar tarefa:
    Ler dados do formulário
    Validar dados (ex: título não vazio, prazo válido)
    Associar tarefa a um utilizador
    Adicionar tarefa à lista
    Guardar lista de tarefas no ficheiro JSON
    Se a tarefa for desbloqueada:
        Enviar email ao utilizador responsável com os detalhes da tarefa
    Atualizar lista apresentada

Ao editar/remover/concluir tarefa:
    Identificar tarefa selecionada
    Aplicar alteração
    Se marcar como concluída:
        Desbloquear automaticamente a próxima tarefa bloqueada (se existir)
    Guardar lista de tarefas no ficheiro JSON
    Atualizar lista apresentada

Ao bloquear/desbloquear tarefa:
    Alterar estado de bloqueio da tarefa selecionada
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
    Se existir pelo menos uma tarefa desbloqueada:
        Enviar email ao utilizador a informar que tem tarefas disponíveis

Ao marcar tarefa como concluída:
    Identificar tarefa selecionada
    Alterar estado de conclusão
    Desbloquear automaticamente a próxima tarefa bloqueada do utilizador (se existir)
    Guardar lista de tarefas no ficheiro JSON
    Atualizar lista apresentada

Ao desmarcar tarefa:
    Identificar tarefa selecionada
    Alterar estado de conclusão para não concluída
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
