import math
import csv
import os


# formula for converting data to dist is derived from calibration data
def convert(x):
    d = 171 - 0.655 * x + 7.27e-04 * (x**2)
    return d


base = os.path.dirname(__file__)
data_path = os.path.join(base, "data.csv")
output_path = os.path.join(base, "output.csv")

with open(data_path) as f, open(output_path, mode="w", newline="") as out:
    writer = csv.writer(out)

    batch = []
    for line in f:
        line = line.strip().strip('"')
        if not line:
            continue

        # split by semicolon
        parts = line.split(";")
        pan_deg = float(parts[0])
        tilt_deg = float(parts[1])
        reading = float(parts[2])

        if reading <= 100:
            continue

        d = convert(reading)
        x = d * math.sin(math.radians(pan_deg)) * math.cos(math.radians(tilt_deg))
        y = d * math.sin(math.radians(pan_deg)) * math.sin(math.radians(tilt_deg))
        batch.append((x, y))

        # every 5 valid readings, write their average
        if len(batch) == 5:
            avg_x = sum(p[0] for p in batch) / 5
            avg_y = sum(p[1] for p in batch) / 5
            writer.writerow([avg_x, avg_y])
            batch = []  # reset for next batch
