# Sistema de Controle Financeiro

transacoes = []

def adicionar_receita():
    valor = float(input("Digite o valor da receita: "))
    descricao = input("Digite a descrição: ")
    transacoes.append({"tipo": "receita", "valor": valor, "descricao": descricao})
    print("Receita adicionada com sucesso!\n")

def adicionar_despesa():
    valor = float(input("Digite o valor da despesa: "))
    descricao = input("Digite a descrição: ")
    transacoes.append({"tipo": "despesa", "valor": valor, "descricao": descricao})
    print("Despesa adicionada com sucesso!\n")

def listar_transacoes():
    if not transacoes:
        print("Nenhuma transação registrada.\n")
        return

    for t in transacoes:
        print(f"{t['tipo'].upper()} - R${t['valor']} - {t['descricao']}")
    print()

def calcular_saldo():
    saldo = 0
    for t in transacoes:
        if t["tipo"] == "receita":
            saldo += t["valor"]
        else:
            saldo -= t["valor"]

    print(f"Saldo atual: R${saldo}\n")

def menu():
    while True:
        print("=== CONTROLE FINANCEIRO ===")
        print("1 - Adicionar Receita")
        print("2 - Adicionar Despesa")
        print("3 - Listar Transações")
        print("4 - Ver Saldo")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_receita()
        elif opcao == "2":
            adicionar_despesa()
        elif opcao == "3":
            listar_transacoes()
        elif opcao == "4":
            calcular_saldo()
        elif opcao == "5":
            print("Encerrando sistema...")
            break
        else:
            print("Opção inválida!\n")

menu()
