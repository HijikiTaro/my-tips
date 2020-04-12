# Docker
## command
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
docker ps ls
```
### stop
起動しているコンテナの停止
```
docker stop <CONTAINER ID>
```

# Dockerfile
