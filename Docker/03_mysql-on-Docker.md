
- [セットアップ](#%e3%82%bb%e3%83%83%e3%83%88%e3%82%a2%e3%83%83%e3%83%97)
  - [環境](#%e7%92%b0%e5%a2%83)
  - [MySQL環境構築](#mysql%e7%92%b0%e5%a2%83%e6%a7%8b%e7%af%89)
    - [対象](#%e5%af%be%e8%b1%a1)
    - [Dockerフォルダ作成](#docker%e3%83%95%e3%82%a9%e3%83%ab%e3%83%80%e4%bd%9c%e6%88%90)
    - [各種ファイル作成](#%e5%90%84%e7%a8%ae%e3%83%95%e3%82%a1%e3%82%a4%e3%83%ab%e4%bd%9c%e6%88%90)
  - [MySQL実行](#mysql%e5%ae%9f%e8%a1%8c)
- [memo](#memo)
  - [docker run エラー](#docker-run-%e3%82%a8%e3%83%a9%e3%83%bc)
- [参考](#%e5%8f%82%e8%80%83)

# セットアップ
## 環境
- OS：Windows 10 Home (64bit)
- Docker Toolbox
## MySQL環境構築
### 対象
- MySQL 5.7
### Dockerフォルダ作成
- 以下のフォルダ構成
```
├── docker
│   └── db
│       ├── data
│       ├── my.cnf
│       └── sql
│           ├── 001-create-tables.sql
│           └── init-database.sh
├── docker-compose.yml
└── init-mysql.sh
```
### 各種ファイル作成
- ファイルを作成し配置

## MySQL実行
- docker起動
  - めちゃめちゃ時間かかる・・・
```sh
docker-compose up -d
```
- docker起動確認
```sh
docker-compose ps
```
```sh
WARNING: Service "db" is using volume "/var/lib/mysql" from the previous container. Host mapping "/C/Users/yshtk/docker/mysql-sample/db/data" has no effect. Remove the existing containers (Recreating mysql_host ... done
```

- 下記でphpMyAdminへ接続
  - http://localhost:8080

  - 「Windows(8080) => VirtualBox(8080) => Docker(80)」となるようにVirtualBoxのネットワーク設定（ポートフォワーディング）を行う

# memo
## docker run エラー
- 現象
```sh
$ docker run -v /C/Users/yshtk/docker/docker-test:/test ubuntu /bin/bash
Unable to find image 'ubuntu:latest' locally
C:\Program Files\Docker Toolbox\docker.exe: Error response from daemon: Get https://registry-1.docker.io/v2/: net/http: request canceled while waiting for connection (Client.Timeout exceeded while awaiting headers).
See 'C:\Program Files\Docker Toolbox\docker.exe run --help'.
```

- 解決策
  - dockerが起動しているVMへ
```sh
$ docker-machine ssh default
```
  - nameserverを変更
    - 「nameserver 10.0.2.3」→「nameserver 8.8.8.8」
```sh
sudo vi /etc/resolv.conf
```
- 原因
  - ネットワーク（DNS？Proxy？が上手くつなげない？）


- [Windows10のDockerでdocker pullしたときに「Error response from daemon」となるときの対応](https://www.scriptlife.jp/contents/programming/2018/11/02/docker-pull-error-response-from-daemon/)
- [dockerでsearchまたはpullした時に名前解決が出来ないエラー](https://qiita.com/tk555/items/23bb5d3d5b613a03ca2b)

# 参考
- [docker-compose でMySQL環境簡単構築](https://qiita.com/A-Kira/items/f401aea261693c395966)
- [Windowsでdocker-composeしてvolumesでハマった時に個人的に気にするリスト](https://qiita.com/tettsu__/items/1e87e4a0d4d2ea96add9)
- [WindowsでDocker Toolbox＆docker-composeを動かす](https://nonsensej.xyz/articles/wp/1500)
- [Docker Toolbox利用時においてホストのディレクトリをマウントできない](https://qiita.com/gisuyama7/items/e2ed9e76cdbef798b48a)