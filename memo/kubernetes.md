
- [Kubernetes](#kubernetes)
  - [Reference](#reference)
  - [開発環境](#%e9%96%8b%e7%99%ba%e7%92%b0%e5%a2%83)
  - [チュートリアル](#%e3%83%81%e3%83%a5%e3%83%bc%e3%83%88%e3%83%aa%e3%82%a2%e3%83%ab)
    - [AWS CLI アップグレード](#aws-cli-%e3%82%a2%e3%83%83%e3%83%97%e3%82%b0%e3%83%ac%e3%83%bc%e3%83%89)
    - [AWS CLI 認証情報を設定する](#aws-cli-%e8%aa%8d%e8%a8%bc%e6%83%85%e5%a0%b1%e3%82%92%e8%a8%ad%e5%ae%9a%e3%81%99%e3%82%8b)
    - [eksctl をインストールする](#eksctl-%e3%82%92%e3%82%a4%e3%83%b3%e3%82%b9%e3%83%88%e3%83%bc%e3%83%ab%e3%81%99%e3%82%8b)
    - [Amazon EKS クラスターとワーカーノードを作成する](#amazon-eks-%e3%82%af%e3%83%a9%e3%82%b9%e3%82%bf%e3%83%bc%e3%81%a8%e3%83%af%e3%83%bc%e3%82%ab%e3%83%bc%e3%83%8e%e3%83%bc%e3%83%89%e3%82%92%e4%bd%9c%e6%88%90%e3%81%99%e3%82%8b)
  - [メモ](#%e3%83%a1%e3%83%a2)

# Kubernetes
## Reference
- [数時間で完全理解！わりとゴツいKubernetesハンズオン！！](https://qiita.com/Kta-M/items/ce475c0063d3d3f36d5d)
- [10分くらいでわかる、KubernetesとEKSの何が便利なのか](https://qiita.com/masachaco/items/3e50a1ac65cdd661a734)
- [Amazon EKS の開始方法](https://docs.aws.amazon.com/ja_jp/eks/latest/userguide/getting-started.html)
- [AWS EKSの公式チュートリアルをやってみる](https://qiita.com/omukaik/items/b032f0b7621d85c74076)
- [kubernetesで変わる開発スタイル 〜マイクロサービスじゃなくてもいいじゃない〜](https://speakerdeck.com/sgeengineer/kubernetesdebian-warukai-fa-sutairu-maikurosabisuziyanakutemoiiziyanai?slide=97)

## 開発環境
- Windows 10 Home
- Bash
- AWS EC2
- AWS CLI

## チュートリアル
eksctl の開始方法
### AWS CLI アップグレード
-python3のインストール
```sh
#コマンド
sudo yum install python3
```
```sh
#実行結果
Loaded plugins: extras_suggestions, langpacks, priorities, update-motd
amzn2-core                                                                                                                                                                                 | 2.4 kB  00:00:00
amzn2extra-docker                                                                                                                                                                          | 1.3 kB  00:00:00
Resolving Dependencies

～(省略)～

Installed:
  python3.x86_64 0:3.7.4-1.amzn2.0.1

Dependency Installed:
  python3-libs.x86_64 0:3.7.4-1.amzn2.0.1                            python3-pip.noarch 0:9.0.3-1.amzn2.0.1                            python3-setuptools.noarch 0:38.4.0-3.amzn2.0.6

Complete!
```
-AWS CLIのアップグレード

```sh
#コマンド
pip3 install --upgrade --user awscli
```
```sh
#実行結果
Collecting awscli
  Downloading https://files.pythonhosted.org/packages/8e/75/d09f1d58254cb1dfb3675f08f00333d97df182b7f681dbb6b2b6c7cc9340/awscli-1.16.215-py2.py3-none-any.whl (1.9MB)

～(省略)～

Installing collected packages: docutils, colorama, pyasn1, rsa, six, python-dateutil, jmespath, urllib3, botocore, s3transfer, PyYAML, awscli
  Running setup.py install for PyYAML ... done
Successfully installed PyYAML-5.1 awscli-1.16.215 botocore-1.12.205 colorama-0.3.9 docutils-0.14 jmespath-0.9.4 pyasn1-0.4.6 python-dateutil-2.8.0 rsa-3.4.2 s3transfer-0.2.1 six-1.12.0 urllib3-1.25.3
```

```sh
#コマンド
export PATH=/home/ec2-user/.local/bin:$PATH
```
```sh
#実行結果なし
```

```sh
#コマンド
aws --version
```
```sh
#実行結果
aws-cli/1.16.215 Python/3.7.4 Linux/4.14.123-111.109.amzn2.x86_64 botocore/1.12.205
```

### AWS CLI 認証情報を設定する
- IAM設定
- ユーザ選択
- プログラムによるアクセス
- EKSを選択
- 完了

```sh
#コマンド
aws configure
```
```sh
#実行結果
AWS Access Key ID [None]: xxxxxxxxxxxxxxxxxxxx
AWS Secret Access Key [None]: xxxxxxxxxxxxxxxxxxxx
Default region name [None]:  us-west-2
Default output format [None]: json
```

### eksctl をインストールする
```sh
#コマンド
curl --silent --location "https://github.com/weaveworks/eksctl/releases/download/latest_release/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
```
```sh
#実行結果なし
```

```sh
#コマンド
sudo mv /tmp/eksctl /usr/local/bin
```
```sh
#実行結果なし
```

```sh
#コマンド
eksctl version
```
```sh
#実行結果
[ℹ]  version.Info{BuiltAt:"", GitCommit:"", GitTag:"0.3.1"}
```
※GitTag のバージョンは 0.1.37 以上であることが必要です

### Amazon EKS クラスターとワーカーノードを作成する
```sh
#コマンド
eksctl create cluster \
--name prod \
--version 1.13 \
--nodegroup-name standard-workers \
--node-type t3.medium \
--nodes 3 \
--nodes-min 1 \
--nodes-max 4 \
--node-ami auto
```
```sh
#実行結果
（失敗）
```


```sh
#コマンド
```
```sh
#実行結果
```

## メモ
- EKSコンソール作成
  - アベイラビリティーゾーンでつまずく
  - とりあえず、だめだったやつを除いて実行していくとできた
- EKSをeksctlで実行しても同様のエラーが発生・・・（解決方法不明）
- kubeconfig作成
```sh
#コマンド
aws eks --region us-east-1 update-kubeconfig --name EKS_TEST
```
```sh
#実行結果
Added new context arn:aws:eks:us-east-1:406183627447:cluster/EKS_TEST to /home/ec2-user/.kube/config
Warning: aws-iam-authenticator is not installed properly or is not in your path.
Refer to the AWS Documentation to download it at https://docs.aws.amazon.com/eks/latest/userguide/configure-kubectl.html
```
- aws-iam-authenticator のインストール
```sh
#コマンド
curl -o aws-iam-authenticator https://amazon-eks.s3-us-west-2.amazonaws.com/1.13.7/2019-06-11/bin/linux/amd64/aws-iam-authenticator
```
```sh
#実行結果
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 17.7M  100 17.7M    0     0  6052k      0  0:00:03  0:00:03 --:--:-- 6052k
```
```sh
#コマンド
curl -o aws-iam-authenticator.sha256 https://amazon-eks.s3-us-west-2.amazonaws.com/1.13.7/2019-06-11/bin/linux/amd64/aws-iam-authenticator.sha256
```
```sh
#実行結果
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    87  100    87    0     0    251      0 --:--:-- --:--:-- --:--:--   251
```

```sh
#コマンド
openssl sha1 -sha256 aws-iam-authenticator
```
```sh
#実行結果
SHA256(aws-iam-authenticator)= cc35059999bad461d463141132a0e81906da6c23953ccdac59629bb532c49c83
```

```sh
#コマンド
chmod +x ./aws-iam-authenticator
```
```sh
#実行結果なし
```

```sh
#コマンド
mkdir -p $HOME/bin && cp ./aws-iam-authenticator $HOME/bin/aws-iam-authenticator && export PATH=$HOME/bin:$PATH
```
```sh
#実行結果なし
```

```sh
#コマンド
echo 'export PATH=$HOME/bin:$PATH' >> ~/.bashrc
```
```sh
#実行結果なし
```

```sh
#コマンド
aws-iam-authenticator help
```
```sh
#実行結果
A tool to authenticate to Kubernetes using AWS IAM credentials

Usage:
  aws-iam-authenticator [command]

Available Commands:
  help        Help about any command
  init        Pre-generate certificate, private key, and kubeconfig files for the server.
  server      Run a webhook validation server suitable that validates tokens using AWS IAM
  token       Authenticate using AWS IAM and get token for Kubernetes
  verify      Verify a token for debugging purpose
  version     Version will output the current build information

Flags:
  -i, --cluster-id ID       Specify the cluster ID, a unique-per-cluster identifier for your aws-iam-authenticator installation.
  -c, --config filename     Load configuration from filename
  -h, --help                help for aws-iam-authenticator
  -l, --log-format string   Specify log format to use when logging to stderr [text or json] (default "text")

Use "aws-iam-authenticator [command] --help" for more information about a command.
```
- EKSはAWS CLIと同じユーザで作成しないとエラーとなる
- 結局上手くいかない・・・