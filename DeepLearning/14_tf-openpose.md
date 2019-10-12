
- [tf-pose-estimation](#tf-pose-estimation)
  - [環境](#%e7%92%b0%e5%a2%83)
  - [環境構築(PC)](#%e7%92%b0%e5%a2%83%e6%a7%8b%e7%af%89pc)
    - [C++ コンパイラインストール](#c-%e3%82%b3%e3%83%b3%e3%83%91%e3%82%a4%e3%83%a9%e3%82%a4%e3%83%b3%e3%82%b9%e3%83%88%e3%83%bc%e3%83%ab)
    - [tf-pose-estimationのダウンロード](#tf-pose-estimation%e3%81%ae%e3%83%80%e3%82%a6%e3%83%b3%e3%83%ad%e3%83%bc%e3%83%89)
  - [環境構築(Anaconda)](#%e7%92%b0%e5%a2%83%e6%a7%8b%e7%af%89anaconda)
    - [構築後のライブラリ](#%e6%a7%8b%e7%af%89%e5%be%8c%e3%81%ae%e3%83%a9%e3%82%a4%e3%83%96%e3%83%a9%e3%83%aa)
    - [手順](#%e6%89%8b%e9%a0%86)
      - [swigのインストール](#swig%e3%81%ae%e3%82%a4%e3%83%b3%e3%82%b9%e3%83%88%e3%83%bc%e3%83%ab)
      - [必要ライブラリのインストール](#%e5%bf%85%e8%a6%81%e3%83%a9%e3%82%a4%e3%83%96%e3%83%a9%e3%83%aa%e3%81%ae%e3%82%a4%e3%83%b3%e3%82%b9%e3%83%88%e3%83%bc%e3%83%ab)
      - [pafprocessのビルド](#pafprocess%e3%81%ae%e3%83%93%e3%83%ab%e3%83%89)
  - [実行(Anaconda)](#%e5%ae%9f%e8%a1%8canaconda)
    - [手順](#%e6%89%8b%e9%a0%86-1)
  - [参考](#%e5%8f%82%e8%80%83)

# tf-pose-estimation
## 環境
- OS：Windows 10 Home (64bit)
- ツール：Anaconda (Python 3.7 version)
## 環境構築(PC)
### C++ コンパイラインストール
Pythonのバージョンに合わせたC++のコンパイラが必要

|Python version	|Visual Studio|
|--|--|
|2.7, 3.4|	2010|
|3.5	|2015 / 2017|
|3.6, 3.7, 3.8|	2017 / 2019|

- Build Tools for Visual Studio 2019 ダウンロード & インストール
- C++ Build Tools インストール
- システム環境変数に下記を設定（設定するパスはインストール時のフォルダ）
  - Path：C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Auxiliary\Build

### tf-pose-estimationのダウンロード
[github](https://github.com/ildoonet/tf-pose-estimation)からダウンロードする

## 環境構築(Anaconda)
- 前提：
  -  「Anaconda navigator」で「Enviroment」を作成済
  -  「Anaconda terminal」で以下を実行
### 構築後のライブラリ
```sh
(tf-openpose-2) xxxx>conda list
# packages in environment at xxxx\Anaconda3\envs\tf-openpose-2:
#
# Name                    Version                   Build  Channel
absl-py                   0.8.0                    pypi_0    pypi
argparse                  1.4.0                    pypi_0    pypi
astor                     0.8.0                    pypi_0    pypi
ca-certificates           2019.8.28                     0
certifi                   2019.9.11                py37_0
chardet                   3.0.4                    pypi_0    pypi
cycler                    0.10.0                   pypi_0    pypi
cython                    0.29.13                  pypi_0    pypi
decorator                 4.4.0                    pypi_0    pypi
dill                      0.3.1.1                  pypi_0    pypi
fire                      0.2.1                    pypi_0    pypi
gast                      0.3.2                    pypi_0    pypi
google-pasta              0.1.7                    pypi_0    pypi
grpcio                    1.24.1                   pypi_0    pypi
h5py                      2.10.0                   pypi_0    pypi
idna                      2.8                      pypi_0    pypi
imageio                   2.5.0                    pypi_0    pypi
keras-applications        1.0.8                    pypi_0    pypi
keras-preprocessing       1.1.0                    pypi_0    pypi
kiwisolver                1.1.0                    pypi_0    pypi
llvmlite                  0.29.0                   pypi_0    pypi
markdown                  3.1.1                    pypi_0    pypi
matplotlib                3.1.1                    pypi_0    pypi
msgpack                   0.6.2                    pypi_0    pypi
msgpack-numpy             0.4.4.3                  pypi_0    pypi
networkx                  2.3                      pypi_0    pypi
numba                     0.45.1                   pypi_0    pypi
numpy                     1.17.2                   pypi_0    pypi
opencv-python             4.1.1.26                 pypi_0    pypi
openssl                   1.1.1d               he774522_2
pillow                    6.2.0                    pypi_0    pypi
pip                       19.2.3                   py37_0
protobuf                  3.10.0                   pypi_0    pypi
psutil                    5.6.3                    pypi_0    pypi
pycocotools               2.0                      pypi_0    pypi
pyparsing                 2.4.2                    pypi_0    pypi
python                    3.7.4                h5263a28_0
python-dateutil           2.8.0                    pypi_0    pypi
pywavelets                1.0.3                    pypi_0    pypi
pyzmq                     18.1.0                   pypi_0    pypi
requests                  2.22.0                   pypi_0    pypi
scikit-image              0.15.0                   pypi_0    pypi
scipy                     1.3.1                    pypi_0    pypi
setuptools                41.2.0                   py37_0
six                       1.12.0                   pypi_0    pypi
slidingwindow             0.0.13                   pypi_0    pypi
sqlite                    3.30.0               he774522_0
swig                      3.0.12               h047fa9f_3
tabulate                  0.8.5                    pypi_0    pypi
tensorboard               1.14.0                   pypi_0    pypi
tensorflow                1.14.0                   pypi_0    pypi
tensorflow-estimator      1.14.0                   pypi_0    pypi
tensorpack                0.9.8                    pypi_0    pypi
termcolor                 1.1.0                    pypi_0    pypi
tqdm                      4.36.1                   pypi_0    pypi
urllib3                   1.25.6                   pypi_0    pypi
vc                        14.1                 h0510ff6_4
vs2015_runtime            14.16.27012          hf0eaf9b_0
werkzeug                  0.16.0                   pypi_0    pypi
wheel                     0.33.6                   py37_0
wincertstore              0.2                      py37_0
wrapt                     1.11.2                   pypi_0    pypi
```
### 手順
#### swigのインストール
```sh
# コマンド
conda install swig
```
```sh
# 結果
～(省略)～

Proceed ([y]/n)? y

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
```
#### 必要ライブラリのインストール
- 「requirements.txt」のインストール
  - pycocotools　はインストールエラーのため、「requirements.txt」からコメントアウト
```sh
# コマンド
pip install -r requirements.txt
```
```sh
# 結果
～(省略)～

Successfully built dill tensorpack tabulate
Installing collected packages: argparse, dill, termcolor, six, fire, cycler, numpy, pyparsing, python-dateutil, kiwisolver, matplotlib, llvmlite, numba, psutil, chardet, idna, urllib3, requests, decorator, networkx, pillow, imageio, PyWavelets, scikit-image, scipy, slidingwindow, tqdm, tabulate, msgpack, msgpack-numpy, pyzmq, tensorpack
Successfully installed PyWavelets-1.0.3 argparse-1.4.0 chardet-3.0.4 cycler-0.10.0 decorator-4.4.0 dill-0.3.1.1 fire-0.2.1 idna-2.8 imageio-2.5.0 kiwisolver-1.1.0 llvmlite-0.29.0 matplotlib-3.1.1 msgpack-0.6.2 msgpack-numpy-0.4.4.3 networkx-2.3 numba-0.45.1 numpy-1.17.2 pillow-6.2.0 psutil-5.6.3 pyparsing-2.4.2 python-dateutil-2.8.0 pyzmq-18.1.0 requests-2.22.0 scikit-image-0.15.0 scipy-1.3.1 six-1.12.0 slidingwindow-0.0.13 tabulate-0.8.5 tensorpack-0.9.8 termcolor-1.1.0 tqdm-4.36.1 urllib3-1.25.6
```

- pycocotoolsのインストール
  - Cython がないとインストールエラーとなる
```sh
# コマンド
pip install Cython
```
```sh
# 結果
～(省略)～

Successfully installed Cython-0.29.13
```
```sh
# コマンド
pip install "git+https://github.com/philferriere/cocoapi.git#egg=pycocotools&subdirectory=PythonAPI"
```
```sh
# 結果
～(省略)～

Successfully built pycocotools
Installing collected packages: pycocotools
Successfully installed pycocotools-2.0
```

- tensorflowのインストール
```sh
# コマンド
pip install tensorflow==1.14.0
```
```sh
# 結果
～(省略)～

Successfully installed absl-py-0.8.0 astor-0.8.0 gast-0.3.2 google-pasta-0.1.7 grpcio-1.24.1 h5py-2.10.0 keras-applications-1.0.8 keras-preprocessing-1.1.0 markdown-3.1.1 protobuf-3.10.0 tensorboard-1.14.0 tensorflow-1.14.0 tensorflow-estimator-1.14.0 werkzeug-0.16.0 wrapt-1.11.2
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

#### pafprocessのビルド
```sh
# コマンド
cd tf_pose/pafprocess
```
```sh
# コマンド
swig -python -c++ pafprocess.i && python setup.py build_ext --inplace
```
```sh
# 結果
～(省略)～

   ライブラリ build\temp.win-amd64-3.7\Release\_pafprocess.cp37-win_amd64.lib とオブジェクト build\temp.win-amd64-3.7\Release\_pafprocess.cp37-win_amd64.exp を作成中
コード生成しています。
コード生成が終了しました。
```

## 実行(Anaconda)
- 前提：
  -  「Anaconda terminal」で以下を実行
### 手順

```sh
# コマンド
python run_webcam.py --model=mobilenet_thin --resize=432x368 --camera=0
```

## 参考
- [github](https://github.com/ildoonet/tf-pose-estimation)
- [tensorflow（tf-openpose）で画像から骨格推定](https://qiita.com/nanako_ut/items/974466acf065b95f984a)
- [WindowsにSWIG導入](http://chachay.hatenablog.com/entry/2016/12/18/090010)
- [Fix Python 3 on Windows error Microsoft Visual C++ 14.0 is required](https://www.scivision.dev/python-windows-visual-c-14-required/)
- [WindowsでChainerを導入するための Visual Studio Build Tool 2015 が見つからず困ったときは](https://qiita.com/SatoshiTerasaki/items/a7724040910c18cd0d55)
- [Failed building wheel for pycocotools - Windows 10 conda](https://github.com/cocodataset/cocoapi/issues/169)
