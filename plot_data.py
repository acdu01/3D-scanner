import matplotlib.pyplot as plt
import csv
import os

x_vals = []
y_vals = []

base = os.path.dirname(__file__)
output_path = os.path.join(base, "output.csv")

# read the csv file
with open(output_path, newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        if row:
            x, y = map(float, row)  # convert strings to floats
            x_vals.append(x)
            y_vals.append(y)

# plot the points
plt.scatter(x_vals, y_vals, c="blue", marker=".")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Scanned Shape")
plt.show()

# might be better for showing 2d shape:
# plt.hexbin(x_vals, y_vals, gridsize=50, cmap="Blues")
# plt.colorbar(label="Density")
# plt.axis("equal")
