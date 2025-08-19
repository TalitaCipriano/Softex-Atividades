### LISTAS ###

#lista = []
#lista = podem utilizar int, str, outra lista
#tupla = listas que não necessitam de alterações

# ADICIONAR ITENS 
#para adiconar itens a lista podemos usar: 
# lista.insert (adiciona o item numa posição específica)
# lista.append (adiciona o item no fim da lista)
#lista+=novalista (adiciona uma lista dentro da lista existente)
#frutas.extend ([itens]) = adiciona itens a lista

frutas = ["limão", "banana", "morango", "coco"]
# print(frutas)
#frutas = ["limão", "banana", "morango", "coco"]
# frutas.insert(1, "melancia")
# print(frutas)

# frutas.append("roma")
# print(frutas)

frutas_vermelhas = ["cereja", "framboesa", "amora", "morango"]
frutas+=frutas_vermelhas
# print(frutas)

# REMOVER ITENS

#lista.remove: podemos localizar itens e remover (caso haja duplicidade ele remove o que aparece 
# primeiro na lista)
#lista.cout("item")
#lista.pop() = remove o ultimo item da lista
#lista.pop(index = posição na lista)
#del = apaga toda a lista
#del [index] = apaga o item especifico da lista
#frutas.clear = apaga toda a lista
 
# print("Removendo elementos")
# print(frutas.count("morango"))
# frutas.remove("morango")
# print(frutas)

# numros = [3, 5, 77, 4, 10, 24]
# #id = mostra o local na memoria onde a informação esta armazenada
# num1 = 3 
# print(id(num1))
# num2 = num1
# print(id(num2))

# numeros = [3, 5, 77, 4, 10, 24]
# numeros2 = numeros

# numeros2.append("42")
# print(id(numeros))
# print(id(numeros2))

# COPIA DE LISTA

# frutas2 = frutas[:]
# frutas = frutas.copy()
# print(frutas2)
# print(id(frutas))
# print(id(frutas2))

#frutas.clear()
frutas.extend(["jaca", "mamao"])
print(frutas)
frutas.index("coco")
print(frutas.index("coco"))
sorted