import pypower.api as pp
from pypower.api import case14


ppc = case14()


[Ybus, YF, YT] = pp.makeYbus(ppc['baseMVA'], ppc['bus'], ppc['branch'])
print(Ybus)


