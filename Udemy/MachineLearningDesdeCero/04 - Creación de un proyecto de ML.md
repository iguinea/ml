# Conjunto de datos
![Alt text](img/creacion-model-ml-conjunto-datos-1.png)

# Visualización del conjunto de datos
Notebook: 6_Visualización del conjunto de datos

Clasificar tráfico de red como anómalo o legítimo

## Buscando correlaciones
* Se puede calcular el coeficiente de correlación estándar para ver la correlación entre cada par de atributos
* El coeficiente de correlación, solo mide correlaciones lineales, esto quiere decir que si x va hacia arriba, mediría si y va hacia arriba o hacia abajo.
* Hay que intentar buscar correlaciones sobre todo con el atributo objetivo (el que queremeos predecir), en este caso class

```python
# Transformamos los valores del atributo class de categoricos a numéricos
from sklearn.preprocessing import LabelEncoder 
labelencoder = LabelEncoder()
df["class"] = labelencoder.fit_transform(df["class"])
df
```
![Alt text](img/creacion-model-ml-correlacion-1.png)

Vemos que tenemos carácteristicas que tienen correlación con la 'class' y otras que no. (en la captura viene ordenado por las que tienen mas correlación)


# Overfitting y underfitting

Overfitting = sobreentranamiento

![Alt text](img/creacion-model-ml-overfitting-1.png)

Regresion lineal
Regresion polinómica

![Alt text](img/creacion-model-ml-overfitting-2.png)

# Soluciones al overfitting

![Alt text](img/creacion-model-ml-solucion-overfitting-1.png)

## Regularización
![Alt text](img/creacion-model-ml-solucion-overfitting-2.png)

* Ridge Regression: Lambda : Le añadiamos a la función de error una penalización: Es una constante

![Alt text](img/creacion-model-ml-solucion-overfitting-3.png)

Hay que buscar un valor de lambda aceptable


# Evaluación del la función hipótesis
Como saber, de manera programática, si la eleccion del numero de caracteristicas a entrenar produce overfitting

![Alt text](img/creacion-model-ml-evaluacion-funcion-hipotesis-1.png)

Dividir nuestros conjuntos de datos:
* Unos para entrenar
* otros para evaluar

![Alt text](img/creacion-model-ml-evaluacion-funcion-hipotesis-2.png)

# Selección del modelo

![Alt text](img/creacion-model-ml-seleccion-modelo-1.png)

Si el error en el train set es bajo, y en el test set es bajo: ok

Si el error en el train set es bajo, y en el test set es alto: overfitting

Si el error en el train set es alto, y en el test set es alto: modelo rigido -> Falta mejorarlos

![Alt text](img/creacion-model-ml-seleccion-modelo-2.png)

## Subconjunto de validación

![Alt text](img/creacion-model-ml-seleccion-modelo-3.png)

## Seleccióm de un modelo

![Alt text](img/creacion-model-ml-seleccion-modelo-4.png)


# Preparación del conjunto de datos

![Alt text](img/creacion-model-ml-preparacion-modelo-1.png)
![Alt text](img/creacion-model-ml-preparacion-modelo-2.png)

![Alt text](img/creacion-model-ml-preparacion-modelo-3.png)
![Alt text](img/creacion-model-ml-preparacion-modelo-4.png)
![Alt text](img/creacion-model-ml-preparacion-modelo-5.png)

![Alt text](img/creacion-model-ml-preparacion-modelo-6.png)
![Alt text](img/creacion-model-ml-preparacion-modelo-7.png)
![Alt text](img/creacion-model-ml-preparacion-modelo-8.png)

![Alt text](img/creacion-model-ml-preparacion-modelo-9.png)


# Caso Práctico: Preparación del conjunto de datos

# Caso Práctico: Creación de Pipelines y Transformadores

![Alt text](img/creacion-model-ml-caso-practico-pipelines-transformadores-1.png)

![Alt text](img/creacion-model-ml-caso-practico-pipelines-transformadores-2.png)

# Evaluación de los resultados

![Alt text](img/creacion-model-ml-avaluacion-resultados-1.png)
![Alt text](img/creacion-model-ml-avaluacion-resultados-2.png)
![Alt text](img/creacion-model-ml-avaluacion-resultados-3.png)

Precision: Vision de los falsos positivos
Exhaustividad: Vision de los falsos negativos

![Alt text](img/creacion-model-ml-avaluacion-resultados-4.png)

![Alt text](img/creacion-model-ml-avaluacion-resultados-5.png)
F1Score=0,9 --> 90% De acierto

![Alt text](img/creacion-model-ml-avaluacion-resultados-6.png)
Para obetener los resultados de la grafica en rojo, se ha eliminado la caracteristica AccountAgeDays del modelo, de manera que vemos que se empieza a comportar peor

![Alt text](img/creacion-model-ml-avaluacion-resultados-7.png)



# Caso Práctico: Evaluación de los resultados

