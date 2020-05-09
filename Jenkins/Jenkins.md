- [Overview](#overview)
- [requirement](#requirement)
- [Pipline Design](#pipline-design)
- [環境](#%e7%92%b0%e5%a2%83)
- [note](#note)
  - [jenkins install](#jenkins-install)
- [reference](#reference)

# Overview
- Jenkins で自分が理想とするCI/CD環境を構築する
  
# requirement
- 1repo：N project
- インターネット接続可能 / 不可能

# Pipline Design
- build
  - maven
  - Git
- unit test
  - Junit 
- deploy
  - docker(container)
- notice
  - Gmail

# 環境
- Windows 10 Home
- Docker

# note
## jenkins install
- Dockerfile 参照
- Jenkins ディレクトリ構成
```
jenkins/
 Dockerfile
```
- docker run
```
docker run -p 8080:8080 -p 50000:50000 jenkins-work
docker run -p 9000:9000 -p 50000:50000 -v `pwd`/jenkins_home:/var/jenkins_home -d jenkins-work
docker run -p 8080:8080 -p 50000:50000 jenkins/jenkins:lts
docker run -d -v jenkins_home:/var/jenkins_home -p 8080:8080 -p 50000:50000 jenkins/jenkins:lts

docker run -p 8080:8080 -p 50000:50000 --restart=always -v jenkins-2150:/var/jenkins_home jenkins/jenkins:2.150.3
```


```docker-compose
version: '2'

services:
  jenkins:
    image: 'jenkins:2.60.3'
    container_name: jenkins
    user: root
    restart: always
    ports:
      - '8080:8080'
      - '50000:50000'
    volumes:
      - ./data/jenkins:/var/jenkins_home
#      - /var/run/docker.sock:/var/run/docker.sock
```

# reference
- https://jenkins.io/
- https://dev.classmethod.jp/articles/jenkins-on-docker/