import numpy as np

def JacobianCalculatorV2(Ybus: np.ndarray,  voltages: np.ndarray, angles: np.ndarray):
    fasorVoltages = np.zeros(len(voltages), dtype ='complex_')
    complexAngles = np.zeros(len(voltages), dtype='complex_')

    for i in range(len(voltages)):
        fasorVoltages[i] = module2Complex(voltages[i], angles[i])

    Ic = Ybus@fasorVoltages
    complexAngles = fasorVoltages/voltages
    
    angleDerivative = 1.j*np.diag(fasorVoltages)@(np.conj(np.diag(Ic)-Ybus@np.diag(fasorVoltages)))

    voltageDerivative = np.diag(np.conj(Ic))@np.diag(complexAngles)+np.diag(fasorVoltages)@(Ybus@np.diag(complexAngles))
    

    return [np.real(angleDerivative), np.imag(angleDerivative), np.real(voltageDerivative), np.imag(voltageDerivative)]

def module2Complex(module, angle):
    """receive a module and angle (IN DREGREES) and returns the complete fasor"""
    return module*np.exp(1.j*angle*np.pi/180)