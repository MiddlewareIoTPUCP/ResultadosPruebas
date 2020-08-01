200 usuarios
10 usuarios/seg
wait_time = [0,1]
3 dispositivos

INFLUX 14943 datos

RabbitMQ sirve como buffer para los mensajes que no se han procesado
(toma algo de 5 minutos en limpiar el buffer, el consumidor procesa ~100msg/seg) 2 workers