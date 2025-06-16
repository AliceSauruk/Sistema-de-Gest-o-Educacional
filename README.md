# Sistema de Gestão Educacional em Python

Este projeto é um sistema de gestão educacional simples, desenvolvido em Python, com foco em operações CRUD (Criar, Listar, Atualizar, Excluir) para as entidades: estudantes, professores, disciplinas, turmas e matrículas.

## Funcionalidades

- **Menu Interativo** no terminal.
- **Cadastro e gerenciamento de:**
  - Estudantes
  - Professores
  - Disciplinas
  - Turmas (vinculadas a disciplinas e professores)
  - Matrículas (vinculadas a estudantes e turmas)
- **Validações integradas:**
  - CPF com 11 dígitos numéricos
  - Códigos únicos e obrigatoriamente inteiros

## Tecnologias e Conceitos Utilizados

- **Python 3** (sintaxe procedural)
- **Arquivos JSON** como base de dados local
- **Módulo `os`** para verificação e manipulação de arquivos
- **Encapsulamento de lógica** por funções genéricas reutilizáveis
- **Interface via terminal** (input/output em linha de comando)

## Como Executar

1. Certifique-se de ter o Python instalado.
2. Salve o código em um arquivo `.py`.
3. Execute o script com:

```bash
python seu_arquivo.py
```

4. Siga as instruções no menu interativo.

## Persistência de Dados

Os dados são salvos automaticamente em arquivos `.json`, que funcionam como "mini bancos de dados" para armazenar cada entidade separadamente:

- `estudantes.json`
- `professores.json`
- `disciplinas.json`
- `turmas.json`
- `matriculas.json`

Esses arquivos são criados e atualizados automaticamente na mesma pasta do script.

## Objetivo Didático

Este projeto foi desenvolvido com fins educacionais para reforçar os seguintes tópicos:

- Lógica de programação
- Manipulação de dados estruturados
- Validação de entrada
- Estruturação de sistemas simples com persistência local