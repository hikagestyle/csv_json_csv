## まえがき

単純に、csvファイルで簡単な範囲の抜き出し（抽出）をしたかった。（pythonのプログラムで）

直接にcsvファイルを「コピペ・加工・編集」をすれば、普通に目的は達成できる。

jsonファイルだと、範囲の抜き出しが簡単そうなpyプログラムだったので、csvも簡単だろうと思っていたところ、5時間くらい調べたり試行錯誤したものの、希望する結果に至らず断念。（残念レベルの腕前）


## 環境

- パソコン: X230（Lenovo ThinkPad）
- OS: Linux Mint 20.3（Xfce）
- Python 3.8.10（python3 --version）


## jsonファイルで範囲抽出のpyファイル（簡単そうに見えた）

test_.py

```
import json

with open('output.json', 'r') as f:
    data = json.load(f)

with open('data.json', 'w') as f:
    json.dump(data[10:25], f, indent=2, ensure_ascii=False)
```

結果、dummy.csv を test_to_json.py で、範囲抽出用のjsonファイル（output.json）を書き出し。

output.json を test_.py で data.json の書き出し。（抽出の範囲は test_.py で決める。※test_to_json.py で 設定を決めることも可能）

- data[10:25]
- data[5:16]
- data

jsonファイル（data.json）を test_to_csv.py で dummy-data.csv に書き出しするという、遠回りの作戦で目標は達成。


## pythonプログラムを実行

- python3 test_to_json.py
- python3 test_.py
- python3 test_to_csv.py


## ターミナルにコピペ

python3 test_to_json.py && python3 test_.py && python3 test_to_csv.py


## 生成されるファイル

- data.json
- dummy-data.csv
- output.json


## あとがき

普通にcsvファイルを編集するはずなので、どの場面で役に立つのか謎。


## 補足

dummy.csv は 個人情報テストデータジェネレーターを編集済み。

[個人情報テストデータジェネレーター](https://testdata.userlocal.jp/)

