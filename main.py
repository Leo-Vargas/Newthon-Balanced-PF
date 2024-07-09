import numpy as np
from functions import openSwitches
from powerFlow import solveNRPF, solveCNRPF
from cases import IEEE30Bus, Saadat3Bus, IEEE14Bus, Class4Bus, Switch4Bus, Class5Bus, Class5BusOpened

# ----------------------- CONFIG ---------------------------
np.set_printoptions(precision=4)
stopCondition = 0.001
maxIter = 10
baseMVA = 100


print('------------- Load case Data -----------------')


caseData = Class5BusOpened()
print(np.absolute(caseData['Ybus']))
print(np.angle(caseData['Ybus'], deg=True))
print(f'is Ybus symmetric? {np.allclose(caseData["Ybus"], caseData["Ybus"].T, rtol=1e-05, atol=1e-08)}')
print('')


print('-------------- Opening Switches --------------')

#caseData = openSwitches(caseData, switches=[])
print(caseData['Ybus'])


print('')
print('--------------- Calculations ---------------')
if caseData['Ybus'].shape[0] > 1:
    solveNRPF(caseData, BaseMVA=baseMVA, StopCondition=stopCondition, MaxIter=maxIter)
else:
    print('o sistema está em aberto e não pode ser resolvido')

