import streamlit as st
import time
# デプロイしたい場合は「requirements.txt」に使用した外部ライブラリを
# 記載する(バージョンも記載要)
# ターミナルに「pip freeze」でバージョン確認できる。
# 今回「time」はpythonに元々入っているライブラリの為、requirements.txtに記載は不要
# pandasやnumpyを使用したらバージョンも含め、requirements.txtに記載する


st.title("Udemyで勉強してまーーす")

st.write("プログレスバーの表示")
"Start!!"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration{i+1}")
    bar.progress(i+1)
    time.sleep(0.1)



left_column, right_column = st.beta_columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ここは右カラム")

expander1 = st.beta_expander("問い合わせ1")
expander1.write("問い合わせ内容を書く")

expander2 = st.beta_expander("問い合わせ2")
expander2.write("問い合わせ内容を書く")

expander2 = st.beta_expander("問い合わせ3")
expander2.write("問い合わせ内容を書く")



# text = st.text_input("あなたの趣味を教えてください。")
# condition = st.slider("あなたの今の調子は？", 0, 100, 50)

# "あなたの趣味:", text
# "コンディション:", condition


# option = st.selectbox(
#     "あなたが好きな数字を教えてください。",
#     list(range(1,11))
# )

# "あなたの好きな数字は", option, "です。"

# if st.checkbox("Show Image"):
#     img = Image.open("C:/Users/softt/OneDrive/画像/kw_illust.jpg")
#     st.image(img,caption="audrey",use_column_width=True)

# df = pd.DataFrame(
#     np.random.rand(100,2)/[50,50] + [35.01411539196339, 135.74826856730232],
#     columns=["lat","lon"]
# )

# dt = np.random.normal(1,10,100)
# dt_re = dt.reshape(50,2)

# df = pd.DataFrame(
#     dt_re/[500,500] + [35.01411539196339, 135.74826856730232],
#     columns=["lat","lon"]
# )

# st.map(df)

# st.line_chart(df,use_container_width=True)
# st.area_chart(df)
# st.bar_chart(df)

# write()でも書けるが、横幅縦幅を調整できない
# st.write(df)

# dataframe()でかけば横幅、縦幅を調整できる。(動的)
# st.dataframe(df.style.highlight_max(axis=0),width=1000,height=1000)

# table()であれば静的な表が書ける
# st.table(df.style.highlight_max(axis=0))

# shift+@でバッククォーテーション(`)
# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import pandas as pd
# import numpy as np
# ```


# """

