---
name: Benchmark proposal
about: Propose a synthetic benchmark for Physical AI decision-layer research
title: "[Benchmark] "
labels: benchmark, synthetic data, feedback wanted
assignees: ""
---

## Benchmark idea

What synthetic benchmark are you proposing?

```text
[Write here]
```

Examples:

- toy process-window recommendation
- sparse-data regression with physics priors
- uncertainty-aware decision support
- synthetic process-structure-property mapping
- next-experiment selection
- noisy feedback-loop simulation

---

## Decision problem

What manufacturing decision should this benchmark represent?

```text
[Write here]
```

Examples:

- Which process setting should be tried next?
- Which region is feasible?
- Which setting is too risky?
- Which experiment reduces uncertainty?
- Which candidate should be inspected first?

---

## Inputs

What synthetic inputs should the benchmark include?

| Input | Type | Description |
|---|---|---|
| Example: `x1` | Numeric | Controllable process setting |
| Example: `x2` | Numeric | Controllable process setting |
| Example: `material_class` | Categorical | Simplified material descriptor |

---

## Outputs

What outputs should the benchmark generate?

| Output | Type | Description |
|---|---|---|
| Example: `y` | Numeric | Synthetic process outcome |
| Example: `feasible` | Binary | Whether the setting satisfies constraints |
| Example: `risk` | Numeric | Synthetic risk score |

---

## Constraints

What constraints should the benchmark include?

```text
[Write here]
```

Examples:

- feasible operating ranges
- target outcome range
- risk threshold
- measurement noise
- equipment limit
- process instability region
- sparse observation setting

---

## Physics-inspired structure

Should the benchmark include any simple physics-inspired structure?

```text
[Write here]
```

Examples:

- monotonic trend
- nonlinear response surface
- feasible window
- threshold behavior
- coupled variables
- sparse-data prior
- known constraint boundary

---

## Uncertainty

How should uncertainty appear in the benchmark?

```text
[Write here]
```

Examples:

- measurement noise
- process noise
- sparse observations
- uncertain feasible boundary
- high-risk region
- delayed feedback

---

## Suggested evaluation metrics

What should be measured?

```text
[Write here]
```

Possible metrics:

- prediction error
- feasible recommendation rate
- target-window hit rate
- false-safe rate
- false-reject rate
- number of experiments needed
- regret relative to best known setting
- uncertainty calibration
- decision quality under sparse data

---

## Baselines

What simple baselines should be included?

```text
[Write here]
```

Examples:

- random search
- grid search
- simple regression
- uncertainty-aware regression
- physics-inspired prior
- constrained optimization over predicted outcomes

---

## Why this benchmark is useful

How would this benchmark help the community study Physical AI, decision layers, or programmable manufacturing?

```text
[Write here]
```

---

## Public-safety check

Please confirm:

- [ ] This benchmark is synthetic.
- [ ] It does not use private production data.
- [ ] It does not include confidential customer or partner information.
- [ ] It does not include sensitive process parameters.
- [ ] It is safe to share publicly.

---

## Related artifacts

This proposal may relate to:

```text
benchmarks/toy-process-window/README.md
docs/physical-ai-stack.md
docs/decision-layer-primer.md
templates/process-mapping-template.md
```
