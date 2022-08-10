---
description: Cirq implementation of Bell Inequality
---

# Bell Inequality

> [Bell Inequality Simulator](lib/bell\_inequality.py)
>
> [Colab Example](notebooks/Bell\_Inequality.ipynb)

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
