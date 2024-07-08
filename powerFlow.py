import numpy as np
import copy
import matplotlib.pyplot as plt

from functions import updateAVvalues, JacobianCalculatorV2, calculatePQ, cutSlack, cutSlackPV

def solveNRPF(caseData: dict, BaseMVA: float = 100.0, StopCondition: float = 0.001, MaxIter: int = 10):
    iterations = 0

    iterationAvector = np.zeros(caseData['angles'].shape[0], dtype=float)
    iterationVvector = np.ones(caseData['voltages'].shape[0], dtype=float)

    iterationAvector = cutSlack(iterationAvector, caseData['busTypes'])
    iterationVvector = cutSlackPV(iterationVvector, caseData['busTypes'])

    scheduledPvector = cutSlack((caseData['generationMw'] - caseData['loadsMw'])/BaseMVA, caseData['busTypes'])
    scheduledQvector = cutSlackPV((caseData['generationMvar'] - caseData['loadsMvar'])/BaseMVA, caseData['busTypes'])

    scheduledPQvector = np.concatenate((scheduledPvector, scheduledQvector), None)

    iterationAVvector = np.concatenate((iterationAvector, iterationVvector), None)
    deltaAVvector = np.zeros(iterationAVvector.shape[0])
    calculatedPQvector = calculatePQ(caseData['Ybus'], caseData['angles'], caseData['voltages'], caseData['busTypes'])


    deltaPQvector = scheduledPQvector - calculatedPQvector

    for i in range(deltaPQvector.shape[0]):
        print(f'DeltaPQ{i} = {scheduledPQvector[i]} - {calculatedPQvector[i]} = {deltaPQvector[i]}')


    while (any(abs(deltaPQ) > StopCondition for deltaPQ in deltaPQvector)) and (MaxIter > iterations):
        iterations+=1
        print(f'iteration {iterations}')

        jacobian = JacobianCalculatorV2(caseData['Ybus'], caseData['voltages'], caseData['angles'], caseData['busTypes'])

        deltaAVvector = np.linalg.solve(jacobian, deltaPQvector)

        iterationAVvector = iterationAVvector + deltaAVvector

        [caseData['angles'], caseData['voltages']] = updateAVvalues(iterationAVvector, caseData['angles'], caseData['voltages'], caseData['busTypes'])
        
        calculatedPQvector = calculatePQ(caseData['Ybus'], caseData['angles'], caseData['voltages'], caseData['busTypes'])
        deltaPQvector = scheduledPQvector - calculatedPQvector

        print(jacobian)
        for i in range(deltaAVvector.shape[0]):
            print(f'DeltaAV{i} = {deltaAVvector[i]}; iterationAV{i} = {iterationAVvector[i]}')

        for i in range(deltaPQvector.shape[0]):
            print(f'DeltaPQ{i} = {scheduledPQvector[i]} - {calculatedPQvector[i]} = {deltaPQvector[i]}')

        print(f'tensões iteração {iterations} = {caseData["voltages"]}')
        print(f'angulos iteração {iterations} = {caseData["angles"]}')

    print('-------------------------------------------')
    print('')
    print(f'tensões finais = {caseData["voltages"]}')
    print(f'angulos finais = {caseData["angles"]}')
    retang = caseData['voltages']*np.exp(1j*caseData['angles']*np.pi/180)
    print(f'em coord retangulares = {retang}')


def solveNRPFprintSupressed(caseData: dict, BaseMVA: float = 100.0, StopCondition: float = 0.001, MaxIter: int = 10):
    iterations = 0

    iterationAvector = np.zeros(caseData['angles'].shape[0], dtype=float)
    iterationVvector = np.ones(caseData['voltages'].shape[0], dtype=float)

    iterationAvector = cutSlack(iterationAvector, caseData['busTypes'])
    iterationVvector = cutSlackPV(iterationVvector, caseData['busTypes'])

    scheduledPvector = cutSlack((caseData['generationMw'] - caseData['loadsMw'])/BaseMVA, caseData['busTypes'])
    scheduledQvector = cutSlackPV((caseData['generationMvar'] - caseData['loadsMvar'])/BaseMVA, caseData['busTypes'])

    scheduledPQvector = np.concatenate((scheduledPvector, scheduledQvector), None)

    iterationAVvector = np.concatenate((iterationAvector, iterationVvector), None)
    deltaAVvector = np.zeros(iterationAVvector.shape[0])
    calculatedPQvector = calculatePQ(caseData['Ybus'], caseData['angles'], caseData['voltages'], caseData['busTypes'])

    deltaPQvector = scheduledPQvector - calculatedPQvector

    while (any(abs(deltaPQ) > StopCondition for deltaPQ in deltaPQvector)) and (MaxIter > iterations):
        iterations+=1

        jacobian = JacobianCalculatorV2(caseData['Ybus'], caseData['voltages'], caseData['angles'], caseData['busTypes'])

        deltaAVvector = np.linalg.solve(jacobian, deltaPQvector)

        iterationAVvector = iterationAVvector + deltaAVvector

        [caseData['angles'], caseData['voltages']] = updateAVvalues(iterationAVvector, caseData['angles'], caseData['voltages'], caseData['busTypes'])
        
        calculatedPQvector = calculatePQ(caseData['Ybus'], caseData['angles'], caseData['voltages'], caseData['busTypes'])
        deltaPQvector = scheduledPQvector - calculatedPQvector

    print('-------------------------------------------')
    print('')
    print(f'tensões finais = {caseData["voltages"]}')
    print(f'angulos finais = {caseData["angles"]}')


def solveCNRPF(caseData: dict, BaseMVA: float = 100.0, StopCondition: float = 0.001, MaxIter: int = 10):
    voltagesRecord = []
    loadsRecord = []

    baseVoltages = copy.deepcopy(caseData['voltages'])
    baseAngles = copy.deepcopy(caseData['angles'])

    while (all(voltage >= 0 for voltage in caseData['voltages'])):
        try:
            caseData['voltages'] = copy.deepcopy(baseVoltages)
            caseData['angles'] = copy.deepcopy(baseAngles)

            solveNRPFprintSupressed(caseData, BaseMVA=BaseMVA, StopCondition=StopCondition, MaxIter=MaxIter)
            voltagesRecord.append(copy.deepcopy(caseData['voltages']))
            loadsRecord.append(copy.deepcopy(caseData['loadsMw']))

            caseData['loadsMw']*=1.01
            caseData['loadsMvar']*=1.01
        except:
            break


    print(len(voltagesRecord))
    for loadBus in caseData['busTypes']['PQ']:
        y = [voltage[loadBus-1] for voltage in voltagesRecord]
        x = [load[loadBus-1] for load in loadsRecord]
        plt.plot(x,y)
    

    plt.show()

