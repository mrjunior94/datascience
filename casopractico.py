import numpy as np 

meses = np.array (['enero', 'febrero', 'marzo','abril','mayo','junio','julio','agosto','septiembre','octubre', 'noviembre', 'diciembre'])

Ventas_A = ([100, 150, 250, 100, 150, 325, 320, 100, 140, 250, 321, 140])
Ventas_B =([33, 12, 15, 30, 14, 25, 32, 25, 48, 50, 60, 25,])
Ventas_C = ([60, 80, 90, 70, 75, 82, 98, 74, 71, 58, 25, 45 ]) 

# Estadisticas basicas 

promedio = np.mean(Ventas_A)
print("Promedios de Ventas para el periodo 2024")
print(f'Poducto A:{promedio}')
promediob = np.mean(Ventas_B)
print(f'Producto B: {promediob}')
promedioc = np.mean(Ventas_C)
print(f'Producto C : {promedioc}')

