from sklearn.datasets import load_wine
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import matplotlib.pyplot as plt

# Carregar o dataset Wine
X, y = load_wine(return_X_y=True)

# Dividir o dataset em conjunto de treino e teste (70% para treino e 30% para teste)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Treinamento do SVM com kernel RBF, você pode alterar conforme desejado
sv = svm.SVC(kernel='rbf', gamma='auto', C=1)
sv.fit(X_train, y_train)

# Previsões
y_pred = sv.predict(X_test)

# Avaliação do modelo
print("Relatório de Classificação:")
print(classification_report(y_test, y_pred))

# Acurácia geral do modelo
accuracy = accuracy_score(y_test, y_pred)
print(f"Acurácia geral do modelo: {accuracy * 100:.2f}%")

# Visualização dos resultados (exemplo: primeira e segunda características)
plt.title("Wine Dataset: Previsões do Modelo SVM")
plt.xlabel("Teor de Álcool")
plt.ylabel("Ácido Málico")
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_pred, cmap='coolwarm', edgecolors='k', s=100)
plt.show()
