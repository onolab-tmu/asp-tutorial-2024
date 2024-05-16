# 間引きによるダウンサンプリング: 8.で保存した wav ファイルを読み込み，サンプリング周波数を 8kHz に変換して保存せよ．

import soundfile as sf

data, fs = sf.read("q08.wav")    # 読み込み
fs = 8000
sf.write("q09.wav", data, fs, subtype="PCM_16")    # 書き込み