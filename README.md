# keywords_memorizer
## keywords_memorizerとは？
pythonistaを使って、単語記憶をサポートするアプリ。

## 用意するmarkdownファイル
通常のmarkdown形式のファイルを使用。
通常のmarkdownで`code`を意味する\`で単語を括くったファイルを`markdown-files`フォルダに格納する。

## 使用法
1. pythonistaから、`markdownFlask.py`を起動する。コンソールに表示されたアドレスをwebviewで起動する
2. `markdown-files`に格納されたファイルが一覧になったindexページが開く。
3. 使用したいファイルを選択する。

## 原理
* 単語の表示・非表示はjavascriptで制御している。
