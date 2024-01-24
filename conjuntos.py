conjunto1 = {1, 2, 3, 4, 5, 6}
conjunto2 = {4, 6, 7, 8, 9, 10}

#conjunto2.discard(3) Para eliminar cosas
#del conjunto

print(conjunto1.union(conjunto2))
        #or for union
print(conjunto1 | conjunto2)

#valores que se repiten en ambas
print(conjunto1.intersection(conjunto2))
        #or
print(conjunto1 & conjunto2)

#valores de a que no estan en b
print(conjunto1.difference(conjunto2))
        #or
print(conjunto1 - conjunto2)

#diferencia simetrica valores que estan presentes en a y b pero
# no en ambos conjuntos
print(conjunto1.symmetric_difference(conjunto2))
        #or
print(conjunto1 ^ conjunto2)

