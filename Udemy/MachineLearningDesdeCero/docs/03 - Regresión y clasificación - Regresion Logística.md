# Regresión Logística o Clasificación
Intentaremos predecir un valor discreto

![Alt text](img/regresion-clasificacion-logistica-1.png)

Es supervisado!

![Alt text](img/regresion-clasificacion-logistica-2.png)

Los problemas que se clasifican en 0 y 1 se llaman--> Clasificación binaria

Problemas de clasificación multiclase--> y {0,1,2,...,n}

regresion-clasificacion-logistica-3.png
![Alt text](img/regresion-clasificacion-logistica-3.png)

## Representación de la función hipótesis
¡Por qué no se usa la regresión linean con threadshold!

![Alt text](img/regresion-clasificacion-logistica-funcion-hipotesis-1.png)


Ojo, cuando tenemos dataset con valores alejados!, se nos aplana la pendiente de la función lineal y nos da falsos negativos

**Por esto mismo no se usa este métodos!!!!**

## Construcción del modelo

Función sigmoide!!!! g(z)

![Alt text](img/regresion-clasificacion-logistica-construccion-modelo-1.png)
 
## Interpretacióm de la función Hipótesis

![Alt text](img/regresion-clasificacion-logistica-interpretación-funcion-hipotesis-1.png)

![Alt text](img/regresion-clasificacion-logistica-interpretación-funcion-hipotesis-2.png)

![Alt text](img/regresion-clasificacion-logistica-interpretación-funcion-hipotesis-3.png)

## Función de coste I

![Alt text](img/regresion-clasificacion-logistica-interpretación-funcion-coste-I-1.png)
Se generan optimos locales, por lo que no se puede usar la función de coste de la regresion lineal para la funcion de coste de la regresion logística

![Alt text](img/regresion-clasificacion-logistica-interpretación-funcion-coste-I-2.png)




















## Función de coste II

regresion-clasificacion-logistica-interpretación-funcion-coste-II-1.png
![Alt text](img/regresion-clasificacion-logistica-interpretación-funcion-coste-II-1.png)

regresion-clasificacion-logistica-interpretación-funcion-coste-II-2.png
![Alt text](img/regresion-clasificacion-logistica-interpretación-funcion-coste-II-2.png)

## Función de optimización


regresion-clasificacion-logistica-interpretación-funcion-optimizacion-1.png
![Alt text](img/regresion-clasificacion-logistica-interpretación-funcion-optimizacion-1.png)
