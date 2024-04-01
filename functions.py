import numpy as np

def JacobianCalculatorV2(Ybus: np.ndarray,  voltages: np.ndarray, angles: np.ndarray, busTypes: dict):
    fasorVoltages = np.zeros(len(voltages), dtype ='complex_')

    for i in range(len(voltages)):
        fasorVoltages[i] = module2Complex(voltages[i], angles[i])

    

    IcDiag = np.diag(Ybus@fasorVoltages)
    complexAnglesDiag = np.diag(fasorVoltages/voltages)
    fasorVoltagesDiag = np.diag(fasorVoltages)

    
    angleDerivative = 1.j*fasorVoltagesDiag@(np.conj(IcDiag-Ybus@fasorVoltagesDiag))

    voltageDerivative = np.conj(IcDiag)@complexAnglesDiag + fasorVoltagesDiag@np.conj(Ybus@complexAnglesDiag)

    
    J11 = np.real(np.delete(np.delete(angleDerivative, busTypes['SLACK'] - 1, axis=0),
                            busTypes['SLACK'] - 1, axis=1))
    
    J21 = np.imag(np.delete(np.delete(angleDerivative, np.concatenate((busTypes['SLACK'], busTypes['PV']), None) - 1, axis=0),
                            busTypes['SLACK'] - 1, axis=1))
    
    J12 = np.real(np.delete(np.delete(voltageDerivative, busTypes['SLACK'] - 1, axis=0), 
                            np.concatenate((busTypes['SLACK'], busTypes['PV']), None) - 1, axis=1))

    J22 = np.imag(np.delete(np.delete(voltageDerivative,  np.concatenate((busTypes['SLACK'], busTypes['PV']), None) - 1, axis=0), 
                            np.concatenate((busTypes['SLACK'], busTypes['PV']), None) - 1, axis=1))

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
    fasorVoltages = np.zeros(len(voltages), dtype ='complex_')
    calculatedS = np.zeros(angles.shape[0], dtype='complex_')

    for i in range(len(voltages)):
        fasorVoltages[i] = module2Complex(voltages[i], angles[i])

    calculatedS = fasorVoltages*(np.conj(Ybus@fasorVoltages))


    calculatedP = np.real(np.delete(calculatedS, busTypes['SLACK'] - 1))
    calculatedQ = np.imag(np.delete(calculatedS,  np.concatenate((busTypes['SLACK'], busTypes['PV']), axis=None) - 1))
    #print(f'active power = {calculatedP}')
    #print(f'reactive power = {calculatedQ}')

    calculatedPQ = np.concatenate((calculatedP, calculatedQ), None)

    return calculatedPQ 


def module2Complex(module, angle):
    """receive a module and angle (IN DREGREES) and returns the complete fasor"""
    return module*np.exp(1.j*angle*np.pi/180)


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

