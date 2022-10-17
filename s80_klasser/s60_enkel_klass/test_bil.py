import unittest
from bil import Bil

enBil = Bil("Mercedes-Benz", "GLC", 12400,  280)

assert (type(enBil) == Bil)
assert (enBil.märke == "Mercedes-Benz",)
assert (enBil.modell == "GLC")
assert (enBil.mil == 12400)
assert (enBil.topphastighet == 280)
