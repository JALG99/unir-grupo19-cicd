# Repo para EIEC - DevOps - UNIR

Este repositorio nos servirá para demostrar el uso de Git en la asignatura de EIEC y muchas cosas mas.

---

Los comandos del Makefile funcionarán en Linux y MacOS. En caso de usar Windows, necesitarás adaptarlos o ejecutarlos en una máquina virtual Linux.

## Ejecución

python3 main.py <filename> <dup>
  filename: **ruta** al fichero que contiene la lista de palabras, una por línea
  dup: **yes|no**, yes para eliminar palabras duplicadas, no para mantener la lista


## Explicación del programa. 
# UNIR Entornos de Integracion y Entrega Continua - Grupo 19

Este programa esta diseñado en python y lo que hace es leer una lista de palabras desde un archivo, las procesa y opcionalmente elimina palabras duplicadas. Finalmente las muestra en orden alfabetico. 

## Ejemplo de ejección. 

# Lista de palabras:
manzana
pera
manzana
platano

## Output 1: Al ejecutar el programa sin eliminar duplicadas
# python main.py ejemplo1.txt no

Se leerán las palabras del fichero ejemplo1.txt
['manzana', 'manzana', 'pera', 'platano']

## Output 2: Eliminando duplicados
# python main.py ejemplo1.txt yes
Se leerán las palabras del fichero ejemplo1.txt
['manzana', 'pera', 'platano']

