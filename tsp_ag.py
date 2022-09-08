import random, numpy as np, math
import operator, pandas as pd, matplotlib.pyplot as plt
import time

def run():
    pass

def calculo_distancias2():

    distancias = [] #Cromosomas
    distancias.clear()

    for i in range(100):
        contador = 0
        d = 0

        while contador < 19:
            punto_1 = poblacion[i][contador]
            punto_2 = poblacion[i][contador + 1]

            d += math.sqrt(((ciudades[punto_2][1] - ciudades[punto_1][1])**2 + (ciudades[punto_2][2] - ciudades[punto_1][2])**2))

            contador +=1

        distancias.append(d)
    
    return distancias

def calculo_distancias(poblacion_cal):

    distancias = [] #Cromosomas
    distancias.clear()

    for i in range(100):
        contador = 0
        d = 0

        while contador < 19:
            punto_1 = poblacion_cal[i][contador]
            punto_2 = poblacion_cal[i][contador + 1]

            d += math.sqrt(((ciudades[punto_2][1] - ciudades[punto_1][1])**2 + (ciudades[punto_2][2] - ciudades[punto_1][2])**2))

            contador +=1

        distancias.append(d)
    
    return distancias

def calculo_dist_sub_opt(array_distancias):
    d_array = calculo_distancias(array_distancias)

    torneo = random.sample(d_array,5) # 5 seleccionados al azar
    ganador = min(torneo)

    return ganador


def generar_hijos(nueva_gen):
    array_mut_aux = np.array(nueva_gen)

    for j in range(100): #Reproduccion, Generación de hijos
        
        numero_aleatorio = random.randint(0, 1)

        if numero_aleatorio == 0: # Mutación 1
            numero_aleatorio_1 = random.randint(0, 8)
            numero_aleatorio_2 = random.randint(9, 18)
            
            array_mut_aux[j][numero_aleatorio_1] = nueva_gen[j][numero_aleatorio_2]
            array_mut_aux[j][numero_aleatorio_1 + 1] = nueva_gen[j][numero_aleatorio_2 + 1]

            array_mut_aux[j][numero_aleatorio_2] = nueva_gen[j][numero_aleatorio_1]
            array_mut_aux[j][numero_aleatorio_2 + 1] = nueva_gen[j][numero_aleatorio_1 + 1]

        else: # Mutación 2
            numero_aleatorio_3 = random.randint(0,10)
            pivote_1 = random.randint(2, (18 - numero_aleatorio_3))
            pivote_2 = pivote_1

            cont_k = 0
            while cont_k < (numero_aleatorio_3 + 1):
                array_mut_aux[j][pivote_1 + cont_k] = nueva_gen[j][((pivote_1 + numero_aleatorio_3) - cont_k)]

                cont_k += 1
    return array_mut_aux



def mutacion(array_mut):
    array_mut_aux.clear()
    array_mut_aux = array_mut
    numero_aleatorio = random.randint(0, 1)

    if numero_aleatorio == 0:
        numero_aleatorio_1 = random.randint(0, 8)
        numero_aleatorio_2 = random.randint(9, 18)
        
        array_mut_aux[numero_aleatorio_1] = array_mut[numero_aleatorio_2]
        array_mut_aux[numero_aleatorio_1 + 1] = array_mut[numero_aleatorio_2 + 1]

        array_mut_aux[numero_aleatorio_2] = array_mut[numero_aleatorio_1]
        array_mut_aux[numero_aleatorio_2 + 1] = array_mut[numero_aleatorio_1 + 1]
    else:
        numero_aleatorio_3 = random.randint(0,10)
        pivote_1 = 20 - numero_aleatorio_3
        pivote_2 = 20 - (pivote_1 + 2)
        numero_aleatorio_4 = random.randint(2,pivote_2)

        for i in range(numero_aleatorio_3):
            array_mut_aux[numero_aleatorio_4 + i] = array_mut[numero_aleatorio_2]

    return array_mut_aux


if __name__ == '__main__':
    run()

    x1 = []
    y1 = []

    ciudades =  np.array([ [0,0,0],
        [1,1,3], [2,2,5], [3,2,7], [4,4,2], [5,4,4], 
        [6,4,7], [7,4,8], [8,5,3], [9,6,1], [10,6,6],
        [11,7,8], [12,8,2], [13,8,7], [14,9,3], [15,10,7],
        [16,11,1], [17,11,4], [18,11,6], [19,12,7], [20,13,5]])
    


    for i in range (len(ciudades)):
        print(ciudades[i])

    distancia_total = [] #Cromosomas
    distancia_total.clear()
    pob = []
    pob.clear()
    poblacion = []
    poblacion.clear()
    hijos = [] 
    hijos.clear()
    array_mut_aux = []
    array_mut_aux.clear()
    gen_nueva_gen = []
    gen_nueva_gen.clear()
    ganador_generacion = []
    ganador_generacion.clear()
    indice = 0
    cityx = []
    cityx.clear()
    cityy = []
    cityy.clear()

    distancia_sub_optima = []

    for comienzo in range(100):

        for start in range(100): 

            pob.clear()
            

            if comienzo == 0: #Generacion de los primeros padres
                for i in range(0, 100):
                    ciudad = random.sample(range(1,21),20)
                    pob.append(ciudad)
                poblacion = np.array(pob)

            else:
                poblacion = np.array(generar_hijos(gen_nueva_gen))

            distancia_total = calculo_distancias(poblacion)

            torneo = random.sample(distancia_total,5) # 5 seleccionados al azar
            ganador = min(torneo)


            indice = distancia_total.index(ganador)

            distancia_total.clear()#
            
            hijos.append(poblacion[indice])
            
            pob.clear()

        gen_nueva_gen = np.array(hijos)

        dis = 0
        dis = calculo_dist_sub_opt(gen_nueva_gen)
        ganador_generacion.append(gen_nueva_gen[indice])

        hijos.clear()

        print('Ganador generación ' + str(comienzo+1) + ' es ' + str(dis))

        distancia_sub_optima.append(dis)

        x = [dis]
        y = [ganador_generacion[comienzo]]

        print(ganador_generacion[comienzo][0])

        for i in range(20):
            v = False
            j = 0
            while v != True:
                if ganador_generacion[comienzo][i] == ciudades[j+1][0]:
                    cityx.append(ciudades[j+1][1])
                    cityy.append(ciudades[j+1][2])
                    v = True
                else:
                    j = j+1
        plt.rcParams["figure.figsize"] = (15,5)
        plt.subplot(1, 2, 1)
        
        # plt.figure(1)
        plt.scatter(comienzo + 1, dis)
        plt.xticks(range(len(distancia_sub_optima)))
        # plt.xlim(0, 102)
        plt.title("Mejores distancias")
        plt.xlabel("Generación") 
        plt.ylabel("Distancia")

        plt.subplot(1, 2, 2)
        plt.plot(cityx, cityy, 'o-')
        plt.title('Mejor ruta')
        plt.xlabel("Eje x") 
        plt.ylabel('Eje y')
        # plt.clf()
        plt.pause(0.2)
        
        plt.cla()
     
        cityx.clear()
        cityy.clear()

    print('fin')
    