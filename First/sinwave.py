import numpy as np

import matplotlib.pyplot as plot


def makeSineWave(waveLength, frequency):
    time = np.arange(0, waveLength, 0.1)

    amplitude = np.sin(time * frequency)

    plot.plot(time, amplitude)

    def showWave(wave):
        wave.title('Sine Wave')
        wave.xlabel('Time')
        wave.ylabel('X')
        wave.grid(True, which='both')
        wave.axhline(y=0, color='k')

        wave.show()

    showWave(plot)

    return plot


simpleSineWave = makeSineWave((np.pi * 6), (np.pi / 4))


def findMax(wave):
    # wave.

    print("TODO")


findMax()
