#include <AFMotor.h>
#include <Servo.h>

String command;
#define trig A4
#define echo A5
#define max_distance 300
long distance = 0;


AF_DCMotor motor1(1, MOTOR12_1KHZ);
AF_DCMotor motor2(2, MOTOR12_1KHZ);
AF_DCMotor motor3(3, MOTOR34_1KHZ);
AF_DCMotor motor4(4, MOTOR34_1KHZ);

Servo myservo;

void setup() {
  Serial.begin(9600);
  pinMode(trig,OUTPUT);
  pinMode(echo,INPUT);
  myservo.attach(10);
  myservo.write(90);
}


void forward() {
  
  motor1.setSpeed(100);
  motor1.run(FORWARD);
  motor2.setSpeed(100);
  motor2.run(FORWARD);
  motor3.setSpeed(100);
  motor3.run(FORWARD);
  motor4.setSpeed(100);
  motor4.run(FORWARD);
  }


void backward() {
  motor1.setSpeed(100);
  motor1.run(BACKWARD);
  motor2.setSpeed(100);
  motor2.run(BACKWARD);
  motor3.setSpeed(100);
  motor3.run(BACKWARD);
  motor4.setSpeed(100);
  motor4.run(BACKWARD);
  delay(1500);
}

void left() {
  myservo.write(0);
  delay(500);
  myservo.write(90);
  delay(500);
  motor1.setSpeed(100);
  motor1.run(FORWARD);
  motor2.setSpeed(100);
  motor2.run(BACKWARD);
  motor3.setSpeed(100);
  motor3.run(FORWARD);
  motor4.setSpeed(100);
  motor4.run(BACKWARD);
  delay(2000);
  motor1.run(RELEASE);
  motor2.run(RELEASE);
  motor3.run(RELEASE);
  motor4.run(RELEASE);
}

void right() {
  myservo.write(180);
  delay(500);
  myservo.write(90);
  delay(500);
  motor1.setSpeed(100);
  motor1.run(BACKWARD);
  motor2.setSpeed(100);
  motor2.run(FORWARD);
  motor3.setSpeed(100);
  motor3.run(BACKWARD);
  motor4.setSpeed(100);
  motor4.run(FORWARD);
  delay(2000);
  motor1.run(RELEASE);
  motor2.run(RELEASE);
  motor3.run(RELEASE);
  motor4.run(RELEASE);
}

void Stop() {
  motor1.run(RELEASE);
  motor2.run(RELEASE);
  motor3.run(RELEASE);
  motor4.run(RELEASE);
}


void loop() {
  
 while(Serial.available()) {
  command = "";  
  command = Serial.readString();
  Serial.print(command);
 }
  if(command == "*move forward#"){

 while(1)
 {
    if(ultrasonic() <10)
    {
             Stop();
             break;
    }
    else
    {
       forward();
    }
  }
    
  }else if(command == "*move backward#"){
    backward();
  }else if(command == "*turn left#"){
    left();
  }else if(command == "*turn right#"){
    right();
  }else if(command == "*stop#") {
    Stop();}
    
  command = "";
}

long ultrasonic()
{
  digitalWrite(trig,LOW);
  delayMicroseconds(2);
  digitalWrite(trig,HIGH);
  delayMicroseconds(10);
  long distance1 = pulseIn(echo,HIGH);
  return distance1 /29/2 ;  
}
