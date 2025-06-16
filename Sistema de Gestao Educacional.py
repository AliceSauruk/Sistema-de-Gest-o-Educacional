import json
import os

ARQUIVOS = {
    'estudantes': 'estudantes.json',
    'professores': 'professores.json',
    'disciplinas': 'disciplinas.json',
    'turmas': 'turmas.json',
    'matriculas': 'matriculas.json'
}

# Função para carregar dados de um arquivo JSON
def carregar_dados(nome_arquivo):
    if os.path.exists(nome_arquivo):  # Verifica se o arquivo existe
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)  # Carrega os dados do arquivo
    return []  # Retorna uma lista vazia se o arquivo não existir

# Função para salvar dados em um arquivo JSON
def salvar_dados(nome_arquivo, dados):
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4)  # Salva os dados no arquivo com indentação para facilitar a leitura

# Função para verificar se um código já existe na lista
def codigo_existe(lista, codigo):
    """
    Verifica se um código já existe na lista.
    """
    return any(str(item.get('codigo')) == str(codigo) for item in lista)

# Função para exibir o menu principal
def menu():
    print()
    print("----- MENU PRINCIPAL -----")
    print()
    print("(1) Gerenciar estudantes.")  # Opção para gerenciar estudantes
    print("(2) Gerenciar professores.")  # Opção para gerenciar professores
    print("(3) Gerenciar disciplinas.")  # Opção para gerenciar disciplinas
    print("(4) Gerenciar turmas.")  # Opção para gerenciar turmas
    print("(5) Gerenciar matrículas.")  # Opção para gerenciar matrículas
    print("(9) Sair.")  # Opção para sair do programa
    print()

# Função genérica para gerenciar uma entidade (estudantes, professores, etc.)
def gerenciar_entidade(nome, campos, lista, salvar_funcao):
    while True:
        print(f"\n----- MENU {nome.upper()} -----")
        print()
        print("(1) Incluir")  # Opção para incluir um novo registro
        print("(2) Listar")  # Opção para listar os registros
        print("(3) Atualizar")  # Opção para atualizar um registro existente
        print("(4) Excluir")  # Opção para excluir um registro
        print("(9) Voltar")  # Opção para voltar ao menu principal
        print()
        try:
            op = int(input("Escolha uma das opções: "))  # Lê a opção do usuário
        except ValueError:
            print("Opção inválida.")  # Trata entradas inválidas
            continue
        if op == 1:
            incluir_dados(lista, campos, nome, salvar_funcao)  # Chama a função para incluir dados
        elif op == 2:
            listar_dados(lista, nome, campos)  # Chama a função para listar dados
        elif op == 3:
            atualizar_dados(lista, nome, campos, salvar_funcao)  # Chama a função para atualizar dados
        elif op == 4:
            excluir_dados(lista, nome, campos, salvar_funcao)  # Chama a função para excluir dados
        elif op == 9:
            break  # Sai do menu da entidade
        else:
            print("Opção inválida.")  # Mensagem para opções inválidas

    return None

# Função para incluir novos dados em uma lista
def incluir_dados(lista, campos, nome_entidade, salvar_funcao):
    print()
    print(f"===== INCLUSÃO DE {nome_entidade.upper()} =====")
    print()
    while True:
        novo_item = {}  # Dicionário para armazenar os dados do novo item
        for campo in campos:
            while True:
                valor = input(f'Informe o {campo} do(a) {nome_entidade}: ')  # Solicita o valor do campo
                if campo == "codigo":
                    if codigo_existe(lista, valor):  # Verifica se o código já existe
                        print(f"Erro: O código {valor} já existe. Tente novamente.")
                        continue
                if campo == "CPF":
                    if not valor.isdigit() or len(valor) != 11:  # Valida o CPF (apenas números e 11 dígitos)
                        print("Erro: O CPF deve conter apenas números e ter 11 dígitos. Tente novamente.")
                        continue
                if campo in ["codigo", "codigo da disciplina", "codigo do professor", "codigo da turma", "codigo do estudante"]:
                    try:
                        valor = int(valor)  # Converte o valor para inteiro
                    except ValueError:
                        print(f"Erro: O campo {campo} deve ser um número inteiro. Tente novamente.")
                        continue
                novo_item[campo] = valor  # Adiciona o campo ao dicionário
                break
        lista.append(novo_item)  # Adiciona o novo item à lista
        salvar_funcao(lista)  # Salva os dados no arquivo
        print(f"{nome_entidade.capitalize()} incluído(a) com sucesso!")
        print()
        if input(f'Deseja incluir um(a) novo(a) {nome_entidade} (s/n): ').lower() == 'n':  # Pergunta se deseja incluir outro item
            print()
            break

    return None

# Função para listar os dados de uma entidade
def listar_dados(lista, nome_entidade, campos):
    print()
    print(f"===== LISTAGEM DE {nome_entidade.upper()} =====")
    print()
    if len(lista) == 0:  # Verifica se a lista está vazia
        print(f"Não há {nome_entidade}s para listar")
        print()
    else:
        for item in lista:  # Itera sobre os itens da lista
            for campo in campos:  # Itera sobre os campos da entidade
                print(f"{campo.capitalize()}: {item.get(campo, '')}")  # Exibe o valor do campo
            print()

    return None

# Função para atualizar os dados de uma entidade
def atualizar_dados(lista, nome_entidade, campos, salvar_funcao):
    print()
    print(f"===== ATUALIZAÇÃO DE {nome_entidade.upper()} =====")
    print()

    if len(lista) == 0:  # Verifica se a lista está vazia
        print(f"Não há {nome_entidade}s para atualizar")
        print()
        return

    codigo = input(f'Digite o código do(a) {nome_entidade} que deseja atualizar: ')  # Solicita o código do item a ser atualizado
    print()

    for item in lista:  # Itera sobre os itens da lista
        if str(item.get('codigo')) == codigo:  # Verifica se o código corresponde
            for campo in campos:  # Itera sobre os campos da entidade
                novo_valor = input(f"Digite novo valor para {campo} (deixe vazio para manter): ")  # Solicita o novo valor
                if novo_valor:
                    if campo in ["codigo", "codigo da disciplina", "codigo do professor", "codigo da turma", "codigo do estudante"]:
                        try:
                            novo_valor = int(novo_valor)  # Converte o valor para inteiro
                        except ValueError:
                            print(f"Erro: O campo {campo} deve ser um número inteiro. Tente novamente.")
                            continue
                    item[campo] = novo_valor  # Atualiza o valor do campo
            salvar_funcao(lista)  # Salva os dados no arquivo
            print(f"{nome_entidade.capitalize()} atualizado(a) com sucesso!")
            print()
            if input(f'Deseja atualizar um(a) novo(a) {nome_entidade} (s/n): ').lower() == 'n':  # Pergunta se deseja atualizar outro item
                print()
                break
            return
    else:
        print(f"Erro: {nome_entidade.capitalize()} com código {codigo} não encontrado(a).")  # Mensagem de erro se o código não for encontrado

    return None

# Função para excluir os dados de uma entidade
def excluir_dados(lista, nome_entidade, campos, salvar_funcao):
    print()
    print(f"===== EXCLUSÃO DE {nome_entidade.upper()} =====")
    print()
    if len(lista) == 0:  # Verifica se a lista está vazia
        print(f"Não há {nome_entidade}s para excluir")
        print()
        return

    while True:
        codigo = input(f'Digite o código do(a) {nome_entidade} que deseja excluir: ')  # Solicita o código do item a ser excluído
        for i, item in enumerate(lista):  # Itera sobre os itens da lista
            if str(item.get('codigo')) == codigo:  # Verifica se o código corresponde
                confirmacao = input(f"Tem certeza que deseja excluir o(a) {nome_entidade} com código {codigo}? (s/n): ").lower()
                if confirmacao == 's':  # Confirma a exclusão
                    del lista[i]  # Remove o item da lista
                    salvar_funcao(lista)  # Salva os dados no arquivo
                    print(f"{nome_entidade.capitalize()} excluído(a) com sucesso!")
                else:
                    print("Operação cancelada.")  # Mensagem de cancelamento
                break
        else:
            print(f"Erro: {nome_entidade.capitalize()} com código {codigo} não encontrado(a).")  # Mensagem de erro se o código não for encontrado
        print()

        if input(f'Deseja excluir um(a) novo(a) {nome_entidade} (s/n): ').lower() == 'n':  # Pergunta se deseja excluir outro item
            print()
            break

    return None

# Função principal do programa
def main():
    # Carrega os dados de cada entidade a partir dos arquivos JSON
    estudantes = carregar_dados(ARQUIVOS['estudantes'])
    professores = carregar_dados(ARQUIVOS['professores'])
    disciplinas = carregar_dados(ARQUIVOS['disciplinas'])
    turmas = carregar_dados(ARQUIVOS['turmas'])
    matriculas = carregar_dados(ARQUIVOS['matriculas'])

    while True:
        menu()  # Exibe o menu principal
        try:
            opcao = int(input("Informe a opção desejada: "))  # Lê a opção do usuário
        except ValueError:
            print("Digite um número válido.")  # Trata entradas inválidas
            continue
        print()

        if opcao not in [1, 2, 3, 4, 5, 9]:  # Verifica se a opção é válida
            print("Opção inválida! Escolha uma opção entre 1 e 5 ou 9 para sair.")
        if opcao == 1:
            gerenciar_entidade("estudante", ['codigo', 'nome', 'CPF'], estudantes, lambda lista: salvar_dados(ARQUIVOS['estudantes'], lista))
        if opcao == 2:
            gerenciar_entidade("professor", ['codigo', 'nome', 'CPF'], professores, lambda lista: salvar_dados(ARQUIVOS['professores'], lista))
        if opcao == 3:
            gerenciar_entidade("disciplina", ['codigo', 'nome'], disciplinas, lambda lista: salvar_dados(ARQUIVOS['disciplinas'], lista))
        if opcao == 4:
            gerenciar_entidade("turma", ['codigo', 'codigo da disciplina', 'codigo do professor'], turmas, lambda lista: salvar_dados(ARQUIVOS['turmas'], lista))
        if opcao == 5:
            gerenciar_entidade("matricula", ['codigo', 'codigo da turma', 'codigo do estudante'], matriculas, lambda lista: salvar_dados(ARQUIVOS['matriculas'], lista))
        elif opcao == 9:
            print("===== ATUALIZAÇÃO =====")
            print()
            print("Finalizando aplicação...")
            break

# Ponto de entrada do programa
if __name__ == "__main__":
    main()