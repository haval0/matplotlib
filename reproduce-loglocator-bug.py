import matplotlib.pyplot as plt
import matplotlib.ticker
import numpy as np

ll = matplotlib.ticker.LogLocator(subs=(1, 2, 5))

### The following code produces a plot with y-axis ticks at the expected locations.

fig, ax = plt.subplots()
x = np.arange(8)
plt.semilogy(x, 10 ** x)
ax.yaxis.set_major_locator(ll)
ax.yaxis.set_minor_locator(ll)
plt.title("Good Plot")
plt.savefig("loglocator-good.png")

### The following code produces a plot with no y-axis ticks
### which is unexpected and undesired.

fig, ax = plt.subplots()
x = np.arange(9)  # The only change is this line
plt.semilogy(x, 10 ** x)
ax.yaxis.set_major_locator(ll)
ax.yaxis.set_minor_locator(ll)
plt.title("Bad Plot")
plt.savefig("loglocator-bad.png")

### The problem is isolated to here, which returns correct values in the first case
### but np.array([]) in the second case:
print(ll.tick_values(1, 1e7))
print(ll.tick_values(1, 1e8))
