#Calcular la diferencia simétrica entre 2 conjuntos

CapitalesMundo_1 = set(['Lima','Buenos Aires','Saopaolo','Montevideo','Asuncion','La paz','Mexico','Caracas','Quito','Bogota']) #se crea el conjunto llamado CapaitalesMundo_1
CapitalesMundo_2 = set(['Washintong DC','Roma','Mdrid','Montevideo','Asuncion','La paz','Mexico'])#se crea el conjunto llamado CapaitalesMundo_2

print("la diferencia simetrica de los conjuntos es: ")
resultado = CapitalesMundo_1.symmetric_difference(CapitalesMundo_2) # se esta utilizando la funcion symmetric_difference
print(resultado)
