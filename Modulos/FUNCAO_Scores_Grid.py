
import pandas as pd
from sklearn.model_selection import GridSearchCV


def grid_scores(x, versao):
    print(f'Resultados do melhor modelo obtido com GridSearchCV para o modelo:', versao)
    print('-' * 80)
    print('Os melhores hiperparâmetros obtidos foram:')
    print(x.best_params_)
    print('-' * 80)
    print('Resultados da métrica de MSE:\n')
    mse_media = round(x.cv_results_['mean_test_neg_mean_squared_error'][x.best_index_], 4)
    print(f'Média de MSE é:', mse_media)
    mse_std = round(x.cv_results_['std_test_neg_mean_squared_error'][x.best_index_], 4)
    print(f'Desvio-padrão de MSE é:', mse_std)
    print('-' * 80)
    print('Resultados da métrica de MAE:\n')
    mae_media = round(x.cv_results_['mean_test_neg_mean_absolute_error'][x.best_index_], 4)
    print(f'Média de MAE é:', mae_media)
    mae_std = round(x.cv_results_['std_test_neg_mean_absolute_error'][x.best_index_], 4)
    print(f'Desvio-padrão de MAE é:', mae_std)
    print('-' * 80)
    print('Resultados da métrica de R2:\n')
    r2_media = round(x.cv_results_['mean_test_r2'][x.best_index_], 4)
    print(f'Média de R2 é:', r2_media)
    r2_std = round(x.cv_results_['std_test_r2'][x.best_index_], 4)
    print(f'Desvio-padrão do R2 é:', r2_std)
    
    