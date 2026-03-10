import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid")

df = pd.read_csv('ecommerce_estatistica.csv', index_col=0)
print(df.head().to_string())
print(df.info())
print(df.describe())

# Gráfico de Histograma
plt.figure(figsize=(10, 6))
sns.histplot(df['Preço'], bins=20, kde=True, stat='count', color='steelblue')
plt.title('Distribuição de Preços')
plt.xlabel('Preço')
plt.ylabel('Quantidade de Produtos')
plt.show()

# Gráfico de Dispersão
sns.scatterplot(x='Preço', y='Nota', data=df, alpha=0.6)
plt.title('Relação entre Preço e Nota')
plt.show()

# Mapa de Calor
plt.figure(figsize=(10, 6))
corr = df[['Preço','Nota','Qtd_Vendidos_Cod','N_Avaliações']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.xticks(rotation=45, ha='right')
plt.title('Correlação Preço e Quantidade de Vendas')
plt.tight_layout()
plt.show()

# Gráfico de Barra
plt.figure(figsize=(10, 6))
sns.countplot(data=df, y='Marca', order=df['Marca'].value_counts().head(10).index)
plt.title('Top 10 Marcas Mais Frequentes')
plt.xlabel('Quantidade')
plt.ylabel('Marca')
plt.show()

# Gráfico de Pizza
temp = df['Temporada'].value_counts()
top = temp.head(4)
outros = temp.iloc[4:].sum()
top['Outros'] = outros

plt.figure(figsize=(8,8))
plt.pie(top.values, labels=top.index, autopct='%1.1f%%', startangle=90)
plt.title('Distribuição de Produtos por Temporada')
plt.show()

# Gráfico de Densidade
plt.figure(figsize=(10, 6))
sns.kdeplot(df['Preço'], fill=True, color='#863e9c')
plt.title('Onde os preços se concentram?')
plt.xlabel('Preço')
plt.show()


# Gráfico de Regressão
sns.regplot(x='Qtd_Vendidos_Cod', y='Nota', data=df, color='#278f65', scatter_kws={'alpha': 0.5, 'color': '#34c289'})
plt.title('Produtos com mais vendas têm melhores avaliações?')
plt.xlabel('Qtd_Vendidos_Cod')
plt.ylabel('Nota')
plt.show()