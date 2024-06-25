**注意: 「実装せよ」など特に明記されている場合を除いて，適当なライブラリを使用して構いません．**
推奨ライブラリは下記の通りです．また，下記ライブラリの使用を前提とした問題も一部出題されます．

- 行列・ベクトル計算: [numpy](https://numpy.org)
- 可視化: [matplotlib](https://matplotlib.org)
- 音声ファイル操作: [soundfile](https://pysoundfile.readthedocs.io/en/latest/)

# 第 1 章: 基礎

1. **正弦波の生成**: 振幅 1, 周波数 440 Hz の正弦波をサンプリング周波数 16000 Hz で 3 秒分作成しプロットせよ．
2. **WAV ファイルの作成（モノラル）**: 1.で作成した正弦波を 16bit PCM フォーマットで wav ファイルとして保存せよ．
3. **WAV ファイルの作成（ステレオ）**: 振幅 1, 周波数 660 Hz の正弦波をサンプリング周波数 16000 Hz で 3 秒分作成し，1.で作成した信号と合わせて 2ch の wav ファイルとして保存せよ．
4. **白色雑音の生成**: ホワイトノイズをサンプリング周波数 16000 Hz で 3 秒分作成しプロットせよ．
5. **信号の混合**: 1.で作成した正弦波と 4.で作成したホワイトノイズと正弦波を混合してプロットせよ．
6. **SN 比**: 信号長の等しい 2 個の信号 $s\lbrack n \rbrack, x \lbrack n \rbrack\; (n = 0, \dots, N-1), $ の信号対雑音比 (SN比) $10 \log \frac{\sum _ {n=0} ^{N-1} s\lbrack n \rbrack ^2}{\sum _ {n=0} ^{N-1} x \lbrack n \rbrack ^2}$ を計算する関数を実装せよ．
7. **SN 比を指定した信号の混合（実装）**: SN 比を任意の値に設定できるようにホワイトノイズの振幅を調整する関数を実装せよ．元信号と所望の SN 比を入力として受け取り，ホワイトノイズを重畳した信号を出力すること．
8. **SN 比を指定した信号の混合（確認）**: 8.で実装した関数を用いて，6.と同様にホワイトノイズと正弦波の混合信号を作成し wav ファイルとして保存せよ．ただし，SN 比が 6dB となるようにすること．
9. **間引きによるダウンサンプリング**: 8.で保存した wav ファイルを読み込み，サンプリング周波数を 8kHz に変換して保存せよ．
10. **簡単なフィルタ処理**: 9.の信号に対して 5 点移動平均フィルタを適用した結果と元の信号をプロットせよ．

# 第 2 章: スペクトル解析

1. **DFT/IDFT の実装**: $N$ 点の信号 $x \lbrack n \rbrack \; (n = 0, \dots , N-1)$ の離散フーリエ変換 (DFT) $X \lbrack k \rbrack = \sum _ {n=0} ^{N-1} x \lbrack n \rbrack \exp \left( -j \frac{2\pi k n}{N} \right) \; (k = 0, \dots, N-1)$ とその逆変換 (IDFT) $x \lbrack n \rbrack = \frac{1}{N} \sum _ {k=0} ^{N-1} X \lbrack k \rbrack \exp \left( j \frac{2\pi k n}{N} \right) \, (n = 0, \dots, N-1)$ を計算する関数を実装せよ．
2. **DFT の確認**: 1.で実装した関数を用いて 8 点の単位インパルス信号 $\delta \lbrack n \rbrack = \lbrack 1, 0, 0, 0, 0, 0, 0, 0 \rbrack$ の DFT を計算せよ．
3. **IDFT の確認**: 2.の結果の IDFT を計算しプロットせよ．
4. **スペクトルの確認**: 2.の結果の振幅スペクトルおよび位相スペクトル $\lvert X\lbrack k\rbrack \rvert, \angle X\lbrack k\rbrack \; (k = 0, \dots, N-1)$ をプロットせよ．
5. **既存の実装との比較**: 8 点の単位インパルス信号の DFT を `numpy.fft.fft` 関数を用いて計算し，2.の結果と比較せよ．なお，これ以降 DFT を計算する場合は `numpy.fft.fft`関数を使用してよい．
6. **正弦波のスペクトル**: 第 1 章 1.で作成した信号の DFT を計算し，振幅スペクトルと位相スペクトルをプロットせよ．（プロットする際はデシベル表記にするために `20 * log10(np.abs(X))` などのようにしてデシベル表記になおしてから計算すると見やすいです．）
7. **窓関数**: 次式で定義される $N$点の Hamming 窓を作成する関数を実装せよ． $w\lbrack n\rbrack = 0.54 - 0.46 \cos (2\pi \frac{n}{N - 1}) \; (n = 0, \dots, N-1)$
8. **窓関数の確認**: 第 1 章 1.で作成した信号に対して 6.の窓関数を適用した信号をプロットせよ．
9. **窓関数の特性**: 第 1 章 1.で作成した信号と同じ長さの Hamming 窓を作成し，DFT を計算せよ．
10. **窓関数とスペクトルの関係**: 第 1 章 1.で作成した信号の DFT を $X\lbrack k\rbrack\; (k = 0, \dots, N-1)$，9.の結果を $Y\lbrack k\rbrack\; (k = 0, \dots, N-1)$ とする． $X\lbrack k\rbrack$ と $Y\lbrack k\rbrack$ の巡回畳み込み $Z\lbrack k\rbrack = \sum _ {n=0} ^{N-1} X\lbrack n\rbrack Y\lbrack k-n\rbrack\; (k = 0, \dots, N-1)$ の IDFT を計算し 8.の結果と比較せよ．

# 第 3 章: 畳み込みと簡単なフィルタ処理

1. **線形畳み込み**: $N$ 点の信号 $x\lbrack n\rbrack, h\lbrack n\rbrack\; (n = 0, \dots, N-1)$ の線形畳み込み $z\lbrack n\rbrack = \sum _ {k = 0} ^{N-1} x\lbrack k\rbrack h\lbrack n - k\rbrack\; (n = 0, \dots, 2N - 2)$ を計算する関数を実装せよ．ただし， $n - k \lt 0$ または $n - k \gt N-1$ では信号の値は 0 とすること．
2. **巡回畳み込み**: $N$ 点の信号 $x\lbrack n\rbrack, h\lbrack n\rbrack\; (n = 0, \dots, N-1)$ の巡回畳み込み $z\lbrack n\rbrack = \sum _ {k = 0} ^{N-1} x\lbrack k\rbrack h\lbrack (n - k) \mod N\rbrack\; (n = 0, \dots, N-1)$ を計算する関数を実装せよ．ただし， $a \mod b$ は $a$ を $b$ で割った余りを表す．
3. **零詰め＋巡回畳み込み**: $N$ 点の信号 $x\lbrack n\rbrack, y\lbrack n\rbrack$ に適切な零詰めを行って巡回畳み込みを計算することで，線形畳み込みと同じ結果を与える関数を実装せよ．
4. **各種畳み込みの関係**: 1., 2., 3. で実装した関数を用いて $x\lbrack n\rbrack = \lbrack 4, 3, 2, 1\rbrack$ と $y\lbrack n\rbrack = \lbrack 1, 0, -1, 0\rbrack$ の線形畳み込み，巡回畳み込み，零詰めを行った巡回畳み込みを計算し結果をプロットせよ．
5. **差分方程式（再帰なし）**: 次の差分方程式 $y\lbrack n\rbrack = 0.2 x\lbrack n\rbrack + 0.2 x\lbrack n-1\rbrack + 0.2 x\lbrack n-2\rbrack + 0.2 x\lbrack n-3\rbrack + 0.2 x\lbrack n-4\rbrack$ で表される信号 $y\lbrack n\rbrack$ をプロットせよ． ただし， $x\lbrack n\rbrack$ は単位インパルス信号として 10 点プロットせよ．
6. **差分方程式（再帰あり）**: 次の差分方程式 $y\lbrack n\rbrack = 0.3 y\lbrack n-1\rbrack + 0.4 x\lbrack n\rbrack$ で表される信号 $y\lbrack n\rbrack$ をプロットせよ． ただし， $x\lbrack n\rbrack$ は単位インパルス信号として 10 点プロットせよ．
7. **差分方程式（一般系）**: 一般の差分方程式 $a _ 0 y\lbrack n\rbrack = - \sum _ {k = 1} ^{N} a _ {k} y\lbrack n-k\rbrack + \sum _ {k = 0} ^{M} b _ {k} x\lbrack n - k\rbrack$ で表される信号を計算する関数を実装せよ．ただし，入力は $a _ {0}, \dots, a _ {N}\; (a _ {0} \neq 0)$ の配列， $b _ {0}, \dots, b _ {M}$ の配列，および入力信号 $x\lbrack n\rbrack\; (n = 0, \dots, N - 1)$ とすること．
8. **周波数応答**: 次の差分方程式 $y\lbrack n\rbrack = - \sum _ {k = 1} ^{N} a _ {k} y\lbrack n-k\rbrack + \sum _ {k = 0} ^{M} b _ {k} x\lbrack n - k\rbrack$ で表される信号の周波数応答 $H(e^{j\omega}) = \frac{\sum _ {k=0} ^M b _ {k} e^{-j\omega k}}{1 + \sum _ {k=1} ^{N} a _ {k} e^{-j\omega k}}$ を計算する関数を実装せよ．ただし， $\omega$ はサンプリング周波数を $f _ \mathrm{s}$ としたときの正規化各周波数 $\omega = \frac{2 \pi f}{f _ \mathrm{s}}\; (0 \leq f \lt f _ \mathrm{s})$ である．
9. **周波数応答の確認（再帰なし）**: 8.で実装した関数を用いて，5.の信号の周波数応答 $H(e^{j\omega})$ を計算し，振幅特性 $\lvert H(e^{j\omega})\rvert$ および位相特性 $\angle H(e^{j\omega})$ をプロットせよ．ただし，サンプリング周波数 $f _ \mathrm{s} = 16000$ とし，$f = 0, \frac{1}{N} f _ \mathrm{s}, \dots, \frac{N-1}{N} f _ \mathrm{s}$ まで計算せよ（$N$ は適当に決めてよい）．
10. **周波数応答の確認（再帰あり）**: 8.で実装した関数を用いて，6.の信号の周波数応答 $H(e^{j\omega})$ を計算し，振幅特性 $\lvert H(e^{j\omega})\rvert$ および位相特性 $\angle H(e^{j\omega})$ をプロットせよ．ただし，サンプリング周波数 $f _ \mathrm{s} = 16000$ とし，$f = 0, \frac{1}{N} f _ \mathrm{s}, \dots, \frac{N-1}{N} f _ \mathrm{s}$ まで計算せよ（$N$ は適当に決めてよい）．

# 第 4 章: 短時間フーリエ変換

1. **零詰め**: 窓幅 $L$ ，シフト幅 $S\; (\lt L)$，および $N$ 点の実数値信号 $x\lbrack n\rbrack\; (n = 0, \dots, N-1)$ を入力とし，下記の手順で零詰めした信号を出力する関数を実装せよ．
   1. 入力の先頭に $L - S$ 個の零詰め: $\lbrack \underbrace{0, \dots, 0} _ {L - S}, x\lbrack 0\rbrack, \dots, x\lbrack N-1\rbrack$
   2. 最終的な信号の長さが $S$ の倍数となるような数を計算 $K \gets \left(N + (L - S)\right) \mod S$
   3. 入力の末尾に $K$ 個の零詰め: $\lbrack \underbrace{0, \dots, 0} _ {L - S}, x\lbrack 0\rbrack, \dots, x\lbrack N-1\rbrack, \underbrace{0, \dots, 0} _ {K}\rbrack$
2. **フレーム分割**: 窓幅 $L$ ，シフト幅 $S\; (\lt L)$，および $N$ 点の実数値信号 $x\lbrack n\rbrack\; (n = 0, \dots, N-1)$ を入力とし，1.で実装した関数を用いて $L$ 点の信号（以下，フレームと呼ぶ）の列を出力する関数を実装せよ．
   1. $t\; (t = 0, \dots, T-1)$ 番目のフレームを次で求める: $x _ {t} \lbrack l\rbrack \coloneqq \tilde{x}\lbrack tS+l\rbrack\; (l = 0, \dots, L-1)$, ただし， $\tilde{x}\lbrack n\rbrack$ は零詰め後の入力
3. **STFT の実装**: 窓幅 $L$ ，シフト幅 $S\; (\lt L)$，窓関数 $w\lbrack l\rbrack\; (l = 0, \dots, L-1)$ ，および $N$ 点の実数値信号 $x\lbrack n\rbrack\; (n = 0, \dots, N-1)$ を入力とし，下記の手順で $x\lbrack n\rbrack$ の短時間フーリエ変換を出力する関数を実装せよ．このとき，出力は $(\frac{L}{2}+1) \times T$ の複素数行列となることに注意せよ．
   1. 2.で実装した関数を用いて，各フレームに対して窓関数 $w\lbrack l\rbrack\; (l = 0, \dots, L-1)$ をかけ `np.fft.rfft` 関数を適用する．
4. **STFT の確認**: 振幅 1, 周波数 440 Hz の正弦波をサンプリング周波数 16000 Hz で 0.1 秒分作成し，2.で実装した関数を用いてスペクトログラムを計算せよ．ただし，窓幅を 1000，窓関数を Hamming 窓，シフト幅を 500 とすること．さらに，振幅スペクトログラム・位相スペクトログラムをプロットせよ．プロットには `matplotlib.pyplot.pcolormesh` を使用すること．
5. **合成窓**: シフト幅 $S$ と $L$ 点の窓関数 $w\lbrack l\rbrack\; (l = 0, \dots, L-1)$ を入力とし，次の結果を出力する関数を実装せよ．なお，これは逆短時間フーリエ変換に用いる最適合成窓のひとつである．
   1. $Q \gets \frac{L}{S}$
   2. $w _ \mathrm{s}\lbrack l\rbrack = \frac{w\lbrack l\rbrack}{\sum _ {m = -(Q - 1)} ^{Q - 1} (w\lbrack l - m S\rbrack) ^ 2}$
6. **ISTFT の実装**: 合成窓 $w _ {\mathrm{s}}(l = 0, \dots, L - 1)$， と $F\times T$ の複素数行列 $X\lbrack f, t\rbrack\; (f = 0, \dots, F-1,\quad t = 0, \dots, T-1)$ を入力とし，下記の手順で $M$ 点の信号 $\hat{x}\lbrack n\rbrack$ を出力する関数を実装せよ．
   1. 窓幅 $N$ を計算および出力信号の長さ $M$ を計算: $N \gets 2 (F - 1)$, $M \gets S (T - 1) + N$
   2. 出力信号を初期化: $\hat{x}\lbrack m\rbrack = 0 \; (m = 0, \dots, M - 1)$
   3. 各フレーム $t$ について逆 DFT を計算: $z _ {t}\lbrack n\rbrack \gets \mathcal{F}^{-1}(X\lbrack 0, t\rbrack, \dots, X\lbrack F-1, t\rbrack)\lbrack n\rbrack\; (n = 0, \dots, N-1)$
      ただし，右辺は $F$ 点の複素数値信号 $X\lbrack 0, t\rbrack, \dots, X\lbrack F-1, t\rbrack$ を逆 DFT した結果の $n$ 番目の要素を表す．逆 DFT には `np.fft.irfft` 関数を使用すること．これにより， $z\lbrack n\rbrack$ の点数は $N = 2(F-1)$ となることに注意せよ．
   4. Overlap add の計算: $\hat{x}\lbrack t S + n\rbrack = \hat{x}\lbrack t S + n\rbrack + w _ {\mathrm{s}}\lbrack n\rbrack z_t\lbrack n\rbrack$
      ただし， $w _ {\mathrm{s}}\lbrack n\rbrack$ は 5.で計算される最適合成窓， $z _ {t}\lbrack n\rbrack$は上で計算した逆 DFT である．
7. **ISTFT の確認**: 6.で実装した関数を用いて，4.の結果の逆短時間フーリエ変換を計算し結果をプロットせよ．
8. **合成窓の確認**: 6.の実装において，合成窓をすべての $n$ に対して $w _ {\mathrm{s}}\lbrack n\rbrack = 1$ とした場合の ISTFT を実装し，前問の結果と比較せよ．
9. **不確定性原理の確認**: 周波数 100 ~ 16000 Hz のチャープ信号をサンプリング周波数 16000 Hz で 1 秒分作成し，窓幅/シフト幅を 100/50, 200/100, 400/200, 800/400 と変えながらスペクトログラムをプロットし結果を比較せよ．なお，チャープ信号の作成には `scipy.signal.chirp` 関数を使用せよ．
10. **時間周波数のインデクスと物理量との対応**: スペクトログラム，サンプリング周波数，シフト幅を入力とし，3.の実装で得られるスペクトログラムの縦軸と横軸の単位をそれぞれ周波数と秒に変換する関数を実装せよ．これを用いて，4.の結果を再度プロットして確認せよ．

# 第 5 章: アレイ信号処理基礎

1. **アレイマニフォールドベクトル（直線状アレイ）**: アレイ間隔 $d$ (m)，マイク数 $M$ ，音源方向 $\theta$，周波数 $f$ (Hz) を入力とし，2 次元平面における直線状等間隔アレイのアレイマニフォールドベクトル $\boldsymbol{a}$ を計算する関数を実装せよ．ただし， $c$ は音速を表し，本演習では $c = 334$ (m/s)とする．また， $\theta$ は $y$ 軸から反時計回りを正の向きにとるものとする．アレイマニフォールドベクトルの $m\; (m=1,\dots,M)$ 番目の要素 $a _ {m}$ は音源方向ベクトル $\boldsymbol{u}$ および$m$ 番目のマイクにおける位置ベクトル $\boldsymbol{p}_ {m}$ を用いて次式で計算される．これを用いて， $d = 0.05$ (m)，$M = 3, \theta = 45 ^{\circ}$, $f = 1000$ (Hz) の場合の結果を print 文で確認せよ．
   $
   \begin{align*}
       a _ {m} &= \exp \left( j \frac{2\pi f}{c} \boldsymbol{u} ^{\top} \boldsymbol{p} _ {m} \right) \newline
       \boldsymbol{u} &= \begin{bmatrix} \sin \theta & \cos \theta & 0 \end{bmatrix} ^{\top} \newline
       \boldsymbol{p} _ {m} &= \begin{bmatrix} \left( (m - 1) - \frac{M-1}{2} \right) d & 0 & 0 \end{bmatrix} ^{\top}
   \end{align*}
   $
2. **アレイマニフォールドベクトル（円状アレイ）**: 1.と同様に，アレイ半径 $r$ (m)，マイク数 $M$ ，音源方向 $\theta$，周波数 $f$ (Hz) を入力とし，2 次元平面における円状等間隔アレイのアレイマニフォールドベクトル $\boldsymbol{a}$ を計算する関数を実装せよ．これを用いて， $r = 0.05$ (m)，$M = 3, \theta = 45 ^{\circ}$, $f = 1000$ (Hz) の場合の結果を print 文で確認せよ．
   $$\boldsymbol{p} _ {m} = \begin{bmatrix} r \sin (\frac{2\pi}{M}(m-1)) & r \cos (\frac{2\pi}{M}(m-1)) & 0 \end{bmatrix} ^{\top}$$
3. **アレイマニフォールドベクトル（一般）**: アレイの座標 $\lbrack x _ {1}, y _ {1}, 0\rbrack, \dots, \lbrack x _ {M}, y _ {M}, 0\rbrack$ (m) ，音源方向 $\theta$，周波数 $f$ (Hz) を入力とし，2 次元平面における一般のマイクアレイのアレイマニフォールドベクトルを計算する関数を実装せよ．これを用いて，1.および 2.と同様の結果となるようなパラメータを与えて結果を print 文で確認せよ．
4. **空間相関行列の計算**: $M$ 個の $F\times T$ の複素数行列 $X _ {m}\lbrack f, t\rbrack\; (f = 0, \dots, F-1,\quad t = 0, \dots, T-1) \; (m = 1,\dots, M)$ を入力とし，下記の手順で空間相関行列を計算する関数を実装せよ．出力は $F$ 個の $M\times M$ 複素数行列となることに注意すること．これを用いて， $X _ {1} = \lbrack \lbrack 1, -1j, -1, 1j\rbrack, \lbrack 2, -2j, -2, 2j\rbrack, \lbrack 3, -3j, -3, 3j\rbrack\rbrack$, $X _ {2} = \lbrack \lbrack 4, -2j, 1, 0\rbrack, \lbrack 2, -1j, 0, 0\rbrack, \lbrack 1, -j, 1, 0\rbrack\rbrack$ として結果を print 文で確認せよ．
   1. $\boldsymbol{x} _ {ft} \coloneqq \begin{bmatrix} X _ {1}\lbrack f, t \rbrack & \dots & X _ {M}\lbrack f, t \rbrack \end{bmatrix} ^{\top}$
   2. $\boldsymbol{R} _ {f} \gets \frac{1}{T} \sum _ {t = 0} ^{T-1} \boldsymbol{x} _ {ft} \boldsymbol{x} _ {ft} ^{\mathsf{H}} \; (f = 0, \dots, F-1)$ （$\boldsymbol{x}^\mathsf{H}$ は複素数ベクトル $\boldsymbol{x}$ の Hermite 転置を表す）
5. **空間相関行列の確認**: サンプリング周波数 16000 (Hz)，長さ 5 (s) のホワイトノイズを 2 チャネル作成し，窓幅 512・シフト幅 256・Hann 窓で STFT した信号に対して，4.で実装した関数を用いて空間相関行列を計算せよ．結果を $\boldsymbol{R} _ {f} \; (f = 0, \dots, 513)$ とするとき， $\boldsymbol{R} _ {100}$ の実部を print 分で確認せよ．
6. **簡単な多チャネル観測シミュレーション**: サンプリング周波数 16000 (Hz)，長さ 1 (s) で振幅 1・周波数 440 (Hz)の正弦波 $s\lbrack n \rbrack$ と， $s\lbrack n \rbrack$ に対して SN 比 10dB になるよう振幅を調整したホワイトノイズ $\varepsilon\lbrack n \rbrack$ を作成せよ．さらに，$x _ {1}\lbrack n \rbrack = s\lbrack n \rbrack + \varepsilon\lbrack n \rbrack, x _ {2}\lbrack n \rbrack = s\lbrack n-10\rbrack + \varepsilon\lbrack n \rbrack, x _ {3}\lbrack n \rbrack = s\lbrack n-20 \rbrack + \varepsilon\lbrack n \rbrack$ として 3 チャネルの信号を作成し結果をプロットせよ．プロットの範囲は `[0, 0.01]` (s) など適当に拡大せよ．
7. **遅延和ビームフォーマ**: 次の手順で 6.の信号を強調した結果をプロットせよ．
   1. 6.の信号をチャネルごとに窓幅 1024・シフト幅 512・Hann 窓で STFT した結果を $X _ {1}\lbrack f,t \rbrack, X _ {2}\lbrack f, t \rbrack, X _ {3}\lbrack f, t \rbrack$ とする．ただし， $F$ は周波数ビンの総数， $T$ はフレーム数である．
   2. $\boldsymbol{x} _ {ft} \gets \begin{bmatrix} X _ {1}\lbrack f, t \rbrack & X _ {2}\lbrack f, t \rbrack & X _ {3}\lbrack f, t \rbrack\end{bmatrix}^{\top}$
   3. 各周波数 $f = \frac{f _ {s} / 2}{F-1} 0, \dots, \frac{f _ {s} / 2}{F-1}$ ごとにビームフォーマ $\boldsymbol{w} _ {f} = \frac{1}{3} \begin{bmatrix} \exp (-j 2\pi f \tau _1) & \exp (-j 2\pi f \tau _2) & \exp (-j 2\pi f \tau _3) & \end{bmatrix}$ を計算する．ただし， $\tau _ {1} = 0, \tau _ {2} = \frac{10}{f _ {s}}, \tau _ {3} = \frac{20}{f _ {s}}$ である．
   4. 各周波数ごとに $Y\lbrack f,t \rbrack = \boldsymbol{w} _ {f}^{\mathsf{H}} \boldsymbol{x} _ {ft}$ として強調信号を求める．
   5. $Y\lbrack f,t \rbrack$ を逆 STFT する．
8. **ビームパターン**: 周波数領域におけるビームフォーマのフィルタ $\boldsymbol{w} _ {f} \; (f = 0, \dots, F-1)$ ，マイクアレイの座標 $\boldsymbol{p} _ {m} \; (m = 1, \dots, M)$，サンプリング周波数 $f _ \mathrm{s}$ を入力とし，次の手順でビームパターンを描画する関数を実装せよ．これを用いて，1.の直線状アレイにおける遅延和ビームフォーマのビームパターンをプロットせよ．
   1. 角度 $\theta = 0, \dots, 360$ (deg) および周波数 $f = \frac{f _ \mathrm{s} / 2}{F-1} 0, \dots, \frac{f _ \mathrm{s} / 2}{F-1} F$ について 3.でアレイマニフォールドベクトル $\boldsymbol{a} _ {f}(\theta)$ を計算する．
   2. 角度 $\theta = 0, \dots, 360$ (deg) について $\Psi (f, \theta) = \boldsymbol{w} _ {f}^{\mathsf{H}} \boldsymbol{a} _ {f} (\theta)$ を計算する．
   3. 横軸を角度，縦軸を周波数として $20 \log _ {10} \lvert \Psi (f, \theta) \rvert$ をカラーバーでプロットする．
9. **空間サンプリング定理**: 空間的エイリアシングを避けるためにはマイク間隔 $d$ を $d \leq \frac{c}{2f}$ となるように選ぶ必要がある．ここで， $c$ (m/s) は音速，$f$ (Hz) は周波数である．8.で実装した関数を用いて，マイク間隔を 2 (cm), 5 (cm), 10 (cm) と変化させながら 1.で求めた直線状アレイのビームパターンをプロットし，結果を確認せよ．
10. **空間スペクトル**: $M$ チャネルの $N$ 点実数値信号 $z _ {m}\lbrack n \rbrack \; (m = 1, \dots, M)$ を入力とし，次の手順で空間スペクトルを計算する関数を実装せよ．これを用いて，マイク数 3，マイク間隔 0.05 m の直線状ビームフォーマおよび 6.で用いた信号を入力とし，周波数ビンインデクス $f=20, 21, \dots, 30$ ごとに結果を描画せよ．6.の信号は窓幅 1024・シフト幅 512・Hann 窓で STFT すること．
    1. 入力信号の STFT を $Z _ {m}\lbrack f,t \rbrack \; (f = 0, \dots, F-1,\; t = 0, \dots, T-1,\; m = 1,\dots, M)$ とする．
    2. 5.で実装した関数を用いて $Z _ {m}\lbrack f,t \rbrack$ の空間相関行列を計算し $\boldsymbol{R} _ {z}$ とする．
    3. 角度 $\theta = 0, \dots, 360$ (deg) についてビームフォーマ $\boldsymbol{w}(\theta)$ を計算する．
    4. 角度 $\theta = 0, \dots, 360$ (deg) について $P(\theta) = \boldsymbol{w} ^{\mathsf{H}} (\theta) \boldsymbol{R} _ {z} \boldsymbol{w} (\theta)$ を計算する．
    5. 横軸を角度，縦軸を $20\log _ {10} \lvert P(\theta) \rvert$ としてプロットする．

# 参考文献

## 書籍

- [浅野: 音のアレイ信号処理, コロナ社, 2011.](https://www.coronasha.co.jp/np/isbn/9784339011166/)
  - アレイ信号処理の基礎からビームフォーミング，ブラインド音源分離にいたるまで詳しく書かれています．
- [貴家: ディジタル信号処理のエッセンス, オーム社, 2014.](https://www.ohmsha.co.jp/book/9784274216060/)
  - 標準的なディジタル信号処理の教科書です．フーリエ級数展開，フーリエ変換，離散時間フーリエ変換，離散フーリエ変換の関係が非常に明確に記述されています．例題が豊富でわかりやすいです．
- [戸上: Python で学ぶ音源分離, インプレス, 2020.](https://book.impress.co.jp/books/1119101154)
  - 音源分離をメインに扱うおそらく日本初の書籍です．Majorization-minimization 法による最適化，残響除去，独立低ランク行列分析など日本語の書籍ではこの本でしか見られない題材が豊富に含まれています．Python 実装も公開されていて，projection back など実装上気をつけなければいけない点も詳しく記述されています．[pyroomacoustics](https://github.com/LCAV/pyroomacoustics)を使ったシミュレーションも少し書かれています．
- [阿部, 八巻, 川又: Python 対応 ディジタル信号処理, 森北出版, 2021.](https://www.morikita.co.jp/books/mid/077661)
  - 例題が非常に豊富で python 実装も読みやすいです．Python はわかるがディジタル信号処理については勉強したことがないという人が最初に読むにはかなり良い本だと思います．フィルタ設計について 4 章にわたって極めて詳しく解説されています．音の信号処理に関してはあまり詳しくないので下記の書籍などが参考になります．フィルタ設計，畳み込みなどの問題の参考にしました．
- [川村: 音声音響信号処理の基礎と実践, コロナ社, 2021.](https://www.coronasha.co.jp/np/isbn/9784339014020/)
  - 音に関する信号処理について平易に解説されています．バイナリマスキング，画像の音変換など他の書籍ではあまり解説されていないものも詳しく書かれています．理論がメインという印象で実装に関しては同じ著者の[プログラム 101 付き 音声信号処理](https://shop.cqpub.co.jp/detail/2539/)が詳しいです．
- [森勢: ひたすら楽して音響信号解析, コロナ社, 2021.](https://www.coronasha.co.jp/np/isbn/9784339009392/)
  - タイトルの通り MATLAB を使ってとにかく楽に音響信号解析をするための本です．フーリエ変換，フィルタ設計の参考にしました．
- [山本, 高道: Python で学ぶ音声合成, インプレス, 2021.](https://book.impress.co.jp/books/1120101073)
  - 前述の Python で学ぶ音源分離と同じシリーズの書籍です．本書籍のために作成されたライブラリである[ttslearn](https://github.com/r9y9/ttslearn)が非常にわかりやすく python ライブラリ設計の参考になります．

## 解説記事

- [小野: 短時間フーリエ変換の基礎と応用, 日本音響学会誌, 2016.](https://doi.org/10.20697/jasj.72.12_764)
  - 短時間フーリエ変換が詳しく解説されています．
- [東京農工大学 矢田部 浩平 准教授](https://twitter.com/yatabe_)の解説記事
  6 回にわたる連載で短時間フーリエ変換が非常に詳しく解説されています．
  1. [第一回：連続信号と離散信号](https://doi.org/10.20697/jasj.77.4_262)
  1. [第二回：離散フーリエ変換](https://doi.org/10.20697/jasj.77.5_331)
  1. [第三回：短時間フーリエ変換](https://doi.org/10.20697/jasj.77.6_396)
  1. [第四回：信号の再構成と窓関数](https://doi.org/10.20697/jasj.77.7_463)
  1. [第五回：実装における諸注意](https://doi.org/10.20697/jasj.77.8_537)
  1. [第六回：時間周波数領域のスパース表現](https://doi.org/10.20697/jasj.77.9_609)

## Web サイト

- [香川高専 北村 大地 講師 ホームページ](http://d-kitamura.net/codes.html)
  - MATLAB ですが短時間フーリエ変換や様々なブラインド音源分離アルゴリズムの実装が公開されています．
- [やる夫で学ぶディジタル信号処理](http://www.ic.is.tohoku.ac.jp/~swk/lecture/yaruodsp/main.html)
  - 日本語で無料で公開されているディジタル信号処理に関する資料の中で最も網羅的かつわかりやすいです．
- [言語処理 100 本ノックを解き始める前に.md](https://gist.github.com/reiyw/9155edf600e85417e82d2e4e4bc9e637)
  - Linux コマンドや python の参考になるリンクがまとまっています．
