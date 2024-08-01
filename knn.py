import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from tabulate import tabulate

file_path = 'C:\\ProjetoBolsa\\petra.csv'
data = pd.read_csv(file_path)
data['Index'] = data.index

print(tabulate(data.head(), headers='keys', tablefmt='pretty'))

X = data[['Index', 'Preço de Abertura', 'Preço de Fechamento']]
y = data['Variacao']

# Definir os intervalos para as categorias
bins = [-np.inf, 0, 1, np.inf]
labels = ['baixo', 'médio', 'alto']

# Converter valores contínuos em categorias discretas
y_discretized = pd.cut(y, bins=bins, labels=labels)

X_train, X_test, y_train, y_test = train_test_split(X, y_discretized, test_size=0.3, random_state=42)

knn = KNeighborsClassifier(n_neighbors=5)

# Treinar o classificador
knn.fit(X_train[['Preço de Abertura', 'Preço de Fechamento']], y_train)

# Fazer previsões no conjunto de teste
y_test_pred = knn.predict(X_test[['Preço de Abertura', 'Preço de Fechamento']])

# Adicionar as previsões ao DataFrame de teste
X_test_with_predictions = X_test.copy()
X_test_with_predictions['Previsão de Variação'] = y_test_pred

# Ordenar o DataFrame de teste pelo índice
X_test_with_predictions = X_test_with_predictions.sort_values(by='Index')

# Remover a coluna de índices para exibição
X_test_with_predictions = X_test_with_predictions.drop(columns=['Index'])

# Calcular a acurácia
train_accuracy = accuracy_score(y_train, knn.predict(X_train[['Preço de Abertura', 'Preço de Fechamento']]))
test_accuracy = accuracy_score(y_test, y_test_pred)

print(f'Acuracia no conjunto de treinamento: {train_accuracy}')
print(f'Acuracia no conjunto de teste: {test_accuracy}')

# Exibir o DataFrame com as previsões
print(tabulate(X_test_with_predictions.head(20), headers='keys', tablefmt='pretty'))

print(data.shape)

