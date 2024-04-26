import numpy as np
from functions import updateAVvalues, JacobianCalculatorV2, calculatePQ, cutSlack, cutSlackPV
from cases import IEEE30Bus, Saadat3Bus, IEEE14Bus, Ghendy4Bus, Switch4Bus

# ----------------------- CONFIG ---------------------------
np.set_printoptions(precision=3)
stopCondition = 0.001
maxIter = 10
baseMVA = 100


# ------------- Load case Data -----------------


[Ybus, busTypes, voltages, angles, loadsMw, loadsMvar, generationMw, generationMvar] = Switch4Bus()
print(Ybus)
print('---------------------------')


# --------------- Calculations ---------------


iterations = 0

iterationAvector = np.zeros(angles.shape[0], dtype=float)
iterationVvector = np.ones(voltages.shape[0], dtype=float)

iterationAvector = cutSlack(iterationAvector, busTypes)
iterationVvector = cutSlackPV(iterationVvector, busTypes)

scheduledPvector = cutSlack((generationMw - loadsMw)/baseMVA, busTypes)
scheduledQvector = cutSlackPV((generationMvar - loadsMvar)/baseMVA, busTypes)

scheduledPQvector = np.concatenate((scheduledPvector, scheduledQvector), None)

iterationAVvector = np.concatenate((iterationAvector, iterationVvector), None)
deltaAVvector = np.zeros(iterationAVvector.shape[0])
calculatedPQvector = calculatePQ(Ybus, angles, voltages, busTypes)


deltaPQvector = scheduledPQvector - calculatedPQvector

for i in range(deltaPQvector.shape[0]):
    print(f'DeltaPQ{i} = {scheduledPQvector[i]} - {calculatedPQvector[i]} = {deltaPQvector[i]}')


while (any(abs(deltaPQ) > stopCondition for deltaPQ in deltaPQvector)) and (maxIter > iterations):
    iterations+=1
    print(f'iteration {iterations}')

    jacobian = JacobianCalculatorV2(Ybus, voltages, angles, busTypes)

    deltaAVvector = np.linalg.solve(jacobian, deltaPQvector)

    iterationAVvector = iterationAVvector + deltaAVvector

    [angles, voltages] = updateAVvalues(iterationAVvector, angles, voltages, busTypes)
    
    calculatedPQvector = calculatePQ(Ybus, angles, voltages, busTypes)
    deltaPQvector = scheduledPQvector - calculatedPQvector

    print(jacobian)
    for i in range(deltaAVvector.shape[0]):
        print(f'DeltaAV{i} = {deltaAVvector[i]}; iterationAV{i} = {iterationAVvector[i]}')

    for i in range(deltaPQvector.shape[0]):
        print(f'DeltaPQ{i} = {scheduledPQvector[i]} - {calculatedPQvector[i]} = {deltaPQvector[i]}')


    print('-------------------------------------------')
    print('')
print(voltages)
print(angles)

