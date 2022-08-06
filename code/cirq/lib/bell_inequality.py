# pylint: disable=wrong-or-nonexistent-copyright-notice
import numpy as np
import cirq


def bitstring(bits):
    return ''.join('1' if e else '_' for e in bits)


class CHSHBell(object):

    def __init__(self, repetitions=1):
        super().__init__()
        self.repetitions = repetitions
    
    def setup(self):
        self.alice_recv = cirq.GridQubit(0, 0)
        self.bob_recv = cirq.GridQubit(1, 0)
        self.alice_retn = cirq.GridQubit(0, 1)
        self.bob_retn = cirq.GridQubit(1, 1)

    def make_bell_test_circuit(self):
        self.setup()
        circuit = cirq.Circuit()

        # Prepare shared entangled state.
        circuit.append([cirq.H(self.alice_recv), cirq.CNOT(self.alice_recv, self.bob_recv)])

        # Referees flip coins.
        circuit.append([cirq.H(self.alice_retn), cirq.H(self.bob_retn)])

        # Players do a sqrt(X) based on their referee's coin.
        circuit.append(
            [cirq.X(self.alice_recv) ** -0.25,
             cirq.CNOT(self.alice_retn, self.alice_recv) ** 0.5,
             cirq.CNOT(self.bob_retn, self.bob_recv) ** 0.5]
        )

        # Then results are recorded.
        circuit.append(
            [
                cirq.measure(self.alice_recv, key='a'),
                cirq.measure(self.alice_recv, key='b'),
                cirq.measure(self.alice_retn, key='x'),
                cirq.measure(self.bob_retn, key='y'),
            ]
        )
        return circuit

    def run_classical_bell_test(self):
        self.setup()
        circuit = cirq.Circuit()
        circuit.append(cirq.CNOT(self.alice_retn, self.alice_recv))
        circuit.append(cirq.CNOT(self.bob_retn, self.bob_recv))

        print('Circuit:')
        print(circuit)

        repetitions = 75
        print(f'Simulating {repetitions} repetitions...')
        result = cirq.Simulator().run(program=circuit, repetitions=self.repetitions)

        # Collect results.
        a = np.array(result.measurements['a'][:, 0])
        b = np.array(result.measurements['b'][:, 0])
        x = np.array(result.measurements['x'][:, 0])
        y = np.array(result.measurements['y'][:, 0])
        outcomes = a ^ b == x & y
        win_percent = len([e for e in outcomes if e]) * 100 / self.repetitions

        # Print data.
        print('Classical best case results')
        print('a:', bitstring(a))
        print('b:', bitstring(b))
        print('x:', bitstring(x))
        print('y:', bitstring(y))
        print('(a XOR b) == (x AND y):\n  ', bitstring(outcomes))
        print(f'Win rate: {win_percent}%')


    def run_quantum_bell_test(self):
        self.circuit = self.make_bell_test_circuit()
        print('Circuit:')
        print(self.circuit)

        repetitions = 75
        print(f'Simulating {repetitions} repetitions...')
        result = cirq.Simulator().run(program=self.circuit, repetitions=self.repetitions)

        # Collect results.
        a = np.array(result.measurements['a'][:, 0])
        b = np.array(result.measurements['b'][:, 0])
        x = np.array(result.measurements['x'][:, 0])
        y = np.array(result.measurements['y'][:, 0])
        outcomes = a ^ b == x & y
        win_percent = len([e for e in outcomes if e]) * 100 / repetitions

        # Print data.
        print('Quantum best case results')
        print('a:', bitstring(a))
        print('b:', bitstring(b))
        print('x:', bitstring(x))
        print('y:', bitstring(y))
        print('(a XOR b) == (x AND y):\n  ', bitstring(outcomes))
        print(f'Win rate: {win_percent}%')


def main():
    belltest = CHSHBell()
    belltest.run_bell_test()
    # # Create circuit.
    # circuit = make_bell_test_circuit()
    # print('Circuit:')
    # print(circuit)

    # # Run simulations.
    # print()
    # repetitions = 75
    # print(f'Simulating {repetitions} repetitions...')
    # result = cirq.Simulator().run(program=circuit, repetitions=repetitions)

    # # Collect results.
    # a = np.array(result.measurements['a'][:, 0])
    # b = np.array(result.measurements['b'][:, 0])
    # x = np.array(result.measurements['x'][:, 0])
    # y = np.array(result.measurements['y'][:, 0])
    # outcomes = a ^ b == x & y
    # win_percent = len([e for e in outcomes if e]) * 100 / repetitions

    # # Print data.
    # print()
    # print('Results')
    # print('a:', bitstring(a))
    # print('b:', bitstring(b))
    # print('x:', bitstring(x))
    # print('y:', bitstring(y))
    # print('(a XOR b) == (x AND y):\n  ', bitstring(outcomes))
    # print(f'Win rate: {win_percent}%')






if __name__ == '__main__':
    main()
