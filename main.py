#【streamlit超入門】データ可視化・分析アプリを爆速で作成できるPythonライブラリ　いまにゅ

#pip install streamlitしておく

import streamlit as st 
#import numpy as np 
#import pandas as pd 
#from PIL import Image
import time

st.title('streamlit超入門')

st.write('Interactive Widgets')
#１　サイドバー表記
#text = st.sidebar.text_input('あなたの趣味を教えてください') #.sidebar.でサイドバー側、左に表記できる
#condition = st.sidebar.slider('あなたの今の調子は？',0, 100, 50) #最小,最大,初期値
#'あなたの趣味:', text
#'コンディション：', condition

#２　2カラムにする
#left_column, right_column = st.columns(2) #カラム数指定 yooutubeではst.beta_columns()だがst.columns()でいけるようになったみたい
#button = left_column.button('右カラムに文字を表示')
#if button: #buttonがTrueなら
#    right_column.write('ここは右カラムです')

#3 expanderの追加　クリックすると拡張
#expander1 = st.expander('問い合わせ1') #これもbeta_いらなくなった
#expander1.write('回答１')
#expander2 = st.expander('問い合わせ2')
#expander2.write('回答２')

#4 プログレスバーの表示 進捗や時間経過を表す
'START'
latest_iteration = st.empty() #空で用意
bar = st.progress(0) #int floatで選ぶ？引数は0と0.0の二つ？

for i in range(100):
    latest_iteration.text(f'Iteration・{i+1}')#上で作った箱にここで数字を入れていく
    bar.progress(i+1) #進捗バー表示
    time.sleep(0.1) #ここ0秒だと一瞬で終わるのでsleep必要

'DONE' #for文が終わったら表示される

