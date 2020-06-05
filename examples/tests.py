
from logicqubit.logic import *
from logicqubit.gates import *

logicQuBit = LogicQuBit(2)

q1 = Qubit()
q2 = Qubit()

q1.X()

logicQuBit.Measure([q1, q2])
logicQuBit.Plot()

gate = Gates(2)
gate.setCuda(False)
X = gate.Y().adjoint()
print(X)
