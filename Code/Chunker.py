import librosa
import numpy as np

class BigChunker:
    def __init__(self, fileName):
        self.fileName = fileName
        y, sr, beats = self.getTempo()
        self.segmenter(y, sr, beats)
        self.soundSplitter(beats, 2)
        self.soundSplitter(beats, 4)

    def getTempo(self):
        y, sr = librosa.load(self.fileName + ".wav")
        tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
        tempo = round((tempo * 2)/2)
        beats = librosa.frames_to_samples(beats)
        return y, sr, beats

    def segmenter(self, y, sr, beats):
        for i in range(len(beats)- 1):
            start = beats[i]
            end = beats[i+ 1]
            clip = y[start:end]
            f = self.fileName + '-1-' + str(i) + ".wav"
            librosa.output.write_wav(f, clip, sr, norm = False)

    def soundSplitter(self, beats, div):
        numFiles = len(beats) - 1
        lastPos = int(div/2)
        x = 0

        for i in range((numFiles * lastPos)):
            y, sr = librosa.load(self.fileName + '-' + str(lastPos) + '-' + str(i) + ".wav")
            end = len(y)
            mid = int(np.ceil(end/2))

            clip = y[0:mid]
            f = self.fileName + '-' + str(div) + '-' + str(x) + ".wav"
            librosa.output.write_wav(self.fileName + '-' + str(div) + '-' + str(x) + ".wav", clip, sr, norm = False)

            clip = y[mid:end]
            f = self.fileName + '-' + str(div) + '-' + str(x + 1) + ".wav"
            librosa.output.write_wav(self.fileName + '-' + str(div) + '-' + str(x + 1) + ".wav", clip, sr, norm = False)

            x+=2

if __name__ == "__main__":
    c = BigChunker("kaoru/kaoru")