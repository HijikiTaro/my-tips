# 環境
- Anaconda
- tensorflow
- OpenCV

```sh
pip install tensorflow==1.13.1
```

```sh
pip install opencv-python
```

# メモ
- shはWindows環境では起動できないため、WSL上で動かす
- object_detection.py の相対パスを絶対パスにしてさらに直書きに修正

```sh
python scripts/object_detection.py -l='models\\coco-labels-paper.txt' -m='models\\ssd_inception_v2_coco_2018_01_28\\frozen_inference_graph.pb'
```

# 参照
- [TensorFlowの物体検出用ライブラリ「Object Detection API」を手軽に使えるソフト「Object Detection Tools」を作ってみた](https://karaage.hatenadiary.jp/entry/2019/05/27/073000)
- [TensorFlowの「Object Detection API」で物体検出の自前データを学習する方法](https://qiita.com/karaage0703/items/76ef6b774e3cd69028bb)

