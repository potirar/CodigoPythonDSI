while True:
    try:
        salario = float(input("Informe seu salário: "))

    except Exception as erro:
        print(f"Erro, informe um valor decimal{erro.__class__}")
    else:
        break

print(f"Seu salário é: R${salario}")
    