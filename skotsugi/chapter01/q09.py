import soundfile as sf

signal, fs = sf.read('./skotsugi/chapter01/q08.wav')

down_scaled = signal[0:-1:2]

sf.write("./skotsugi/chapter01/q09.wav", down_scaled, 8000)
