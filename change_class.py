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
        annotation = f.read().split( )

    # 数値に変換
    annotation = [float(num) for num in annotation]
    annotation = np.array(annotation).reshape(-1,5)

    # 文字列置換
    annotation[:, 0] = np.where(annotation[:, 0] == beforechgnum, afterchgnum, annotation[:, 0])

    np.savetxt(fileName, annotation, fmt ='%.6f')

    with open(fileName, encoding="cp932") as f:
        annotation = f.read()

    # float -> int
    annotation = annotation.replace(".000000 ", " ")

    with open(fileName, mode="w", encoding="cp932") as f:
        f.write(annotation)

print("finish!")