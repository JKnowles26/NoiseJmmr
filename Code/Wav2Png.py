from pydub import AudioSegment
import matplotlib.pyplot as plt
import numpy as np
import wave
import sys

class Wav2Img:
    def __init__(self, filename):
        spf = AudioSegment.from_wav(filename)
        spf = spf.set_channels(1)
        spf.export(filename, format="wav")
        spf = wave.open(filename,'r')
        sig = spf.readframes(-1)
        sig = np.frombuffer(sig, dtype=int)
        sr = spf.getframerate()
        self.plot_waveform(sig)
        self.plot_spectrogram(sig, sr)

    def plot_waveform(self, sig):
        fig = plt.figure(figsize=(6, 2))
        ax = plt.axes()
        ax.set_axis_off()
        plt.plot(sig)
        plt.savefig("/tmp/waveform.png", bbox_inches='tight',
                    pad_inches=0.0, transparent=True)

    def plot_spectrogram(self, sig, sr):
        plt.figure(figsize=(6, 2))
        ax = plt.axes()
        ax.set_axis_off()
        plt.specgram(sig, Fs=sr)
        plt.savefig("/tmp/spectrogram.png", bbox_inches='tight',
                    pad_inches=0, transparent=True)
