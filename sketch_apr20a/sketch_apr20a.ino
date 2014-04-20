#include <Servo.h> 

Servo myservo;

void setup() 
{ 
  Serial.begin(9600);
  myservo.attach(9);
  myservo.write(90);  // set servo to mid-point
} 

void loop() {
  while (!Serial.available());
  int in_byte = Serial.read();
  if(in_byte < 127)
  {
   myservo.write((90 - (127 - in_byte))*2); 
  }
  else
  {
    myservo.write((90 + (in_byte - 127))*2);
  }
 // (((Serial.read()-127)/127)*90));
}
  
 
