# Bell Inequality
## Imports
import numpy as np
import cirq

## Utility functions
def bitstring(bits):
    return ''.join('1' if e else '_' for e in bits)


class CHSHBell(object):

    def __init__(self, repetitions=1):
        super().__init__()
        self.repetitions = repetitions
    
    def setup(self):
        alice_recv = cirq.NamedQubit("x")
        bob_recv = cirq.NamedQubit("y")
        alice_retn = cirq.NamedQubit("a")
        bob_retn = cirq.NamedQubit("b")
        return alice_recv, bob_recv, alice_retn, bob_retn

    def make_quantum_bell_test_circuit(self, alice_recv, bob_recv, alice_retn, bob_retn):
        circuit = cirq.Circuit()

        # Prepare shared entangled state.
        circuit.append([cirq.H(alice_retn), cirq.CNOT(alice_retn, bob_retn)])

        # Received bits are randomized.
        circuit.append([cirq.H(alice_recv), cirq.H(bob_recv)])

        # Players do a sqrt(X) based on their received bit.
        circuit.append(
            [cirq.X(alice_retn) ** -0.25,
             cirq.CNOT(alice_recv, alice_retn) ** 0.5,
             cirq.CNOT(bob_recv, bob_retn) ** 0.5]
        )
        # Then results are recorded.
        circuit.append(
            [
                cirq.measure(alice_recv, key='x'),
                cirq.measure(alice_retn, key='a'),
                cirq.measure(bob_recv, key='y'),
                cirq.measure(bob_retn, key='b'),
            ]
        )
        return circuit

    def run_quantum_bell_test(self):
        alice_recv, bob_recv, alice_retn, bob_retn = self.setup()
        self.circuit = self.make_quantum_bell_test_circuit(alice_recv, bob_recv, alice_retn, bob_retn)
        print('Quantum Best Strategy Circuit:')
        print(self.circuit)

        print(f'Simulating {self.repetitions} repetitions...')
        result = cirq.Simulator().run(program=self.circuit, repetitions=self.repetitions)

        # Collect results.
        a = np.array(result.measurements['a'][:, 0])
        b = np.array(result.measurements['b'][:, 0])
        x = np.array(result.measurements['x'][:, 0])
        y = np.array(result.measurements['y'][:, 0])
        outcomes = a ^ b == x & y
        win_percent = len([e for e in outcomes if e]) * 100 / self.repetitions

        # Print data.
        print('Results')
        print('a:', bitstring(a))
        print('b:', bitstring(b))
        print('x:', bitstring(x))
        print('y:', bitstring(y))
        print('(a XOR b) == (x AND y):\n  ', bitstring(outcomes))
        print(f'Win rate: {win_percent}%')

    def make_classical_bell_test_circuit(self, alice_recv, bob_recv, alice_retn, bob_retn):
        circuit = cirq.Circuit()
        # Received bits are randomized.
        circuit.append([cirq.H(alice_recv), cirq.H(bob_recv)])
        # Alice and Bob simply return 0s.
        # Then results are recorded.
        circuit.append(
            [
                cirq.measure(alice_recv, key='x'),
                cirq.measure(alice_retn, key='a'),
                cirq.measure(bob_recv, key='y'),
                cirq.measure(bob_retn, key='b'),
            ]
        )
        return circuit

    def run_classical_bell_test(self):
        alice_recv, bob_recv, alice_retn, bob_retn = self.setup()
        self.circuit = self.make_classical_bell_test_circuit(alice_recv, bob_recv, alice_retn, bob_retn)
        print('Classical Best Strategy Circuit:')
        print(self.circuit)

        print(f'Simulating {self.repetitions} repetitions...')
        result = cirq.Simulator().run(program=self.circuit, repetitions=self.repetitions)

        # Collect results.
        a = np.array(result.measurements['a'][:, 0])
        b = np.array(result.measurements['b'][:, 0])
        x = np.array(result.measurements['x'][:, 0])
        y = np.array(result.measurements['y'][:, 0])
        outcomes = a ^ b == x & y
        win_percent = len([e for e in outcomes if e]) * 100 / self.repetitions

        # Print data.
        print('Results')
        print('a:', bitstring(a))
        print('b:', bitstring(b))
        print('x:', bitstring(x))
        print('y:', bitstring(y))
        print('(a XOR b) == (x AND y):\n  ', bitstring(outcomes))
        print(f'Win rate: {win_percent}%')


def main():
    belltest = CHSHBell()
    belltest.run_classical_bell_test()
    belltest.run_quantum_bell_test()


if __name__ == '__main__':
    main()
