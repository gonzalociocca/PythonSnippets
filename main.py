# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def solucionarRompecabezas(N):
    var_A = 1
    var_B = 1
    var_C = 1
    var_D = 1
    resultado = -1

    for i in range(N):
        resultado = 3 * var_D + 1 * var_C + 4 * var_B + 1 * var_A
        var_A = var_B
        var_B = var_C
        var_C = var_D
        var_D = resultado

    resultado = resultado%10000000000
    print(resultado)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solucionarRompecabezas(10)
    solucionarRompecabezas(100)
    solucionarRompecabezas(pow(2023, 100))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
