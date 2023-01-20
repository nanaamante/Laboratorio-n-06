#Realizar operaciones de unión, intersección y diferencia
#de conjuntos
#se define los conjuntos con el metodo set 
grupo_a = set([1,2,3,4,5,6,7,8,9]) #se crea el conjunto llamado grupo_a
grupo_b = set([1,3,5,7,9,12,15,18]) # se crea el conjunto llamado grupo_b
#union
print("La union de los conjuntos: ")
union = grupo_a.union(grupo_b)#se esta utilizando la funciòn union para unir
print(union)
#interseccion
print("La interseccion de los conjuntos: ")
interseccion = grupo_a.intersection(grupo_b)# se esta utilizando la funcion intersection para intersectar
print(interseccion)
# diferencia
print("La diferencia de los conjuntos: ")  # se esta utilizando la funcion defference
diferencia = grupo_a.difference(grupo_b)
print (diferencia)