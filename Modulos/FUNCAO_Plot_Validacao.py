
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error


def plot_validacao(Ytrain, Ytest, PREDtrain, PREDtest):
    
    
    fig, axs = plt.subplots(1, 2, figsize=(12, 8))
    
    # Treino
    axs[0].scatter(Ytrain, PREDtrain)
    axs[0].plot([Ytrain.min(), Ytrain.max()], [Ytrain.min(), Ytrain.max()], 'k--', lw = 4)
    axs[0].set_xlabel('Valores Originais')
    axs[0].set_ylabel('Valores Previstos')
    axs[0].set_title('Dados de Treino')
    axs[0].spines['top'].set_visible(False)
    axs[0].spines['right'].set_visible(False)
    
    # Teste
    axs[1].scatter(Ytest, PREDtest)
    axs[1].plot([Ytest.min(), Ytest.max()], [Ytest.min(), Ytest.max()], 'k--', lw = 4)
    axs[1].set_xlabel('Valores Originais')
    axs[1].set_ylabel('Valores Previstos')
    axs[1].set_title('Dados de Teste')
    axs[1].spines['top'].set_visible(False)
    axs[1].spines['right'].set_visible(False)
    
    # Show
    
    plt.show()