import matplotlib.pyplot as plt
import csv

x_vals = []
y_vals = []

# read the csv file
with open('output.csv', newline='') as file:
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
