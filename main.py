import streamlit as st

import pandas as pd

import matplotlib.pyplot as plt

st.title('火星隕石のスペクトルデータの可視化')

uploaded_file = st.file_uploader("CSVファイルをアップロードしてください",type="csv")
if uploaded_file is not None:
	df = pd.read_csv(uploaded_file)
	st.write(df)

	#描画対象の選択
	options = st.multiselect(
		'表示するスペクトルを選択してください',
		df.columns[1:10], #最初の列は通常インデックスやID、残りを選択肢に
		default=df.columns[1] #デフォルトで最初の列を選択
	)

	
	if options:
		#グラフの描画
		fig, ax = plt.subplots()
		for column in options:
			ax.plot(df[df.columns[0]], df[column], label =column)
		
		ax.set_xlabel(df.columns[0])
		ax.set_ylabel('Reflectance')
		ax.legend()
		st.pyplot(fig)
	else:
		st.write('少なくとも一つの列を選択してください')
