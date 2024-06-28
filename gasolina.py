import seaborn as sns
import pandas as pd

data=pd.read_csv("gasolina.csv")
#data=sns.load_dataset("gasolina.csv")
data.head()

with sns.axes_style('whitegrid'):

  grafico = sns.lineplot(data=data, x="dia", y="venda")
  grafico.set(title='Preço da gasolina 01-10/07', xlabel='Mês', ylabel='Preço/L');
  grafico.figure.savefig("gasolina.png")
  