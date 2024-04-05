import numpy as np
from functions import readYbus
from filePath import IEEE30BusPath, IEEE14BusPath

def IEEE30bus():
    Ybus = readYbus(IEEE30BusPath)

    busTypes = {
    'SLACK': np.array([1, ]),
    'PV': np.array([2, 5, 8, 11, 13]),
    'PQ': np.array([3, 4, 7, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])
    }

    voltages = np.array([1.06, 1.043, 1.0, 1.06, 1.01, 1.0, 1.0, 1.01, 1.0, 1.0, 1.082, 1.0, 1.071, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
    angles = np.zeros(voltages.shape[0], dtype=float)

    loadsMw = np.array([0.0, 21.7, 2.4, 7.6, 94.2, 0.0, 22.8, 30.0, 0.0, 5.8, 0.0, 11.2, 0.0, 6.2, 8.2, 3.5, 9.0, 3.2, 9.5, 2.2, 17.5, 0.0, 3.2, 8.7, 0.0, 3.5, 0.0, 0.0, 2.4, 10.6])
    loadsMvar = np.array([0.0, 12.7, 1.2, 1.6, 19.0, 0.0, 10.9, 30.0, 0.0, 2.0, 0.0, 7.5, 0.0, 1.6, 2.5, 1.8, 5.8, 0.9, 3.4, 0.7, 11.2, 0.0, 1.6, 6.7, 0.0, 2.3, 0.0, 0.0, 0.9, 1.9])

    generationMw = np.array([0.0, 40.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    generationMvar = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -19.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -4.3, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

    #voltagesEnd = np.array([1.06, 1.043, 1.022, 1.013, 1.01, 1.012, 1.003, 1.01, 1.051, 1.044, 1.082, 1.057, 1.071, 1.042, 1.038, 1.045, 1.039, 1.028, 1.025, 1.029, 1.032, 1.033, 1.027, 1.022, 1.019, 1.001, 1.026, 1.011, 1.006, 0.995])
    #anglesEnd = np.array([0.0, -5.497, -8.004, -9.661, -14.381, -11.398, -13.158, -12.115, -14.434, -16.024, -14.434, -15.302, -15.302, -16.191, -16.278, -15.88, -16.188, -16.884, -17.052, -16.852, -16.468, -16.455, -16.662, -16.83, -16.424, -16.842, -15.912, -12.057, -17.136, -18.015])


    return [Ybus,  busTypes, voltages, angles, loadsMw, loadsMvar, generationMw, generationMvar]


def Saadat3Bus():
    Ybus = np.array([
    (20.0-50.0j, -10.0+20.0j, -10.0+30.0j),
    (-10.0+20.0j, 26.0-52.0j, -16.0+32.0j),
    (-10.0+30.0j, -16.0+32.0j, 26.0-62.0j)
    ])

    busTypes = {
    'SLACK': np.array([1, ]),
    'PV': np.array([3, ]),
    'PQ': np.array([2, ]),
    }

    voltages = np.array([1.05, 1.0, 1.04])
    angles = np.zeros(voltages.shape[0], dtype=float)

    loadsMw = np.array([0.0, 400.0, 0.0])
    loadsMvar = np.array([0.0, 250.0, 0.0])

    generationMw = np.array([0.0, 0.0, 200.0])
    generationMvar = np.array([0.0, 0.0, 0.0])

    return [Ybus, busTypes, voltages, angles, loadsMw, loadsMvar, generationMw, generationMvar]


def IEEE14Bus():
    Ybus = readYbus(IEEE14BusPath)

    busTypes = {
        'SLACK': np.array([1, ]),
        'PV': np.array([2, 3, 6, 8]),
        'PQ': np.array([4, 5, 7, 9, 10, 11, 12, 13, 14])
    }

    voltages = np.array([1.06, 1.045, 1.01, 1.0, 1.0, 1.07, 1.0, 1.09, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
    angles = np.zeros(voltages.shape[0], dtype=float)

    loadsMw = np.array([0.0, 21.7, 94.2, 47.2, 7.6, 11.2, 0.0, 0.0, 29.5, 9.0, 3.5, 6.1, 13.5, 14.9])
    loadsMVar = np.array([0.0, 12.7, 19.0, -3.9, 1.6, 7.5, 0.0, 0.0, 16.6, 5.8, 1.8, 1.6, 5.8, 5.0])

    generationMw = np.array([0.0, 40.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    generationMvar = np.array([0.0, 42.4, 23.4, 0.0, 0.0, 12.2, 0.0, 17.4, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

    return [Ybus, busTypes, voltages, angles, loadsMw, loadsMVar, generationMw, generationMvar]


def GhendyCase():
    Ybus = np.array([
        (0.0236+1j*0.0233, -0.0236-1j*0.0233, 0, 0),
        (-0.0236-1j*0.0233, 0.0239+1j*0.0235, -0.0003-1j*0.0002, 0),
        (0, -0.0003-1j*0.0002, 0.0054+1j*0.0007, -0.0051-1j*0.0005),
        (0, 0, -0.0051-1j*0.0005, 0.0051+1j*0.0005)
    ])

    busTypes = {
        'SLACK': np.array([1, ]),
        'PV': np.array([]),
        'PQ': np.array([2, 3, 4])
    }

    voltages = np.array([1.05, 1.0, 1.0, 1.0])
    angles = np.array([0.0, 0.0, 0.0, 0.0])

    loadsMw = np.array([0.0, 1.28, 0.32, 1.6])*100
    loadsMvar = np.array([0.0, 1.28, 0.16, 0.8])*100

    genereationMw = np.array([0.0, 0.0, 0.0, 0.0])
    generationMvar = np.array([0.0, 0.0, 0.0, 0.0])

    return [Ybus, busTypes, voltages, angles, loadsMw, loadsMvar, genereationMw, generationMvar]