import numpy as np
from functions import openSwitches
from powerFlow import solveNRPF
from cases import IEEE30Bus, Saadat3Bus, IEEE14Bus, Ghendy4Bus, Switch4Bus

# ----------------------- CONFIG ---------------------------
np.set_printoptions(precision=3)
stopCondition = 0.001
maxIter = 10
baseMVA = 100


print('------------- Load case Data -----------------')


caseData = Switch4Bus()
print(caseData['Ybus'])
print('')


print('-------------- Opening Switches --------------')

caseData = openSwitches(caseData, switches=[5])
print(caseData['Ybus'])


print('')
print('--------------- Calculations ---------------')
if caseData['Ybus'].shape[0] > 1:
    solveNRPF(caseData, BaseMVA=baseMVA, StopCondition=stopCondition, MaxIter=maxIter)
else:
    print('o sistema está em aberto e não pode ser resolvido')
