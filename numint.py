import matplotlib.pyplot as plt

# Initial variables
m = 10
nAxis = []
lRAxis = []
mRAxis = []
tAxis = []

# left riemann sum
for n in range(1, 100):
    x = 0
    fSum = 0
    for j in range(n):
        x: float = j / (n / m)
        f = 4 * x ** 3 + 2 * x
        fSum += f
    lRSum = (m / n) * fSum
    perError = abs(10100 - lRSum)/101
    lRAxis.append(perError)
    nAxis.append(n)

# midpoint
for n in range(1, 100):
    x = 0
    fSum = 0
    for j in range(n):
        x: float = 1/(2*n/m) + j/(n/m)
        f = 4 * x ** 3 + 2 * x
        fSum += f*(m/n)
    perError = abs(10100 - fSum)/101
    mRAxis.append(perError)


# Trapezoidal
for n in range(1, 100):
    x = 0
    fSum = 0
    for j in range(n+1):
        x: float = j/(n/m)
        if j == 0 or j == n:
            f = 4 * x ** 3 + 2 * x
        else:
            f = 2 * (4 * x ** 3 + 2 * x)
        fSum += f * (m/(n*2))
    perError = abs(10100-fSum)/101
    tAxis.append(perError)

# Simpson's Rule

# Plot
plt.plot(nAxis, lRAxis, label="Left Riemann Sum")
plt.plot(nAxis, mRAxis, label="Midpoint Rule")
plt.plot(nAxis, tAxis, label="Trapezoid Rule")

plt.legend()

plt.xlabel("Number of iterations")
plt.ylabel("% Error")
plt.title("Error vs Iterations")

plt.show()
