---
description: Cirq implementation of Bernstein-Vazirani
---

# Bernstein-Vazirani

> [Open in Colab notebook](https://githubtocolab.com/niranjansd/qswe/blob/main/code/cirq/notebooks/Cirq\_Bernstein\_Vazirani.ipynb)

```
#@title Bernstein-Vazirani Algorithm Simulator
## Imports
import numpy as np
import cirq
import random

class BV(object):

  def __init__(self, bitstring_length=8, repetitions=10):
    self.repetitions = repetitions
    self.num_qubits = bitstring_length + 1
    # Choose qubits to use.
    self.input_qubits = [cirq.GridQubit(i, 0) for i in range(self.num_qubits)]
    self.output_qubit = cirq.GridQubit(self.num_qubits, 0)

  def make_oracle(self, input_qubits, output_qubit,
                  secret_bitstring=None, secret_bias_bit=None):
    """Gates implementing the function f(a) = a·string + bias (mod 2)."""
    if secret_bias_bit:
        yield cirq.X(self.output_qubit)
    for qubit, bit in zip(self.input_qubits, secret_bitstring):
        if bit:
            yield cirq.CNOT(qubit, self.output_qubit)

  def make_bernstein_vazirani_circuit(self, input_qubits, output_qubit, oracle):
      """Solves for factors in f(a) = a·factors + bias (mod 2) with one query."""
      c = cirq.Circuit()
      # Initialize qubits.
      c.append([cirq.X(output_qubit), cirq.H(output_qubit), cirq.H.on_each(*input_qubits)])
      # Query oracle.
      c.append(oracle)
      # Measure in X basis.
      c.append([cirq.H.on_each(*input_qubits), cirq.measure(*input_qubits, key='result')])
      return c

  def run_bernstein_vazirani_simulation(self, secret_bitstring=None,
                                        secret_bias_bit=None):
    # Embed the oracle into a special quantum circuit querying it exactly once.
    if not secret_bias_bit:
      secret_bias_bit = random.randint(0, 1)
    if not secret_bitstring:
      secret_bitstring = [random.randint(0, 1)
                          for _ in range(self.num_qubits)]
    oracle = self.make_oracle(self.input_qubits, self.output_qubit,
                              secret_bitstring, secret_bias_bit)
    circuit = self.make_bernstein_vazirani_circuit(self.input_qubits,
                                                   self.output_qubit, oracle)
    print('######### Printing Circuit ##########')
    print(circuit)

    # Sample from the circuit a couple times.
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=self.repetitions)
    frequencies = result.histogram(key='result', fold_func=bitstring)
    print('######### Printing Results ##########')
    print(f"Targeted secret string: {''.join(map(str, secret_bitstring))}",
          "||", "% of measurements")
    for k, v in frequencies.items():
      print(f"Measured secret string: {k}", "||", v*100/self.repetitions)


def bitstring(bits):
    return ''.join(str(int(b)) for b in bits)


dsim = BV(bitstring_length=5)
dsim.run_bernstein_vazirani_simulation()
```
