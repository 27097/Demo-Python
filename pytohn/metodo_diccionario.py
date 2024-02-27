#metodos para diccionarios

#1) keys() -> devuelve las claves
#2) get()  -> devuelve el valor de una clave
#3) clear() -> elimina tods los elementos
#4) pop() -> elimina un elemento
#5) items() -> para iterar el diccionario

diccionario = {
    'name':'Roberto',
    'lastname':'Perez',
    'subs':1000000
}
# 1
claves = diccionario.keys() #nos retorna un objeto dict_items que se puede iterar

# 2
get_by_key = diccionario.get('name') # me retora el valor que tiene la key que le pase por marametro // si no lo encuentra me retorna none
get_by = diccionario['name'] # me retorna lo mismo que si usara el get() // si no lo encuentra me arroja una excepcion

# 3
# diccionario.clear() #elimina todos los elementos del diccionario

# 4
diccionario.pop('name') #eliminando un elemento del diccionario pasando la key por parametro
# diccionario.pop("lastname","name") #eliminando varios elemento del diccionario pasando la key por parametro
 
# 5
diccionario_iterable = diccionario.items() 

 



print(diccionario_iterable)