//Practica 10 NTI
#define sensorPin 7
String bufer; //variable donde guardaremos nuestro payload
String bufer2="\n";   //agregamos un salto de linea al final de nuestro payload
String bufer3;

// Incluimos librería
#include <DHT11.h>
#include <SoftwareSerial.h>
// Definimos el pin digital donde se conecta el sensor
#define DHTPIN 2
// Dependiendo del tipo de sensor
#define DHTTYPE DHT11
 
// Inicializamos el sensor DHT11
DHT11 dht11(DHTPIN);

//Setup para obtener ID y PAC
void setup() {
//  dht11.begin();
  pinMode(13,OUTPUT);
  Serial.begin(9600);
  Serial3.begin(9600);
  Serial.println("----Iniciar Monitor Serial----");
  digitalWrite(13,LOW);
  delay(200);
  digitalWrite(13,HIGH);
  delay(200);
  Serial.println("AT"); //PC
  Serial3.write("AT\n"); //Modulo Sigfox
  delay(30);
  //read from port 1, send to port 0
  while(Serial3.available()){
    int inByte = Serial3.read();
    Serial.write(inByte);
  }
  
  Serial3.write("AT$I=10\n");
  delay(30);
  //read from port 1, send to port 0
  while(Serial3.available()){
    int inByte = Serial3.read();
    Serial.write(inByte);
  }

  Serial3.write("AT$I=11\n");
  delay(30);
  //read from port 1, send to port 0
  while(Serial3.available()){
    int inByte = Serial3.read();
    Serial.write(inByte);
  }
}

void leer_temperatura_humedad()
{
  Serial.println("Humedad: ");
  //float h = dht.readHumidity();
  //Serial.println(h);
  //Serial.println("Grados Cº: ");
  //float t = dht.readTemperature();
  //Serial.print(t);
  float t,h;
  int err;
  err =dht11.read(h,t);
  Serial.println(h);
  Serial.println("Grados Cº: ");
  Serial.println(t);

 //-----------------------------------------------------
  //AT$SF= comando para mandar la informacion por sigfox
  //Maximo 12 bytes
  //bufer="AT$SF=";
  
  byte* a1 = (byte*) &t;    //convertimos el dato a bytes
  byte* a2 = (byte*) &h;    //convertimos el dato a bytes

  //Serial.println(a1);
  String temp, hum;
  for(int i=0;i<4;i++)
  {
    temp=String(a1[i], HEX);    //convertimos el valor hex a string
    
    //Serial.println(temp);
    if(temp.length()<2)
    {
      bufer3+=0+temp;    //si no, se agrega un cero
    }
    else
    {
      bufer3+=temp;    //si esta completo, se copia tal cual
    }
    
  }
for(int k = 0; k<4;k++){
  hum=String(a2[k], HEX);    //convertimos el valor hex a string
  if(hum.length()<2)
    {
      bufer3+=0+hum;    //si no, se agrega un cero
    }
    else
    {
      bufer3+=hum;    //si esta completo, se copia tal cual
    }
}
  

  
    
  
  Serial3.print("AT$SF=");
  for (int j=0; j< bufer3.length();j++){
    Serial3.print(bufer3[j]);
  }
  Serial3.print("\n");
}

void add_float(float var1) //funcion para agregar flotantes al payload
{
  byte* a1 = (byte*) &var1;    //convertimos el dato a bytes
  String str1;
  //agregamos al comando AT$SF= nuestra informacion a enviar
  for(int i=0;i<4;i++)
  {
    str1=String(a1[i], HEX);    //convertimos el valor hex a string 
    if(str1.length()<2)
    {
      bufer+=0+str1;    //si no, se agrega un cero
    }
    else
    {
      bufer+=str1;    //si esta completo, se copia tal cual
    }
  }
}


boolean enviado = false;
uint8_t msg[12];

void loop() {
 if (!enviado){
  Serial.println("Enviando mensaje de temperatura...");
  enviado = true;
  digitalWrite(13,HIGH);
  delay(200);
  //digitalWrite(13,LOW);
  //delay(200)
  leer_temperatura_humedad();
  //Serial3.write("AT$SF=19201111,1\n");
  //Serial.println("Mensaje Modem");
  //Serial.println(Serial3.read());
  delay(30);
 }
}
