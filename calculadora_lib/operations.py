def add(a: float, b: float) -> float:
  
    return a + b

def subtract(a: float, b: float) -> float:
  
    return a - b

def multiply(a: float, b: float) -> float:

    return a * b

def divide(a: float, b: float) -> float:
    
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b

def exponenciar(base: float, expoente: float) -> float:
    return base ** expoente



def raiz(valor: float) -> float:
    if valor < 0:
        raise ValueError("Raiz quadrada de número negativo não é permitida.")
    return math.sqrt(valor)    