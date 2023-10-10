import matplotlib.pyplot as plt

BTS_population = 15
WTS_population = 20
BTS_birth_fraction = 1
WTS_birth_fraction = 1
BTS_death_proportionality_constant = 0.20
WTS_death_proportionality_constant = 0.27

dt = 0.01  # Time step
duration = 5 
iteration = int(duration / dt)

B = []
W = []
T = []

for i in range(iteration):
    BTS_births = BTS_population * BTS_birth_fraction
    BTS_deaths = BTS_death_proportionality_constant * WTS_population * BTS_population
    WTS_births = WTS_population * WTS_birth_fraction
    WTS_deaths = WTS_death_proportionality_constant * BTS_population * WTS_population

    BTS_population += (BTS_births - BTS_deaths) * dt
    WTS_population += (WTS_births - WTS_deaths) * dt

    B.append(BTS_population)
    W.append(WTS_population)
    t = i * dt
    T.append(t)

plt.plot(T, B, color="red", label="BTS")
plt.plot(T, W, color="blue", label="WTS")

plt.xlabel("Time (months)")
plt.ylabel("Population")
plt.title("Competition Of Species")
plt.legend()
plt.grid(True)
plt.show()
