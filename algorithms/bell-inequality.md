---
description: The flagship experiment of quantum physics
---

# Bell Inequality

{% hint style="info" %}
Code: [Cirq](../code/cirq/bell-inequality.md)
{% endhint %}

[Bell's theorem](https://en.wikipedia.org/wiki/Bell's\_theorem) proves that [quantum entanglement](https://en.wikipedia.org/wiki/Quantum\_entanglement) cannot be explained by any [local realist theory](https://en.wikipedia.org/wiki/Principle\_of\_locality#Quantum\_mechanics). Bell inequality has been tested experimentally for more than 50 years and has proven conclusively that reality does not obey local realist classical physics, **reality is quantum**.

There are many ways to setup an experiment that demonstrates Bell Inequality. We will look at one that is close to quantum computing.

### Objective

Victor is the dealer. Every round, Victor sends 1 random qubit to Alice, x, and 1 random qubit to Bob, y. Alice then returns 1 qubit to Victor, a, as does Bob, b. Alice and Bob win the round if logical AND of x, y is the logical XOR of a, b.

$$
x \land b =a \oplus  b
$$

### Prerequisites

* Victor's bits x, y are picked at random.
* Alice and Bob can perform any operations they want on x and y. They could also just have two readymade qubits a and b to send back.
* Before the experiment starts**,** Alice and Bob can agree on their team's strategy. But they cannot communicate during the experiment, e.g. by measuring 1 qubit and then deciding what to do with the other qubit.

### Classical best case

It can be proven that the best classical strategy Alice and Bob can use is "_do nothing, just return 0"_, which has a 75% win rate.

### Run protocol

The best quantum strategy Alice and Bob can use involves the use of quantum entanglement.&#x20;

1. Before the experiment, Alice and Bob create an entangled pair of qubits, a and b. Alice keeps a and Bob keeps b.
2. During the experiment, Alice entangled her received qubit x with a. Bob entangled his received qubit y with b.
3. Alice returns a, x and Bob returns b, y to Victor.
4. Victor measures the quantities $$a \oplus b$$ and $$x \land y$$​.

### Quantum best case

In the quantum protocol, all 4 qubits x, y, a and b are entangled, therefore their measurement results are correlated. Therefore, we find that the best quantum strategy can get a 85.3% win rate.

### Expectation vs Reality

* An individual round results in a binary result, win or loss. The win rate is the probability of winning and requires a large number of rounds to observed in practice.
* In practice, entangled states decohere due to noise. Therefore 85.3% which is the maximum win rate possible is hard to achieve in practice.&#x20;
* Making entangled states in the lab is hard. Bell inequality violation, i.e. achieving an observed win rate > 75%, is used as proof that non-classical, entangled states are being created in the lab.
