#Bank System
saldo_cliente = 100       #saldo do cliente

while True:     #Menu do sistema bancário
    print("Bem-vindo de volta!")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Ver saldo")
    print("4 - Sair")

    opcao_escolhida = input("Escolha uma opção: ")  #Escolha do usuário

    if opcao_escolhida == "1":     #opção que realiza o depósito.
        print("Quanto você deseja depositar?")
        deposito_valor = float(input("Depósito: "))
        saldo_cliente += deposito_valor  #Adição do valor depositado mais o saldo do cliente.
        print("Valor de R$", deposito_valor, "depositado com sucesso!")

    elif opcao_escolhida == "2":   #Opção que realizada o saque.
        print("Quanto você deseja sacar?")
        sacar_dinheiro = float(input("Sacar:"))

        if sacar_dinheiro <= saldo_cliente:
            saldo_cliente -= sacar_dinheiro   #Saque retirado do saldo total do cliente.

            print("Valor de R$", sacar_dinheiro, "sacado com sucesso!")
        else:
            print("Saldo insuficiente!")

    elif opcao_escolhida == "3":
        print(f"Seu saldo é: R${saldo_cliente:.2f}")  #Mostra o saldo ao cliente.

    elif opcao_escolhida == "4":
        print("Obrigado por usar o nosso sistema!")   #Usuário fecha o sistema.
        break

    else:
         print("Opção inválida.")   #Opção inválida caso o usuário escolha algo além das opções disponíveis.
