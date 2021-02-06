from Libros import libros
from Biblioteca import biblioteca
def Crear_libro():
    nombre=input("Digite el nombre del libro")
    autor=input("Digite el nombre del autor")
    genero=input("Especifique el Genero")
    precio=input("Digite el precio del libro")
    
    return libros(nombre,autor,genero,precio)
    
libro1=libros("Climbing","Hortua","Aventura",15000)
libro2=libros("Programando","Daniel","Informática",20000)
libro3=libros("Aprendiendo","Dennis","Software",25000)
biblioteca=biblioteca("Luis Angel")
biblioteca.Agregar_libro(libro1,3)
while True:
    print("Bienvenido a " + biblioteca.nombre + '\n')
    cli=int(input("Desea:\n 1. Agregar_libro \n 2. Prestar_libro \n 3. Vender_libro \n 4. Buscar_libro \n" ))
    if cli==1:
        cant=int(input("Que cantidad del mismo libro que desea agregar \n"))
        biblioteca.Agregar_libro(Crear_libro(),cant)
    if cli==2:
        cant=int(input("Que cantidad del mismo libro que desea para prestamo \n"))
        eti=int(input("Digite la etiqueta del libro si no la conoce oprima 0 \n"))
        if eti==0:
            busq=input("Busque por nombre de autor,libro o genero \n")
            print(biblioteca.Buscar_libro(busq))
        elif eti!=0:
            biblioteca.Prestar_libro(biblioteca.libro[eti-1],cant)
    if cli==3:
        cant=int(input("Que cantidad del mismo libro que desea para venta \n"))
        eti=int(input("Digite la etiqueta del libro si no la conoce oprima 0 \n"))
        if eti==0:
            busq=input("Busque por nombre de autor,libro o genero \n")
            biblioteca.Buscar_libro(busq)
        elif eti!=0:
            biblioteca.Vender_libros(biblioteca.libro[eti-1],cant)
    if cli==4:
        busq=input("Busque por nombre de autor,libro o genero \n")
        print(biblioteca.Buscar_libro(busq))