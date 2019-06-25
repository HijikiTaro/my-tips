# Visual Studio Code メモ

2019.06.23

- [Visual Studio Code メモ](#Visual-Studio-Code-%E3%83%A1%E3%83%A2)
  - [参考](#%E5%8F%82%E8%80%83)
  - [Visual Studio Code インストール](#Visual-Studio-Code-%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB)
  - [Git](#Git)
    - [Git インストール](#Git-%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB)
    - [Git 連携手順](#Git-%E9%80%A3%E6%90%BA%E6%89%8B%E9%A0%86)
  - [拡張機能](#%E6%8B%A1%E5%BC%B5%E6%A9%9F%E8%83%BD)
    - [Markdown All in One](#Markdown-All-in-One)

## 参考
https://qiita.com/y-tsutsu/items/2ba96b16b220fb5913be
https://qiita.com/takanatsu/items/fc89de9bd11148da1438
https://code.visualstudio.com/docs/editor/versioncontrol#_common-questions

## Visual Studio Code インストール
* 下記URLをクリックし、画像の「Download For Windows」をクリックする  
https://code.visualstudio.com/
  
![install01](image/001.PNG "install01")
  
ダウンロードされるのをひたすら待つ  
  
* ダウンロードされたexeを実行する  
![install02](image/002.PNG "install02")
  
* 「次へ」をクリックする  
![install03](image/003.PNG "install03")
  
* 「同意する」を選択し、「次へ」をクリックする  
![install04](image/004.PNG "install04")
  
* デフォルトのままで「次へ」をクリックする  
![install05](image/005.png "install05")
  
* デフォルトのままで「次へ」をクリックする  
![install06](image/006.PNG "install06")
  
* 下図の設定をして、「次へ」をクリックする  
![install07](image/007.PNG "install07")
  
* 「インストール」をクリックする  
![install08](image/008.PNG "install08")
  
* インストールされるのを待つ  
![install09](image/009.PNG "install09")
  
* 「完了」をクリックする  
![install10](image/010.PNG "install10")
  
* 下図の画面が表示されたら完了  
![install11](image/011.PNG "install11")

## Git
### Git インストール
* 下記URLをクリックし、画像の「Download」をクリックする
https://gitforwindows.org/
  
![install101](image/101.PNG "install101")
  
ダウンロードされるのをひたすら待つ  
  
* ダウンロードされたexeを実行する
![install102](image/102.PNG "install102")

* 「はい」をクリックし、「Next」をクリックする
![install103](image/103.PNG "install103")
  
* デフォルトのままで「Next」をクリックする  
![install104](image/104.PNG "install104")
  
* デフォルトのままで「Next」をクリックする  
![install105](image/105.PNG "install105")
  
* デフォルトのままで「Next」をクリックする  
![install106](image/106.PNG "install106")
  
* 下図の設定で「Next」をクリックする  
![install107](image/107.PNG "install107")
  
* デフォルトのままで「Next」をクリックする  
![install108](image/108.PNG "install108")
  
* デフォルトのままで「Next」をクリックする  
![install109](image/109.PNG "install109")
  
* デフォルトのままで「Next」をクリックする  
![install110](image/110.PNG "install110")
  
* デフォルトのままで「Next」をクリックする  
![install111](image/111.PNG "install111")
  
* デフォルトのままで「Next」をクリックする  
![install112](image/112.PNG "install112")
  
* デフォルトのままで「Install」をクリックする  
![install113](image/113.PNG "install113")
  
* インストールされるのを待つ  
![install114](image/114.PNG "install114")
  
* デフォルトのままで「Finish」をクリックする  
![install115](image/115.PNG "install115")

### Git 連携手順
* ローカルリポジトリとするフォルダを開く

* Gitにてローカルリポジトリを作成する

* 「Terminal」→「New Terminal」をクリックする
![aaa](image/116.PNG "aaa")

* 下記コマンドを実行し、ローカルリポジトリとリモートリポジトリを連携する
```
git remote add origin https://github.com/<repo owner>/<repo name>.git
```

* 下記コマンドを実行し、ローカルリポジトリをリモートリポジトリと同期をとる
```
git merge --allow-unrelated-histories origin/master
```

* 編集作業開始

## 拡張機能
### Markdown All in One
* Visual Studio Code を起動して、「表示」→ 「拡張機能」を選ぶ
* テキストボックスに 「markdown」と入力し、「Markdown All in One」をクリックしてインストールする
  
![aaa](image/201.PNG "aaa")
  
  
