def change():
    expense = 23.75
    money = 100
    vuelto = money - expense
    pesos = int(vuelto)
    centavos = round((vuelto - pesos) * 100)

    print("Ingresar gasto:", expense)
    print("Dinero recibido:", money)
    print("\nVuelto")
    print(f"Pesos: {pesos}")
    print(f"Centavos: {centavos}")

change()
