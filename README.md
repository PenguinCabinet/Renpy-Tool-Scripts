# Renpy Tool Scripts
Renpy用のツールキットです。

# ダウンロード
(Download)[https://github.com/PenguinCabinet/Renpy-Tool-Scripts/archive/refs/heads/main.zip]

# 使い方

## 想定してるワークフロー
1. シナリオをプレーンテキストで執筆
2. Convert_script_to_rpyで、シナリオテキストファイルをRenpy用スクリプトに変換
3. 選択肢の部分を実装
4. ダミーデータを使用し、背景や立ち絵、BGM、SEをスクリプトに設定
5. Get_info_from_rpyで使用している素材を列挙
6. 素材を集める
7. 完成

## Convert_script_to_rpy
一般的なシナリオテキストファイルを、Renpy用スクリプトに変換するプログラムです。
```bash
python Convert_script_to_rpy.py Scenario_text.txt script.rpy
What is the label of 佐藤 >Satou
What is the label of 山田 >Yamada
```
プログラムを実行すると、人名のラベルをどうするか、対話的に聞かれます。   

Scenario_text.txtの中身    
```text
山田を見かけた。話しかけてみよう。

佐藤「こんにちは」
山田「こんにちは」
```
変換先のscript.rpy(コメント等は消去)
```rpy
define Satou = Character('佐藤', color="#000000")
define Yamada = Character('山田', color="#000000")

label start:

    "山田を見かけた。話しかけてみよう。"
    Satou "「こんにちは」"
    Yamada "「こんにちは」"

    return
```
「」の有無にて会話文か地の文であるか判定し、変換しています。   
`"`があると正しく変換できません。また`「`と`」`が一行に複数あると正しく変換されません。

## Get_info_from_rpy

Renpy用スクリプトから使用している素材ファイルを抽出し、列挙するプログラムです。
```bash
python Get_info_from_rpy.py script.rpy report.txt
```

script.rpyの中身    
```rpy
define Satou = Character('佐藤', color="#000000")
define Yamada = Character('山田', color="#000000")

image Satou smile="Satou-smile.png"
image Yamada smile="Yamada-smile.png"

label start:
    play music "bgm/room1.ogg" fadeout 1.0 fadein 1.0 loop
    play sound "SE/open_door1.ogg" volume 1.5
    scene bg-room1

    "山田を見かけた。話しかけてみよう。"
    Satou "「こんにちは」"
    Yamada "「こんにちは」"

    return
```

変換先のreport.txtの中身    
```text
キャラクター立ち絵
Satou-smile.png
Yamada-smile.png

背景画像
bg-room1

BGM
bgm/room1.ogg

SE
SE/open_door1.ogg
```

正規表現を利用して、簡易的に抽出しているため、上手くいかない場合があるかもしれません。
