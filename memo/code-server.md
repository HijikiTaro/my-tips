

```
docker run -it -p 8080:8080 -v ~/code-server:/home/coder codercom/code-server:latest
docker run -it -p 8080:8080 codercom/code-server:latest
```

```Dockerfile
FROM codercom/code-server:latest
VOLUME /home/coder

# RUN yum install -y java     # ②
# ADD files/apache-tomcat-9.0.6.tar.gz /opt/  # ③
# CMD [ "/opt/apache-tomcat-9.0.6/bin/catalina.sh", "run" ]  # ④


```
