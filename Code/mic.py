import pyaudio
import numpy as np
from os import listdir
import librosa
import wave
from playsound import playsound

stds = []
paths = listdir("azu")
for path in paths:
    y, sr = librosa.load('azu/' + path)
    std = np.mean(librosa.feature.chroma_stft(y=y, sr=sr, n_chroma=6))
    loc = [path, std]
    stds.append(loc)
print('done')

CHUNK = 768 
RATE = 44100 # time resolution of the recording device (Hz)

p1=pyaudio.PyAudio() # start the PyAudio class
inp_stream=p1.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
              frames_per_buffer=CHUNK)    
p2=pyaudio.PyAudio() # start the PyAudio class
out_stream=p2.open(format=pyaudio.paFloat32, channels=1, rate=RATE, output=True,
                frames_per_buffer=CHUNK)

def play(name):
    f = wave.open(name, 'rb')
    d = f.readframes(CHUNK)
    while d != '':
            out_stream.write(f)
            d = f.readframes(CHUNK)

while True:
    y = librosa.util.buf_to_float(inp_stream.read(CHUNK))
    std = np.mean(librosa.feature.chroma_stft(y=y, sr=sr, n_chroma=6))
    i = min(stds, key=lambda x:abs(x[1]-std))
    #print(i)
    playsound('azu/' + i[0])