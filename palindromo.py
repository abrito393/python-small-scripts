from operator import truediv


def run():
    palabra = input('Escribe una palabra: ')
    print(es_palindromo(palabra))


def es_palindromo(palabra):
    if palabra.replace(" ","") == palabra.replace(" ","")[::-1]:
        return 'Es palindromo'
    else:
        return 'No es palindromo'


if __name__ == '__main__':
    run()