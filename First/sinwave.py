from xml.dom.expatbuilder import theDOMImplementation
import numpy as np

import matplotlib.pyplot as plot


def makeSineWave(waveLength, frequency):
    time = np.arange(0, waveLength, 0.1)

    amplitude = np.sin(time * frequency)

    plot.plot(time, amplitude)

    def showWave(wave):
        wave.title('Sine Wave')
        wave.xlabel('T')
        wave.ylabel('X')
        wave.grid(True, which='both')
        wave.axhline(y=0, color='k')

        wave.show()

    showWave(plot)

    def findMax(arr):
        tempMax
        for val in arr:
            if val > tempMax:
                tempMax = val
        return tempMax

    def findMin(arr):
        tempMin
        for val in arr:
            if val < tempMin:
                tempMin = val
        return tempMin

    print("MAXIMUM POINT: ", findMax(amplitude))
    print("MINIMUM POINT: ", findMin(amplitude))

    return plot


simpleWave = makeSineWave((np.pi * 6), (np.pi / 4))


def findMax(wave):
    print("TODO: Separate findMax fns (access to inner sinewave function")


findMax()
