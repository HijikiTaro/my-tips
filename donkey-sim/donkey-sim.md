- [Overview](#overview)
- [実施日](#%e5%ae%9f%e6%96%bd%e6%97%a5)
- [環境](#%e7%92%b0%e5%a2%83)
- [手順](#%e6%89%8b%e9%a0%86)
  - [Donkey Simulatorをインストールする](#donkey-simulator%e3%82%92%e3%82%a4%e3%83%b3%e3%82%b9%e3%83%88%e3%83%bc%e3%83%ab%e3%81%99%e3%82%8b)
  - [DonkeyCarをセットアップする（ Anaconda 上での作業）](#donkeycar%e3%82%92%e3%82%bb%e3%83%83%e3%83%88%e3%82%a2%e3%83%83%e3%83%97%e3%81%99%e3%82%8b-anaconda-%e4%b8%8a%e3%81%a7%e3%81%ae%e4%bd%9c%e6%a5%ad)
  - [donkey project を作成する（ Anaconda 上での作業）](#donkey-project-%e3%82%92%e4%bd%9c%e6%88%90%e3%81%99%e3%82%8b-anaconda-%e4%b8%8a%e3%81%a7%e3%81%ae%e4%bd%9c%e6%a5%ad)
  - [シミュレーターを起動してテスト走行する ~ 学習する](#%e3%82%b7%e3%83%9f%e3%83%a5%e3%83%ac%e3%83%bc%e3%82%bf%e3%83%bc%e3%82%92%e8%b5%b7%e5%8b%95%e3%81%97%e3%81%a6%e3%83%86%e3%82%b9%e3%83%88%e8%b5%b0%e8%a1%8c%e3%81%99%e3%82%8b--%e5%ad%a6%e7%bf%92%e3%81%99%e3%82%8b)
  - [自律走行してみる](#%e8%87%aa%e5%be%8b%e8%b5%b0%e8%a1%8c%e3%81%97%e3%81%a6%e3%81%bf%e3%82%8b)
- [Think](#think)
- [参考](#%e5%8f%82%e8%80%83)

# Overview
Donkey Simulator で学習モデルを使った自律走行を試してみる。
Donkey Car の仮想環境でのデータ収集、学習、検証のお試し。
環境を Windows で試す。

# 実施日
- 2020/03/12

# 環境
- Windows 10 Home
- Anacoda 3
- Ptyhon 3.7

# 手順
＊基本は [Donkey Carを組み立てる前にシミュレーターで楽しんでみる Donkey Car 3.1.0編](https://qiita.com/bathtimefish/items/99afeaa406cc60ff2204) と同じ手順（ただし、記事は Mac のため、多少手順が異なる）

## Donkey Simulatorをインストールする
- 下記リンク先の DonkeySimWindows.zip をダウンロードし、任意のフォルダへ展開する
  - はMac版で記載
  - https://github.com/tawnkramer/gym-donkeycar/releases/tag/v18.9
  - 任意のフォルダを C:\tools とする

## DonkeyCarをセットアップする（ Anaconda 上での作業）
- 任意のフォルダを作成し、そのフォルダまで移動する
  - 任意のフォルダを donkeypjtest とする
- tensorflow をインストールする
  - 記事との差異： tensorflow のバージョンを指定する
    - ＊手順を実行する時期によって、 tensorflow の最新バージョンが異なるため。2020/03/12時点で tensorflow をバージョン指定なしでインストールすると 2.x 系となり、後続の作業が失敗する。（ここで以外にハマった）
```sh
pip install tensorflow==1.15.0
```
- donkeycar と gym-donkeycar は記事と同じ手順を実施する
```sh
# donkeycar clone & install
git clone -b master https://github.com/autorope/donkeycar
pip install -e donkeycar
# gym-donkeycar clone & install
git clone https://github.com/tawnkramer/gym-donkeycar
pip install -e gym-donkeycar
```

## donkey project を作成する（ Anaconda 上での作業）
- プロジェクトを作成する
  - 上記の手順の続きのフォルダから実施する
```sh
# create project
donkey createcar --path ./mycar
cd ./mycar
```
- myconfig.py を編集する
  - 200行目あたりの3行のコメントを外す
  - DONKEY_SIM_PATH は展開した DonkeySimWindows.zip 直下の DonkeySim.exe を指定する
```.py
DONKEY_GYM = True
DONKEY_SIM_PATH = "C:/tools/DonkeySimWindows/DonkeySim.exe"
DONKEY_GYM_ENV_NAME = "donkey-generated-track-v0"
```

## シミュレーターを起動してテスト走行する ~ 学習する
- 記事と手順は同じ
  - ＊とにかくシミュレーターで Donkey car を楽しむ
```sh
# train command
python manage.py train --tub=logs --model=models/mypilot.h5 --type=categorical
```

## 自律走行してみる
- Tips
  - 何度やっても自律走行しなかった原因は自分の環境では下記でした
    - 原因：Donkey Monitor で設定する Mode & Pilot の値が反映されない
      - 学習が上手くいっていないではなかった（このパターンもあるが、上記が原因）
      - そもそもなぜ反映されないかは不明（記事では上手くいっているっぽいので、自分の環境が悪いのか、どこかでソースが変わっているのかは判別していない）
    - 対策： donkeycar\donkeycar\parts\web_controller\web.py の LocalWebController を書き換える（Donkey Monitor は関係なく、学習モデルで走行するように変更）
```py
class LocalWebController():
#  set mode = 'user'
  set mode = 'local'
```
- 記事と手順は同じ
```sh
python manage.py drive --type=categorical --model=models/mypilot.h5
```

# Think
- 学習モデルで自律走行させるのは、なかなか面白い。が、まだまだコースを一周できる学習モデルができていない。この学習モデルのコツが難しそう。
- 学習のロジックが理解できていない。この部分を理解しないと学習精度の向上や改善ができなさそう
- 仕組みの理解がないと問題の調査にかなり時間がかかる。が、調査するためにプリントデバッグを仕込んで値を確認しながら実施することで、設定の問題を解決することができたため、調査時は値を確認することが一番の近道だということを知れたことは大きい。それに、仕組みの理解もかなり進んだのではと感じる。（図で書いてみるか・・・）

# 参考
- https://qiita.com/bathtimefish/items/99afeaa406cc60ff2204
- https://docs.donkeycar.com/guide/host_pc/setup_mac/