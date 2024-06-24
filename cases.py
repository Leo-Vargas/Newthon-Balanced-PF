import numpy as np
from functions import readYbus
from filePath import IEEE30BusPath, IEEE14BusPath
from Topology import Topology

def IEEE30Bus():
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


    switchData = {
    }

    caseData = {
        'Ybus': Ybus,
        'busTypes': busTypes,
        'voltages': voltages,
        'angles': angles,
        'loadsMw': loadsMw,
        'loadsMvar': loadsMvar,
        'generationMw': generationMw,
        'generationMvar': generationMvar,
        'switches': switchData
    }

    return caseData


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

    switchData = {
    }

    caseData = {
        'Ybus': Ybus,
        'busTypes': busTypes,
        'voltages': voltages,
        'angles': angles,
        'loadsMw': loadsMw,
        'loadsMvar': loadsMvar,
        'generationMw': generationMw,
        'generationMvar': generationMvar,
        'switches': switchData
    }

    return caseData


def IEEE14Bus():
    #Ybus = readYbus(IEEE14BusPath)

    Ybus = np.array([
    (6.025 - 19.447j, -4.9991 + 15.263j, 0 + 0j, 0 + 0j, -1.0259 + 4.235j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j),
    (-4.9991 + 15.263j, 9.5213 - 30.272j, -1.135 + 4.7819j, -1.686 + 5.1158j, -1.7011 + 5.1939j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j),
    (0 + 0j, -1.135 + 4.7819j, 3.121 - 9.8224j, -1.986 + 5.0688j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j),
    (0 + 0j, -1.686 + 5.1158j, -1.986 + 5.0688j, 10.513 - 38.654j, -6.841 + 21.579j, 0 + 0j, 0 + 4.8895j, 0 + 0j, 0 + 1.8555j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j),
    (-1.0259 + 4.235j, -1.7011 + 5.1939j, 0 + 0j, -6.841 + 21.579j, 9.568 - 35.534j, 0 + 4.2574j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j),
    (0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 4.2574j, 6.5799 - 17.341j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, -1.955 + 4.0941j, -1.526 + 3.176j, -3.0989 + 6.1028j, 0 + 0j),
    (0 + 0j, 0 + 0j, 0 + 0j, 0 + 4.8895j, 0 + 0j, 0 + 0j, 0 - 19.549j, 0 + 5.677j, 0 + 9.0901j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j),
    (0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 5.677j, 0 - 5.677j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j),
    (0 + 0j, 0 + 0j, 0 + 0j, 0 + 1.8555j, 0 + 0j, 0 + 0j, 0 + 9.0901j, 0 + 0j, 5.3261 - 24.093j, -3.902 + 10.365j, 0 + 0j, 0 + 0j, 0 + 0j, -1.424 + 3.0291j),
    (0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, -3.902 + 10.365j, 5.7829 - 14.768j, -1.8809 + 4.4029j, 0 + 0j, 0 + 0j, 0 + 0j),
    (0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, -1.955 + 4.0941j, 0 + 0j, 0 + 0j, 0 + 0j, -1.8809 + 4.4029j, 3.8359 - 8.497j, 0 + 0j, 0 + 0j, 0 + 0j),
    (0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, -1.526 + 3.176j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 4.015 - 5.4279j, -2.489 + 2.252j, 0 + 0j),
    (0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, -3.0989 + 6.1028j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, -2.489 + 2.252j, 6.7249 - 10.67j, -1.137 + 2.315j),
    (0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, -1.424 + 3.0291j, 0 + 0j, 0 + 0j, 0 + 0j, -1.137 + 2.315j, 2.561 - 5.344j),
])
    
    #print(np.allclose(Ybus,YbusMatPower, 0.005))


    busTypes = {
        'SLACK': np.array([1, ]),
        'PV': np.array([2, 3, 6, 8]),
        'PQ': np.array([4, 5, 7, 9, 10, 11, 12, 13, 14])
    }

    voltages = np.array([1.06, 1.045, 1.01, 1.0, 1.0, 1.07, 1.0, 1.09, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
    angles = np.zeros(voltages.shape[0], dtype=float)

    loadsMw = np.array([0.0, 21.7, 94.2, 47.2, 7.6, 11.2, 0.0, 0.0, 29.5, 9.0, 3.5, 6.1, 13.5, 14.9])
    loadsMvar = np.array([0.0, 12.7, 19.0, -3.9, 1.6, 7.5, 0.0, 0.0, 16.6, 5.8, 1.8, 1.6, 5.8, 5.0])

    generationMw = np.array([0.0, 40.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    generationMvar = np.array([0.0, 42.4, 23.4, 0.0, 0.0, 12.2, 0.0, 17.4, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

    print(f'Ybus shape:{Ybus.shape[0]},{Ybus.shape[1]}')
    print(f'voltages shape:{voltages.shape[0]}')
    print(f'angles shape: {angles.shape[0]}')


    switchData = {
    }

    caseData = {
        'Ybus': Ybus,
        'busTypes': busTypes,
        'voltages': voltages,
        'angles': angles,
        'loadsMw': loadsMw,
        'loadsMvar': loadsMvar,
        'generationMw': generationMw,
        'generationMvar': generationMvar,
        'switches': switchData
    }

    return caseData


def Class4Bus():
    Ybus = np.array([
        (21.457-21.185j, -21.457+21.185j, 0, 0),
        (-21.457+21.185j, 2328.149779016-1559.646245j, -2306.69231+1538.461538j, 0),
        (0, -2306.69231+1538.461538j, 2500.90403656-1557.50190404j, -194.211728+19.0403655j),
        (0, 0, -194.211728+19.0403655j, 194.211728-19.0403655j)
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

    generationMw = np.array([0.0, 0.0, 0.0, 0.0])
    generationMvar = np.array([0.0, 0.0, 0.0, 0.0])

    switchData = {
    }

    caseData = {
        'Ybus': Ybus,
        'busTypes': busTypes,
        'voltages': voltages,
        'angles': angles,
        'loadsMw': loadsMw,
        'loadsMvar': loadsMvar,
        'generationMw': generationMw,
        'generationMvar': generationMvar,
        'switches': switchData
    }

    return caseData


def Switch4Bus():

    Ybus = np.array([
        ((1/(0.0236+0.0233j))+0.001j, -1/(0.0236+0.0233j), 0 + 0j, 0 + 0j),
        (-1/(0.0236+0.0233j), (1/(0.0236+0.0233j)) + (1/(0.045+0.03j)) + (1/(0.0051+0.0005j)) + 0.003j, -1/(0.045+0.03j), -1/(0.0051+0.0005j)),
        (0 + 0j, -1/(0.045+0.03j), (1/(0.045+0.03j)) + 0.001j, 0 + 0j),
        (0 + 0j, -1/(0.0051+0.0005j), 0 + 0j, (1/(0.0051+0.0005j)) + 0.001j),
    ])

    busTypes = {
        'SLACK': np.array([1, ]),
        'PV': np.array([]),
        'PQ': np.array([2, 3, 4])
    }

    switchData = {
        1: np.array([0, 1]),
        2: np.array([0, 1]),
        3: np.array([1, 2]),
        4: np.array([1, 2]),
        5: np.array([1, 3]),
        6: np.array([1, 3])
    }

    gridTopology = Topology()
    gridTopology.addLine(0, 1)
    gridTopology.addLine(1, 2)
    gridTopology.addLine(1, 3)

    voltages = np.array([1.03, 1.0, 1.0, 1.0])
    angles = np.array([0.0, 0.0, 0.0, 0.0])

    loadsMw = np.array([0.0, 1.28, 0.32, 1.6])*100
    loadsMvar = np.array([0.0, 1.28, 0.16, 0.8])*100

    generationMw = np.array([0.0, 0.0, 0.0, 0.0])
    generationMvar = np.array([0.0, 0.0, 0.0, 0.0])

    caseData = {
        'Ybus': Ybus,
        'busTypes': busTypes,
        'voltages': voltages,
        'angles': angles,
        'loadsMw': loadsMw,
        'loadsMvar': loadsMvar,
        'generationMw': generationMw,
        'generationMvar': generationMvar,
        'switches': switchData,
        'gridTopology': gridTopology
    }

    return caseData

def Class5Bus():
    Ybus = np.array([
        ((1/(0.05+0.11j)) + (1/(0.05+0.11j)) + (1/(0.03+0.08j)) + 0.03j, -1/(0.05+0.11j), -1/(0.05+0.11j), 0, -1/(0.03+0.08j)),
        (-1/(0.05+0.11j), (1/(0.05+0.11j)) + (1/(0.04+0.09j)) + (1/(0.04+0.09j)) + 0.03j, -1/(0.04+0.09j), 0, -1/(0.04+0.09j)),
        (-1/(0.05+0.11j), -1/(0.04+0.09j), (1/(0.05+0.11j)) + (1/(0.04+0.09j)) + (1/(0.06+0.13j)) + 0.035j, -1/(0.06+0.13j), 0),
        (0, 0, -1/(0.06+0.13j), (1/(0.06+0.13j)) + (1/(0.04+0.09j)) + 0.025j, -1/(0.04+0.09j)),
        (-1/(0.03+0.08j), -1/(0.04+0.09j), 0, -1/(0.04+0.09j), (1/(0.03+0.08j)) + (1/(0.04+0.09j)) + (1/(0.04+0.08j)) + 0.03j)
    ])

    busTypes = {
        'SLACK': np.array([1, ]),
        'PV': np.array([]),
        'PQ': np.array([2, 3, 4, 5])
    }

    voltages = np.array([1.0, 1.0, 1.0, 1.0, 1.0])
    angles = np.array([0.0, 0.0, 0.0, 0.0, 0.0])

    loadsMw = np.array([0.0, 40.0, 25.0, 40.0, 50.0])
    loadsMvar = np.array([0.0, 20.0, 15.0, 20.0, 20.0])

    generationMw = np.array([0.0, 0.0, 0.0, 0.0, 0.0])
    generationMvar = np.array([0.0, 0.0, 0.0, 0.0, 0.0])

    caseData = {
        'Ybus': Ybus,
        'busTypes': busTypes,
        'voltages': voltages,
        'angles': angles,
        'loadsMw': loadsMw,
        'loadsMvar': loadsMvar,
        'generationMw': generationMw,
        'generationMvar': generationMvar,
    }

    return caseData

def Class5BusOpened():
    Ybus = np.array([
        ((1/(0.05+0.11j)) + (1/(0.05+0.11j)) + (1/(0.03+0.08j)) + 0.03j, -1/(0.05+0.11j), -1/(0.05+0.11j), 0, 0, -1/(0.03+0.08j), 0, 0),
        (-1/(0.05+0.11j), (1/(0.05+0.11j)) + (1/(0.04+0.09j)) + (1/(0.04+0.09j)) + 0.03j, 0, -1/(0.04+0.09j), 0, 0, 0, -1/(0.04+0.09j)),
        (-1/(0.05+0.11j), 0, (1/(0.05+0.11j)) + (1/(0.06+0.13j)) + 0.025j, 0, -1/(0.06+0.13j), 0, 0, 0),
        (0, -1/(0.04+0.09j), 0, 1/(0.04+0.09j) + 0.01j, 0, 0, 0, 0),
        (0, 0, -1/(0.06+0.13j), 0, (1/(0.06+0.13j)) + (1/(0.04+0.09j)) + 0.025j, 0, -1/(0.04+0.09j), 0),
        (-1/(0.03+0.08j), 0, 0, 0, 0, (1/(0.03+0.08j)) + 0.01j, 0, 0),
        (0, 0, 0, 0, -1/(0.04+0.09j), 0, (1/(0.04+0.09j)) + 0.01j, 0),
        (0, -1/(0.04+0.09j), 0, 0, 0, 0, 0, (1/(0.04+0.09j)) + 0.01j),
    ])

    busTypes = {
        'SLACK': np.array([1, ]),
        'PV': np.array([]),
        'PQ': np.array([2, 3, 4, 5, 6, 7, 8])
    }

    voltages = np.array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
    angles = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

    loadsMw = np.array([0.0, 40.0, 12.5, 12.5, 40.0, 50.0/3, 50.0/3, 50.0/5])
    loadsMvar = np.array([0.0, 20.0, 7.5, 7.5, 20.0, 20.0/3, 20.0/3, 20.0/3])

    generationMw = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    generationMvar = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

    caseData = {
        'Ybus': Ybus,
        'busTypes': busTypes,
        'voltages': voltages,
        'angles': angles,
        'loadsMw': loadsMw,
        'loadsMvar': loadsMvar,
        'generationMw': generationMw,
        'generationMvar': generationMvar,
    }

    return caseData