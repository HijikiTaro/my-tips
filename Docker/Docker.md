
- [Reference](#reference)
- [Development Environment](#development-environment)
- [Goal](#goal)
- [DockerHub](#dockerhub)
  - [Setup](#setup)
- [Docker](#docker)
  - [概要](#%e6%a6%82%e8%a6%81)
  - [手順](#%e6%89%8b%e9%a0%86)
- [docker-compose](#docker-compose)
  - [概要](#%e6%a6%82%e8%a6%81-1)
  - [使い方](#%e4%bd%bf%e3%81%84%e6%96%b9)

# Reference
- [Docker Documentation](https://docs.docker.com/get-started/)
- [AWS Docker](https://aws.amazon.com/jp/docker/)
- [Docker入門 #1 【Dockerとは】](https://qiita.com/wMETAw/items/b9bc643ded4b92bf6add)
- [Docker入門 #2 【Dockerチュートリアル】](https://qiita.com/wMETAw/items/8d1b0c053a39841765bf)
- [いまさらDockerに入門したので分かりやすくまとめます](https://qiita.com/gold-kou/items/44860fbda1a34a001fc1)
- [機械学習の環境構築のために今更ながらDocker入門](https://karaage.hatenadiary.jp/entry/2019/05/17/073000)
- [docker-composeを使うと複数コンテナの管理が便利に](https://qiita.com/y_hokkey/items/d51e69c6ff4015e85fce)
- [AWS EC2インスタンスにdockerとdocker-composeをインストールして簡単なWEBサービスを立ち上げる方法](https://qiita.com/y-do/items/e127211b32296d65803a)
- [AWS LambdaのCustom RuntimeでCOBOLを動かしてみた ](https://dev.classmethod.jp/cloud/aws/lambda-custom-runtimes-cobol/)
- [Dockerのまとめ - コンテナとイメージ編](https://qiita.com/kompiro/items/4153b4066a1837be7f98)

# Development Environment
- AWS EC2 Amazon Linux 2 AMI (HVM), SSD Volume Type

# Goal
- Dockerインストール　〇
- Docker起動　〇
- Dockerイメージ作成　〇
- DockerHubからプルしてDocekr起動　〇
- Dockerイメージをちょい修正してDockerイメージを作ってDokcerHubにあげる　〇
- Docker Composeを使ってみる 〇
- 

# DockerHub
## Setup
- [Docker Hub](https://hub.docker.com/)を開き、「Sign up for Docker Hub」をクリック
  - 1
- ユーザ情報を入力し、「Continue」をクリック
  - 2
- ユーザ情報を入力し、「Continue」をクリック
  - 3
- 「Docker Hub」から来たメールのリンクをクリックし、完了
  - 4
  
# Docker
## 概要
- Dockerイメージをダウンロード(Docker Pull)
- ダウンロードしたDockerイメージからコンテナを起動させる
## 手順
- Dockerイメージをダウンロードする
```sh
docker pull tensorflow/tensorflow
```

- Dockerイメージを検索する
```sh
docker search 'numpy'
```

- Dockerを起動する
```
docker run -it --rm --name tensorflow tensorflow/tensorflow
```

- Dockerを起動すると以下画面が表示される。(ここ以降はDocker内の作業となる)
```
$ docker run -it --rm --name tensorflow tensorflow/tensorflow

________                               _______________
___  __/__________________________________  ____/__  /________      __
__  /  _  _ \_  __ \_  ___/  __ \_  ___/_  /_   __  /_  __ \_ | /| / /
_  /   /  __/  / / /(__  )/ /_/ /  /   _  __/   _  / / /_/ /_ |/ |/ /
/_/    \___//_/ /_//____/ \____//_/    /_/      /_/  \____/____/|__/


WARNING: You are running this container as root, which can cause new files in
mounted volumes to be created as the root user on your host machine.

To avoid this, run the container by specifying your user's userid:

$ docker run -u $(id -u):$(id -g) args...

```

- ホストとコンテナでファイル共有
```
docker run -it -v $PWD/docker_share:/share --rm --name tensorflow tensorflow/tensorflow
```

- コンテナで起動したJupyter Notebookにホストのブラウザからアクセス
  - ここでいうホストはAWS
  - pullせずいきなりDockerを起動する
```
docker run -p 8888:8888 -it --rm --name ds jupyter/datascience-notebook
```

- Dockerイメージの作成（保存）
  - コンテナからイメージ作成
  - Dockerfileからイメージ作成
  - GitHubとDockerHubを連携させてイメージ作成

- コンテナからイメージ作成
```sh
docker commit ds hijikitaro/ds-image
```
- TODO:失敗
```
error during connect: Post http://docker:2375/v1.40/commit?author=&comment=&container=ds&repo=hijikitaro%2Fds-image&tag=latest: dial tcp: lookup docker on 172.31.0.2:53: no such host
```

- Dockerfileからイメージ作成
- Dockerfileを作成(ファイル名Dockerfile)
```
FROM centos:6

RUN set -x && \
    yum install -y epel-release && \
    yum install -y nginx && \
    sed -i -e "s/index  index.html index.htm/proxy_pass http:\/\/ip-api.com\/json/" \
        /etc/nginx/conf.d/default.conf && \
    ln -sf /dev/stdout /var/log/nginx/access.log && \
    ln -sf /dev/stderr /var/log/nginx/error.log

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

- DockerfileからDockerイメージ作成
```
docker build -t test-image .
```
- TODO:失敗

- 作成したDockerイメージをDockerHubへアップロード
```
docker login
```


# docker-compose
## 概要
- 複数Dockerを一つのファイルで管理できる


## 使い方
- AWS EC2 docker-composeをインストールする
  - [docker-compose](https://github.com/docker/compose/releases)
  - スーパーユーザの権限で実行
```
sudo -i
curl -L "https://github.com/docker/compose/releases/download/1.23.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
hmod +x /usr/local/bin/docker-compose
```

- 成功するdocker-compose
```sh
sudo curl -L "https://github.com/docker/compose/releases/download/1.23.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0$ docker-compose --version
docker-compose version 1.23.1, build b02f1306
100   617    0   617    0     0   4820      0 --:--:-- --:--:-- --:--:--  4820
100 11.1M  100 11.1M    0     0  28.9M      0 --:--:-- --:--:-- --:--:-- 28.9M

```
- 失敗するdocker-compose
```sh
curl -L https://github.com/docker/compose/releases/download/1.24.1/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   617    0   617    0     0   1804      0 --:--:-- --:--:-- --:--:--  1804
Warning: Failed to create the file /usr/local/bin/docker-compose: Permission
Warning: denied
  0 15.4M    0 16360    0     0  44336      0  0:06:04 --:--:--  0:06:04 44336
curl: (23) Failed writing body (0 != 16360)

```

- githubからDockerFile含めて一式ほしい場合は、gitをインストール
```sh
sudo yum install git
```


- docker image connect redmine
```
http://[AWSグローバルアドレス]:[ports]
```

- 起動中のDockerにDockerコマンドで入る場合
```sh
docker exec -it [CONTAINER ID] /bin/bash
```

- dockerにimageをコミット(DockerHubへではない)
```sh
docker commit docker-redmine_redmine_1_cbcb421fcbed hijikitaro/ds-image
```

- DockerHubにimageをpush
```sh
docker push [Dockerhubユーザ名]/[REPOSITORY]
```