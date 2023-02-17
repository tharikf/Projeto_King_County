


# Visualização de Dados
import matplotlib.pyplot as plt
import seaborn as sns

def histograma_plt(data, x):
    fig, ax = plt.subplots(figsize = (8, 4))
    
    ax = sns.histplot(data = data, x = x, kde = True, color = 'green')
    ax.set_title('Histograma de: ' + x, fontsize = 10)
    ax.set_xlabel(x)
    ax.set_ylabel('')
    plt.ticklabel_format(style = 'plain', axis = 'x')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    fig.tight_layout()
    plt.show();


