#%%

def SoyMejor(personaA,personaB):

    if personaA[0] != personaB[0]:

        if int(personaA[2]) > int(personaB[2]):
            return True
        
        elif int(personaA[2]) < int(personaB[2]):
            return False
        else:
            pass #case equal grade
    else:

        if personaA[2] >= personaB[2]:
            return True
        else:
            return False
        
def espacioGanador(ganador1, ganador2, ganador3):
    uno = ganador1
    dos = ganador2
    tres = ganador3
    nuevo2 = uno
    nuevo3 = dos
    nuevo4 = tres
    return nuevo2, nuevo3, nuevo4

n = int(input())

ganador1 = []
ganador2 = []
ganador3 = []
ganador4 = []
for envio in range(n):

    linea = input().split()


    if len(ganador1)== 0:
        ganador1 = linea
    elif len(ganador2) == 0:

        if SoyMejor(linea,ganador1):
            dos = ganador1
            ganador1 = linea
            ganador2 = dos
        else:
            ganador2 = linea

    elif len(ganador3) == 0:

        if SoyMejor(linea,ganador2):

            if SoyMejor(linea,ganador1):

                dos = ganador1
                tres = ganador2
                
                ganador1 = linea
                ganador2 = dos
                ganador3 = tres
            else:
                tres = ganador2
                
                ganador2 = linea
                ganador3 = tres
            



        ganador3 = linea
    elif len(ganador4) == 0:
        ganador4 = linea
    else:
        pass



    if len(ganador1) != 0:
        
        if SoyMejor(linea,ganador1):
            ganador2,ganador3,ganador4 = espacioGanador(ganador1,ganador2,ganador3)
            ganador1 = linea
        
            

    elif len(ganador3) != 0:
        
        if SoyMejor(linea):
            pass






    
    # print(linea)
    

    

    

