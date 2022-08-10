---
description: Cirq implementation of Bell Inequality
---

# Bell Inequality

> [Bell Inequality Simulator on Github](lib/bell\_inequality.py)
>
> [Colab example](https://githubtocolab.com/niranjansd/qswe/blob/main/code/cirq/notebooks/Cirq\_Bell\_Inequality.ipynb)

```
!pip install cirq
!git clone https://github.com/niranjansd/qswe.git

import sys
sys.path.append('qswe/code/cirq')
from lib import bell_inequality

belltest = bell_inequality.CHSHBell()
belltest.run_classical_bell_test()
belltest.run_quantum_bell_test()
```
