import numpy as np
import os

###############################################################

# 数値設定
beforechgnum = 1  # 変えたいクラスID
afterchgnum = 80  # 変更後のクラスID

# ディレクトリ設定
directory = "/content/a/"

################################################################



for file in os.listdir(directory):
    base, ext = os.path.splitext(file)
    # txtファイルだけ抽出
    if ext == '.txt':
        fileName = directory + file 

    # ファイルオープン
    with open(fileName, encoding="cp932") as f:
        data_lines = f.read().split( )

    # 数値に変換
    data_lines = [float(num) for num in data_lines]
    data_lines = np.array(data_lines).reshape(-1,5)

    # 文字列置換
    data_lines[:, 0] = np.where(data_lines[:, 0] == beforechgnum, afterchgnum, data_lines[:, 0])

    np.savetxt(fileName, data_lines, fmt ='%.6f')

    with open(fileName, encoding="cp932") as f:
        data_lines = f.read()

    data_lines = data_lines.replace(".000000 ", " ")

    with open(fileName, mode="w", encoding="cp932") as f:
        f.write(data_lines)

print("finish!")