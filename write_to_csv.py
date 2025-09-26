
import serial
import csv

arduinoComPort = "COM6"

baudRate = 9600

serialPort = serial.Serial(arduinoComPort, baudRate, timeout=1)

while True:
  lineOfData = serialPort.readline().decode()
  if len(lineOfData) > 0:
    print("Received: " + lineOfData)
    with open('data.csv', mode='a', newline='') as file:
      writer = csv.writer(file)
      writer.writerow([lineOfData])
