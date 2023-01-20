#Calcular la diferencia entre dos conjuntos

colores_a = set(['Azul', 'Rosado', 'Negro', 'Amarrillo','Verde','violeta','Jade','Esmeralda'])#se crea el conjunto llamado colores_a
colores_b = set(['Rosado', 'Naranja', 'Lila', 'Fucsia','Beige','Azul','Negro','Marron'])#se crea el conjunto llamado colores_b

#diferencia de un conjunto 
print("La diferencia entre los dos conjuntos es: ")
diferencia = colores_a.difference(colores_b)# se esta utilizando la funcion defference
print(diferencia)