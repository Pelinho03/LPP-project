# **FocusFlow**

Sistema de Gestão de Tarefas com Prioridades e Utilizadores

Este repositório contém a implementação de uma aplicação desenvolvida no âmbito da unidade curricular de **Linguagens e Paradigmas da Programação**, do curso de **Engenharia Informática**. O projeto tem como objetivo melhorar a organização de equipas e aumentar a produtividade através da gestão estruturada de tarefas com diferentes prioridades, prazos e responsáveis.

----------

## Objetivo

O principal objetivo deste projeto é:

-   Desenvolver uma aplicação funcional para **gestão de tarefas** com interface gráfica.
    
-   Permitir a associação de **utilizadores** com diferentes permissões.
    
-   Promover uma solução prática para problemas de organização em projetos reais.
    
-   Aplicar conceitos de **Programação Orientada a Objetos**, **modularização**, **estruturação de dados** e boas práticas de desenvolvimento.
    

----------
## Funcionalidades

### Gestão de Tarefas

-   Criar, editar, remover e concluir tarefas.
    
-   Associar tarefas a utilizadores específicos.
    
-   Ordenar por prioridade ou data.
    
-   Pesquisa de tarefas por título.
    

### Gestão de Utilizadores

-   Criar utilizadores com grupos diferentes:
    
    -   **Admin**: acesso total à aplicação.
        
    -   **Equipa de Desenvolvimento** e **Design**: acesso limitado às suas tarefas.
        
-   Login com base no grupo de utilizador.
    

----------

## Tecnologias Utilizadas

-   **Python 3**
    
-   **PyQt6** – Interface gráfica (GUI)
    
-   **JSON** – Armazenamento persistente de dados
    
-   **Visual Studio Code** – Ambiente de desenvolvimento
    
-   **Git/GitHub** – Controlo de versões
    

----------

## Estrutura do Projeto

```bash
trabalho/
│
├── tarefa/
│   ├── tarefa.py           # Classe Tarefa
│   ├── tarefa_json.py      # Funções para carregar/guardar tarefas
│
├── user/
│   ├── user.py             # Classe User
│   ├── user_json.py        # Funções para carregar/guardar utilizadores
│
├── ui/
│   ├── adminUI.py          # Interface para administradores
│   ├── userUI.py           # Interface para utilizadores normais
│   ├── loginUI.py          # Interface de login
│
├── styles/
│   ├── style.qss           # Ficheiro com estilos CSS da aplicação
│
├── json/
│   ├── tarefas.json        # Armazena as tarefas
│   ├── utilizadores.json   # Armazena os utilizadores
│
├── main.py                 # Ponto de entrada da aplicação
└── README.md               # Este documento

```

----------

## Como Executar o Projeto

1.  **Clonar o repositório:**
    

```bash
git clone https://github.com/Pelinho03/LPP-project.git

```

2.  **Navegar para o diretório do projeto:**
    

```bash
cd LPP-project

```

3.  **Instalar as dependências:**
    

```bash
pip install -r requirements.txt

```

4.  **Executar a aplicação:**
    

```bash
python main.py

```

----------

## Ideia Central

> Este projeto procura não só implementar um software funcional, mas também demonstrar como uma ferramenta simples pode ter **impacto real** na produtividade de equipas e na organização de fluxos de trabalho.

----------

## Desenvolvido por

**Paulo Guimarães**  
[GitHub](https://github.com/Pelinho03)
