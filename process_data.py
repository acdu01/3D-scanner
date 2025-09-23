pan_total_deg = 181
tilt_total_deg = 181

for line in data.csv:
    if line <= 100:
        continue

    else:
        # formula for converting data to dist is derived from calibration data: INSERT FORMULA HERE
        x = formula(line) * sin(pan_total_deg)
        y = formula(line) * sin(tilt_total_deg)
        with open('output.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([x, y])


