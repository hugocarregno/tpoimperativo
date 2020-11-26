#Realizado por Carreño Hugo

#TRABAJADORES
#Se cuenta con la siguiente información:

#Crear una archivo de texto que contenga las siguientes listas
"""●Lista de tareas. Donde una tarea está definida por una descripción (String) y un nivel de complejidad (número entero). tarea(descripcion, complejidad).
●Lista de trabajos. Donde un trabajo está definida por un trabajador (número de DNI) y una tarea. trabajo(trabajador, tarea).
●Lista de lugares de trabajo(poder judicial,poder legislativo,poder ejecutivo o prensa) de los trabajadores.
Para cada trabajador (número de DNI) se define su lugar de trabajo (String). poder(trabajador, poder).
●Lista de partidos a los que pertenece cada trabajador.
Para cada trabajador (número de DNI) se conoce el partido al que está afiliado (String). partido(trabajador, partido).

a)Definir las estructuras de datos para la información anterior.
b)Definir ejemplos concretos para los datos anteriores.
"""


"""
c)Definir las siguientes funciones:

1.Conocer todas las tareas estresantes. Se considera una tarea estresante si su complejidad es mayor a 5.
"""

import ast

def extraccion(filtro):
  archivo.seek(0)
  n = (archivo.read()).find(filtro)
  if(filtro == "tarea"):
    n += 8
  if(filtro == "trabajo"):
    n += 21
  if(filtro == "poder"):
    n += 30
  if(filtro == "partido"):
    n += 43
  archivo.seek(n)
  aux = (archivo.read()).find('}') - n + 1
  leer = aux + n
  archivo.seek(n)
  return leer

archivo = open('datos.txt','r')

leer = extraccion("tarea")

tarea = ast.literal_eval(archivo.read(leer))
lista_tareas = [tarea]

leer = extraccion("trabajo")

trabajo = ast.literal_eval(archivo.read(leer))
lista_trabajos = [trabajo]

leer = extraccion("poder")

poder = ast.literal_eval(archivo.read(leer))
lista_poder = [poder]

leer = extraccion("partido")

partido = ast.literal_eval(archivo.read(leer))
lista_partidos = [partido]

archivo.close()

def tareas_estresantes():
  resultado = []
  for tarea, complejidad in (lista_tareas[0]).items():
    if(complejidad>5):
      #print(tarea," --> ",complejidad,"\n")
      resultado.append((tarea,complejidad))
  return resultado

"""
2.Se quiere conocer a todas las personas que están estresadas. Se considera a una persona estresada si realiza al menos una tarea estresante o si pertenece al poder ejecutivo.
"""

def personas_estresadas():
  
  resultado = []
  trabajadores = list(lista_trabajos[0].items())
  trabajos = list(lista_trabajos[0].values())
  i = 0

  for persona, tarea in trabajadores:
    #print(persona, tarea)
    j=0
    max_tarea = len(tarea)
    
    for tareas in tareas_estresantes():
      if(max_tarea>1):
        j = 0
        while(j != max_tarea):
          if(tarea[j] == tareas[0]):
            resultado.append(persona)
          j += 1
      else:
        if(trabajos[i][0] == tareas[0]):
          resultado.append(persona)
    i += 1

  for persona,poder in (lista_poder[0]).items():
    if(poder == "ejecutivo"):
      resultado.append(persona)

  return set(resultado)

"""
3.Se quiere conocer si un trabajador se encuentra en peligro, teniendo en cuenta que todas las personas estresadas que no pertenecen al poder legislativo se encuentran en peligro, como así también, todas las que trabajan en la prensa.
"""

def trabajador_en_peligro(trabajador):

  resultado = "No esta en peligro"
  for persona in personas_estresadas():
    if(lista_poder[0][persona] != "legislativo" and persona == trabajador):
      resultado = "Esta en peligro"
  #for persona,poder in (lista_poder[0]).items():
  if(lista_poder[0][trabajador] == "prensa"):
    resultado = "Esta en peligro"

  return resultado

"""
4.Los trabajadores tienen enemigos natos.
Estos están dados por los poderes en los que trabaja cada uno. Desarrollar una solución teniendo en cuenta que:
a.Los trabajadores del poder judicial son enemigos de los del poder ejecutivo.
b. Los trabajadores del poder legislativo:
(1) son enemigos de los del poder judicial;
(2) son enemigos de los legisladores de otros partidos
c. Los trabajadores de la prensa son enemigos de todos (menos de si mismos).
Se desea todas las personas enemigas entre si.
"""

def son_enemigos(trabajador1,trabajador2):
  
  resultado ="No son enemigos"
  
  if((lista_poder[0][trabajador1] == "ejecutivo" and
  lista_poder[0][trabajador2] == "judicial") or (lista_poder[0][trabajador1] == "judicial" and lista_poder[0][trabajador2] == "ejecutivo")):
    resultado = "Son enemigos"
  
  return resultado

def son_enemigos2(trabajador1,trabajador2):
  
  resultado ="No son enemigos"
  
  if((lista_poder[0][trabajador1] == "legislativo" and
  lista_poder[0][trabajador2] == "judicial") or (lista_poder[0][trabajador1] == "judicial" and lista_poder[0][trabajador2] == "legislativo") or (lista_poder[0][trabajador1] == "legislativo" and lista_poder[0][trabajador2] == "legislativo" and lista_partidos[0][trabajador1] != lista_partidos[0][trabajador2])):
    resultado = "Son enemigos"
  
  return resultado

def son_enemigos3(trabajador1,trabajador2):
  
  resultado ="No son enemigos"
  
  if((lista_poder[0][trabajador1] == "prensa" and lista_poder[0][trabajador2] and trabajador1 != trabajador2) or (lista_poder[0][trabajador2] == "prensa" and lista_poder[0][trabajador1] and trabajador2 != trabajador1)):
    resultado = "Son enemigos"
  
  return resultado

"""
5.Encontrar el trabajador que tiene la tarea con mayor complejidad.
"""

def trabajador_tarea_compleja():
    
  resultado = []
  i = 0
  maximo = max((lista_tareas[0]).values())
  
  for tarea,complejidad in (lista_tareas[0]).items():
    if(complejidad == maximo):
      for persona, tareas in (lista_trabajos[0]).items():
        if(len(tareas)>1):
          while(i != len(tareas)):
            i += 1
          i = 0
        else:
          if(lista_trabajos[0][persona][0] == tarea):
            resultado.append(persona)

  return resultado

"""
6.Encontrar a todos los trabajadores que tienen una única tarea.
"""

def unica_tarea():
  
  resultado = []
  for persona, tarea in (lista_trabajos[0]).items():
    if(len(tarea) == 1):
      resultado.append(persona)
  
  return resultado

print("Tareas estresantes\n")
lista_tareas_estresantes = tareas_estresantes()

for tarea, complejidad in lista_tareas_estresantes:
    if(complejidad>5):
      print(tarea," --> ",complejidad,"\n")

print("Personas estresadas")
lista_personas_estresadas = personas_estresadas()
print(lista_personas_estresadas)

print("\nTrabajador en peligro")
resultado = trabajador_en_peligro(35555555)
print(resultado)

print("\nTrabajadores enemigos")
resultado = son_enemigos(30000000,32222222)
print(resultado)

print("\nTrabajadores enemigos2")
resultado = son_enemigos2(33333333,34444444)
print(resultado)

print("\nTrabajadores enemigos3")
resultado = son_enemigos3(35555555,34444444)
print(resultado)

print("\nListado de pares de trabajadores enemigos")
trabajadores = trabajo.keys()
enemigos = []
for t in trabajadores:
  for t2 in trabajadores:
    if(son_enemigos(t,t2) == "Son enemigos"):
      enemigos.append([t,t2])
    if(son_enemigos2(t,t2) == "Son enemigos"):
      enemigos.append([t,t2])
    if(son_enemigos3(t,t2) == "Son enemigos"):
      enemigos.append([t,t2])

for resultado in enemigos:
  print(resultado)


print("\nTrabajador con tarea compleja")
resultado = trabajador_tarea_compleja()
print(resultado)

print("\nUnica tarea")
resultado = unica_tarea()
print(resultado)