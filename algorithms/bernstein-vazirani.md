---
description: Supercharging Deutsch-like algorithms
---

# Bernstein-Vazirani

{% hint style="info" %}
Code : [Cirq](../code/cirq/bernstein-vazirani.md)
{% endhint %}

The Bernstein-Vazirani (BV) algorithm can be considered an extension of the [Deutsch ](deutsch.md)algorithm, and is in some ways even simpler to implement. However, the output of the BV algorithm is much more useful in practical applications and therefore important to understand.

### Objective

Similar to [Deutsch ](deutsch.md)algorithm, we have a oracle that implements a black box function f that maps $$\{X_k\} \rightarrow \{0,1\}$$, where $$X_k = x_{k1}...x_{kn}$$ is a bitstring of length n i.e. $$x_{ki} \in \{0,1\}$$

We know more about the function now, we know that $$f(X) = s \cdot X \mod 2$$, where s is a unknown bitstring. We want to find s.&#x20;

### Classical protocol

The only way to identify s with classical bit is to **query the oracle n times**, with n different inputs. The simplest set of such inputs is$$\{100...0 | 010...0 | 001...0| ... | 000...1\}$$.

### Quantum protocol​

Using quantum interference and phase kickback, we can solve this problem exactly using **just 1 query to the oracle**.&#x20;

1. Prepare n input qubits in $$|\psi\rangle_{in} =|000...0 \rangle$$state. Prepare the output qubit in $$|-\rangle$$state.
2. Apply Hadamard gates to all input qubits. This create a equiprobable superposition of all possible input combinations, i.e. $$|\psi\rangle = \sum |X_i\rangle$$ up to some normalization constant.
3. Query the oracle with input qubits. The oracle effectively acts on all possible input combinations at the same time.
4. The trick is how the oracle writes the result of its calculation : using a CNOT on the output qubit. Just like in the Deutsch algorithm, this kicks out the results of the computation and stores it in the phase of the input state. $$|\psi\rangle_{in} = \sum (-1)^{s.X_k}|X_k\rangle$$
5. Apply Hadamard gates to the input qubits. This destructively interferes for all $$X_k$$, except when $$X_k==s$$. therefore now $$|\psi\rangle_{in}=|s\rangle$$.
6. Measure all input qubits, the result is the bitsting s.

### Expectation vs Reality

The key difference between Deutsch and BV algorithms is that we have reduced our undefined function to a well defined function of an unknown bitstring s. While this reduces the space of functions, it makes the algorithm much more powerful in this restricted space.

> The algorithm works for **any length of string s**, which means in principle we can read any s, (even say millions of bits long), with just 1 single query to the function.

However it suffers from the same problem as Deutsch, does such a specific problem ever arise in practice for us to solve?&#x20;
