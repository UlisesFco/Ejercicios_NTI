#Lectura de archivo csv del medidor

#librerías requeridas
require(tidyverse)
require(dplyr)
require(lubridate)
require(ggplot2)

#leer datos
data <- read_csv("datos_medidor.csv")

#juntar date y time en una sola columna
data <- data %>%
  unite("date_time",date,time,sep=" ")
data$date_time <- ymd_hms(data$date_time)

#graficar la primera fase de corriente
ggplot(data,aes(x=date_time,y=i1)) +
  geom_line() +
  labs(x="tiempo", y="Corriente [A]") +
  theme(axis.text.x = element_text(angle = 90, hjust = 1))+
  ggtitle("Corriente de la fase 1 a lo largo del tiempo")

#graficar la segunda fase de corrienteempo
ggplot(data,aes(x=date_time,y=i2)) +
  geom_line() +
  labs(x="tiempo", y="Corriente [A]") +
  theme(axis.text.x = element_text(angle = 90, hjust = 1))+
  ggtitle("Corriente de la fase 2 a lo largo del tiempo")

#graficar la tercera fase de corriente
ggplot(data,aes(x=date_time,y=i3)) +
  geom_line() +
  labs(x="tiempo", y="Corriente [A]") +
  theme(axis.text.x = element_text(angle = 90, hjust = 1))+
  ggtitle("Corriente de la fase 3 a lo largo del tiempo")
