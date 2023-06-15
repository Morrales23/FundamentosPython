def saluda():
    print("Hola Developer!")
    
    
    saluda()
    
def duplica(number):
        print(number * 2)
        
duplica(23)
        
def suma(num, num2):
        print(num + num2)
            
            
suma(12, 34)

def listas_drinks(d1 = "beer", d2 = "water"):
    print(d1)
    print(d2)
    
    
listas_drinks("Tequila","¿Juise")
listas_drinks("Tequila")
listas_drinks()
listas_drinks(d2='soda', d1='vodka')


def get_list():
    return [1, 2, 3]

list_gotten = get_list()
print(list_gotten)

def resta(num1 , num2):
    return num1 -num2


result = resta(13, 2)
print (result)

def duplica_lista(lista):
    new_list = []
    for item in lista:
        new_list.append(item * 2)
    return new_list
    
my_list = [1, 2, 3, 4, 5]
print(my_list)
new_list = duplica_lista(my_list)
print(new_list)

















    
    


