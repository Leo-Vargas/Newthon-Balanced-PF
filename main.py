import numpy as np
from functions import updateAVvalues, JacobianCalculatorV2, calculatePQ, cutSlack, cutSlackPV
from cases import IEEE30Bus, Saadat3Bus, IEEE14Bus, Ghendy4Bus, Switch4Bus

# ----------------------- CONFIG ---------------------------
np.set_printoptions(precision=3)
stopCondition = 0.001
maxIter = 10
baseMVA = 100


# ------------- Load case Data -----------------



caseData = Switch4Bus()
print(caseData['Ybus'])
print('---------------------------')


# --------------- Calculations ---------------


iterations = 0

iterationAvector = np.zeros(caseData['angles'].shape[0], dtype=float)
iterationVvector = np.ones(caseData['voltages'].shape[0], dtype=float)

iterationAvector = cutSlack(iterationAvector, caseData['busTypes'])
iterationVvector = cutSlackPV(iterationVvector, caseData['busTypes'])

scheduledPvector = cutSlack((caseData['generationMw'] - caseData['loadsMw'])/baseMVA, caseData['busTypes'])
scheduledQvector = cutSlackPV((caseData['generationMvar'] - caseData['loadsMvar'])/baseMVA, caseData['busTypes'])

scheduledPQvector = np.concatenate((scheduledPvector, scheduledQvector), None)

iterationAVvector = np.concatenate((iterationAvector, iterationVvector), None)
deltaAVvector = np.zeros(iterationAVvector.shape[0])
calculatedPQvector = calculatePQ(caseData['Ybus'], caseData['angles'], caseData['voltages'], caseData['busTypes'])


deltaPQvector = scheduledPQvector - calculatedPQvector

for i in range(deltaPQvector.shape[0]):
    print(f'DeltaPQ{i} = {scheduledPQvector[i]} - {calculatedPQvector[i]} = {deltaPQvector[i]}')


while (any(abs(deltaPQ) > stopCondition for deltaPQ in deltaPQvector)) and (maxIter > iterations):
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


    print('-------------------------------------------')
    print('')
print(f'tensões finais = {caseData['voltages']}')
print(f'angulos finais = {caseData['angles']}')

