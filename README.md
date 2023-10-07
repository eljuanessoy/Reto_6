# Reto #6 😲
By Juan Esteban Molina Rey (eljuanessoy)

### 1. Dado la figura de la imagen, desarrolle:
+ Una función matemática para calcular el volumen y el área superficial.
+ Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r1, r2 y h.
+ Revise como utilizar el valor de pi usando import math y math.pi

Para realizar esto primero importe de la función de pi. Cree una primera función para el volumen y una segunda funcion para el area superficial. Puse la opcion para ingresar los valores y luego la ejecuté.

```python
import math
pi = math.pi

def Volumen(r1:float, r2:float, h:float):
  ResultadoVolumen = ((4*pi*(r1**3))/3) + (((pi*(r2**2)*h))/3)
  return ResultadoVolumen

def AreaSuperficial(r1:float, r2:float, h:float):
  ResultadoAreaSuperficial = (4*pi*(r1**2)) + (pi*r2*(math.sqrt((r2**2)+(h**2))))
  return ResultadoAreaSuperficial

if __name__ == "__main__":
  r1 = float(input("Ingrese el valor del radio de la esfera: "))
  r2 = float(input("Ingrese el valor del radio del cono: "))
  h = float(input("Ingrese la altura del cono: "))
  VolumenFinal = Volumen(r1, r2, h)
  AreaSuperficialFinal = AreaSuperficial(r1, r2, h)
  
  print()
  print("El volumen total es " + str(VolumenFinal))
  print("El area superficial total es " + str(AreaSuperficialFinal))
```

### 2. Dado la figura de la imagen, desarrolle:
+ Una función matemática para calcular el área y el perimetro.
+ Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r, a y b.
+ Revise como utilizar el valor de pi usando import math y math.pi

Para realizar esto primero importe de la función de pi. Cree una primera función para el area y una segunda funcion para el perimetro. Puse la opcion para ingresar los valores y luego la ejecuté.

```python
import math
pi = math.pi

def Area(r:float, h:float, b:float):
  ResultadoArea = (2*(pi*(r**2))) + (b*h)
  return ResultadoArea

def Perimetro(r:float, h:float, b:float):
  ResultadoPerimetro = (2*pi*r) + (2*(b+h))
  return ResultadoPerimetro

if __name__ == "__main__":
  r = float(input("Ingrese el valor del radio de los circulos: "))
  h = float(input("Ingrese el valor de la altura del rectangulo: "))
  b = float(input("Ingrese el valor de la base del rectangulo: "))
  AreaFinal = Area(r, h, b)
  PerimetroFinal = Perimetro(r, h, b)
  
  print()
  print("El area final es " + str(AreaFinal))
  print("El perimetro final es " + str(PerimetroFinal))
```

### 3. Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.

Para realizar esto primero cree una función para calcular el peso de la carne, puse la opcion para ingresar los valores y luego la ejecuté.

```python
def Carne(n:float, m:float, k:float):
  TotalCarne = (6*n) + (7*m) + (k)
  return TotalCarne

if __name__ == "__main__":
  n = float(input("Ingrese la cantidad de gallinas: "))
  m = float(input("Ingrese la cantidad de gallos: "))
  k = float(input("Ingrese la cantidad de pollos: "))
  TotaldeCarne = Carne(n, m, k)
  
  print()
  print(f"El peso de la carne son {TotaldeCarne}kg")
```

### 4. Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.

Para realizar esto primero cree una función para calcular el valor total de lo que debo pagar y a su vez para saber si debo dinero, me deben dinero, o si nadie le debe nada a nadie, luego puse la opcion para ingresar los valores y luego la ejecuté.

```python
def Vueltas(p:int, l:int, h:int, B:int):
  ValorTotal = (300*p) + (3300*l) + (350*h)
  Cambio = B-ValorTotal
  return Cambio

if __name__ == "__main__":
  p = int(input("Ingrese la cantidad de panes: "))
  l = int(input("Ingrese la cantidad de bolsas de leche: "))
  h = int(input("Ingrese la cantidad de huevos: "))
  B = int(input("Ingrese el valor del billete con el que va a pagar: "))
  LasVueltas = Vueltas(p, l, h, B)

  print()
  if LasVueltas>0:
    print("El vendedor me debe dar $" + str(LasVueltas))
  if LasVueltas<0:
    print("Le debo al vendedor $" + str(LasVueltas))
  elif LasVueltas == 0:
    print("No debo ni me deben nada")
```

### 5. Haga un programa que utilice una función para calcular el valor de un préstamo C usando interés compuesto del i por n meses.

Para realizar esto primero cree una función para calcular el interés compuesto, en donde por medio de una ecuacion puedo hallarlo, luego puse la opcion para ingresar los valores del prestamo, el interes al año y la cantidad de meses, y luego la ejecuté.

```python
def Prestamo(c:float, i:float, n:float):
  Interes = i/12
  TotalPrestamo = c*((1+Interes)**n)
  return TotalPrestamo

if __name__ == "__main__":
  c = float(input("Ingrese el valor del prestamo: "))
  i = float(input("Ingrese el interés al año: "))
  n = float(input("Ingrese la cantidad de meses: "))
  IC = Prestamo(c, i, n)

  print()
  print("El interés compuesto es del prestamo es " + str(IC))
```

### 6. El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.

Para realizar esto primero cree una función para calcular la cantidad de contagios despues de cierta cantidad de dias, luego puse la opcion para ingresar los valores y la ejecuté.

```python
def Contagios(x:int, n:int) -> int:
  TotalContagios = n*(2**x)
  return TotalContagios

if __name__ == "__main__":
  d = int(input("Ingrese el número de días: "))
  c = int(input("Ingrese la cantidad de personas contagiadas actualmente: "))
  TotaldeContagios = Contagios(d, c)

  print()
  print(f"El total de personas contagiadas en NuncaLandia es de {TotaldeContagios} personas")
```

### 7. Escriba un programa que pida 5 números reales y calcule las siguientes operaciones usando una función para cada una:

+ El promedio
+ La mediana
+ El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
+ Ordenar los números de forma ascendente
+ Ordenar los números de forma descendente
+ La potencia del mayor número elevado al menor número
+ La raíz cúbica del menor número

Para realizar esto primero cree varias funciones para calcular las operaciones anteriormente mencionadas, luego puse la opcion para ingresar los valores y la ejecuté.

```python
def Promedio(a, b, c, d, e) -> float:
    ResultadoPromedio = (a+b+c+d+e)/5
    return ResultadoPromedio
def PromedioMultiplicativo(a, b, c, d, e) -> float:
    ResultadoPM = (a*b*c*d*e)**(1/5)
    return ResultadoPM
def OrdenAscendente(a, b, c, d, e) -> float:
    ListaA = [a, b, c, d, e]
    Ascendente = sorted(ListaA)
    return Ascendente
def OrdenDescendente(a, b, c, d, e) -> float:
    ListaB = [a, b, c, d, e]
    Descendente = sorted(ListaB, reverse = True)
    return Descendente
def Mediana(a, b, c, d, e) -> float:
    ListaC = [a, b, c, d, e]
    ListaCord = sorted(ListaC)
    ListaClong = len(ListaC)
    ResultadoMediana = ListaCord[ListaClong // 2]
    return ResultadoMediana
def Potencia(a, b, c, d, e) -> float:
    ListaD = [a, b, c, d, e]
    M = max(ListaD)
    M = min(ListaD)
    ResultadoPotencia = M**n
    return ResultadoPotencia
def RaizCubica(a, b, c, d, e) -> float:
    ListaE = [a, b, c, d, e]
    menor1 = min(ListaE)
    ResultadoRaizCubica = menor1**(1/3)
    return ResultadoRaizCubica

if __name__ == "__main__":
  a = float(input("Ingrese un número real: "))
  b = float(input("Ingrese un número real: "))
  c = float(input("Ingrese un número real: "))
  d = float(input("Ingrese un número real: "))
  e = float(input("Ingrese un número real: "))
  PromedioFinal = Promedio(a, b, c, d, e)
  PMFinal = PromedioMultiplicativo(a, b, c, d, e)
  OrdenA = OrdenAscendente(a, b, c, d, e)
  OrdenB = OrdenDescendente(a, b, c, d, e)
  MedianaFinal = Mediana(a, b, c, d, e)
  PotenciaFinal = Potencia(a, b, c, d, e)
  RaizCubicaFinal = RaizCubica(a, b, c, d, e)

  print()
  print("El promedio es " +str(PromedioFinal))
  print("El promedio multiplicatvo es " +str(PMFinal))
  print("Números ordenados en forma ascendente: " +str(OrdenA))
  print("Números ordenados en forma descendente: " +str(OrdenB))
  print("La mediana es el número " +str(MedianaFinal))
  print("La potencia del mayor número elevado al menor número es: " +str(PotenciaFinal))
  print("La raíz cúbica del menor número es: " +str(RaizCubicaFinal))
```

### 8. Para el punto anterior incluir las funciones en un archivo independiente e importarlas para su uso.

```python
from Funciones Punto 7 import Promedio
from Funciones Punto 7 import PromedioMultiplicativo
from Funciones Punto 7 import OrdenAscendente
from Funciones Punto 7 import OrdenDescendente
from Funciones Punto 7 import Mediana
from Funciones Punto 7 import Potencia
from Funciones Punto 7 import RaizCubica
if __name__ == "__main__":
  a = float(input("Ingrese un número real: "))
  b = float(input("Ingrese un número real: "))
  c = float(input("Ingrese un número real: "))
  d = float(input("Ingrese un número real: "))
  e = float(input("Ingrese un número real: "))
  PromedioFinal = Promedio(a, b, c, d, e)
  PMFinal = PromedioMultiplicativo(a, b, c, d, e)
  OrdenA = OrdenAscendente(a, b, c, d, e)
  OrdenB = OrdenDescendente(a, b, c, d, e)
  MedianaFinal = Mediana(a, b, c, d, e)
  PotenciaFinal = Potencia(a, b, c, d, e)
  RaizCubicaFinal = RaizCubica(a, b, c, d, e)

  print()
  print("El promedio es " +str(PromedioFinal))
  print("El promedio multiplicatvo es " +str(PMFinal))
  print("Números ordenados en forma ascendente: " +str(OrdenA))
  print("Números ordenados en forma descendente: " +str(OrdenB))
  print("La mediana es el número " +str(MedianaFinal))
  print("La potencia del mayor número elevado al menor número es: " +str(PotenciaFinal))
  print("La raíz cúbica del menor número es: " +str(RaizCubicaFinal))
```

### 9. Consultar qué es y cómo funciona pip en python.

+ Pip, un gestor de paquetes diseñado para Python, destaca como una utilidad esencial en el ámbito del desarrollo. Su función principal radica en facilitar la instalación, desinstalación y actualización de paquetes de software escritos en este lenguaje de programación. Este proyecto de código abierto se encuentra disponible para una amplia gama de sistemas operativos, consolidándose como una herramienta versátil y accesible. La capacidad de Pip para administrar bibliotecas y dependencias en proyectos Python lo convierte en un elemento fundamental para el desarrollo de aplicaciones más complejas. Al simplificar la gestión de funcionalidades específicas de terceros, Pip contribuye significativamente a la eficiencia y robustez del proceso de desarrollo.

+ Pip opera mediante la utilización de un depósito de paquetes conocido como Python Package Index (PyPI). Este último es una plataforma en línea que hospeda una amplia variedad de paquetes de software desarrollados en Python. La instalación de un paquete proveniente de PyPI se lleva a cabo mediante el comando pip install. Al proporcionar el nombre del paquete como argumento, el comando pip install procede a instalar dicho paquete en el sistema correspondiente.

### 10. Hacer un listado de módulos populares para python que se puedan instalar com pip y consultar cómo instalarlos.

+ Scikit-learn: Un módulo para aprendizaje automático.
+ Matplotlib: Un módulo para visualización de datos.
+ Requests: Es una biblioteca HTTP
+ PyTorch: Un framework para aprendizaje profundo.
+ TensorFlow: Un framework para aprendizaje automático.
+ Pandas: biblioteca de análisis de datos.
+ NumPy: Un módulo para computación numérica.
+ SciPy: Un módulo para computación científica.
+ Django: Un framework web.
+ Flask: Un microframework web.

Para instalar estos programas debes hacer uso de este codigo:

```
pip install [Nombre del módulo]
```

Referencias: 
+ https://es.linkedin.com/learning/python-esencial-15349768/instalacion-de-paquetes-con-pip#:~:text=pip%20es%20el%20instalador%20y,desde%20la%20shell%20de%20Python.
+ https://geekland.eu/como-instalar-y-usar-el-gestor-de-paquetes-pip/#:~:text=Pip%20es%20un%20gestor%20de%20paquetes%20utilizado%20para%20instalar%20y,y%20buscar%20paquetes%20de%20Python.
+ https://docs.python.org/3/installing/
