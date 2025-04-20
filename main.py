#MapPlot.py
#Name:Cameron Sailors
#Date:4/20/2025
#Assignment:Lab 10

import earthquakes
earthquake = earthquakes.get_earthquake()
import pandas as pd
import matplotlib.pyplot as plt

magnitude = []
impact = []

for quake in earthquake:
    magn = quake["impact"]["magnitude"]
    significance = quake["impact"]["significance"]

    if magn <= 10 and significance <= 800:
        magnitude.append(magn)
        impact.append(significance)

# Create a DataFrame using a dictionary of lists
df = pd.DataFrame({"MAGNITUDE": magnitude,"SIGNIFICANCE": impact})

print(df)

# Create a scatter plot
df.plot(kind="scatter", x="MAGNITUDE", y="SIGNIFICANCE")

# Save the plot to a file
plt.savefig("output.png")
