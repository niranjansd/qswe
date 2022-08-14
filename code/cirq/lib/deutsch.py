import random
import numpy as np
import cirq


class Deutch():

  def __init__(self):
    # Initialize qubits.
    self.q0, self.q1 = cirq.LineQubit.range(2)

  def make_oracle(self, q0, q1, secret_function=[]):
    """Gates implementing the secret function f(x)."""
    # If secret function is not provided, pick a random function.
    if not secret_function:
      secret_function = [np.random.randint(0, 2) for _ in range(2)]
    print('######### Printing Secret Function ##########')
    print(f"Secret function:\nf(0, 1) = ({', '.join(str(e) for e in secret_function)})")
    # Encode secret function as the oracle circuit.
    if secret_function[0] != secret_function[1]:
      yield cirq.CNOT(q0, q1)

  def make_deutsch_circuit(self, q0, q1, oracle):
    """Make circuit for Deutsch algorithm."""
    c = cirq.Circuit()
    # Initialize qubits.
    c.append([cirq.X(q1), cirq.H(q1), cirq.H(q0)])
    # Query oracle exactly once.
    c.append(oracle)
    # Measure qubit 1 in X basis.
    c.append([cirq.Moment(cirq.H(q0)),
              cirq.Moment(cirq.measure(q0, key='result'))])
    return c

  def run_deutsch_algorithm(self, secret_function=[]):
    self.oracle = self.make_oracle(self.q0, self.q1, secret_function)
    self.circuit = self.make_deutsch_circuit(self.q0, self.q1, self.oracle)
    print('######### Printing Circuit ##########')
    print(self.circuit)

    # Simulate the circuit.
    simulator = cirq.Simulator()
    result = simulator.run(self.circuit)
    print('######### Result of f(0)⊕f(1) ##########')
    print(result)




if __name__ == '__main__':
    dsim = Deutch()
    dsim.run_deutsch_algorithm()
