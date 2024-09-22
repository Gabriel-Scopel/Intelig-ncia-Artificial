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
