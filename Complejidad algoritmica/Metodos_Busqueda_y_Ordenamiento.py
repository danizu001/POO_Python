import random
import time

def busqueda_lineal(lista, objetivo):
    match = False
    i=0
    for elemento in lista: # O(n)
        i+=1
        if elemento == objetivo:
            match = True
            break

    return (match,i)

def busqueda_binaria(lista,comienzo,final,objetivo,j):
    print(f'buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')
    j+=1
    if comienzo > final:
        return False,j
    medio = (comienzo + final) // 2    
    if lista[medio]==objetivo:
        return True,j    
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio+1, final, objetivo,j)
    elif lista[medio] > objetivo:
        return busqueda_binaria(lista,comienzo,medio-1,objetivo,j)

def Ordenamiento_burbuja(lista):
    for i in range(len(lista)):
        for j in range(len(lista)-i-1):
            if lista[j]>lista[j+1]:
                savior=lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=savior
    return lista
            
def Ordenamiento_Insercion(lista):
    for i in range(1,len(lista)):
        while lista[i] < lista[i-1]:
            lista[i],lista[i-1]=lista[i-1],lista[i]
            i-=1
    return lista
def Ordenamiento_Mezcla(lista):
    if len(lista) >1:
        medio=len(lista)//2
        izquierda=lista[:medio]
        derecha=lista[medio:]
        
        print(izquierda,'*'*5,derecha)
        
        izquierda=Ordenamiento_Mezcla(izquierda)
        derecha=Ordenamiento_Mezcla(derecha)
  
        i=0
        j=0
        
        k=0
        
        while i<len(izquierda) and j<len(derecha):
            if izquierda[i]<derecha[j]:
                lista[k]=izquierda[i]
                i+=1
            else:
                lista[k]=derecha[j]
                j+=1
            k+=1
        while i<len(izquierda):
            lista[k] = izquierda[i]
            i+=1
            k+=1
        while j<len(derecha):
            lista[k] = derecha[j]
            j+=1
            k+=1
        print(f'izq:{izquierda},der:{derecha}')
        print(lista)
        print('*'*50)
        
    return lista            
if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano sera la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

    lista =Ordenamiento_Mezcla([random.randint(0, 100) for i in range(tamano_de_lista)])
    first=time.time()
    encontrado,j = busqueda_binaria(lista,0,len(lista),objetivo,0)
    finalf=time.time()
    encontrado,i = busqueda_lineal(lista, objetivo)
    finals=time.time()
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
    print(f'Busqueda binaria se demora{finalf-first} con {j} iteraciones')
    print(f'Busqueda lineal se demora{finals-finalf} con {i} iteraciones')