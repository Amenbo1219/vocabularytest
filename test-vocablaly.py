from os import stat_result
import pandas as pd
import sys
from random import randint
args = sys.argv
from gtts import gTTS
import os
#files = "./1.xlsx"
files = "./newword/"+args[1]+".xlsx"
start = int(input("最初の番号を入力してください。"))
end = int(input("最後の番号を入力してください。"))
jpn = []
eng = []
num = 0
df = pd.read_excel(files)
for key in df.values: 
    #print(key)
    if start <= num < end:
        eng.append(key[0])
        jpn.append(key[1])
    else:
        None
    num+=1

for i,n in enumerate(eng):
    print(f"{n}の意味を答えろ！")
    key1 = input("音声出力させたい場合は'y'を入力してください")
    if key1=='y':
        while(True):
            text = gTTS(text=n,lang='en')
            file = './newword/temp/temp.mp3'
            text.save(file)
            os.system("afplay "+file)
            key1 = input("もう一度再生させますか?y|n:")
            if key1 == 'n':
                os.remove(file)
                break
    print(jpn[i])