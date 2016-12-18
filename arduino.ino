char pyin;
int cw,b,cw2;
int senswal;

int number[3],x,p=0;
String strings[3];
char command[3];

void setup() {
  Serial.begin(9600);
}

void loop() {
 //enter user code here. Whenever you think a command is needed from the python, use pyduino() function
 pyduino();
}

void pyduino(){
  
  x=ReceiveData();
  //analyzing the intput to determine function
  cw = x;
  //Serial.println(cw);
  if(cw & 64){
    darw(cw);
  }
  else if(cw & 32){
    pm(cw);
  }
}

void darw(int cw){
  if( cw & 32){
    if(cw & 16){
      delay(2);
      x = ReceiveData();
      cw2=x;
      //b = Serial.read();
      //cw2 = b;
      if(cw2 & 15)
      digitalWrite(cw & 15,HIGH);
      else 
      digitalWrite(cw & 15,LOW);
    }
    else{
      Serial.flush();
      senswal = digitalRead(cw & 15);
      Serial.write(senswal);
    }
  }
  else{
    if( cw & 16){
      int pin =(int) cw & 15;
      delay(2);
      if(Serial.available()){
       b=ReceiveData();
       int val= (int) (b & 255);
       analogWrite(pin,val);   
      }
    }  
    else{
      senswal = analogRead(cw & 15);
      Serial.write(senswal);
    }
  }
}

int pm(int cw){
  if(cw & 16){
    pinMode(cw & 15, OUTPUT);
    //Serial.println("pm output");
    return 1;
  }
  else{
    pinMode(cw & 15, INPUT);
    //Serial.println("pm input");
    return 1;
  }
}


int ReceiveData()
{
  p=0;
  while(!Serial.available())
  {
  } 
  for(int i=0;i<3;i++)
  {
    if(Serial.available()>0){
      strings[i]="";
    }
    while(Serial.available()>0){
      command[i]=((byte)(Serial.read()));
      if(command[i]>0){ //its not null
        if(command[i] == ':')
          break;
          else
            strings[i] += command[i];
      }
      delay(5);
    }
    number[i] = (int)strings[i][0];
    //Serial.write(number);
    //Serial.write(number1);
    number[i] = number[i]-48;
    p= p + number[i]*powint(10,i);
  }
return(p);
}

int powint(int x, int y)
{
 if (y==0)
   return(1);
 else
   return(powint(x,y-1)*x);
}
