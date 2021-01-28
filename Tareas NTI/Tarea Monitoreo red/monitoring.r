#Lectura de archivo csv del monitoreo

#librerías requeridas
require(tidyverse)
require(dplyr)
require(lubridate)
require(stringr)
require(ggplot2)

#leer datos
data <- read_csv("monitoreo.csv")
#modificar formatos de fecha
data$ini_monit <- str_replace(data$ini_monit," 2019","")
data$ini_monit <- str_replace(data$ini_monit,"Mon ","2019 ")
data$ini_monit <- str_replace(data$ini_monit,"Tue ","2019 ")
data$ini_monit <- str_replace(data$ini_monit,"Wed ","2019 ")
data$ini_monit <- str_replace(data$ini_monit,"Thu ","2019 ")
data$ini_monit <- str_replace(data$ini_monit,"Fri ","2019 ")
data$ini_monit <- str_replace(data$ini_monit,"Sat ","2019 ")
data$ini_monit <- str_replace(data$ini_monit,"Sun ","2019 ")
data$ini_monit <- ymd_hms(data$ini_monit)

#agregar tiempo en segundos
data <- data %>%
  mutate(tiempo = as.integer(as.POSIXct(ini_monit)))

#resumen de los datos
summary(data)
total_desc = sum(data$desconexion)
print(paste("Número de desconexiones totales: ",total_desc))

write.table(data, file = "datosWSN.csv",row.names=FALSE, na="",col.names=TRUE, sep=",")

#agrupar tabla por nodo y ordenar por latencia (ascendente)
data_monitor_nodo <- data %>%
  group_by(mac_local,mac_destino) %>%
  summarise(latencia_prom= mean(latencia), latencia_var = var(latencia), 
            min_lat = min(latencia), max_lat = max(latencia),
            rssi_prom = mean(rssi),rssi_var = var(rssi), 
            rssi_min = min(rssi), rssi_max = max(rssi),
            lqi_prom = mean(lqi), lqi_var = var(lqi),
            lqi_min = min(lqi), lqi_max = max(lqi)) %>%
  arrange(mac_destino, mac_local)

write.table(data_monitor_nodo, file = "stats_WSN.csv",row.names=FALSE, na="",col.names=TRUE, sep=",")

print("Latencia promedio por radio [ms]")
print(data_monitor_nodo)

#agrupar por nodo
data_monitor_desc <- data %>%
  filter(desconexion > 0) %>%
  group_by(mac_local,mac_destino) %>%
  arrange(ini_monit)

write.table(data_monitor_desc, file = "desconexiones_WSN_raw.csv",row.names=FALSE, na="",col.names=TRUE, sep=",")
print("datos agrupados por nodo")
head(data_monitor_desc)

#obtener mac y numero de desconexiones de los nodos
desconectados <-data_monitor_desc %>%
  group_by(mac_local,mac_destino) %>%
  summarise(num_desc = sum(desconexion))

aux_desc <-data %>%
  group_by(mac_local,mac_destino) %>%
  summarise(n=n())

desconectados <- inner_join(desconectados,aux_desc)

desconectados <- desconectados %>%
  mutate(proporcion_desc = num_desc/n)

write.table(desconectados, file = "datos_desconexion.csv",row.names=FALSE, na="",col.names=TRUE, sep=",")

print("Estadísticas de desconexión")
desconectados

#graficar rssi a lo a lo largo del tiempo
ggplot(data,aes(x=ini_monit,y=rssi,color=mac_destino)) +
  geom_line() +
  labs(x="tiempo", y="rssi") +
  theme(axis.text.x = element_text(angle = 90, hjust = 1))+
  ggtitle("RSSI a lo largo del tiempo de monitoreo por MAC de destino")

#graficar lqi a lo a lo largo del tiempo
ggplot(data,aes(x=ini_monit,y=lqi,color=mac_destino)) +
  geom_line() +
  labs(x="Tiempo", y="lqi") +
  theme(axis.text.x = element_text(angle = 90, hjust = 1)) +
  ggtitle("LQI a lo largo del tiempo de monitoreo por MAC de destino")

#histograma de desconexiones:
ggplot(data_monitor_desc,aes(x=mac_local,y=desconexion)) +
  geom_bar(stat = "identity") +
  labs(x="MAC de radio", y="# desconexiones") +
  ggtitle("Número de desconexiones por mac local")
