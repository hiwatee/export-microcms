# export-microcms

## 概要

microCMS のコンテンツを csv 形式で export します。

## 環境

python >= 3.7.3

## インストール

```
pip install -r requirements.txt
```

.env-sample を.env に変更しそれぞれのパラーメーターを埋めてください

## 起動/エクスポート

下書きを取得しない場合

```
python main.py
```

下書きも取得する場合

```
python main.py draft
```

UTF-8 で出力されますので Excel での利用時は各自で Shift-JIS に変換してください
