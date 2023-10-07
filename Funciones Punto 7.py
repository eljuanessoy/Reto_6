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