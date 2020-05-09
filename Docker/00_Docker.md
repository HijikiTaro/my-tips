# Docker
## command
### build
docker image build 
```
docker build -t {iamge name}:{tag} . -f {file name}
```
### image
docker image のリスト
```
docker iamge ls
```
### run
コンテナの起動
＊ iamge からコンテナ起動
＊ image がない場合は、Docker Hub から pull してくる
```
docker run -p 8080:8080 -p 50000:50000 jenkins-work
```
### ps
起動しているコンテナのリスト
```
docker ps
```
### stop
起動しているコンテナの停止
```
docker stop <CONTAINER ID>
```
### exec
```
docker exec -i -t 14ef96591ba0 /bin/bash
```


# Dockerfile

# docker compose

