
- [Kubernetes](#kubernetes)
  - [Reference](#reference)
  - [開発環境](#%e9%96%8b%e7%99%ba%e7%92%b0%e5%a2%83)
  - [チュートリアル](#%e3%83%81%e3%83%a5%e3%83%bc%e3%83%88%e3%83%aa%e3%82%a2%e3%83%ab)
    - [AWS CLI アップグレード](#aws-cli-%e3%82%a2%e3%83%83%e3%83%97%e3%82%b0%e3%83%ac%e3%83%bc%e3%83%89)
    - [AWS CLI 認証情報を設定する](#aws-cli-%e8%aa%8d%e8%a8%bc%e6%83%85%e5%a0%b1%e3%82%92%e8%a8%ad%e5%ae%9a%e3%81%99%e3%82%8b)
    - [eksctl をインストールする](#eksctl-%e3%82%92%e3%82%a4%e3%83%b3%e3%82%b9%e3%83%88%e3%83%bc%e3%83%ab%e3%81%99%e3%82%8b)
    - [Amazon EKS クラスターとワーカーノードを作成する](#amazon-eks-%e3%82%af%e3%83%a9%e3%82%b9%e3%82%bf%e3%83%bc%e3%81%a8%e3%83%af%e3%83%bc%e3%82%ab%e3%83%bc%e3%83%8e%e3%83%bc%e3%83%89%e3%82%92%e4%bd%9c%e6%88%90%e3%81%99%e3%82%8b)
  - [メモ](#%e3%83%a1%e3%83%a2)

# MediaPipe
## Reference
- [MediaPipe(gitHub)](https://github.com/google/mediapipe)

## 開発環境
- Windows 10 Home
- Windows Subsystem for Linux (WSL)
  - Ubuntu 16.04

## WSL手順
```sh
# コマンド
sudo apt-get update && sudo apt-get install -y --no-install-recommends build-essential git python zip adb openjdk-8-jdk
```
```sh
# 実行結果
Hit:1 http://archive.ubuntu.com/ubuntu xenial InRelease
Get:2 http://archive.ubuntu.com/ubuntu xenial-updates InRelease [109 kB]
Get:3 http://archive.ubuntu.com/ubuntu xenial-backports InRelease [107 kB]
Get:4 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 Packages [1,009 kB]
Get:5 https://download.docker.com/linux/ubuntu bionic InRelease [64.4 kB]
Get:6 https://download.docker.com/linux/ubuntu bionic/stable amd64 Packages [7,889 B]
Get:7 http://archive.ubuntu.com/ubuntu xenial-updates/main Translation-en [396 kB]
Get:8 http://archive.ubuntu.com/ubuntu xenial-updates/universe amd64 Packages [761 kB]
Get:9 http://archive.ubuntu.com/ubuntu xenial-updates/universe Translation-en [318 kB]
Get:10 http://archive.ubuntu.com/ubuntu xenial-updates/multiverse amd64 Packages [16.7 kB]
Get:11 http://archive.ubuntu.com/ubuntu xenial-backports/universe amd64 Packages [8,064 B]
～（省略）～
update-alternatives: using /usr/lib/jvm/java-8-openjdk-amd64/bin/schemagen to provide /usr/bin/schemagen (schemagen) in auto mode
update-alternatives: using /usr/lib/jvm/java-8-openjdk-amd64/bin/jps to provide /usr/bin/jps (jps) in auto mode
update-alternatives: using /usr/lib/jvm/java-8-openjdk-amd64/bin/xjc to provide /usr/bin/xjc (xjc) in auto mode
update-alternatives: using /usr/lib/jvm/java-8-openjdk-amd64/bin/rmic to provide /usr/bin/rmic (rmic) in auto mode
update-alternatives: using /usr/lib/jvm/java-8-openjdk-amd64/bin/jstatd to provide /usr/bin/jstatd (jstatd) in auto mode
update-alternatives: using /usr/lib/jvm/java-8-openjdk-amd64/bin/jdb to provide /usr/bin/jdb (jdb) in auto mode
update-alternatives: using /usr/lib/jvm/java-8-openjdk-amd64/bin/serialver to provide /usr/bin/serialver (serialver) in auto mode
update-alternatives: using /usr/lib/jvm/java-8-openjdk-amd64/bin/wsgen to provide /usr/bin/wsgen (wsgen) in auto mode
update-alternatives: using /usr/lib/jvm/java-8-openjdk-amd64/bin/jcmd to provide /usr/bin/jcmd (jcmd) in auto mode
update-alternatives: using /usr/lib/jvm/java-8-openjdk-amd64/bin/jarsigner to provide /usr/bin/jarsigner (jarsigner) in auto mode
update-alternatives: using /usr/lib/jvm/java-8-openjdk-amd64/bin/jmap to provide /usr/bin/jmap (jmap) in auto mode
Setting up openjdk-8-jdk:amd64 (8u222-b10-1ubuntu1~16.04.1) ...
update-alternatives: using /usr/lib/jvm/java-8-openjdk-amd64/bin/appletviewer to provide /usr/bin/appletviewer (appletviewer) in auto mode
update-alternatives: using /usr/lib/jvm/java-8-openjdk-amd64/bin/jconsole to provide /usr/bin/jconsole (jconsole) in auto mode
Processing triggers for libc-bin (2.23-0ubuntu11) ...
Processing triggers for systemd (229-4ubuntu21.22) ...
Processing triggers for ureadahead (0.100.0-19.1) ...
Processing triggers for ca-certificates (20170717~16.04.2) ...
Updating certificates in /etc/ssl/certs...
0 added, 0 removed; done.
Running hooks in /etc/ca-certificates/update.d...

done.
done.
```
```sh
# コマンド
curl -sLO --retry 5 --retry-max-time 10 \
https://storage.googleapis.com/bazel/0.27.0/release/bazel-0.27.0-installer-linux-x86_64.sh && \
sudo mkdir -p /usr/local/bazel/0.27.0 && \
chmod 755 bazel-0.27.0-installer-linux-x86_64.sh && \
sudo ./bazel-0.27.0-installer-linux-x86_64.sh --prefix=/usr/local/bazel/0.27.0 && \
source /usr/local/bazel/0.27.0/lib/bazel/bin/bazel-complete.bash
```
```sh
# 実行結果
Bazel installer
---------------

Bazel is bundled with software licensed under the GPLv2 with Classpath exception.
You can find the sources next to the installer on our release page:
   https://github.com/bazelbuild/bazel/releases
～（省略）～
## Build information
   - [Commit](https://github.com/bazelbuild/bazel/commit/c82eb48)

unzip not found, please install the corresponding package.
See http://bazel.build/docs/install.html for more information on
dependencies of Bazel.
```
```sh
# コマンド
/usr/local/bazel/0.27.0/lib/bazel/bin/bazel version && \
alias bazel='/usr/local/bazel/0.27.0/lib/bazel/bin/bazel'
```
```sh
# 実行結果
Extracting Bazel installation...
WARNING: --batch mode is deprecated. Please instead explicitly shut down your Bazel server using the command "bazel shutdown".
Build label: 0.27.0
Build target: bazel-out/k8-opt/bin/src/main/java/com/google/devtools/build/lib/bazel/BazelServer_deploy.jar
Build time: Mon Jun 17 13:00:46 2019 (1560776446)
Build timestamp: 1560776446
Build timestamp as int: 1560776446
```
```sh
# コマンド
sudo apt-get install libopencv-core-dev libopencv-highgui-dev \
                       libopencv-imgproc-dev libopencv-video-dev
```
```sh
# 実行結果
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following packages were automatically installed and are no longer required:
  bridge-utils containerd pigz runc ubuntu-fan
～（省力）～
Setting up libraw1394-tools (2.1.1-2) ...
Setting up libx11-doc (2:1.6.3-1ubuntu2.1) ...
Setting up libxcb-xfixes0:amd64 (1.11.1-1ubuntu1) ...
Setting up mesa-va-drivers:amd64 (18.0.5-0ubuntu0~16.04.1) ...
Setting up i965-va-driver:amd64 (1.7.0-1) ...
Setting up va-driver-all:amd64 (1.7.0-1ubuntu0.1) ...
Setting up dh-strip-nondeterminism (0.015-1) ...
Setting up debhelper (9.20160115ubuntu3) ...
Processing triggers for libc-bin (2.23-0ubuntu11) ...
```
```sh
# コマンド
sh setup_opencv.sh
```
```sh
# 実行結果
～（省略）～
INFO: Elapsed time: 4404.038s, Critical Path: 1986.42s
INFO: 2486 processes: 2 local, 2484 processwrapper-sandbox.
INFO: Build completed successfully, 2543 total actions
```

## Object Detection on Desktop
```sh
# コマンド
bazel build -c opt \
    --define MEDIAPIPE_DISABLE_GPU=1 \
    --define no_aws_support=true \
    mediapipe/examples/desktop/object_detection:object_detection_tensorflow
```

```sh
# コマンド
bazel-bin/mediapipe/examples/desktop/object_detection/object_detection_tensorflow \
  --calculator_graph_config_file=mediapipe/graphs/object_detection/object_detection_desktop_tensorflow_graph.pbtxt \
  --input_side_packets=input_video_path=mediapipe/examples/desktop/object_detection/test_video.mp4,output_video_path=mediapipe/examples/desktop/object_detection/output_test_video.mp4
```

```sh
# 実行結果
I0901 17:15:06.323043 13246 simple_run_graph_main.cc:38] Get calculator graph config contents: # MediaPipe graph that performs object detection on desktop with TensorFlow
# on CPU.
# Used in the example in
# mediapipie/examples/desktop/object_detection:object_detection_tensorflow.
～（省略）～
019-09-01 17:15:06.658800: I external/org_tensorflow/tensorflow/cc/saved_model/loader.cc:212] The specified SavedModel has no variables; no checkpoints were restored. File does not exist: mediapipe/models/object_detection_saved_model/variables/variables.index
2019-09-01 17:15:06.667998: I external/org_tensorflow/tensorflow/cc/saved_model/loader.cc:311] SavedModel load for tags { serve }; Status: success. Took 243937 microseconds.
I0901 17:15:19.379387 13246 simple_run_graph_main.cc:67] Success!
```


