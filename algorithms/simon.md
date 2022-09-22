---
description: First demonstration of exponential speedup
---

# Simon

Simon's algorithm is the first real demonstration of quantum algorithms providing an exponential speedup over classical algorithm. Both [Deutsch](deutsch.md) and [Bernstein-Vazirani](bernstein-vazirani.md) algorithms that we have seen so far provide a linear speedup over classical algorithms going from O(n) to O(1).

### Objective

We are given an unknown function _f_, which is guaranteed to be map exactly two inputs to every unique output, using a hidden bitstring, b, such that :

$$f(x_1)=f(x_2) \hspace{5mm} \text{if}  \hspace{2mm}  x_1 \oplus x_2 = b$$​

So we want to identify b.

### Classical protocol

In the worst case, we have to query the function with $$2^{n-1} +1$$ different inputs (n is the number of bits in the input) i.e. checking just over half of all the possible inputs until we find two cases of the same output.

### Quantum protocol

The Simon oracle takes as input $$|x\rangle |0\rangle$$​and returns $$|x\rangle|\text{Perm}(x\oplus b)\rangle$$​where Perm is any fixed bitwise permutation. $$\text{Perm}(x\oplus b)$$​has the same value for two values of x that satisfy the [objective condition](simon.md#objective).

1. Prepare 2n qubits in $$|0_n\rangle|0_n\rangle$$, i.e n input and n output qubits.
2. Apply Hadamard gates to all input qubits. This create a equiprobable superposition of all possible input combinations, i.e $$|\psi\rangle = \sum |X_k\rangle$$ up to some normalization constant.
3. Query the oracle with input qubits. The oracle effectively acts on all possible input combinations at the same time. The output is written on the output qubits using CNOT gates.
4. Apply Hadamard gates to the input qubits. This destructively interferes for all input states $$|X_k\rangle$$where $$X_k\oplus s$$ is odd and destructively interferes for all $$|X_k\rangle$$where $$X_k\oplus s$$ is even.
5. Measure all input qubits. The result is one of the possible $$X_k$$ i.e. $$X_k\oplus s=0$$.
6. If we repeat this experiment n times, we get n different values for $$X_k$$. Solve the linear system of equations $$X_{nk}\cdot s = 0$$ to find s.

### Expectation vs Reality

Simon algorithm is very similar to [Bernstein-Vazirani](bernstein-vazirani.md) and [Deutsch](deutsch.md) algorithm. Once again we have simply changed the definition of the oracle function making it much harder to solve.&#x20;

> The classical complexity required goes from O(n) in the BV algorithm to O(2^n) in the Simon problem. In comparison, the quantum complexity goes from O(1) to O(n), making this the first demonstration of a true **exponential** advantage of quantum computers over classical algorithms.

While Deutsch, BV and Simon algorithm's are important form a historical and theoretical perspective, they have little practical utility since each requires the existence of a very contrived oracle function.
