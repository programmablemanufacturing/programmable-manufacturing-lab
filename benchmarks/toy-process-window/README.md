# Toy Process-Window Benchmark

A synthetic benchmark for exploring process-window recommendation under constraints.

This benchmark is designed as a public, educational example for Physical AI decision-layer research. It does not represent any specific production process. The goal is to study how data, physics-inspired structure, uncertainty, and constraints can be combined to recommend better manufacturing decisions.

---

## Motivation

Many manufacturing problems are not just prediction problems.

In practice, engineers often need to answer questions such as:

- Which settings are likely to produce an acceptable outcome?
- Which region of the process space is feasible?
- Which next experiment should be run?
- Which settings are too risky to try?
- How should uncertainty affect the recommendation?

This benchmark focuses on the decision problem behind those questions.

Instead of asking only:

```text
Can we predict the output?
```

the benchmark asks:

```text
Can we recommend a useful process window under uncertainty and constraints?
```

---

## Concept

The benchmark represents a simplified manufacturing process with:

- controllable input variables
- synthetic process constraints
- a target outcome region
- noisy measurements
- feasible and infeasible process regions
- an objective for recommending process settings

The process is intentionally synthetic. It is meant to be simple enough for learning, testing, and discussion.

---

## Example setup

A toy process may include two controllable variables:

```text
x1 = process setting 1
x2 = process setting 2
```

The synthetic process generates an outcome:

```text
y = process outcome
```

The goal is to find a region of `(x1, x2)` where the outcome is likely to satisfy a target condition:

```text
target_low <= y <= target_high
```

while respecting constraints such as:

```text
x1_min <= x1 <= x1_max
x2_min <= x2 <= x2_max
risk(x1, x2) <= threshold
```

---

## Candidate tasks

This benchmark can support several simple tasks:

### 1. Forward prediction

Predict the process outcome from controllable inputs.

```text
inputs: x1, x2
output: predicted y
```

### 2. Feasibility classification

Classify whether a process setting is likely to be feasible.

```text
inputs: x1, x2
output: feasible / infeasible
```

### 3. Process-window recommendation

Recommend settings that are likely to satisfy the target outcome and constraints.

```text
inputs: candidate settings
output: recommended process window
```

### 4. Uncertainty-aware decision support

Recommend settings while accounting for uncertainty.

```text
inputs: predicted outcome + uncertainty
output: safe / uncertain / high-risk regions
```

### 5. Next-experiment selection

Suggest the next setting to test in order to improve the process map.

```text
inputs: current observations
output: next experiment
```

---

## Why this is useful

This toy benchmark can help explore questions such as:

- When does a physics-inspired prior help under sparse data?
- How much data is needed before recommendations become useful?
- How should uncertainty change the recommended process window?
- How should constraints be represented?
- How should decision quality be evaluated?
- When does a model have good prediction accuracy but poor decision usefulness?

---

## Suggested synthetic variables

A simple version may include:

| Variable | Type | Description |
|---|---|---|
| `x1` | Numeric | Controllable process setting |
| `x2` | Numeric | Controllable process setting |
| `y` | Numeric | Synthetic process outcome |
| `noise` | Numeric | Measurement or process noise |
| `feasible` | Binary | Whether the setting satisfies constraints |
| `risk` | Numeric | Synthetic risk score |
| `recommended` | Binary | Whether the setting is recommended |

---

## Suggested evaluation metrics

Possible metrics include:

### Prediction metrics

- mean absolute error
- root mean squared error
- calibration error

### Decision metrics

- feasible recommendation rate
- target-window hit rate
- false-safe rate
- false-reject rate
- number of experiments needed to find a feasible window
- regret relative to best known feasible setting

### Uncertainty metrics

- coverage of uncertainty intervals
- risk-aware recommendation quality
- rate of recommendations in high-uncertainty regions

---

## Baseline methods

Possible baselines:

- random search
- grid search
- simple regression model
- uncertainty-aware regression model
- physics-inspired synthetic prior
- constrained optimization over predicted outcomes

The goal is not to create a complex benchmark at first. The goal is to create a simple public example where decision-layer ideas can be tested.

---

## Decision-layer framing

A useful model should not only predict `y`.

It should help answer:

```text
What should the engineer try next?
```

or:

```text
Which settings are likely to be safe, feasible, and useful?
```

This benchmark is therefore focused on the path from prediction to decision.

```text
candidate settings
        ↓
prediction + uncertainty
        ↓
constraint check
        ↓
recommended process window
        ↓
synthetic feedback
```

---

## Planned files

Future versions may include:

```text
benchmarks/toy-process-window/
│
├── README.md
├── data/
│   └── synthetic_process_window.csv
│
├── notebooks/
│   └── toy_process_window_demo.ipynb
│
└── src/
    └── generate_synthetic_data.py
```

These files are planned placeholders. The first version of this benchmark begins with the design document.

---

## Open questions

Community feedback is welcome on:

- what variables should be included
- how constraints should be represented
- how uncertainty should be measured
- what metrics best capture decision quality
- how to keep the benchmark simple but meaningful
- what baseline methods should be included first

---

## Contribution ideas

Good first contributions:

- suggest a synthetic process function
- propose a decision-quality metric
- add a simple baseline method
- create a small synthetic dataset
- propose a visualization for process windows
- improve the benchmark framing
- connect this benchmark to the readiness scorecard or process-mapping template

---

## Status

Status: design placeholder.

The next step is to create a small synthetic dataset and a minimal notebook that demonstrates:

1. generating candidate process settings
2. predicting synthetic outcomes
3. identifying feasible regions
4. recommending a process window
5. visualizing uncertainty
