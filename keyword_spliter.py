'''このモジュールは、覚えたい単語とその意味を記述してあるテキストファイルを用いて、
    morkdownFlask.pyで使用できる形のマークダウンファイルを生成するためのモジュールです。
    テキストファイルはキーワードとその意味が、「xxxとは、yyy」の形式で記述されている必要があります。
    xxxの部分を<code>タグで囲み、markdownファイルとして出力します。
    またその逆のyyyの部分を<code>タグで囲むファイルも生成できます。'''

import re
import os
import sys

def toha_braker(file_name, keyword_separator='とは、'):
    with open(file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            # パターンの生成
            regex = re.compile(r'^- (.*)' + keyword_separator)
            if re.match(regex, line):
                # 「xxxとは」のxxx部分を<code>タグで囲む
                line = re.sub(regex, '- <code>\\1</code>', line)
                # output.mdに書き込み
                with open('output.md', 'a', encoding='utf-8') as f:
                    f.write(line)
        

if __name__ == "__main__":
    # テキストファイルのパスを引数として受け取る
    args = sys.argv
    # 引数の数をチェック
    # 引数の数が2ならば、separatorはデフォルト値とする。
    if len(args) == 2:
        file_name = args[1]
        toha_braker(file_name)
    elif len(args) == 3:
        file_name = args[1]
        separator = args[2]
        toha_braker(file_name, separator)
    else:
        #エラーメッセージの表示
        print('引数の数が不正です。')
        print('python keyword_spliter.py <file_name> [<separator>]')
        sys.exit()
