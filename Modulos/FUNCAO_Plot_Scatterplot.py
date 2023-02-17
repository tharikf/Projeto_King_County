


# Visualização de Dados
import matplotlib.pyplot as plt
import seaborn as sns

def scater_plt(data, x, y):
    fig, ax = plt.subplots(figsize = (8, 4))
    
    ax = sns.scatterplot(data = data, x = x, y = y, color = 'green')
    ax.set_title('Scatterplot de: ' + x + ' e ' + y, fontsize = 10)
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    plt.ticklabel_format(style = 'plain', axis = 'x')
    plt.ticklabel_format(style = 'plain', axis = 'y')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    fig.tight_layout()
    plt.show();

