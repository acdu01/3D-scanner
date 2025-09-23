#include <Servo.h>

int IRpin = A1;      // select the pin for IR sensor
int sensorValue = 0;
int timefordelay = 50;  // variable to store the value coming from the sensor

Servo pan;  // create servo object to control a servo
Servo tilt;  // create servo object to control a servo
int pos = 0;    // variable to store the servo position
bool done = false;
int p = 0;
int t = 0;

void setup() {
  // begin reading data from IR sensor
  pinMode(IRpin, INPUT);
  Serial.begin(9600);
  // connect servos to digital pins
  pan.attach(9);  
  tilt.attach(10);  

  // send data setup
  long baudRate = 9600;       // NOTE1: The baudRate for sending & receiving programs must match
  Serial.begin(baudRate);     // NOTE2: Set the baudRate to 115200 for faster communication

  Serial.println("Start of Program");
}

void servoSweep(int pos, Servo& myservo){
  myservo.write(pos);
  sensorValue = analogRead(IRpin);
  Serial.println(sensorValue);
  delay(15);
}

void loop() {
  for (p = 0; p <= 180; p++){
    // move pan first each row
    servoSweep(p, pan);
    // sweep tilt serpentine style
    if (p % 2 == 0) {
      for (t = 0; t <= 180; t++){
        servoSweep(t, tilt);
      }
    }
    else {
      for (t = 180; t >= 0; t--){
        servoSweep(t, tilt);
      }
    }
    
  }
  // stop after one full scan
  while (true) {}

}