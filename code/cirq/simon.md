---
description: Cirq implementation of Simon's algorithm
---

# Simon

> [Open in Colab Notebook](https://githubtocolab.com/niranjansd/qswe/blob/main/code/cirq/notebooks/Cirq\_Simon.ipynb)

```
#@title Simons's Algorithm Simulator
## Imports
from collections import Counter
import numpy as np
import scipy as sp
import cirq


class Simon(object):

  def __init__(self, num_qubits=3):
    self.num_qubits = num_qubits

  def make_oracle(self, input_qubits, output_qubits, secret_string):
    """Gates implementing the function f(a) = f(b) iff a ⨁ b = s"""
    # Copy contents to output qubits:
    for control_qubit, target_qubit in zip(input_qubits, output_qubits):
        yield cirq.CNOT(control_qubit, target_qubit)

    # Create mapping:
    if sum(secret_string):  # check if the secret string is non-zero
        # Find significant bit of secret string (first non-zero bit)
        significant = list(secret_string).index(1)

        # Add secret string to input according to the significant bit:
        for j in range(len(secret_string)):
            if secret_string[j] > 0:
                yield cirq.CNOT(input_qubits[significant], output_qubits[j])
    # Apply a random permutation:
    pos = [0, len(secret_string) - 1] 
    # Swap some qubits to define oracle. We choose first and last:
    yield cirq.SWAP(output_qubits[pos[0]], output_qubits[pos[1]])

  def make_simon_circuit(self, input_qubits, output_qubits, oracle):
    """Solves for the secret period s of a 2-to-1 function such that
    f(x) = f(y) iff x ⨁ y = s
    """
    c = cirq.Circuit()
    # Initialize qubits.
    c.append([cirq.H.on_each(*input_qubits)])
    # Query oracle.
    c.append(oracle)
    # Measure in X basis.
    c.append([cirq.H.on_each(*input_qubits), cirq.measure(*input_qubits, key='result')])
    return c

  def post_processing(self, data, results):
    """Solves a system of equations with modulo 2 numbers"""
    sing_values = sp.linalg.svdvals(results)
    tolerance = 1e-5
    if sum(sing_values < tolerance) == 0:  # check if measurements are linearly dependent
        flag = True
        null_space = sp.linalg.null_space(results).T[0]
        solution = np.around(null_space, 3)  # chop very small values
        minval = abs(min(solution[np.nonzero(solution)], key=abs))
        solution = (solution / minval % 2).astype(int)  # renormalize vector mod 2
        data.append(str(solution))
        return flag

  def run_simon_simulation(self, secret_string=""):
    # define a secret string:
    if secret_string:
      secret_string = np.array(list(secret_string)).astype(int)
      if len(secret_string) != self.num_qubits:
        raise ValueError(f'Secret string must have {self.num_qubits} qubits.')
    else:
      secret_string = np.random.randint(2, size=self.num_qubits)
    print(f'Secret string = {secret_string}')

    data = []  # we'll store here the results

    n_samples = 100
    for _ in range(n_samples):
        flag = False  # check if we have a linearly independent set of measures
        while not flag:
            # Choose qubits to use.
            input_qubits = [cirq.GridQubit(i, 0) for i in range(self.num_qubits)]  # input x
            output_qubits = [
                cirq.GridQubit(i + self.num_qubits, 0) for i in range(self.num_qubits)
            ]  # output f(x)
            # Pick coefficients for the oracle and create a circuit to query it.
            oracle =self.make_oracle(input_qubits, output_qubits, secret_string)
            # Embed oracle into special quantum circuit querying it exactly once
            circuit = self.make_simon_circuit(input_qubits, output_qubits, oracle)
            # Sample from the circuit a n-1 times (n = qubit_count).
            simulator = cirq.Simulator()
            results = [simulator.run(circuit).measurements['result'][0]
                       for _ in range(self.num_qubits - 1)]

            # Classical Post-Processing:
            flag = self.post_processing(data, results)

    freqs = Counter(data)
    print('######### Printing Circuit ##########')
    print(circuit)
    print('######### Printing Results ##########')
    print(f'Most common answer was : {freqs.most_common(1)[0]}')
```
