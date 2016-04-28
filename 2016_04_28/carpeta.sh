#!/bin/bash

fecha=$(date +"%Y_%m_%d")
pwd=$(pwd)


echo "Ingrese carpeta a respaldar"
read Fuente
echo "Ingrese carpeta de destino"
read Destino 

tar -cvf $fecha"_$Fuente".tar $Fuente #Se crea el archivo .tar a respaldar 

cp $pwd/$fecha"_$Fuente".tar $Destino #y luego se copia en la carpeta de destino en HOME



