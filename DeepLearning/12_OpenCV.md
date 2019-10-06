
- [OpenCV](#opencv)
  - [環境](#%e7%92%b0%e5%a2%83)
  - [環境構築(Anaconda)](#%e7%92%b0%e5%a2%83%e6%a7%8b%e7%af%89anaconda)
    - [構築後のライブラリ](#%e6%a7%8b%e7%af%89%e5%be%8c%e3%81%ae%e3%83%a9%e3%82%a4%e3%83%96%e3%83%a9%e3%83%aa)
    - [手順](#%e6%89%8b%e9%a0%86)
  - [実行(Anaconda)](#%e5%ae%9f%e8%a1%8canaconda)
    - [手順](#%e6%89%8b%e9%a0%86-1)
  - [参考](#%e5%8f%82%e8%80%83)

# OpenCV
## 環境
- OS：Windows 10 Home (64bit)
- ツール：Anaconda (Python 3.7 version)

## 環境構築(Anaconda)
- 前提：
  -  「Anaconda navigator」で「Enviroment」を作成済
  -  「Anaconda terminal」で以下を実行
- 注意：
  - 下記手順を実施するタイミングによって、各ライブラリのバージョンが変わっている可能性があるため、なるべくバージョン指定で実行する方がよい
### 構築後のライブラリ
```sh
(opencv) xxxx>conda list
# packages in environment at xxxx\Anaconda3\envs\opencv:
#
# Name                    Version                   Build  Channel
certifi                   2019.9.11                py36_0
numpy                     1.17.2                   pypi_0    pypi
opencv-contrib-python     4.1.1.26                 pypi_0    pypi
opencv-python             4.1.1.26                 pypi_0    pypi
pip                       19.2.3                   py36_0
python                    3.6.9                h5500b2f_0
setuptools                41.2.0                   py36_0
sqlite                    3.30.0               he774522_0
vc                        14.1                 h0510ff6_4
vs2015_runtime            14.16.27012          hf0eaf9b_0
wheel                     0.33.6                   py36_0
wincertstore              0.2              py36h7fe50ca_0
```
### 手順
- OpenCVのインストール
```sh
# コマンド
pip install opencv-python
```
```sh
# 結果
～(省略)～

Successfully installed numpy-1.17.2 opencv-python-4.1.1.26
```
```sh
# コマンド
pip install opencv-contrib-python
```
```sh
# 結果
～(省略)～

Successfully installed opencv-contrib-python-4.1.1.26
```
- Pillowのインストール
```sh
# コマンド
pip install Pillow
```
```sh
# 結果
～(省略)～

Successfully installed Pillow-6.2.0
```

- 顔認識のモデルをダウンロード
[github](https://github.com/opencv/opencv)をダウンロードする。今回使用するのは「haarcascade_frontalface_default.xml」

## 実行(Anaconda)
- 前提：
  -  「Anaconda terminal」で以下を実行
### 手順

```py
import cv2
import datetime
import numpy as np
from PIL import Image

# オーバーレイ画像の読み込み
ol_imgae_path = "my_demo_sample/waraiotoko.png"    
ol_image = cv2.imread(ol_imgae_path,cv2.IMREAD_UNCHANGED)

def resize_image(image, height, width):

    # 元々のサイズを取得
    org_height, org_width = image.shape[:2]

    # 大きい方のサイズに合わせて縮小
    if float(height)/org_height > float(width)/org_width:
        ratio = float(height)/org_height
    else:
        ratio = float(width)/org_width

    resized = cv2.resize(image,(int(org_height*ratio),int(org_width*ratio)))

    return resized    

# PILを使って画像を合成
def overlayOnPart(src_image, overlay_image, posX, posY):

    # オーバレイ画像のサイズを取得
    ol_height, ol_width = overlay_image.shape[:2]

    # OpenCVの画像データをPILに変換
    #　BGRAからRGBAへ変換
    src_image_RGBA = cv2.cvtColor(src_image, cv2.COLOR_BGR2RGB)
    overlay_image_RGBA = cv2.cvtColor(overlay_image, cv2.COLOR_BGRA2RGBA)

    #　PILに変換
    src_image_PIL=Image.fromarray(src_image_RGBA)
    overlay_image_PIL=Image.fromarray(overlay_image_RGBA)

    # 合成のため、RGBAモードに変更
    src_image_PIL = src_image_PIL.convert('RGBA')
    overlay_image_PIL = overlay_image_PIL.convert('RGBA')

    # 同じ大きさの透過キャンパスを用意
    tmp = Image.new('RGBA', src_image_PIL.size, (255, 255,255, 0))
    # 用意したキャンパスに上書き
    tmp.paste(overlay_image_PIL, (posX, posY), overlay_image_PIL)
    # オリジナルとキャンパスを合成して保存
    result = Image.alpha_composite(src_image_PIL, tmp)

    # COLOR_RGBA2BGRA から COLOR_RGBA2BGRに変更。アルファチャンネルを含んでいるとうまく動画に出力されない。
    return  cv2.cvtColor(np.asarray(result), cv2.COLOR_RGBA2BGR)


face_cascade = cv2.CascadeClassifier('data/haarcascades/haarcascade_frontalface_default.xml')
 
 
def detect_face(img):
 
    face_img = img.copy()
  
    # グレースケールに変換
    frame_gray = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)
    
    # 顔認識の実行
    face_rects = face_cascade.detectMultiScale(frame_gray, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))
 
    for (x,y,w,h) in face_rects:
        cv2.rectangle(face_img, (x,y), (x+w,y+h), (255,255,255), 10)
        # 認識範囲にあわせて画像をリサイズ
        resized_ol_image = resize_image(ol_image, w, h)

        # オーバレイ画像の作成
        face_img = overlayOnPart(img, resized_ol_image, x, y)
 
    return face_img
    
cap = cv2.VideoCapture(0)
 
while True:
 
    ret, frame = cap.read(0)
 
    frame = detect_face(frame)
    
    cv2.imshow('Video Face Detection', frame)
 
    if cv2.waitKey(1) & 0xFF == 27:
        break
 
cap.release()
cv2.destroyAllWindows()
```

```sh
python opencv_run.py
```

## 参考
- [github](https://github.com/opencv/opencv)
- [PythonでOpenCVをはじめる（Windows10、Anaconda 2018.12、Python3.7.1、OpenCV4.0.0）](https://qiita.com/SatoshiGachiFujimoto/items/94da93f88578b87f6a89)
- [Detect Objects Using Your Webcam](https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/camera.html)
- [Python + OpenCV で雑コラ動画を作成する① 顔認識](https://qiita.com/k_sui_14/items/5386db1a118103b1828f)
- [pythonのOpenCVでリアルタイムに笑い男](https://blanktar.jp/blog/2015/02/python-opencv-realtime-lauhgingman.html)
