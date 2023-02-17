



def calculo_informacoes_categoricas(x):
    print('O valor mínimo da variável é: ' + str(x.min()))
    print('O valor máximo da variável é: ' + str(x.max()))
    print('O valor médio é: ' + str(round(x.mean(), 2)))
    print('O valor mediano é: ' + str(x.median()))
    print('O valor moda é: ' + str(x.mode()[0]))

