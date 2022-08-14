---
description: Simplest demonstration of quantum computation
---

# Deutsch

{% hint style="info" %}
Code : [Cirq](../code/cirq/deutsch.md)
{% endhint %}

[Deutsch's algorithm](https://en.wikipedia.org/wiki/Deutsch%E2%80%93Jozsa\_algorithm) is one of the simplest demonstrations of an **exponential** improvement of quantum computation over classical computation using [superposition](https://en.wikipedia.org/wiki/Quantum\_superposition), [interference](https://en.wikipedia.org/wiki/Wave\_interference#Quantum\_interference) and [phase kickback](deutsch.md#undefined).

### Objective

Consider an unknown function that maps {0, 1} to {0, 1}. We want to know if $$f(0)==f(1)$$ .

### Prerequisites

We have two qubits. We can design a circuit with any gates including a black box oracle gate that implements the unknown function.

### Classical protocol

The only way to get the answer is to measure f(0) and f(1), i.e. **query the oracle twice**.

### Phase kickback

Phase kickback is the workhorse in almost every quantum algorithm.&#x20;

Classical bits can only be flipped, from 0 to 1 and back. Therefore information must be encoded in a series of bits.

Qubits have one additional degree of freedom which is phase. For example, $$Z|1\rangle = -|1\rangle$$. More generally, $$e^{i \theta}|\psi\rangle$$ is phase-shifted away from $$|\psi\rangle$$ by an angle $$\theta$$. Why is this important?

Encoding information in the phase allows us to perform certain computations with exponentially fewer qubits. However, this new kind of information encoding also makes it very difficult and non-intuitive to create new quantum computing algorithms.

### Running the algorithm

To identify if $$f(0)==f(1)$$, we can calculate $$f(0) \oplus f(1)$$. Thanks to quantum superposition, we can do that with just **1 query of the oracle**.

1. Prepare two qubits in the $$|+\rangle_1|-\rangle_2$$​ state.
2.  Apply the oracle such that $$O|+\rangle_1|-\rangle_2 = |+\rangle_1|f(+)\oplus -\rangle_2$$.

    This can be achieved by first applying the secret function $$f$$ on qubit 1 and then a CNOT gate on qubit 2.&#x20;
3. Applying a Hadamard on qubit 1 and rearranging the states the output becomes $$={\frac  {1}{2}}((1+(-1)^{x})|0\rangle_1 +(1-(-1)^{x})|1\rangle_1 )|-\rangle_2$$, where $$x=f(0) \oplus f(1)$$.
4. Measure qubit 1. \
   If $$f(0) \oplus f(1) = 0$$, then $$|1\rangle_1$$ interferes destructively and vanishes and the output is 0. \
   If $$f(0) \oplus f(1)=1$$, then $$|0\rangle_1$$ interferes destructively and vanishes and the output is 1.&#x20;

### Expectation vs Reality

Deutsch algorithm does not have any practical application. The algorithm (and its [extensions](https://en.wikipedia.org/wiki/Deutsch%E2%80%93Jozsa\_algorithm)) uses exponentially fewer queries of the oracle that the classical best case, a huge improvement in principle.

But, in practice, the secret function is fairly contrived and we know of no application where this function is both important and expensive to query.
