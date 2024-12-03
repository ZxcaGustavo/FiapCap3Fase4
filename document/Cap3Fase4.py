# Importar bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Passo 1: Carregar o Dataset
file_path = r"C:\Users\Zxca-hunter\Downloads\seeds_dataset.txt"
column_names = [
    'Area', 'Perimetro', 'Compacidade',
    'Comprimento_Nucleo', 'Largura_Nucleo',
    'Coeficiente_Assimetria', 'Comprimento_Sulco', 'Classe'
]

# Carregar dados, ignorando linhas problemáticas
data = pd.read_csv(file_path, sep='\t', header=None, names=column_names, on_bad_lines='skip')

# Exibir informações básicas do dataset
print("Dados carregados com sucesso!")
print(data.head())
print(data.describe())

# Passo 2: Verificar valores ausentes e tratar
print("Valores ausentes por coluna:\n", data.isnull().sum())
data.dropna(inplace=True)  # Remover linhas com valores ausentes

# Passo 3: Visualização de Dados
# Histogramas
data.hist(bins=20, figsize=(10, 10))
plt.show()

# Boxplots
data.boxplot(figsize=(12, 6))
plt.show()

# Passo 4: Pré-processamento
X = data.iloc[:, :-1]  # Características
y = data['Classe']  # Classe alvo

# Padronizar os dados
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Dividir em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# Passo 5: Treinar e Avaliar Modelos
# a) K-Nearest Neighbors (KNN)
print("Modelo: K-Nearest Neighbors")
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test)
print(confusion_matrix(y_test, y_pred_knn))
print(classification_report(y_test, y_pred_knn))

# b) Support Vector Machine (SVM)
print("Modelo: Support Vector Machine")
svm = SVC(kernel='linear', random_state=42)
svm.fit(X_train, y_train)
y_pred_svm = svm.predict(X_test)
print(confusion_matrix(y_test, y_pred_svm))
print(classification_report(y_test, y_pred_svm))

# c) Random Forest
print("Modelo: Random Forest")
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)
print(confusion_matrix(y_test, y_pred_rf))
print(classification_report(y_test, y_pred_rf))

# Passo 6: Comparar Modelos
print("Resumo dos Resultados")
print("KNN - Acurácia: {:.2f}".format(knn.score(X_test, y_test)))
print("SVM - Acurácia: {:.2f}".format(svm.score(X_test, y_test)))
print("Random Forest - Acurácia: {:.2f}".format(rf.score(X_test, y_test)))
