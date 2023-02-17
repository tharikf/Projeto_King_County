


# Visualização de Dados
import matplotlib.pyplot as plt
import seaborn as sns

def count_plt(data, x):
    fig, ax = plt.subplots(figsize = (8, 4))
    
    ax = sns.countplot(data = data, x = x, palette = 'Greens')
    
    ax.set_title('Quantidade de ' + x, fontsize = 10)
    ax.set_xlabel(x)
    ax.set_ylabel('')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    fig.tight_layout()
    plt.show();



