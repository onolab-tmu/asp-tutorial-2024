import soundfile as sf

data, samplerate = sf.read('q08_audio.wav')
sf.write("q09_audio.wav", data, 8000, subtype="PCM_16")