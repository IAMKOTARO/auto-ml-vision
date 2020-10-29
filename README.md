# auto-ml-vision
Googleが提供している、AutoMLVision APIを利用して手書き文字認識を行うコードです。

# 実行方法
1. venv、anaconda、gitなどのツールがインストールされていることを確認してください。またお使いのGCPアカウントでサービスアカウントキーも取得しておいてください。
詳しくは[こちら](https://qiita.com/IAMKOTARO/items/ef4493ef6fdaf129fb57)

2. リポジトリをクローンしてください
```
git clone https://github.com/IAMKOTARO/auto-ml-vision.git
```

3. install.shを実行してください
```
source install.sh
```

4. プログラムを実行してください
```
python detect.py [path/to/key.json]
```
