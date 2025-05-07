from fastapi import FastAPI
from pydantic import BaseModel
import math

app = FastAPI()

class Operacao(BaseModel):
    a: float
    b: float

class Numero(BaseModel):
    valor: float

@app.post("/somar")
def somar(valores: Operacao):
    return {"resultado": valores.a + valores.b}

@app.post("/subtrair")
def subtrair(valores: Operacao):
    return {"resultado": valores.a - valores.b}

@app.post("/multiplicar")
def multiplicar(valores: Operacao):
    return {"resultado": valores.a * valores.b}

@app.post("/dividir")
def dividir(valores: Operacao):
    if valores.b == 0:
        return {"erro": "Divisão por zero não é permitida"}
    return {"resultado": valores.a / valores.b}

@app.post("/exponenciar")
def exponenciar(valores: Operacao):
    return {"resultado": valores.a ** valores.b}

@app.post("/raiz")
def raiz(valor: Numero):
    if valor.valor < 0:
        return {"erro": "Raiz quadrada de número negativo não é permitida"}
    return {"resultado": math.sqrt(valor.valor)}
