
- [Object Detection Tools](#object-detection-tools)
  - [環境](#%e7%92%b0%e5%a2%83)
  - [環境構築(PC)](#%e7%92%b0%e5%a2%83%e6%a7%8b%e7%af%89pc)
    - [Object Detection Toolsのダウンロード](#object-detection-tools%e3%81%ae%e3%83%80%e3%82%a6%e3%83%b3%e3%83%ad%e3%83%bc%e3%83%89)
    - [学習済みモデルのダウンロード](#%e5%ad%a6%e7%bf%92%e6%b8%88%e3%81%bf%e3%83%a2%e3%83%87%e3%83%ab%e3%81%ae%e3%83%80%e3%82%a6%e3%83%b3%e3%83%ad%e3%83%bc%e3%83%89)
  - [環境構築(Anaconda)](#%e7%92%b0%e5%a2%83%e6%a7%8b%e7%af%89anaconda)
    - [構築後のライブラリ](#%e6%a7%8b%e7%af%89%e5%be%8c%e3%81%ae%e3%83%a9%e3%82%a4%e3%83%96%e3%83%a9%e3%83%aa)
    - [手順](#%e6%89%8b%e9%a0%86)
  - [実行(Anaconda)](#%e5%ae%9f%e8%a1%8canaconda)
    - [手順](#%e6%89%8b%e9%a0%86-1)
    - [補足](#%e8%a3%9c%e8%b6%b3)
  - [参考](#%e5%8f%82%e8%80%83)

# Object Detection Tools
## 環境
- OS：Windows 10 Home (64bit)
- ツール：Anaconda (Python 3.7 version)
## 環境構築(PC)
### Object Detection Toolsのダウンロード
[github](https://github.com/karaage0703/object_detection_tools)からダウンロードする

### 学習済みモデルのダウンロード
「Object Detection Tools」の「models」内の「get_ssd_inception_v2_coco_model.sh」を実行することでダウンロードできる。

※ただし、shellのためWSL（Windows Subsystem for Linux）で実行し、「models」にコピーすることを今回は実施。

## 環境構築(Anaconda)
- 前提：
  -  「Anaconda navigator」で「Enviroment」を作成済
  -  「Anaconda terminal」で以下を実行
### 構築後のライブラリ
```sh
(od-tools-2) xxxx>conda list
# packages in environment at xxxx\Anaconda3\envs\od-tools-2:
#
# Name                    Version                   Build  Channel
absl-py                   0.8.0                    pypi_0    pypi
astor                     0.8.0                    pypi_0    pypi
ca-certificates           2019.8.28                     0
certifi                   2019.9.11                py37_0
gast                      0.3.2                    pypi_0    pypi
grpcio                    1.24.1                   pypi_0    pypi
h5py                      2.10.0                   pypi_0    pypi
keras-applications        1.0.8                    pypi_0    pypi
keras-preprocessing       1.1.0                    pypi_0    pypi
markdown                  3.1.1                    pypi_0    pypi
mock                      3.0.5                    pypi_0    pypi
numpy                     1.17.2                   pypi_0    pypi
opencv-python             4.1.1.26                 pypi_0    pypi
openssl                   1.1.1d               he774522_2
pip                       19.2.3                   py37_0
protobuf                  3.10.0                   pypi_0    pypi
python                    3.7.4                h5263a28_0
setuptools                41.2.0                   py37_0
six                       1.12.0                   pypi_0    pypi
sqlite                    3.30.0               he774522_0
tensorboard               1.13.1                   pypi_0    pypi
tensorflow                1.13.1                   pypi_0    pypi
tensorflow-estimator      1.13.0                   pypi_0    pypi
termcolor                 1.1.0                    pypi_0    pypi
vc                        14.1                 h0510ff6_4
vs2015_runtime            14.16.27012          hf0eaf9b_0
werkzeug                  0.16.0                   pypi_0    pypi
wheel                     0.33.6                   py37_0
wincertstore              0.2                      py37_0
```
### 手順
- tensorflowのインストール
```sh
# コマンド
pip install tensorflow==1.13.1
```
```sh
# 結果
～(省略)～

Successfully installed absl-py-0.8.0 astor-0.8.0 gast-0.3.2 grpcio-1.24.1 h5py-2.10.0 keras-applications-1.0.8 keras-preprocessing-1.1.0 markdown-3.1.1 mock-3.0.5 numpy-1.17.2 protobuf-3.10.0 six-1.12.0 tensorboard-1.13.1 tensorflow-1.13.1 tensorflow-estimator-1.13.0 termcolor-1.1.0 werkzeug-0.16.0
```
- OpenCVのインストール
```sh
# コマンド
pip install opencv-python
```
```sh
# 結果
～(省略)～

Successfully installed opencv-python-4.1.1.26
```

## 実行(Anaconda)
- 前提：
  -  「Anaconda terminal」で以下を実行
### 手順
※object_detection.py の「labels」と「model」の部分が相対パスでは動作しなかったため、絶対パスに変更している。
Windowsだと時々遭遇する問題らしく、参照する際の相対パスを絶対パスに書き換えると解消するらしい。（今回もこれで解消しているが、原因はわからない。）

```sh
# コマンド
python scripts/object_detection.py
```

### 補足
学習モデルを変えることで、手の検出も簡単に行える。

## 参考
- [github](https://github.com/karaage0703/object_detection_tools)
- [TensorFlowの物体検出用ライブラリ「Object Detection API」を手軽に使えるソフト「Object Detection Tools」を作ってみた](https://karaage.hatenadiary.jp/entry/2019/05/27/073000)
- [ディープラーニングで高性能な手の検出器を簡単に作る方法](https://qiita.com/karaage0703/items/962c550868b9383e78c7)
- [[TF] Object Detection API でNewRandomAccessFile failed to Create/Openエラー](https://qiita.com/onehara/items/4c69c9a81832f472445f)

