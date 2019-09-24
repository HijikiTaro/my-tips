# 環境
- Anaconda
- python 3.6
- tensorflow 1.14.0
- OpenCV 

```sh
(tf-openpose) [directory]> conda list
# packages in environment at C:\Users\yshtk\Anaconda3\envs\tf-openpose:
#
# Name                    Version                   Build  Channel
absl-py                   0.8.0                    pypi_0    pypi
argparse                  1.4.0                    pypi_0    pypi
astor                     0.8.0                    pypi_0    pypi
certifi                   2019.6.16                py36_1
chardet                   3.0.4                    pypi_0    pypi
cycler                    0.10.0                   pypi_0    pypi
cython                    0.29.13                  pypi_0    pypi
decorator                 4.4.0                    pypi_0    pypi
dill                      0.3.0                    pypi_0    pypi
fire                      0.2.1                    pypi_0    pypi
gast                      0.3.2                    pypi_0    pypi
google-pasta              0.1.7                    pypi_0    pypi
grpcio                    1.23.0                   pypi_0    pypi
h5py                      2.10.0                   pypi_0    pypi
idna                      2.8                      pypi_0    pypi
imageio                   2.5.0                    pypi_0    pypi
keras-applications        1.0.8                    pypi_0    pypi
keras-preprocessing       1.1.0                    pypi_0    pypi
kiwisolver                1.1.0                    pypi_0    pypi
llvmlite                  0.29.0                   pypi_0    pypi
markdown                  3.1.1                    pypi_0    pypi
matplotlib                3.1.1                    pypi_0    pypi
msgpack                   0.6.1                    pypi_0    pypi
msgpack-numpy             0.4.4.3                  pypi_0    pypi
networkx                  2.3                      pypi_0    pypi
numba                     0.45.1                   pypi_0    pypi
numpy                     1.17.2                   pypi_0    pypi
opencv-python             3.4.7.28                 pypi_0    pypi
pillow                    6.1.0                    pypi_0    pypi
pip                       19.2.2                   py36_0
protobuf                  3.9.1                    pypi_0    pypi
psutil                    5.6.3                    pypi_0    pypi
pycocotools               2.0                      pypi_0    pypi
pyparsing                 2.4.2                    pypi_0    pypi
python                    3.6.9                h5500b2f_0
python-dateutil           2.8.0                    pypi_0    pypi
pywavelets                1.0.3                    pypi_0    pypi
pyzmq                     18.1.0                   pypi_0    pypi
requests                  2.22.0                   pypi_0    pypi
scikit-image              0.15.0                   pypi_0    pypi
scipy                     1.3.1                    pypi_0    pypi
setuptools                41.0.1                   py36_0
six                       1.12.0                   pypi_0    pypi
slidingwindow             0.0.13                   pypi_0    pypi
sqlite                    3.29.0               he774522_0
swig                      3.0.12               h047fa9f_3
tabulate                  0.8.3                    pypi_0    pypi
tensorboard               1.14.0                   pypi_0    pypi
tensorflow                1.14.0                   pypi_0    pypi
tensorflow-estimator      1.14.0                   pypi_0    pypi
tensorpack                0.9.8                    pypi_0    pypi
termcolor                 1.1.0                    pypi_0    pypi
tqdm                      4.35.0                   pypi_0    pypi
urllib3                   1.25.3                   pypi_0    pypi
vc                        14.1                 h0510ff6_4
vs2015_runtime            14.16.27012          hf0eaf9b_0
werkzeug                  0.15.6                   pypi_0    pypi
wheel                     0.33.4                   py36_0
wincertstore              0.2              py36h7fe50ca_0
wrapt                     1.11.2                   pypi_0    pypi
```

```sh
(tf-openpose) [directory]> pip install tensorflow
```

```sh
(tf-openpose) [directory]> pip install opencv-python==3.4.7.28
```

# 手順
```sh
# 展開ディレクトリへ移動
cd ./tf-pose-estimation
```

```sh
# 必要なライブラリをインストール
pip install -r requirements.txt
```

- pycocotools　はインストールエラーのため、コメントアウト

- Build c++ library for post processing

```sh
cd tf_pose/pafprocess
```
```sh
swig -python -c++ pafprocess.i && python3 setup.py build_ext --inplace
```
```sh
running build_ext
building '_pafprocess' extension
swigging pafprocess.i to pafprocess_wrap.cpp
C:\Users\yshtk\Anaconda3\envs\tf-openpose\Library\bin\swig.exe -python -c++ -o pafprocess_wrap.cpp pafprocess.i
error: Unable to find vcvarsall.bat
```
C++ コンパイラの手順で解決


# swigインストール
- [SWIG](http://www.swig.org/download.html)
- 環境変数の設定

```sh
conda install swig
```

# C++ コンパイラ

- Build Tools for Visual Studio 2019 ダウンロード & インストール
- C++ Build Tools インストール
- C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Auxiliary\Build
- 環境変数に設定

一番最初に必要かも


# エラー

```sh
 ERROR: Command errored out with exit status 1:
     command: 'C:\Users\yshtk\Anaconda3\envs\tf-openpose\python.exe' -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'C:\\Users\\yshtk\\AppData\\Local\\Temp\\pip-install-6tl7g6o9\\pycocotools\\setup.py'"'"'; __file__='"'"'C:\\Users\\yshtk\\AppData\\Local\\Temp\\pip-install-6tl7g6o9\\pycocotools\\setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base pip-egg-info
         cwd: C:\Users\yshtk\AppData\Local\Temp\pip-install-6tl7g6o9\pycocotools\
    Complete output (5 lines):
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
      File "C:\Users\yshtk\AppData\Local\Temp\pip-install-6tl7g6o9\pycocotools\setup.py", line 2, in <module>
        from Cython.Build import cythonize
    ModuleNotFoundError: No module named 'Cython'
    ----------------------------------------
ERROR: Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
```

```sh
pip install Cython
```

```sh
Failed to build pycocotools
Installing collected packages: pycocotools
  Running setup.py install for pycocotools ... error
    ERROR: Command errored out with exit status 1:
     command: 'C:\Users\yshtk\Anaconda3\envs\tf-openpose\python.exe' -u -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'C:\\Users\\yshtk\\AppData\\Local\\Temp\\pip-install-q2paqqpb\\pycocotools\\setup.py'"'"'; __file__='"'"'C:\\Users\\yshtk\\AppData\\Local\\Temp\\pip-install-q2paqqpb\\pycocotools\\setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' install --record 'C:\Users\yshtk\AppData\Local\Temp\pip-record-d9pk7qom\install-record.txt' --single-version-externally-managed --compile
         cwd: C:\Users\yshtk\AppData\Local\Temp\pip-install-q2paqqpb\pycocotools\
    Complete output (19 lines):
    running install
    running build
    running build_py
    creating build
    creating build\lib.win-amd64-3.6
    creating build\lib.win-amd64-3.6\pycocotools
    copying pycocotools\coco.py -> build\lib.win-amd64-3.6\pycocotools
    copying pycocotools\cocoeval.py -> build\lib.win-amd64-3.6\pycocotools
    copying pycocotools\mask.py -> build\lib.win-amd64-3.6\pycocotools
    copying pycocotools\__init__.py -> build\lib.win-amd64-3.6\pycocotools
    running build_ext
    building 'pycocotools._mask' extension
    creating build\temp.win-amd64-3.6
    creating build\temp.win-amd64-3.6\Release
    creating build\temp.win-amd64-3.6\Release\pycocotools
    creating build\temp.win-amd64-3.6\Release\common
    C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Tools\MSVC\14.22.27905\bin\HostX86\x64\cl.exe /c /nologo /Ox /W3 /GL /DNDEBUG /MT -IC:\Users\yshtk\Anaconda3\envs\tf-openpose\lib\site-packages\numpy\core\include -Icommon -IC:\Users\yshtk\Anaconda3\envs\tf-openpose\include -IC:\Users\yshtk\Anaconda3\envs\tf-openpose\include "-IC:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Tools\MSVC\14.22.27905\include" "-IC:\Program Files (x86)\Windows Kits\NETFXSDK\4.7.2\include\um" "-IC:\Program Files (x86)\Windows Kits\10\include\10.0.18362.0\ucrt" "-IC:\Program Files (x86)\Windows Kits\10\include\10.0.18362.0\shared" "-IC:\Program Files (x86)\Windows Kits\10\include\10.0.18362.0\um" "-IC:\Program Files (x86)\Windows Kits\10\include\10.0.18362.0\winrt" "-IC:\Program Files (x86)\Windows Kits\10\include\10.0.18362.0\cppwinrt" /Tcpycocotools/_mask.c /Fobuild\temp.win-amd64-3.6\Release\pycocotools/_mask.obj -Wno-cpp -Wno-unused-function -std=c99
    cl : コマンド ライン error D8021 : 数値型引数 '/Wno-cpp' は無効です。
    error: command 'C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\BuildTools\\VC\\Tools\\MSVC\\14.22.27905\\bin\\HostX86\\x64\\cl.exe' failed with exit status 2
    ----------------------------------------
ERROR: Command errored out with exit status 1: 'C:\Users\yshtk\Anaconda3\envs\tf-openpose\python.exe' -u -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'C:\\Users\\yshtk\\AppData\\Local\\Temp\\pip-install-q2paqqpb\\pycocotools\\setup.py'"'"'; __file__='"'"'C:\\Users\\yshtk\\AppData\\Local\\Temp\\pip-install-q2paqqpb\\pycocotools\\setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' install --record 'C:\Users\yshtk\AppData\Local\Temp\pip-record-d9pk7qom\install-record.txt' --single-version-externally-managed --compile Check the logs for full command output.
```
```sh
pip install "git+https://github.com/philferriere/cocoapi.git#egg=pycocotools&subdirectory=PythonAPI"
```

# 参照
- [tensorflow（tf-openpose）で画像から骨格推定](https://qiita.com/nanako_ut/items/974466acf065b95f984a)
- [github](https://github.com/ildoonet/tf-pose-estimation)
- [How To Install Swig On MacOS, Linux And Windows](https://www.dev2qa.com/how-to-install-swig-on-macos-linux-and-windows/)
- [Installing SWIG on Windows](https://simpletutorials.com/c/2135/Installing+SWIG+on+Windows)
- [WindowsでChainerを導入するための Visual Studio Build Tool 2015 が見つからず困ったときは](https://qiita.com/SatoshiTerasaki/items/a7724040910c18cd0d55)
- [Fix Python 3 on Windows error Microsoft Visual C++ 14.0 is required](https://www.scivision.dev/python-windows-visual-c-14-required/)

