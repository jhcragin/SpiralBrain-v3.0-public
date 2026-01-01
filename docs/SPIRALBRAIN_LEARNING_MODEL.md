# SpiralBrain v3.0 — What "Learning" Means (and Does *Not* Mean)

## Purpose of This Document

This document defines **exactly what learning is and is not in SpiralBrain v3.0**. Its goal is to prevent misinterpretation, over-claiming, or category errors when comparing SpiralBrain to traditional AI systems.

SpiralBrain deliberately **does not implement learning in the conventional AI sense**. At the same time, it **does support discovery, adaptation, and improvement at the level of the experimental process**. This distinction is foundational to the project.

---

## Executive Summary

**SpiralBrain v3.0 does not learn.**

* No training phase
* No dataset-driven optimization
* No reinforcement learning
* No gradient descent
* No persistent memory across runs
* No accumulated experience inside the brain

Instead:

* SpiralBrain exhibits **within-run regulatory adaptation**
* Behavioral variation arises from **architecture, constraints, and dynamics**
* **Learning occurs externally**, in the *research loop* that observes the brain
* Each brain instantiation begins from a **clean initial state**

SpiralBrain is best understood as a **learnable object**, not a learning system.

---

## Why the Word "Learning" Is Dangerous

In AI research, *learning* usually implies at least one of the following:

1. **Parameter optimization** (e.g., gradient descent, RL updates)
2. **Experience accumulation** that influences future behavior
3. **Persistent memory** that alters future runs
4. **Improvement over time due to stored internal state**

SpiralBrain implements **none** of these.

Using the word "learning" without qualification invites incorrect assumptions about memory, training data, and optimization mechanisms that do not exist in SpiralBrain.

---

## What SpiralBrain Does *Within a Single Run*

During a single execution, SpiralBrain:

* Processes inputs through a unified, multi-lobe architecture
* Monitors internal state variables (coherence, drift, hazard, stability)
* Regulates behavior through homeostasis and affective control
* Adjusts pathway activation *transiently* in response to conditions
* Recovers elastically after perturbation

These changes are:

* **Ephemeral**
* **Bounded**
* **Non-persistent**

When the run ends, all internal state is discarded.

This is **within-run regulation**, not learning.

---

## What SpiralBrain Does *Not* Do Across Runs

Across runs, SpiralBrain:

* Does **not** retain memory
* Does **not** ingest prior logs or results
* Does **not** modify parameters based on outcomes
* Does **not** improve performance due to prior executions

Every run is a **fresh instantiation** of the same cognitive organism.

Any difference in outcomes between runs arises from:

* Different inputs
* Different experimental conditions
* Different perturbations

—not from accumulated experience.

---

## Where "Learning" Actually Occurs

Learning occurs **outside the brain**, in the **experimental loop**.

The full loop is:

1. SpiralBrain executes a task
2. Internal state is measured and logged (JSON, telemetry)
3. Researchers analyze results
4. Experimental design is refined
5. SpiralBrain is run again from a clean state

This is analogous to:

* Physics experiments
* Biological assays
* Control systems research

The *organism does not learn*; **the scientist learns**.

---

## Self-Observation vs. Self-Modification

SpiralBrain supports **observability without interference**:

* Internal state can be inspected in real time
* Monitoring does not alter cognitive behavior
* No feedback channel feeds observations back into control logic

Crucially:

* SpiralBrain does **not** read its own logs
* SpiralBrain does **not** interpret prior results
* SpiralBrain does **not** adjust itself based on past performance

Observation is external and non-actuating.

---

## Plasticity in SpiralBrain (Clarification)

SpiralBrain documentation may reference:

* Synaptic plasticity
* Homeostatic plasticity
* Metaplasticity
* Structural plasticity

These terms refer to:

* **Regulatory elasticity**
* **Control-law modulation**
* **Transient reconfiguration**

They **do not** refer to:

* Learned representations
* Stored knowledge
* Persistent parameter updates

Plasticity in SpiralBrain is **bounded regulation**, not learning.

---

## Correct Terminology

Preferred terms:

* *Regulatory adaptation*
* *Within-run adaptation*
* *Elastic regulation*
* *Architectural emergence*
* *Experimental learning (external)*

Terms to avoid without qualification:

* Learning
* Training
* Self-learning
* Experience accumulation

---

## Canonical Statement (Use This)

> **SpiralBrain v3.0 does not perform learning in the traditional AI sense.**
> It performs regulated cognition under observation, while learning occurs in the experimental process that studies it. Each brain instantiation begins from a clean initial state, with no memory, no training, and no persistent parameter change. Behavioral variation arises from architectural dynamics and constraint-driven regulation, not from accumulated experience.

---

## Why This Matters

This separation:

* Preserves scientific integrity
* Prevents anthropomorphic misinterpretation
* Enables falsifiable experimentation
* Distinguishes SpiralBrain from learning-based AI systems
* Positions SpiralBrain as a **research instrument**, not a product model

SpiralBrain's contribution is not that it learns —

**It shows what cognition looks like *without* learning.**

---

## Summary

* SpiralBrain does not learn
* SpiralBrain adapts transiently
* The research loop learns
* The organism remains uncontaminated
* Every run starts clean

This distinction is fundamental to SpiralBrain's identity and scientific value.</content>
<parameter name="filePath">c:\Users\johnc\source\repos\SpiralBrain-v3.0\docs\LEARNING_DEFINITION.md