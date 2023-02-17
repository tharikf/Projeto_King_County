


# Visualização de Dados
import matplotlib.pyplot as plt
import seaborn as sns

def box_plt(data, x):
    
    fig, ax = plt.subplots(figsize = (8, 4))
    
    ax = sns.boxplot(data = data, x = x, orient = 'h', palette = 'Greens')
    ax.set_title('Esse é o boxplot da variável ' + x, fontsize = 10)
    ax.set_xlabel(x)
    ax.set_ylabel('')
    plt.ticklabel_format(style = 'plain', axis = 'x')
    plt.yticks(rotation = 45)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    fig.tight_layout()
    plt.show();


