import random as r ##importamos random para hacer oracionRandom()

articulos = ["la","el","una"]
sujeto = ["perro","gato","niña","juan","pedro","daniel","maria"]
conectivos = ["con","y"]
verbo = ["es","son","corre","corren","estudia","estudian","come","comen","juegan","juega"]
predicado = ["rapido","rapidos","abogado","abogados","ingeniero","ingenieros","arroz"," matematicas","baloncesto",]
## instanciamos limitados articulos, sujetos,conectivos,verbos y predicados(se pueden meter todos los que quieras)


def continuar():## para hacer el "presione enter para continuar... lo que nos permite ver el resultado con el tiempo que queramos"
  print("\n\nPresione Enter para continuar...")
  x = input()
  if input != "":
    Menu()

def verificarinput():
  print("\n Ingrese una oracion para verificar :  ", end= " ")
  msg1 = input().lower() ## el input lo pasamos a minusculas para evitar errores 
  if msg1.isnumeric(): ## verificamos que el input no sean numeros
        print("Porfavor ingrese letras solamente")
        verificarinput() ## llamamos la funcion para que el usuario pueda poner una oracion correctamente

  else:
        msg = msg1.split() ## separamos palabra por palabra
        n = 0## es la posicion de la palabra a evaluar en la oracion
        comprobarsimple(msg,n)



def comprobarsimple(msg,n):

    if msg[n] in articulos: ##verifica si la primera palabra es un articulo1
      n = n+1
        

        
    elif msg[n] in sujeto: ##verifica si la n palabra es un sujeto
        n= n+1
        
        if msg[n] in conectivos:##verifica si lo ¿n es un conectivo
          n= n+1
          
          if msg[n] in sujeto:##verifica si despues del conectivo hay un sujeto
            n= n+1
            
        if msg[n] in verbo:##verifica que la palabra n sea un verbo
          n= n+1


          if n < len(msg): ##Verifica si la oracion termina o sigue
            
            if msg[n] in predicado:
              print("Oracion valida1")
              continuar()
            else:
              print("invalido, revisa la ", n+1 ,"palabra")
              continuar()
          else:
            print("Oracion valida2")
            continuar()
        else:
          print("invalido, revisa la ", n+1 ,"palabra")
          continuar()
    else:
      print("invalido, revisa la ", n+1, "palabra")
      continuar()
      ## ¿Por qué tantos else?: Para poder indicar exactamente donde está el error
  


  
def oracionRandom():
  print(r.choice(articulos) +" "+ r.choice(sujeto) +" "+ r.choice(verbo) +" "+ r.choice(predicado))
  continuar()
  


def Menu():
      print("▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂\n")
      print("▆ Bienvenido al verificador de oraciones    ▆\n")
      print("▆▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▆\n")
      print("▆                                           ▆\n")
      print("▆ 1. Verificar oracion                      ▆\n")
      print("▆ 2. Generar oracion aleatoria              ▆\n")
      print("▆ 3. Leer Descripcion y restricciones       ▆\n")
      print("▆     del programa                          ▆\n")
      print("▆ 0. Salir                                  ▆\n")
      print("▆▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▆\n")
      print("Ingrese una opcion: ", end= " ")
      while 0==0:

        opcion = 0
        opcion = input()
        try:
          opcion = int(opcion)
          if opcion == 1:
            verificarinput()
          elif opcion == 2:
            oracionRandom()
          elif opcion == 3:
            print("Este programa tiene un numero limitado de Articulos, Sujetos, Conectivos, verbos y predicados y son:")
            print("Articulos: ", articulos)
            print("Sujetos: ", sujeto)
            print("Conectivos: ", conectivos)
            print("Verbos: " , verbo)
            print("Predicados: " , predicado)
            print("\n Nota: El programa aún no distingue generos, ni cantidades ")
            continuar()
          elif opcion == 0:
            print("\n Saliendo del programa...")
            print(quit())

        except ValueError:
          print("Ingrese una opcion valida: ", end="")


      
    
    

Menu()
