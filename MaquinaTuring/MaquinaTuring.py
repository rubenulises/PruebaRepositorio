#Acemos las importaciones que sean necesarios
import re
import os

#Definimos las clases necesarias
def pedirNumeroEntero():
    correcto = False
    num = 0
    while(not correcto):
        try:
            num = int(input("OPCION:"))
            correcto = True
        except ValueError:
            print("-----------------------------------------------------------------------------------------" + "\n" +
                   'Opcion no validad' + "\n" + "VUELVA A INTENTAR"+ "\n" + 
                   "-----------------------------------------------------------------------------------------")
     
    return num
 #Declaramos 
salir = False
opcion = 0
def MT (estado = None,  #Estado de la maquina
                    blanco = None,  #Simbolo Blanco
                    reglas = [],    #Regas de transicion
                    cinta = [],     #Cintas de la Maquina
                    final = None,   #Estado Final 
                    posicion = 0):  #Pasicion de la Maquina

    ul = estado
    #Prevencion de Errores
    if not cinta: cinta = [blanco]
    if posicion < 0 : posicion += len(cinta)
    if posicion >= len(cinta) or posicion < 0 : raise Error ("Mala posicion")
    
    reglas = dict(((s0, v0), (v1, dr, s1)) for (s0, v0, v1, dr, s1) in reglas)
    """
    Estado	 Símbolo leído	  Símbolo escrito	    Mov. 	  Estado sig.
    p(s0)	      1(v0)	          0(v1)            R(dr)	     p(s1)
    """
    while True:
        print (ul, '\t', end = " ")
        for i, v in enumerate(cinta):
            if i == posicion: print ("[%s]"%(v,),end=" ")
            else: print (v,end=" ")
        print()

        if ul == final : break
        if (ul, cinta[posicion]) not in reglas : break

        (v1,dr,s1) = reglas [(ul, cinta[posicion])]
        cinta[posicion] = v1 # Reescribe el simbolo 
    
    #Cabezal
        if dr == 'left': 
            if posicion > 0 : posicion -= 1
            else: cinta.insert(0, blanco)
        if dr == 'right': 
            posicion += 1
            if posicion >= len(cinta): cinta.append(blanco)
        ul = s1
print("")
print("A G R E G U E E S T A L I N E A D E C O D I G O")
print("*****************************************************")
print("*********** M a q u i n a d e t u r i n g ***********")
print("*****************************************************")
while not salir:
    print()
    print("-----------------------------------------------------------------------------------------")
    print("Elija una opcion")
    print ("1. Maquina Turing." +"\n"+ 
           "2. Maquina Turing Incremento." + "\n" +
           "3. Maquina Turing Resta." + "\n" +
           "4. Maquina Turing Suma." + "\n" +
           "5. Salir."
          )
    print("-----------------------------------------------------------------------------------------")
   
    #Concatenamos 
    opcion = pedirNumeroEntero()
    #Declaramos un IF para hacer las operaciones propuestas por el maestro
    if opcion == 1:
        print()
        entra1 = input ("Maquina Turing"  +"\n" + "Ingrese un numero:" ) #1011
        print()
        MT (estado = 'p', #estado inicial de la maquina de turing
                    blanco = 'b', #simbolo blanco de el alfabeto dela cinta
                    cinta = list(entra1),#inserta los elementos en la cinta
                    final = 'q',  #estado valido y/o final
                    reglas = map(tuple,#reglas de transicion
                                 [
                                  "p 1 x right p".split(),
                                  "p 0 0 right p".split(),
                                  "p b b right q".split(),
                                 ]   
                                )
                  )
         
    elif opcion == 2:
         print()
         print("Incremento")
         entra2 = input ("Ingrese un numero:")#111
         print()
         MT (estado = 's1', #estado inicial de la maquina de turing
                blanco = 'b', #simbolo blanco de el alfabeto dela cinta
                cinta = list(entra2),#inserta los elementos en la cinta
                final = 's6',  #estado valido y/o final
                reglas = map(tuple,#reglas de transicion
                              [
                              "s1 1 b right s2".split(),
                              "s2 1 1 right s2".split(),
                              "s2 b b right s3".split(),
                              "s3 1 1 right s3".split(),
                              "s3 b 1 left s4".split(),
                              "s4 1 1 left s4".split(),
                              "s4 b b left s5".split(),
                              "s5 1 1 left s5".split(),
                              "s5 b 1 right s6".split(),
                          ]   
                         )
             ) 

    elif opcion == 3:
         print()
         print("Resta ")
         entra2 = input ("Resta de A-B-N:")#111
         print()
         MT (estado = 'q0', #estado inicial de la maquina de turing
                blanco = 'b', #simbolo blanco de el alfabeto dela cinta
                cinta = list(entra2),#inserta los elementos en la cinta
                final = 'q18',  #estado valido y/o final
                reglas = map(tuple,#reglas de transicion
                          [
                          "q0 1 1 right q1".split(),
                          "q1 1 1 right q1".split(),
                          "q1 0 x right q2".split(),
                          "q2 1 0 right q2".split(),
                          "q2 0 x right q2".split(),
                          "q2 b b left q3".split(),
                          "q3 0 0 left q3".split(),
                          "q3 x 0 right q4".split(),
                          "q4 0 x right q5".split(),
                          "q5 b b left q6".split(),
                          "q5 0 0 left q8".split(),
                          "q6 x b left q7".split(),
                          "q7 0 0 left q8".split(),
                          "q8 0 0 left q8".split(),
                          "q8 x 0 right q4".split(),
                          "q8 1 1 right q9".split(),
                          "q9 0 0 right q9".split(),
                          "q9 b b left q10".split(),
                          "q10 0 0 left q11".split(),
                          "q11 0 0 left q11".split(),
                          "q11 1 0 right q12".split(),
                          "q12 0 0 right q13".split(),
                          "q13 0 0 right q14".split(),
                          "q14 0 0 right q14".split(),
                          "q14 b b left q15".split(),
                          "q15 0 b left q16".split(),
                          "q16 0 b left q11".split(),
                          "q13 b b left q17".split(),
                          "q17 0 b left q17".split(),
                          "q17 b b right q18".split(),
                          "q17 1 1 right q18".split(),
                          ]   
                         )
             )
    
    elif opcion == 4:
         print()
         print("Suma de A+B-N")
         entra3 = input ("Ingrese el numero a sumar:")
         print()
         MT (estado = 'q0', #estado inicial de la maquina de turing
                blanco = 'b', #simbolo blanco de el alfabeto dela cinta
                cinta = list(entra3),#inserta los elementos en la cinta
                final = 'q8',  #estado valido y/o final
                reglas = map(tuple,#reglas de transicion
                          [
                          "q0 1 1 right q1".split(),
                          "q1 1 1 right q1".split(),
                          "q1 0 0 right q1".split(),
                          "q1 b b left q2".split(),
                          "q2 1 1 left q2".split(),
                          "q2 0 1 right q3".split(),
                          "q3 1 0 right q4".split(),
                          "q4 b b left q4".split(),
                          "q4 0 0 left q4".split(),
                          "q4 1 1 left q5".split(),
                          "q5 1 1 left q5".split(),
                          "q5 0 1 right q3".split(),
                          "q5 b b right q6".split(),
                          "q6 1 1 right q6".split(),
                          "q6 0 b right q7".split(),
                          "q7 0 b right q7".split(),
                          "q7 b b left q8".split(),
                                                         
                          ]   
                         )
             )

    elif opcion == 5:
            salir = True
    else:
        print ("VUELVA A INTENTAR" + "\n" + "Elija una opcion entre 1 al 3")
 
print ("-----------------------------------------------------------------------------------------" + "\n" +
        "TENGA UN BUEN DIA"  + "\n" + 
        "-----------------------------------------------------------------------------------------" + "\n" +
        "ELABORADO POR:" + "\n" + 
        "Ruben Ulises Arce Nahuat." 	+ "\n" + 	
        "Beatriz Adriana Cohuo Chan." + "\n" + 		
        "Francisco Javier Reyes Carranza."	 + "\n" + 
        "-----------------------------------------------------------------------------------------")