#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Este script contiene la la integracion de de La ecuación de Fisher-KPP
que describe el comportamiento animal mediante el metodo de euler y
cranck nicolson
'''


from __future__ import division
import numpy as np
import matplotlib.pyplot as plt


def inicializa_n(n, N_steps, h):
    '''
    Rellena T con las condiciones iniciales del problema.
    Se asegura que las condiciones en los bordes sean cero.
    '''
    for i in range(N_steps):
        n[i] = random[i]
    n[0] = 0
    n[-1] = 0


def calcula_b(b, N_steps, r):
    for j in range(1, N_steps - 1):
        # aqui se agrega la solucion euler
        b[j] = r * n[j+1] + (1 - 2 * r + dt * u * (1-n[j]**2)) * n[j] \
                   + r * n[j-1]


def calcula_alpha_y_beta(alhpa, beta, b, r, N_Steps):
    Aplus = -1 * r
    Acero = (1 + 2 * r)
    Aminus = -1 * r
    alpha[0] = 0
    beta[0] = 0  # viene de la condicion de borde T(t, 0) = 0
    for i in range(1, N_steps):
        alpha[i] = -Aplus / (Acero + Aminus*alpha[i-1])
        beta[i] = (b[i] - Aminus*beta[i-1]) / (Aminus*alpha[i-1] + Acero)


def avanza_paso_temporal(n, n_next, alpha, beta, N_steps):
    n_next[0] = 0
    n_next[-1] = 0
    for i in range(N_steps - 2, 0, -1):
        n_next[i] = alpha[i] * n_next[i+1] + beta[i]


# Main

# setup
N_steps = 499
N_pasos_temporales = 50

h = 1 / (N_steps - 1)
# dt = h**2 / 2 # Este es el máximo teórico para el metodo explicito
dt = 0.1
y = 0.001
r = (dt * y) / (2 * h**2)

u = 1.5
n = np.zeros(N_steps)
n_next = np.zeros(N_steps)
b = np.zeros(N_steps)
# en random se ingresa la semilla
random = np.random.uniform(low=-0.3, high=0.3, size=Nx)

alpha = np.zeros(N_steps)
beta = np.zeros(N_steps)

inicializa_n(n, N_steps, h)

# Queremos guardar las soluciones en cada paso
n_solucion = np.zeros((N_pasos_temporales, N_steps))
n_solucion[0, :] = n.copy()

for i in range(1, N_pasos_temporales):
    calcula_b(b, N_steps, r)
    calcula_alpha_y_beta(alpha, beta, b, r, N_steps)
    avanza_paso_temporal(n, n_next, alpha, beta, N_steps)
    n = n_next.copy()
    n_solucion[i, :] = n.copy()

# Plots
x = np.linspace(0, 1, N_steps)
'''
fig = plt.figure(1)
fig.clf()
ax = fig.add_subplot(111)
plt.title('Difusion Conveccion con u=1.5 y gamma=0.001')
plt.xlabel('Distancia [Unidad de largo]')
plt.ylabel('Tiempo [Unidad de tiempo]')
for i in range(0, N_pasos_temporales, 10):
    ax.plot(x, n_solucion[i, :])
ax.set_ylim(-1, 1)

'''
# ejemplo 2
# usar el plano x, t y plotear T en la 3a dimension
fig3 = plt.figure(2)
ax1 = fig3.add_subplot(111, projection='3d')
y = np.arange(0, N_pasos_temporales) * dt
X, Y = np.meshgrid(x, y)
ax1.plot_wireframe(X, Y, n_solucion, rstride=5, cstride=5)
plt.title('Difusion Conveccion con u=1.5 y gamma=0.001')
plt.xlabel('Distancia [Unidad de largo]')
plt.ylabel('Tiempo [Unidad de tiempo]')

plt.show()
plt.draw()
