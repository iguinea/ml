# Introducción

Nos permite hacer tareas de regresion y clasificacion

Funciona bien para conjuntos de datos pequeños y complejos

![Alt text](img/svm-intro--1.png)

## Conjuntos de datos linealmente separables:

* En un conjunto de datos linealmente separable, es posible trazar un límite de decisión lineal que pueda separar perfectamente las diferentes clases.
* Un ejemplo clásico es cuando las dos clases de datos se pueden separar utilizando una línea recta en un plano bidimensional o un hiperplano en espacios de mayor dimensión.
* Los algoritmos de clasificación lineal, como la regresión logística o las máquinas de vectores de soporte (SVM) con un kernel lineal, son apropiados para conjuntos de datos linealmente separables.

## Conjuntos de datos no linealmente separables:

* En un conjunto de datos no linealmente separable, no es posible trazar un límite de decisión lineal que pueda separar perfectamente las clases.
* Se necesitan límites de decisión más complejos, no lineales, para separar las clases de manera efectiva.
* Algoritmos como las máquinas de vectores de soporte con kernel no lineal, redes neuronales con capas no lineales (como las capas ocultas con funciones de activación no lineales), y otros métodos no lineales pueden ser más apropiados para manejar conjuntos de datos no linealmente separables.

La naturaleza lineal o no lineal de un conjunto de datos influye en la elección del modelo de aprendizaje automático adecuado. En la práctica, muchos conjuntos de datos del mundo real no son linealmente separables, lo que hace que algoritmos más complejos sean necesarios para realizar tareas de clasificación de manera efectiva.

![Alt text](img/svm-intro-2.png)
![Alt text](img/svm-intro-3.png)

Para soluciona este problema, svm- large margin classification

![Alt text](img/svm-intro-4.png)

# Hard Margin Classification
![Alt text](img/svm-hardmargin-1.png)
![Alt text](img/svm-hardmargin-2.png)
![Alt text](img/svm-hardmargin-3.png)
![Alt text](img/svm-hardmargin-4.png)

# Construcción del modelo lineal - Función Coste
![Alt text](img/svm-modelolineal-coste-1.png)
![Alt text](img/svm-modelolineal-coste-2.png)
Con la funcion sigmoide

![Alt text](img/svm-modelolineal-coste-3.png)
![Alt text](img/svm-modelolineal-coste-4.png)

**Hinge Loss** : Así se le llama a la función de error

# Construcción del modelo lineal - Función Hipótesis
![Alt text](img/svm-modelolineal-hipotesis-1.png)
![Alt text](img/svm-modelolineal-hipotesis-2.png)
![Alt text](img/svm-modelolineal-hipotesis-3.png)

Que pasa si ajustamos la h a lo siguiente:

![Alt text](img/svm-modelolineal-hipotesis-4.png)

Elegimos una nueva h para alejarse mas, hacer el error mas pequeño
![Alt text](img/svm-modelolineal-hipotesis-5.png)
![Alt text](img/svm-modelolineal-hipotesis-6.png)
Nueva h:

![Alt text](img/svm-modelolineal-hipotesis-7.png)
![Alt text](img/svm-modelolineal-hipotesis-8.png)

Resumen: aun cuando las h calculadas predecian correctamente, no estaban los suficientemente alejadas y nos generaban un error. Alejandonos tenemos error = 0 


# Soft Margin Classification
![Alt text](img/svm-softmargin-1.png)
Para los support vectors que son anómalos, que tengan menos peso/influencia


![Alt text](img/svm-softmargin-2.png)
A medida que vamos disminuyendo el valor del hiperparámetro C, vamos restando importancia o influencia en la construcción del modelo a esos ejemplo que se encuentran mas cerca del modelo,  vectores de soporte

![Alt text](img/svm-softmargin-3.png)

# Kernels: Regresion Polinómica
Para conjuntos de datos que no se pueden separar linealmente

![Alt text](img/svm-kernel-regression-1.png)
![Alt text](img/svm-kernel-regression-2.png)
![Alt text](img/svm-kernel-regression-3.png)
![Alt text](img/svm-kernel-regression-4.png)
![Alt text](img/svm-kernel-regression-6.png)


# Kernels: Gaussian Kernel

![Alt text](img/svm-kernel-gaussian-1.png)
![Alt text](img/svm-kernel-gaussian-2.png)
![Alt text](img/svm-kernel-gaussian-3.png)
![Alt text](img/svm-kernel-gaussian-4.png)
![Alt text](img/svm-kernel-gaussian-5.png)

![Alt text](img/svm-kernel-gaussian-6.png)





