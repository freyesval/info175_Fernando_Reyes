#! /bin/bash
#Declara un arreglo con 4 elementos
ARRAY=( 'Debian Linux' 'Redhat Linux' 'Ubuntu Linux')
#Obtener el numero de elementos
ELEMENTS=${#ARRAY[@]}
#IMPRIMIR TODOS LOS ELEMENTOS CON UN FOR
for ((i=o;i<$ELEMENTS;I++ )); do
	echo ${ARRAY[${i}]}
done