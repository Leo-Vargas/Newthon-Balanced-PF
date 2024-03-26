import numpy as np
from scipy import linalg
from classes import Measurement, StateData
from functions import hSetup, makeBusConfiguration
from JacobianCalculator import JacobianCalculator, ReducedJacobian
from JacobianCalculatorV2 import JacobianCalculatorV2

# --------------- entry data ---------------
measurementDict = {
    'P1': Measurement(0, 1, 0),
    'p2': Measurement(0, 2, 1),
    'p3': Measurement(0, 3, 2),
    'p4': Measurement(0, 4, 2),
    'p5': Measurement(0, 5, 1),
    'p6': Measurement(0, 6, 2),
    'p7': Measurement(0, 7, 2),
    'p8': Measurement(0, 8, 1),
    'p9': Measurement(0, 9, 2),
    'p10': Measurement(0, 10, 2),
    'p11': Measurement(0, 11, 1),
    'p12': Measurement(0, 12, 2),
    'p13': Measurement(0, 13, 1),
    'p14': Measurement(0, 14, 2),
    'p15': Measurement(0, 15, 2),
    'p16': Measurement(0, 16, 2),
    'p17': Measurement(0, 17, 2),
    'p18': Measurement(0, 18, 2),
    'p19': Measurement(0, 19, 2),
    'p20': Measurement(0, 20, 2),
    'p21': Measurement(0, 21, 2),
    'p22': Measurement(0, 22, 2),
    'p23': Measurement(0, 23, 2),
    'p24': Measurement(0, 24, 2),
    'p25': Measurement(0, 25, 2),
    'p26': Measurement(0, 26, 2),
    'p27': Measurement(0, 27, 2),
    'p28': Measurement(0, 28, 2),
    'p29': Measurement(0, 29, 2),
    'p30': Measurement(0, 30, 2),
    'q1': Measurement(1, 1, 0),
    'q2': Measurement(1, 2, 1),
    'q3': Measurement(1, 3, 2),
    'q4': Measurement(1, 4, 2),
    'q5': Measurement(1, 5, 1),
    'q6': Measurement(1, 6, 2),
    'q7': Measurement(1, 7, 2),
    'q8': Measurement(1, 8, 1),
    'q9': Measurement(1, 9, 2),
    'q10': Measurement(1, 10, 2),
    'q11': Measurement(1, 11, 1),
    'q12': Measurement(1, 12, 2),
    'q13': Measurement(1, 13, 1),
    'q14': Measurement(1, 14, 2),
    'q15': Measurement(1, 15, 2),
    'q16': Measurement(1, 16, 2),
    'q17': Measurement(1, 17, 2),
    'q18': Measurement(1, 18, 2),
    'q19': Measurement(1, 19, 2),
    'q20': Measurement(1, 20, 2),
    'q21': Measurement(1, 21, 2),
    'q22': Measurement(1, 22, 2),
    'q23': Measurement(1, 23, 2),
    'q24': Measurement(1, 24, 2),
    'q25': Measurement(1, 25, 2),
    'q26': Measurement(1, 26, 2),
    'q27': Measurement(1, 27, 2),
    'q28': Measurement(1, 28, 2),
    'q29': Measurement(1, 29, 2),
    'q30': Measurement(1, 30, 2)
}    
gridTopology = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])

Ybus = np.array([
(6.46838346734966 - 20.6959477620055j, -5.22464617988566 + 15.6467268408034j, -1.24373728746401 + 5.09602092120209j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j),
(-5.22464617988566 + 15.6467268408034j, 9.75228216552403 - 30.6486628926761j, 0.00000000000000 + 0.00000000000000j, -1.70553031669903 + 5.19737922825651j, -1.13596078817388 + 4.77247932828136j, -1.68614488076547 + 5.11647749533481j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j),
(-1.24373728746401 + 5.09602092120209j, 0.00000000000000 + 0.00000000000000j, 9.43918632977612 - 28.6022935502649j, -8.19544904231211 + 23.5308726290628j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j),
(0.00000000000000 + 0.00000000000000j, -1.70553031669903 + 5.19737922825651j, -8.19544904231211 + 23.5308726290628j, 16.3141030891857 - 55.8200477304928j, 0.00000000000000 + 0.00000000000000j, -6.41312373017456 + 22.3112035654812j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 4.74646293582023j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j),
(0.00000000000000 + 0.00000000000000j, -1.13596078817388 + 4.77247932828136j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 4.08998082413586 - 12.1188472450551j, 0.00000000000000 + 0.00000000000000j, -2.95402003596198 + 7.44926791677370j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j),
(0.00000000000000 + 0.00000000000000j, -1.68614488076547 + 5.11647749533481j, 0.00000000000000 + 0.00000000000000j, -6.41312373017456 + 22.3112035654812j, 0.00000000000000 + 0.00000000000000j, 18.4741606772999 - 67.0448396645865j, -3.59021042398099 + 11.0261144107281j, -6.28930817610063 + 22.0125786163522j, 0.00000000000000 + 4.73431049501951j, 0.00000000000000 + 1.86785870919009j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, -0.495373466278286 + 0.0147121179186223j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j),
(0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, -2.95402003596198 + 7.44926791677370j, -3.59021042398099 + 11.0261144107281j, 6.54423045994298 - 18.3848823275018j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j),
(0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, -6.28930817610063 + 22.0125786163522j, 0.00000000000000 + 0.00000000000000j, 7.73328723749608 - 26.5276932748284j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, -1.44397906139545 + 4.54081465847625j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j),
(0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 4.73431049501951j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 - 11.4139457664638j, 0.00000000000000 + 1.79856115107914j, 0.00000000000000 + 4.80769230769231j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j),
(0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 1.86785870919009j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 1.79856115107914j, 13.4620428145242 - 34.4714127276924j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, -3.95603912571535 + 10.3174477198441j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, -1.78483031526663 + 3.98535828943083j, -5.10185382015965 + 10.9807141129298j, -2.61931955338260 + 5.40077030332945j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j),
(0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 4.80769230769231j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 - 4.80769230769231j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j),
(0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 4.74646293582023j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 6.57396158377616 - 19.9813139751750j, 0.00000000000000 + 1.79856115107914j, -1.52656760883956 + 3.17342527296542j, -3.09539618265643 + 6.09727586432626j, -1.95199779228017 + 4.10435937911185j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j),
(0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 1.79856115107914j, 0.00000000000000 - 1.79856115107914j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j),
(0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, -1.52656760883956 + 3.17342527296542j, 0.00000000000000 + 0.00000000000000j, 4.62196379149599 - 9.27070113729168j, -3.09539618265643 + 6.09727586432626j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j),
(0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, -3.09539618265643 + 6.09727586432626j, 0.00000000000000 + 0.00000000000000j, -3.09539618265643 + 6.09727586432626j, 9.96684093197897 - 19.8620405912426j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, -1.80769961776445 + 3.69142398580871j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, -1.96834894890166 + 3.97606487678136j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j),
(0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, -1.95199779228017 + 4.10435937911185j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 3.81980085692792 - 8.48372287534904j, -1.86780306464775 + 4.37936349623719j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j),
(0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, -3.95603912571535 + 10.3174477198441j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, -1.86780306464775 + 4.37936349623719j, 5.82384219036310 - 14.6968112160812j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j),
(0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, -1.80769961776445 + 3.69142398580871j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 4.88338605177317 - 9.91018278508768j, -3.07568643400872 + 6.21875879927897j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j),
(0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, -3.07568643400872 + 6.21875879927897j, 8.95803937518519 - 17.9834646816319j, -5.88235294117647 + 11.7647058823529j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j),
(0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, -1.78483031526663 + 3.98535828943083j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, -5.88235294117647 + 11.7647058823529j, 7.66718325644310 - 15.7500641717838j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j),
(0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, -5.10185382015965 + 10.9807141129298j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 21.8764951898959 - 45.1084327617036j, -16.7746413697362 + 34.1277186487737j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j),
(0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, -2.61931955338260 + 5.40077030332945j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, -16.7746413697362 + 34.1277186487737j, 21.9344990753744 - 43.4828918151792j, 0.00000000000000 + 0.00000000000000j, -2.54053815225556 + 3.95440286307604j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j),
(0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, -1.96834894890166 + 3.97606487678136j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 3.42975455538499 - 6.96530361731543j, -1.46140560648333 + 2.98923874053408j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j),
(0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, -2.54053815225556 + 3.95440286307604j, -1.46140560648333 + 2.98923874053408j, 5.31183670261313 - 9.27126365731517j, -1.30989294387425 + 2.28762205370506j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j),
(0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, -1.30989294387425 + 2.28762205370506j, 4.49571508032199 - 7.86497876196962j, -1.21653011944949 + 1.81714404634750j, -1.96929201699825 + 3.76021266191706j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j),
(0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, -1.21653011944949 + 1.81714404634750j, 1.21653011944949 - 1.81714404634750j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j),
(0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, -1.96929201699825 + 3.76021266191706j, 0.00000000000000 + 0.00000000000000j, 3.65228147077859 - 9.46044252232512j, 0.00000000000000 + 2.63568784599992j, -0.995533550952680 + 1.88100584035782j, -0.687455902827657 + 1.29397149479772j),
(0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, -0.495373466278286 + 0.0147121179186223j, 0.00000000000000 + 0.00000000000000j, -1.44397906139545 + 4.54081465847625j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 2.63568784599992j, 1.93935252767373 - 7.05287930164740j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j),
(0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, -0.995533550952680 + 1.88100584035782j, 0.00000000000000 + 0.00000000000000j, 1.90758675798496 - 3.60436440120705j, -0.912053207032276 + 1.72335856084923j),
(0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, 0.00000000000000 + 0.00000000000000j, -0.687455902827657 + 1.29397149479772j, 0.00000000000000 + 0.00000000000000j, -0.912053207032276 + 1.72335856084923j, 1.59950910985993 - 3.01733005564695j)
])
#print(Ybus)
#print('\n')
#is_symmetric(Ybus)

busConfiguration = makeBusConfiguration(measurementDict)

PQ = 0
PV = 0

for key in measurementDict:
    if (measurementDict[key].busType == 2):
        PQ +=1
    elif measurementDict[key].busType == 1:
        PV +=1

PQ /=2
PV /=2

#print(f'PQ buses: {PQ}')
#print(f'PV buses: {PV}')
#print('\n')
  
voltages = np.array([1.06, 1.043, 1.022, 1.013, 1.01, 1.012, 1.003, 1.01, 1.051, 1.044, 1.082, 1.057, 1.071, 1.042, 1.038, 1.045, 1.039, 1.028, 1.025, 1.029, 1.032, 1.033, 1.027, 1.022, 1.019, 1.001, 1.026, 1.011, 1.006, 0.995])
angles = np.array([0.0, -5.497, -8.004, -9.661, -14.381, -11.398, -13.158, -12.115, -14.434, -16.024, -14.434, -15.302, -15.302, -16.191, -16.278, -15.88, -16.188, -16.884, -17.052, -16.852, -16.468, -16.455, -16.662, -16.83, -16.424, -16.842, -15.912, -12.057, -17.136, -18.015])

[hValues, hDataDict] = hSetup(gridTopology, angles, voltages)

# --------------- Calculations ---------------
np.set_printoptions(precision=3)
jacobian = JacobianCalculator(list(measurementDict.values()), hDataDict, Ybus, hValues, gridTopology, busConfiguration)

[PA, QA] = JacobianCalculatorV2(Ybus, voltages, angles)

print(jacobian[0:29,0:29])
print(jacobian.shape)

print('---------------------barreira--------------------')
print(PA)
print('---------------------barreira--------------------')
print(QA)




