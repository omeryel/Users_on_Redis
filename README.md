**Gerekenler:**\
-docker\
-docker.io\
-docker-engine\
-docker-compose

**Çalıştırma:**\
-docker-compose.yml dosyasının bulunduğu dizinde komut istemcisini çalıştırıyoruz.\
-`sudo docker-compose build`\
-`sudo docker-compose up`

**Çalışma Mantığı:**\
-`sudo docker-compose` build aşamasında python ,golang ve redis için containerler hazırlanıyor.\
-`sudo docker-compose up` containerler sırasıyla redis ,python, golang olarak çalıştırılıyor.\
-Redis 0.0.0.0:6379 da çalışıyor.\
-Golang client , python server olarak 50051 portunda çalısıyor.\
-Client "jsons" dizinini dolaşarak dosyaları okuyup grpc aracılıyla servere gönderiyor.\
-Server veriyi redise kayıt edip cliente yanıt dönüyor.

