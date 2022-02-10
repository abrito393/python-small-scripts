menu = """
    Bienvenido al conversor de monedas 🤑

    1 - Pesos colombianos
    2 - Pesos argentinos
    3 - Pesos mexicanos

    Elige una opcion: """

opcion = int(input(menu))

def conversor(valor_dolar,moneda):
    cantidad_convertir = input("Cuantos pesos "+moneda+" tienes: ")
    print( "tienes $" + str( round ( float(cantidad_convertir) / valor_dolar, 2 ) ) + " dolares" )

if opcion == 1:
    conversor(3967.47, 'colombianos')
elif opcion == 2:
    conversor(105.90, 'argentinos')
elif opcion == 3:
    conversor(20.51, 'mexicanos')
else:
    print('Debe eligir una opcion correcta')



