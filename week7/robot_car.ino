//L293D
//Motor A
const int motorPin1  = 5;  // Pin 14 of L293
const int motorPin2  = 6;  // Pin 10 of L293
//Motor B
const int motorPin3  = 10; // Pin  7 of L293
const int motorPin4  = 9;  // Pin  2 of L293

void turn_left_motor_clockwise(void);
void turn_left_motor_anticlockwise(void);


void turn_right_motor_clockwise(void);
void turn_right_motor_anticlockwise(void);
void stop_motors(void);
void init_motors(void);

//This will run only one time.
void setup(){
 
    init_motors();
}


void loop(){
  turn_left_motor_clockwise();
  turn_right_motor_clockwise();
  
  turn_left_motor_anticlockwise();
  turn_right_motor_anticlockwise();
  
   stop_motors();
  
}

void turn_left_motor_clockwise(void){
  //This code  will turn left motor  clockwise for 2 sec.
    digitalWrite(motorPin1, HIGH);
    digitalWrite(motorPin2, LOW);
    digitalWrite(motorPin3, LOW);
    digitalWrite(motorPin4, LOW);
    delay(2000); 
  
}
void turn_left_motor_anticlockwise(void){
//This code will turn left Motor  counter-clockwise for 2 sec.
    digitalWrite(motorPin1, LOW);
    digitalWrite(motorPin2, HIGH);
    digitalWrite(motorPin3, LOW);
    digitalWrite(motorPin4, LOW);
    delay(2000);
  
}
void turn_right_motor_clockwise(void){
  //This code will turn  right Motor  clockwise for 2 sec.
    digitalWrite(motorPin1, LOW);
    digitalWrite(motorPin2, LOW);
    digitalWrite(motorPin3, HIGH);
    digitalWrite(motorPin4, LOW);
    delay(2000); 

  
}
void turn_right_motor_anticlockwise(void){
//This code will turn right Motor  counter-clockwise for 2 sec.
    digitalWrite(motorPin1, LOW);
    digitalWrite(motorPin2, LOW);
    digitalWrite(motorPin3, LOW);
    digitalWrite(motorPin4, HIGH);
    delay(2000); 
  
}

void init_motors(void){
  //Set pins as outputs
    pinMode(motorPin1, OUTPUT);
    pinMode(motorPin2, OUTPUT);
    pinMode(motorPin3, OUTPUT);
    pinMode(motorPin4, OUTPUT); 
}
 void stop_motors(void){
    digitalWrite(motorPin1, LOW);
    digitalWrite(motorPin2, LOW);
    digitalWrite(motorPin3, LOW);
    digitalWrite(motorPin4, LOW);
 }
