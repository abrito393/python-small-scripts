def run():
    # ciclo_while()
    ciclo_for()


def ciclo_while():
    LIMIT = 100000
    index = 0
    potency = 2**index
    
    while potency < LIMIT:
        print("el resultado es: " + str(potency))
        potency = 2**index
        index += 1

def ciclo_for():
    for index in range(10):
        print("el resultado es: " + str(2**index))


if __name__ == '__main__':
    run()