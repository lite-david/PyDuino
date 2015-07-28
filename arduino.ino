char a;
char b;
int pin;
void setup() {
  Serial.begin(9600);
}

void loop() {
  
  if(Serial.available()){
    a = Serial.read();
    
    Serial.println((int)a);
    delay(1);
    if(Serial.available()){
        b = Serial.read();
        pin = a & 15;
        Serial.println(pin);
        if(b & 1){
            digitalWrite(pin,HIGH);
            delay(2000);
         }
        else{
            digitalWrite(pin,LOW);
            delay(2000);
        }
    }
  }
}
