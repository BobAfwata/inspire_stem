#include <BluetoothSerial.h>

// L293D Motor Driver Pins
const int motorPin1 = 5;  // Pin 14 of L293
const int motorPin2 = 6;  // Pin 10 of L293
const int motorPin3 = 10; // Pin  7 of L293
const int motorPin4 = 9;  // Pin  2 of L293

BluetoothSerial SerialBT;

void setup() {
  SerialBT.begin("ESP32_BT_Control"); // Bluetooth device name
  init_motors(); // Initialize motors
}

void loop() {
  if (SerialBT.available()) {
    char command = SerialBT.read();
    execute_command(command);
  }
}

void execute_command(char command) {
  switch (command) {
    case 'f':
      move_forward();
      break;
    case 'b':
      move_backward();
      break;
    case 'l':
      move_left();
      break;
    case 'r':
      move_right();
      break;
    case 's':
      stop_motors();
      break;
    default:
      break;
  }
}

void move_forward() {
  digitalWrite(motorPin1, HIGH);
  digitalWrite(motorPin2, LOW);
  digitalWrite(motorPin3, HIGH);
  digitalWrite(motorPin4, LOW);
  delay(2000);
  stop_motors();
}

void move_backward() {
  digitalWrite(motorPin1, LOW);
  digitalWrite(motorPin2, HIGH);
  digitalWrite(motorPin3, LOW);
  digitalWrite(motorPin4, HIGH);
  delay(2000);
  stop_motors();
}

void move_left() {
  digitalWrite(motorPin1, LOW);
  digitalWrite(motorPin2, HIGH);
  digitalWrite(motorPin3, HIGH);
  digitalWrite(motorPin4, LOW);
  delay(2000);
  stop_motors();
}

void move_right() {
  digitalWrite(motorPin1, HIGH);
  digitalWrite(motorPin2, LOW);
  digitalWrite(motorPin3, LOW);
  digitalWrite(motorPin4, HIGH);
  delay(2000);
  stop_motors();
}

void stop_motors() {
  digitalWrite(motorPin1, LOW);
  digitalWrite(motorPin2, LOW);
  digitalWrite(motorPin3, LOW);
  digitalWrite(motorPin4, LOW);
}

void init_motors() {
  pinMode(motorPin1, OUTPUT);
  pinMode(motorPin2, OUTPUT);
  pinMode(motorPin3, OUTPUT);
  pinMode(motorPin4, OUTPUT);
}
