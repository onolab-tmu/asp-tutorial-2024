import soundfile as sf

data, samplerate = sf.read('q08_audio.wav')
y = data[::2]
sf.write("q09_audio.wav", y, 8000, subtype="PCM_16")