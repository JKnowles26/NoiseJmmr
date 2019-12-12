import librosa
import acoustid
import matplotlib.pyplot as plt
from os import listdir
from fuzzywuzzy import fuzz

class AudioAnalysis:
    def __init__(self):
        print()

    def assignMfcc(self, y, sr):
        mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=1)
        print(mfcc)
        #return mfcc

    def crossSim(path1, path2):
        i = 0
        maxSim = 0
        maxIndex = 0
        fPrints1 = []
        fPrints2 = []
        indexMaps = []

        for file in listdir(path1):
            fpEncode = acoustid.fingerprint_file(file)
            fPrints1.append(fpEncode)
        for file in listdir(path2):
            fpEncode = acoustid.fingerprint_file(file)
            fPrints2.append(fpEncode)
        for i in fPrints2:
            for n in fPrints1:
                similarity = fuzz.ratio(fPrints2[i], fPrints2[n])
                if similarity > maxSim:
                    maxIndex = n
            indexMaps.append(maxIndex)
        print(indexMaps)

    def imageDiffs(path1, path2):
        maxDifs = 0
        dif = 0
        maxIndex = 0
        specs1 = []
        specs2 = []
        indexMaps = []

        for file in listdir(path1):
            spec = plt.figure(file)
            specs1.append(spec)
        for file in listdir(path2):
            spec = plt.figure(file)
            specs2.append(spec)
        for i in specs1:
            for n in specs2:
                dif = specs1[i] - specs2[n]
                if dif < maxDifs:
                    maxIndex = n
            indexMaps.append(maxIndex)
        print(indexMaps)
path1 = "Fifep3/"
path2 = "party3/"

AudioAnalysis.imageDiffs(path1, path2)

