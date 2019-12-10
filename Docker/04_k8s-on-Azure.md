- Kubernetes on Azure ハッカソン@名古屋　勉強会
  - 「0-Dockerfile-for-Maven」
    - ライブラリの依存関係用のイメージ（ビルドで使うイメージ）
  - 「1-Dockerfile-Multi」
    - マルチステージBuild用（より軽量化したイメージを作るため）
      - 1は成果物用、2は動くモノのみ
      - 軽量化することで処理を早くする（高速化）
  - 「2-build-create.sh」
    - 実行の前にコンテナレジストリ作成
    - Versionのtagをかならずつける（つけないとデフォルトでlatestが勝手につく）
      - latestは最悪
  - 「k8s コンテナ・レジストリの接続情報を作成」
    - AKSを先に作成する（コマンドラインVer）
      - 「az login」でazのログイン情報を作成がコマンドの前に実行
      - コマンドだとTeraform使える
  - AKS
    - MC****の中にロードバランサーなどの実態のサービスが作られる
    - K8sをローカルで一から作るのは激ムズ（スペシャリストでないと不可）←おすすめしない
      - セキュリティ管理が大変
      - OpenShiftなどのサポートがあるものを使ってオンプレに作った方がよい
    - Virtual Node ←サーバーレスで実行可能（必要な時に起動？）
    - kubectl get node -o wide
    - AKSからACRへ接続設定が必要
      - docker-reg-credential
  - k8s
    - Pod
      - 依存関係を一つにまとめてリソースやライブラリを共有（ネットワーク通信しなくても済むように）
      - 自動修復機能などはなし（コンテナちょい拡張ぐらい）
    - Deployment
      - 自動修復、ローリングなどの機能あり
      - containers
        - 今回作ったイメージ
      - resources
        - PodのCPUへのリソース割り当て
        - かならず指定が必要（1000m = 1Core）→割り当て内と危険（他も殺す可能性あり）
      - kubectl apply -f 4-create-deployment-svc.yaml
    - Service
      - BackEndの制御
      - Deploymentの接続先や接続方法などを管理する？
      - Deploymentのlabels重要
      - 接続先を設定で瞬時に変更できる（管理しやすい）
    - Ingress
      - FrontEndの制御
      - 前準備：Helmのインストール
      - Hostの設定（IPで接続ではなく、DNS経由で接続するように設定）
        - DNSは別途設定が必要？
      - ingressのインストールが必要（namesapceにあるか重要）
  - DevOps（コンテナCI/CD）
    - コンテナイメージをACRから持ってくる設定を忘れないように
    - 対象ファイルを忘れないように
  - ※キャッシュを使うことで、毎回作り直すことはしない
  - ※開発の繰り返し（ソース修正→Tag→push）
  - 寺田さんの話
    - コンテナ注意点
      - latest
      - 小さいイメージ（容量を意識）
        - もとのVMの容量へ影響
        - キャッシュの意識（効くように）
      - ユーザのパーミッション
      - DockerHubのイメージを信じすぎない
        - セキュリティ脆弱性をチェックできるツールは使おう
    - k8s開発
      - Deploymentの利用を推奨（今は）
        - コンテナの配布
      - CPUとメモリのリソースを意識
        - 1個のpodが他に影響を与えないように
      - LabelとSelectorは重要
        - バージョンの切り替えがしやすい
      - ServiceでLoadBalancerは使用しない
        - 外部はIngress Controller経由
        - IPアドレスが増えるとコスト増
      - k8sではまったら
        - コマンドいろいろ（下記に残したコマンド）
    - k8s運用
      - すべての機能を利用する必要なし
      - 複雑な構成を作らない
        - Simple
        - バージョンアップの頻度4か月に一回→EOLは4世代前のバージョンまで（AKSの考え）
          - 1年後には作り直さないといけない（追従のため）
        - namespaceで本番、テスト、開発は分けない・・・ダメ、ゼッタイ
      - k8sはポータビリティがある？
        - ある点とない点がある
        - 各クラウドによってk8sは様々な部分で異なる。（バージョンやランタイムなど）
      - どのバージョンを利用しているか
      - 大規模k8sクラスタは構築しない
        - node = VM 上限は100
        - 影響度としてもNG
          - モノリスを作るのと同じ
        - Design for failer
        - バージョンアップは慎重に
          - 新しいk8sクラスタの構築
          - AKSの上位で振り分けしてバージョンアップ
      - ボリュームを扱う際は注意
        - できるだけしない（アプリがスケールしづらくなる）
        - データ管理はそもそもサービスとして提供されているものを使う方がよい
      - DBはマネージドサービスを利用
        - 開発をコンテナならOK、本番はNG
      - k8s上のアプリのデバッグ（Azure Dev Space）
        - リモートデバッグ
        - VSCode
      - Azure Managedなモニタリング
      - Azure DevOps
        - DevOps Project（Javaを選ぶとよい）
          - デフォルトでいろいろ設定されている
      - ※便利機能だけ便利に使う
- その他
  - Azure
    - AKS
      - コンテナ ランタイム Docker → Moby
    - リージョンで先にリリースされる機能が異なる。（AKSは東日本が先）
    - https://azure.microsoft.com/ja-jp/services/azure-bastion/
  - サービスメッシュ
  - 経営層やユーザへはビジネスの利点を伝えて、エンジニアは好きなテクノロジーを利用して課題を解決してあげる
    - 例えば、開発が早くなり、複数回リリースできる。運用コストが下がる。　など
  - AKSは自分で頑張る。OpenShiftはパートナーに任せる。
- TODO
  - AKSの構築実施（外部公開まで）
  - DevOpsを使用したCI/CD（コンテナイメージ作成→push→k8s適用）
  - MVP

- 自分のターン
  - k8s の基本的な操作（ログなどの状態の調査）
    - deployment
    - ログ
    - 修復
    - スケール
    - 復帰の確認
    - システムPod
    - など

```sh
# k8s の基本的な操作に関するコマンド
cd k8s-Azure-Container-Service-AKS--on-Azure/
cd FrontService/
ls
vi 4-create-deployment-svc.yaml
less 4-create-deployment-svc.yaml
## pod確認
kubectl get po
kubectl get po -o wide
kubectl get po -o wide -w
kubectl get po -n kube-system
## pod削除
kubectl delete po spring-front-service-7d8dc8fdc8-j4f54
## deployment確認
kubectl get deployment
## deploymentをフィルタして取得（labelなど）
kubectl get po --selector app=spring-front-service
kubectl get po --selector app=spring-front-service,version=v1
kubectl get po --selector app=spring-front-service,version=v2
## podの状況確認
kubectl describe po spring-front-service-7d8dc8fdc8-klxh2
## secret確認（接続情報）
kubectl get secret
## podでコマンド実行
kubectl exec -it spring-front-service-7d8dc8fdc8-j4f54 env
kubectl exec -it spring-front-service-7d8dc8fdc8-j4f54 /bin/sh
## deploymentのscale
kubectl scale deployment/spring-front-service --replicas=3
## namespace確認
kubectl get ns
## Service確認
kubectl get svc
## Ingress確認
kubectl get ing
## logs確認
kubectl logs [pod]
kubectl logs -n kube-system coredns-866fc6b6c8-2dmrf
## メトリクスで取得しているPodごとのメモリ確認
kubectl top po
## yamlの適用
kubectl apply -f 4-create-deployment-svc.yaml
## deploymentをじかに編集（あまりやらないのがおすすめ）
kubectl edit deployment/spring-front-service
## port-forward設定（kubectl経由でAKS podへ）
kubectl port-forward spring-front-service-6667858b55-6rrhs 8080:8080
```

