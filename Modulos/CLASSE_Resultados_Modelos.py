
import pandas as pd
from math import sqrt
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, mean_absolute_percentage_error



class Resultados_Modelos:

    resultados_todos_modelos = []

    def __init__(self, ytest, previsao, nome_modelo):
        self.ytest = ytest
        self.previsao = previsao
        self.nome_modelo = nome_modelo
        self.salvando_resultado()
        
    def salvando_resultado(self):
        RMSE = round(sqrt(mean_squared_error(self.ytest, self.previsao)), 4)
        MAE = round(mean_absolute_error(self.ytest, self.previsao), 4)
        R2 = round(r2_score(self.ytest, self.previsao), 4)
        MAPE = str(round(mean_absolute_percentage_error(self.ytest, self.previsao) * 100, 2)) + '%'


        dicionario_resultados = {'Algoritmo': self.nome_modelo, 'RMSE': RMSE, 'MAE': MAE, 'R2': R2, 'MAPE' : MAPE}
        self.resultados_todos_modelos.append(dicionario_resultados)
        self.resultados_todos_modelos = pd.DataFrame(self.resultados_todos_modelos)

    @staticmethod
    def obter_resultados():
        return Resultados_Modelos.resultados_todos_modelos



