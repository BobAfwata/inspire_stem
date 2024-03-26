#include <BluetoothSerial.h>

// L293D Motor Driver Pins
const int motorPin1 = 5;  // Pin 14 of L293
const int motorPin2 = 6;  // Pin 10 of L293
const int motorPin3 = 10; // Pin  7 of L293
const int motorPin4 = 9;  // Pin  2 of L293
const int buzzerPin = 7;  // Pin for the buzzer

BluetoothSerial SerialBT;
bool paired = false;

void setup() {
  SerialBT.begin("ESP32_BT_Control"); // Bluetooth device name
  init_motors(); // Initialize motors
  pinMode(buzzerPin, OUTPUT); // Initialize buzzer pin
  buzz(3); // Beep 3 times to indicate device not paired initially
}

void loop() {
  if (!paired && !SerialBT.isConnected()) {
    buzz(1); // Beep once to indicate not paired
  }
  
  if (SerialBT.available()) {
    paired = true;
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
  buzz_continuous(); // Make continuous sound while moving
}

void move_backward() {
  digitalWrite(motorPin1, LOW);
  digitalWrite(motorPin2, HIGH);
  digitalWrite(motorPin3, LOW);
  digitalWrite(motorPin4, HIGH);
  buzz_continuous(); // Make continuous sound while moving
}

void move_left() {
  digitalWrite(motorPin1, LOW);
  digitalWrite(motorPin2, HIGH);
  digitalWrite(motorPin3, HIGH);
  digitalWrite(motorPin4, LOW);
  buzz_continuous(); // Make continuous sound while moving
}

void move_right() {
  digitalWrite(motorPin1, HIGH);
  digitalWrite(motorPin2, LOW);
  digitalWrite(motorPin3, LOW);
  digitalWrite(motorPin4, HIGH);
  buzz_continuous(); // Make continuous sound while moving
}

void stop_motors() {
  digitalWrite(motorPin1, LOW);
  digitalWrite(motorPin2, LOW);
  digitalWrite(motorPin3, LOW);
  digitalWrite(motorPin4, LOW);
  buzz_stop(); // Silence the buzzer when motors stop
}

void init_motors() {
  pinMode(motorPin1, OUTPUT);
  pinMode(motorPin2, OUTPUT);
  pinMode(motorPin3, OUTPUT);
  pinMode(motorPin4, OUTPUT);
}

void buzz(int times) {
  for (int i = 0; i < times; i++) {
    digitalWrite(buzzerPin, HIGH);
    delay(100);
    digitalWrite(buzzerPin, LOW);
    delay(100);
  }
}

void buzz_continuous() {
  digitalWrite(buzzerPin, HIGH); // Make continuous sound while moving
}

void buzz_stop() {
  digitalWrite(buzzerPin, LOW); // Silence the buzzer when motors stop
}
