import numpy as np
import matplotlib.pyplot as plt


def euler(f, t0, y0, h, n):
    t = t0
    y = y0
    y_values = [y0]
    for i in range(n):
        y += h * f(t, y)
        t += h
        y_values.append(y)
    return y_values


def midpoint(f, t0, y0, h, n):
    t = t0
    y = y0
    y_values = [y0]
    for i in range(n):
        k1 = h * f(t, y)
        k2 = h * f(t + 0.5 * h, y + 0.5 * k1)
        y += k2
        t += h
        y_values.append(y)
    return y_values


def euler_trapezoid(f, t0, y0, h, n):
    t = t0
    y = y0
    y_values = [y0]
    for i in range(n):
        k1 = h * f(t, y)
        k2 = h * f(t + h, y + k1)
        y += 0.5 * (k1 + k2)
        t += h
        y_values.append(y)
    return y_values


def rk2(f, t0, y0, h, n):
    t = t0
    y = y0
    y_values = [y0]
    for i in range(n):
        k1 = h * f(t, y)
        k2 = h * f(t + h, y + k1)
        y += k2
        t += h
        y_values.append(y)
    return y_values


def rk3(f, t0, y0, h, n):
    t = t0
    y = y0
    y_values = [y0]
    for i in range(n):
        k1 = h * f(t, y)
        k2 = h * f(t + h/2, y + k1/2)
        k3 = h * f(t + h, y - k1 + 2*k2)
        y += (k1 + 4*k2 + k3) / 6
        t += h
        y_values.append(y)
    return y_values


def rk4(f, t0, y0, h, n):
    t = t0
    y = y0
    y_values = [y0]
    for i in range(n):
        k1 = h * f(t, y)
        k2 = h * f(t + 0.5 * h, y + 0.5 * k1)
        k3 = h * f(t + 0.5 * h, y + 0.5 * k2)
        k4 = h * f(t + h, y + k3)
        y += (k1 + 2*k2 + 2*k3 + k4) / 6
        t += h
        y_values.append(y)
    return y_values


def function(t, y):
    return np.exp(-t) - y**2


def exact_solution(t):
    return


plt.figure(figsize=(10, 6))
t0 = 0
y0 = 0
h = 0.1
n = 100

y_euler = euler(function, t0, y0, h, n)
y_midpoint = midpoint(function, t0, y0, h, n)
y_euler_trapezoid = euler_trapezoid(function, t0, y0, h, n)
y_rk2 = rk2(function, t0, y0, h, n)
y_rk3 = rk3(function, t0, y0, h, n)
y_rk4 = rk4(function, t0, y0, h, n)

# Create time points
time = np.linspace(t0, t0 + h * n, n + 1)

y_exact = [exact_solution(t) for t in time]

print(y_euler)
print(y_midpoint)
print(y_euler_trapezoid)
print(y_rk2)
print(y_rk3)
print(y_rk4)

# Plot the solutions
plt.figure(figsize=(10, 6))
plt.plot(time, y_euler, label='Euler')
plt.plot(time, y_midpoint, label='Midpoint')
plt.plot(time, y_euler_trapezoid, label='Euler Trapezoid')
plt.plot(time, y_rk2, label='RK2')
plt.plot(time, y_rk3, label='RK3')
plt.plot(time, y_rk4, label='RK4')
plt.plot(time, y_exact, label='Exact', linestyle='--')

plt.legend()
plt.show()
