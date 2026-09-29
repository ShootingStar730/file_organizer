1.概要
    指定したフォルダ内を整理するツール。

2.機能

    ・フォルダ内のファイルとファイルの拡張子の取得
    ・拡張子の種類に応じて、対応するフォルダへの格納処理
    ・

3.動作環境
4.使い方

---

① ファイル整理ツール

例：python organizer.py ./downloads

.jpg → images/
.pdf → documents/
.zip → archives/
同名ファイルへの対応
--dry-run で実際には移動しない
エラー処理

学べること

pathlib
ファイル操作
条件分岐
関数
CLI引数