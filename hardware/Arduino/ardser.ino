#include <SoftwareSerial.h>
#include <Servo.h>

SoftwareSerial espSerial(0,1); // RX, TX

Servo metalBin;
Servo plasticBin;
Servo glassBin;


void setup() {
  Serial.begin(9600);
  espSerial.begin(115200);
  metalBin.attach(8);
  plasticBin.attach(9);
  glassBin.attach(10);

  metalBin.write(90);
  plasticBin.write(90);
  glassBin.write(90);

}

void loop() {
  if (espSerial.available()){
    String pred = espSerial.readString();
    if (pred.toInt() == 0){
      metalBin.write(180);
      delay(10000);
      metalBin.write(90);
    } else if (pred.toInt() == 1){
      plasticBin.write(180);
      delay(10000);
      plasticBin.write(90);
    } else if (pred.toInt() == 2){
      glassBin.write(180);
      delay(10000);
      glassBin.write(90);
    }
  }
}