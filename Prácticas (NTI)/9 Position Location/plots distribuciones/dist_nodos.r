require(tidyverse)
require(dplyr)
require(ggplot2)

data <- read.csv("rssi_prom_total.csv")
#dist nodo 4
ggplot(data, aes(x=N0004)) + 
  geom_histogram(aes(y=..density..), colour="black", fill="white")+
  geom_density(alpha=.2, fill="#FF6666") +
  geom_vline(aes(xintercept=mean(N0004)),
             color="black", linetype="dashed", size=1) +
  labs(title="Histograma de N0004",x="rssi", y = "densidad")

#dist nodo 5
ggplot(data, aes(x=N0005)) + 
  geom_histogram(aes(y=..density..), colour="black", fill="white")+
  geom_density(alpha=.2, fill="#228B22") +
  geom_vline(aes(xintercept=mean(N0005)),
             color="black", linetype="dashed", size=1) +
  labs(title="Histograma de N0005",x="rssi", y = "densidad")
#dist nodo 6
ggplot(data, aes(x=N0006)) + 
  geom_histogram(aes(y=..density..), colour="black", fill="white")+
  geom_density(alpha=.2, fill="#2233DD") +
  geom_vline(aes(xintercept=mean(N0006)),
             color="black", linetype="dashed", size=1) +
  labs(title="Histograma de N0006",x="rssi", y = "densidad")

#dist nodo 7
ggplot(data, aes(x=N0007)) + 
  geom_histogram(aes(y=..density..), colour="black", fill="white")+
  geom_density(alpha=.2, fill="#DFFD31") +
  geom_vline(aes(xintercept=mean(N0007)),
             color="black", linetype="dashed", size=1) +
  labs(title="Histograma de N0007",x="rssi", y = "densidad")

#dist nodo 14
ggplot(data, aes(x=N0014)) + 
  geom_histogram(aes(y=..density..), colour="black", fill="white")+
  geom_density(alpha=.2, fill="#4B0082") +
  geom_vline(aes(xintercept=mean(N0014)),
             color="black", linetype="dashed", size=1) +
  labs(title="Histograma de N0014",x="rssi", y = "densidad")

#Datos de desviación estándar
rssi_data <- data %>%
  summarise(sd_0004 = sd(N0004), sd_0005 = sd(N0005),
            sd_0006 = sd(N0006), sd_0007 = sd(N0007), sd_0014 = sd(N0014))
print("Desviación estándar por nodo")
print(rssi_data)

global_sd <- sd(rssi_data[1,])
msg <- paste("Desviación estándar global:", global_sd)
print(msg)
