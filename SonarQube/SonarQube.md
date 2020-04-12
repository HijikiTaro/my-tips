- [Overview](#overview)
  - [なぜ使うのか](#%e3%81%aa%e3%81%9c%e4%bd%bf%e3%81%86%e3%81%ae%e3%81%8b)
- [実施日](#%e5%ae%9f%e6%96%bd%e6%97%a5)
- [環境](#%e7%92%b0%e5%a2%83)
- [手順](#%e6%89%8b%e9%a0%86)
  - [Docker Host Requirements](#docker-host-requirements)
- [参考](#%e5%8f%82%e8%80%83)
- [メモ](#%e3%83%a1%e3%83%a2)

# Overview
- SonarQube を Docker で実施
  
## なぜ使うのか
- Java のみでなく、複数の言語が混ざったプロジェクトに対して静的コード解析を実施したい
- できれば見栄えがわかりやすい
- いっそのこと UnitTest も同時に実行したい
- そんなCIツールを見つけたい

# 実施日
- 2020/03/12

# 環境
- Windows 10 Home
- Docker

# 手順
＊基本は [SonaQube](https://hub.docker.com/_/sonarqube/) 

## Docker Host Requirements
- 実行すると下記エラーが発生
  - Elasticsearch で発生するエラーらしい（カーネルパラメータを増やせということらしい）
```
sonarqube_1  | ERROR: [1] bootstrap checks failed
sonarqube_1  | [1]: max virtual memory areas vm.max_map_count [65530] is too low, increase to at least [262144]
```

- サイト記載の下記設定を行う
  - 設定は VM 上で設定を行う（VirtualBox）
```sh
docker@default:~$ cat /proc/sys/vm/max_map_count
65530
docker@default:~$ sudo sysctl -w vm.max_map_count=262144
vm.max_map_count = 262144
docker@default:~$ cat /proc/sys/vm/max_map_count
262144
```
- 下記は Docker Hub の手順に書いてあった内容
  - 実際には1行目のみ設定
```sh
# Docker Host Requirements 
sysctl -w vm.max_map_count=262144
sysctl -w fs.file-max=65536
ulimit -n 65536
ulimit -u 4096
```

- 下記エラー発生
  - sysctl コマンドを実行してみると発生
```
bash: sysctl: command not found
```



# 参考
- https://hub.docker.com/_/sonarqube/
- https://github.com/spring-projects/spring-framework

# メモ
mvn sonar:sonar -Dsonar.projectKey=test2 -Dsonar.host.url=http://localhost:9000 -Dsonar.login=4c076e2a14e0fdf5d89a1e35ab522d133a0f6ec

SonarScanner for Gradle
```
gradlew sonarqube -Dsonar.projectKey=test2 -Dsonar.host.url=http://localhost:9000 -Dsonar.login=4c076e2a14e0fdf5d89a1e35ab522d133a0f6ecc

> Task :sonarqube
SonarScanner will require Java 11 to run starting in SonarQube 8.x

Deprecated Gradle features were used in this build, making it incompatible with Gradle 6.0.
Use '--warning-mode all' to show the individual deprecation warnings.
See https://docs.gradle.org/5.6.4/userguide/command_line_interface.html#sec:command_line_warnings

BUILD SUCCESSFUL in 1h 25m 8s
```

- 使い方は英語のチュートリアルを見ればわかる
- みんなが知りたいことはなぜ使うのか、どういう背景・目的があるか