import math
import time
from decimal import Decimal, getcontext
from math import factorial

# Aumentar precisão para Ramanujan e BBP
getcontext().prec = 50

def pi_leibniz(n):
    pi_aprox = 0
    for k in range(n):
        pi_aprox += (-1)**k / (2 * k + 1)
    return 4 * pi_aprox

def pi_nilakantha(n):
    pi_aprox = 3.0
    sinal = 1
    for i in range(2, 2 * n + 1, 2):
        termo = 4 / (i * (i + 1) * (i + 2))
        pi_aprox += sinal * termo
        sinal *= -1
    return pi_aprox

def arctan(x, n):
    resultado = 0
    for k in range(n):
        resultado += (-1)**k * (x**(2*k + 1)) / (2*k + 1)
    return resultado

def pi_machin(n):
    return 16 * arctan(1/5, n) - 4 * arctan(1/239, n)

def pi_ramanujan(n):
    total = Decimal(0)
    fator = Decimal(2).sqrt() * Decimal(2) / Decimal(9801)
    for k in range(n):
        num = Decimal(factorial(4*k)) * (1103 + 26390*k)
        den = (Decimal(factorial(k)) ** 4) * (Decimal(396) ** (4*k))
        total += num / den
    return float(1 / (fator * total))

def pi_bbp(n):
    pi = Decimal(0)
    for k in range(n):
        k = Decimal(k)
        termo = (Decimal(1) / (Decimal(16) ** k)) * (
            Decimal(4) / (8 * k + 1) -
            Decimal(2) / (8 * k + 4) -
            Decimal(1) / (8 * k + 5) -
            Decimal(1) / (8 * k + 6)
        )
        pi += termo
    return float(pi)

# Número de termos
n_termos = 1000
pi_real = math.pi
resultado = []

def medir(metodo, nome, n):
    inicio = time.time()
    pi_aprox = metodo(n)
    fim = time.time()
    erro_abs = abs(pi_real - pi_aprox)
    erro_pct = (erro_abs / pi_real) * 100
    tempo = fim - inicio
    resultado.append((nome, n, pi_aprox, erro_abs, erro_pct, tempo))

# Medições
medir(pi_leibniz, "Leibniz", n_termos)
medir(pi_nilakantha, "Nilakantha", n_termos)
medir(pi_machin, "Machin", n_termos)
medir(pi_ramanujan, "Ramanujan", n_termos)
medir(pi_bbp, "BBP", n_termos)

# Impressão tabular
print(f"{'Método':<12} {'Termos':<8} {'π Aproximado':<20} {'Erro Absoluto':<18} {'Erro Percentual (%)':<20} {'Tempo (s)':<12}")
print("-" * 110)
for metodo, termos, pi_aprox, erro_abs, erro_pct, tempo in resultado:
    print(f"{metodo:<12} {termos:<8} {pi_aprox:<20.15f} {erro_abs:<18.15f} {erro_pct:<20.12f} {tempo:<12.6f}")
