import numpy as np
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