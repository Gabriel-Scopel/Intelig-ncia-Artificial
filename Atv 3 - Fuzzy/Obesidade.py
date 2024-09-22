#pip install scikit-fuzzy

import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl

#Variaveis de Entrada (Antecedent)
comer = ctrl.Antecedent(np.arange(0, 10, 1), 'comer')
#Variaveis de saída (Consequent)
peso = ctrl.Consequent(np.arange(0, 16, 1), 'peso')

# automf -> Atribuição de categorias automaticamente
""" comer.automf(names=['pouco','razoavel','bastante'],)
peso.automf(names=['leve','medio','pesado']) """

# atribuicao sem o automf
comer['pouco'] = fuzz.trapmf(comer.universe,[0,0,2,5])
comer['razoavel'] = fuzz.trapmf(comer.universe, [2,4,7,9])
comer['bastante'] = fuzz.trapmf(comer.universe, [4,7,10,10])

peso['leve'] = fuzz.trapmf(peso.universe,[0,0,4,7])
peso['medio'] = fuzz.trapmf(peso.universe, [4,7,9,11])
peso['pesado'] = fuzz.trapmf(peso.universe, [9,11,16,16])

comer.view()
peso.view()


#Criando as regras
regra_1 = ctrl.Rule(comer['bastante'] , peso['pesado'])
regra_2 = ctrl.Rule(comer['razoavel'] , peso['medio'])
regra_3 = ctrl.Rule(comer['pouco'] , peso['leve'])

controlador = ctrl.ControlSystem([regra_1, regra_2, regra_3])


#Simulando
CalculoPeso = ctrl.ControlSystemSimulation(controlador)

qtdeComida = int(input('qtde kcal comida: '))
CalculoPeso.input['comer'] = qtdeComida
CalculoPeso.compute()

valorPeso = CalculoPeso.output['peso']

print("\nqtde comida %d \nPeso %5.2f" %(
        qtdeComida,
        valorPeso))


comer.view(sim=CalculoPeso)
peso.view(sim=CalculoPeso)

plt.show()
