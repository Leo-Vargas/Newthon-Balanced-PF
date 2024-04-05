import numpy as np

def JacobianCalculatorV2(Ybus: np.ndarray,  voltages: np.ndarray, angles: np.ndarray, busTypes: dict):

    fasorVoltages = voltages*np.exp(1.j*angles*np.pi/180)    

    IcDiag = np.diag(Ybus@fasorVoltages)
    complexAnglesDiag = np.diag(fasorVoltages/voltages)
    fasorVoltagesDiag = np.diag(fasorVoltages)

    
    angleDerivative = 1.j*fasorVoltagesDiag@(np.conj(IcDiag-Ybus@fasorVoltagesDiag))

    voltageDerivative = np.conj(IcDiag)@complexAnglesDiag + fasorVoltagesDiag@np.conj(Ybus@complexAnglesDiag)

    
    J11 = np.real(cutSlack(cutSlack(angleDerivative, busTypes, axis=0),
                            busTypes, axis=1))
    
    J21 = np.imag(cutSlack(cutSlackPV(angleDerivative, busTypes, axis=0),
                            busTypes, axis=1))
    
    J12 = np.real(cutSlackPV(cutSlack(voltageDerivative, busTypes, axis=0), 
                            busTypes, axis=1))

    J22 = np.imag(cutSlackPV(cutSlackPV(voltageDerivative, busTypes, axis=0), 
                            busTypes, axis=1))

    jacobian = np.concatenate((np.concatenate((J11, J21), axis=0),np.concatenate((J12, J22), axis=0)), axis=1)

#    print(f'J11 shape: {J11.shape}')
#    print(f'J21 shape: {J21.shape}')
#    print(f'J12 shape: {J12.shape}')
#    print(f'J22 shape: {J22.shape}')
#    print(f'Jacobian shape: {jacobian.shape}')
    
#    print(J11)
#    print(J12)


    return jacobian 


def calculatePQ(Ybus:np.ndarray, angles: np.ndarray, voltages: np.ndarray, busTypes: dict):

    fasorVoltages = voltages*np.exp(1.j*angles*np.pi/180)

    calculatedS = fasorVoltages*(np.conj(Ybus@fasorVoltages))


    calculatedP = np.real(cutSlack(calculatedS, busTypes))
    calculatedQ = np.imag(cutSlackPV(calculatedS, busTypes))
    #print(f'active power = {calculatedP}')
    #print(f'reactive power = {calculatedQ}')

    calculatedPQ = np.concatenate((calculatedP, calculatedQ), None)

    return calculatedPQ 



def updateAVvalues(iterationAVvector: np.ndarray, angles: np.ndarray, voltages: np.ndarray, busTypes: dict):

    angleMismatch = 0
    voltageMismatch = 0
    voltageShift = angles.shape[0]-busTypes['SLACK']
    
    for i in range(angles.shape[0]):
        if (all((slackBus - 1) != i for slackBus in busTypes['SLACK'])):
            angles[i] = iterationAVvector[i-angleMismatch]*180/np.pi
            
            if (all((PVbus - 1) != i for PVbus in busTypes['PV'])):
                voltages[i] = iterationAVvector[i+voltageShift-voltageMismatch]
            else:
                voltageMismatch+=1
        else:
            angleMismatch+=1
            voltageMismatch+=1

    return [angles, voltages]


def readYbus(filePath: str):
    data = []
    with open(filePath, 'r') as file:
        # Skip the first line
        next(file)
        for line in file:
            # Split the line by spaces and remove any leading/trailing whitespaces
            lineData = line.strip().split()
            # Append the data to the list
            data.append(lineData)

    #print(data)

    nl = np.array([int(row[0]) for row in data]) - 1
    nr = np.array([int(row[1]) for row in data]) - 1
    R = np.array([float(row[6]) for row in data])
    X = np.array([float(row[7]) for row in data])
    Bc = np.array([float(row[8]) for row in data])
    #a = np.array([float(row[9]) for row in data])

    #print(nl)
    #print(nr)
    #print(R)
    #print(X)
    #print(Bc)

    nbr = nl.shape[0]
    nbus = int(np.max([np.max(nl), np.max(nr)]))
    Z = R + 1j*X
    y = np.ones(nbr)/Z

    Ybus = np.zeros((nbus + 1, nbus + 1), dtype='complex_')

        #formation of the off diagonal elements
    for i in range(nbr):
        Ybus[nl[i], nr[i]] = Ybus[nl[i], nr[i]] - y[i]
        Ybus[nr[i], nl[i]] = Ybus[nl[i], nr[i]]

    for  n in range(nbus):
        for k in range(nbr):
            if (nl[k] == n) or (nr[k] == n):
                Ybus[n,n] = Ybus[n,n] + y[k] + 1j*Bc[k]


    return Ybus


def cutSlack(array: np.ndarray, busTypes: dict, axis=None):
    return np.delete(array, busTypes['SLACK']-1, axis)

def cutSlackPV(array: np.ndarray, busTypes: dict, axis=None):
    if busTypes['PV'].size == 0:
        return np.delete(array, busTypes['SLACK']-1, axis)
    return np.delete(array, np.concatenate((busTypes['SLACK'], busTypes['PV']), None) - 1)