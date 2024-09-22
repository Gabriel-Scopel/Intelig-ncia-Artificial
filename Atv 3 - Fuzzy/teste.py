import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl

# Variáveis de Entrada (Antecedent)
comer = ctrl.Antecedent(np.arange(0, 9, 1), 'comer')

# Variáveis de Saída (Consequent)
peso = ctrl.Consequent(np.arange(0, 15, 1), 'peso')

# Definindo as funções de pertinência triangulares (trimf)
comer['pouco'] = fuzz.trimf(comer.universe, [0, 2, 4])  # Forma triangular entre 0 e 4, com pico em 2
comer['razoavel'] = fuzz.trimf(comer.universe, [2, 5, 7])  # Forma triangular entre 2 e 7, com pico em 5
comer['bastante'] = fuzz.trimf(comer.universe, [5, 7, 9])  # Forma triangular entre 5 e 9, com pico em 7

peso['leve'] = fuzz.trimf(peso.universe, [0, 3, 6])  # Forma triangular entre 0 e 6, com pico em 3
peso['medio'] = fuzz.trimf(peso.universe, [4, 7, 10])  # Forma triangular entre 4 e 10, com pico em 7
peso['pesado'] = fuzz.trimf(peso.universe, [9, 12, 15])  # Forma triangular entre 9 e 15, com pico em 12

# Visualizando as variáveis
comer.view()
peso.view()

# Criando as regras (o operador mínimo é usado implicitamente)
regra_1 = ctrl.Rule(comer['bastante'], peso['pesado'])  # Se comer bastante, o peso é pesado
regra_2 = ctrl.Rule(comer['razoavel'], peso['medio'])   # Se comer razoavelmente, o peso é médio
regra_3 = ctrl.Rule(comer['pouco'], peso['leve'])       # Se comer pouco, o peso é leve

# Criando o sistema de controle fuzzy com as regras
controlador = ctrl.ControlSystem([regra_1, regra_2, regra_3])

# Criando a simulação do sistema de controle fuzzy
CalculoPeso = ctrl.ControlSystemSimulation(controlador)

# Solicitando a entrada do usuário (quantidade de comida ingerida)
qtdeComida = int(input('qtde kcal comida: '))
CalculoPeso.input['comer'] = qtdeComida

# Computando o resultado com base nas regras fuzzy e operador mínimo
CalculoPeso.compute()

# Obtendo o valor da saída (peso resultante)
valorPeso = CalculoPeso.output['peso']

# Exibindo o resultado
print("\nqtde comida %d \nPeso %5.2f" % (qtdeComida, valorPeso))

# Visualizando as variáveis de entrada e saída com os resultados da simulação
comer.view(sim=CalculoPeso)
peso.view(sim=CalculoPeso)

plt.show()
