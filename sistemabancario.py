aldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
  opcao = input(" o que voce deseja executar(s) Sacar\n(e) Extrato\n(d) Depositar\n(f) Finalizar\n").lower()

  if opcao == "d":
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
      saldo += valor
      extrato += f"Depósito: R$ {valor:.2f}\n"
      print("Depósito realizado com sucesso!")
    else:
      print("Valor inválido para depósito.")

  elif opcao == "s":
    if numero_saques < LIMITE_SAQUES:
      valor = float(input("Informe o valor do saque: "))
      if valor > 0 and valor <= limite and valor <= saldo:
          saldo -= valor
          extrato += f"Saque: R$ {valor:.2f}\n"
          numero_saques += 1
          print("Saque realizado com sucesso!")
      elif valor > saldo:
          print("Saldo insuficiente.")
      elif valor > limite:
          print("Limite de saque excedido.")
      else:
          print("Valor inválido para saque.")
    else:
      print("Limite diário de saques atingido.")

  elif opcao == "e":
    print("\nExtrato:")
    if not extrato:
      print("Não foram realizadas movimentações.")
    else:
      print(extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")

  elif opcao == "f":
    print("Obrigado por utilizar nossos serviços!")
    break

  else:
    print("Operação inválida, por favor selecione novamente a operação desejada.")

     