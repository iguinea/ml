# Regresión Lineal



![Alt text](img/regresion-clasificacion-lineal-1.png)

![Alt text](img/regresion-clasificacion-lineal-2.png)

Caracteristicas de entrada: features
Caracteristicas de salida: target
Conjunto de datos: dataset

x1, x2, x3,... diferentes caracteristicas o variables de entrada

![Alt text](img/regresion-clasificacion-lineal-3.png)

## Función hipótesis

![Alt text](img/regresion-clasificacion-lineal-funcion-hipotesis-1.png)

Si solo tenemos una característica de entrada --> Regression linean univariable

Si tenemos varias: regresion linean multi variable

y(x1,x2,...,xn)= o0 + o1*x1 + o2*x2 + ... + o2*xn

## Construcción del modelo

![Alt text](img/regresion-clasificacion-lineal-modelo-1.png)

## Función de coste

**Mean Square Error (MSE)**

![Alt text](img/regresion-clasificacion-lineal-funcion-coste-1.png)

## Función de optimización

**Gradient descent**

Su objetivo es minimizar el resultado de la función de coste/error

![Alt text](img/regresion-clasificacion-lineal-funcion-optimizacion-1.png)

alfa = learning rate
El learning rate se suele poner a 0,5 (1/2)

![Alt text](img/regresion-clasificacion-lineal-funcion-optimizacion-2.png)
Hemos obtenido 3, vamos a repetir el proceso con x=3

![Alt text](img/regresion-clasificacion-lineal-funcion-optimizacion-3.png)

Lo hacemos para teta0 (o0)y teta1 (o1)
![Alt text](img/regresion-clasificacion-lineal-funcion-optimizacion-4.png)


## Jupyter Notebook 4
Haremos el ejemplo de dicho notebook

# Links
[Linear Regression Reference](https://scikit-learn.org/stable/modules/classes.html#module-sklearn.linear_model)
