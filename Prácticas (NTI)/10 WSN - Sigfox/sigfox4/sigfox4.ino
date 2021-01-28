//Practica 10 NTI
#define sensorPin 7
String bufer; //variable donde guardaremos nuestro payload
String bufer2="\n";   //agregamos un salto de linea al final de nuestro payload
String bufer3;

// Incluimos librería
#include <DHT.h>
#include <SoftwareSerial.h>
// Definimos el pin digital donde se conecta el sensor
#define DHTPIN 2
// Dependiendo del tipo de sensor
#define DHTTYPE DHT11
 
// Inicializamos el sensor DHT11
DHT dht(DHTPIN, DHTTYPE);

//Setup para obtener ID y PAC
void setup() {
  dht.begin();
  
  pinMode(13,OUTPUT);
  //Iniciar interfaces seriales
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
  float h = dht.readHumidity();
  h = 24.0;
  Serial.println(h);
  Serial.println("Grados Cº: ");
  float t = dht.readTemperature();
  t = 14.0;
  Serial.print(t);
  
  
 //-----------------------------------------------------
  //AT$SF= comando para mandar la informacion por sigfox
  //Maximo 12 bytes
  
  byte* a1 = (byte*) &t;    //convertimos el dato a bytes
  byte* a2 = (byte*) &h;    //convertimos el dato a bytes

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
   for(int i=0;i<4;i++)
  {
    hum =String(a2[i],HEX);    //convertimos el valor hex a string
    //Serial.println(hum);
    if(hum.length()<2)
    {
      bufer3+=0+hum;    //si no, se agrega un cero
    }
    else
    {
      bufer3+=hum;    //si esta completo, se copia tal cual
    }
  }
  Serial3.write("AT$SF=");
  for (int j=6; j< bufer3.length();j++){
    Serial3.write(bufer3[j]);
  }
  Serial3.write("\n");
}

boolean enviado = false;

void loop() {
 if (!enviado){
  Serial.println("Enviando mensaje de temperatura...");
  enviado = true;
  digitalWrite(13,LOW);
  delay(200);
  digitalWrite(13,HIGH);
  delay(200);
  leer_temperatura_humedad();
  //Serial3.write("AT$SF=19201111,1\n");
  //Serial.println("Mensaje Modem");
  //Serial.println(Serial3.read());
  delay(30);
 }
}
