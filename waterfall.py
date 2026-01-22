import numpy as np
import matplotlib.pyplot as plt

fp = open("weather.txt", "r")
a, b, c = map(float, fp.read().split())
fp.close()

time = np.arange(0, 25, 1)
temperature = a*time**2 + b*time + c

print("Waterfall Model Coefficients:")
print("a =", a, "b =", b, "c =", c)

plt.plot(time, temperature)
plt.xlabel("Time of the Day (00–24)")
plt.ylabel("Temperature (°C)")
plt.title("Weather Prediction - Waterfall Model")
plt.show()
