# Manufacturing Process Mapping Template

A lightweight template for translating a manufacturing problem into a structured decision problem.

This template is designed for early scoping. It helps clarify whether an AI-assisted workflow has a real operational anchor: a clear bottleneck, measurable inputs and outputs, controllable variables, a decision point, and a feedback loop.

The goal is not to describe a full production system. The goal is to create a shared structure for discussing manufacturing AI opportunities in a safe, generalized, and practical way.

---

## 1. Use case summary

### Use case name

```text
Example: Reducing defect risk in a high-value manufacturing process
```

### Manufacturing context

Briefly describe the process area.

```text
Example: A process where engineers adjust operating conditions to improve quality, yield, or consistency.
```

### Current pain point

What problem is the team trying to improve?

```text
Example: The team sees recurring defects, but the relationship between process conditions and final outcomes is not fully clear.
```

### Why this matters

What is the operational or economic impact?

```text
Example: Each iteration requires engineering time, machine time, inspection, and delayed qualification.
```

---

## 2. Operational bottleneck

What is the specific bottleneck?

Avoid vague descriptions such as:

```text
Improve quality
Use AI
Reduce cost
Optimize manufacturing
```

Prefer operational descriptions such as:

```text
Reduce the number of trial builds needed to identify a feasible process window.
```

or:

```text
Predict whether a process setting is likely to produce an acceptable outcome before running a full experiment.
```

### Bottleneck description

```text
[Write here]
```

### Where does it occur?

```text
[Process step, machine, material family, part family, inspection stage, or workflow stage]
```

### When does it occur?

```text
[During setup, production, qualification, inspection, parameter tuning, etc.]
```

### Under what conditions does it occur?

```text
[Known operating regimes, material conditions, equipment states, environmental factors, or product variants]
```

---

## 3. Inputs

What information is available before the decision is made?

Inputs may include controllable variables, observed process states, material descriptors, machine settings, environmental information, or historical context.

| Input | Type | Controllable? | Available before decision? | Notes |
|---|---|---|---|---|
| Example: process setting A | Numeric | Yes | Yes | Adjustable within a feasible range |
| Example: material condition | Categorical / numeric | No | Yes | Known before processing |
| Example: sensor signal | Time-series | No | Sometimes | May require preprocessing |

### Input notes

```text
[Write here]
```

---

## 4. Outputs

What result is the team trying to predict, improve, or control?

Outputs should be measurable.

| Output | Type | Measurement method | Timing | Notes |
|---|---|---|---|---|
| Example: defect indicator | Binary / categorical | Inspection | After process | Used to evaluate outcome |
| Example: property value | Numeric | Testing | After process | May be slow or expensive |
| Example: yield | Percentage | Production data | Batch-level | May depend on multiple factors |

### Output notes

```text
[Write here]
```

---

## 5. Process states

What intermediate states can be observed during or after the process?

These may help connect inputs to outputs.

Examples:

- temperature-related signals
- force, vibration, acoustic, or imaging signals
- machine state
- material state
- inspection features
- operator notes
- environmental conditions
- batch or lot information

| Process state | Observable? | Measurement type | Linked to outcome? | Notes |
|---|---|---|---|---|
| Example: in-process signal | Yes | Sensor / image / time-series | Partially | Needs alignment with outcome |
| Example: machine state | Yes | Log data | Unknown | May help explain variation |

### Process-state notes

```text
[Write here]
```

---

## 6. Controllable variables

What can engineers or operators actually change?

A good AI-assisted workflow needs control levers. Prediction is useful only if it can change a decision.

| Variable | Adjustable by whom? | Adjustment frequency | Feasible range | Constraints |
|---|---|---|---|---|
| Example: setting A | Engineer | Per run | Low / medium / high | Equipment limits |
| Example: setting B | Operator | During setup | Defined range | Quality / safety constraints |

### Control notes

```text
[Write here]
```

---

## 7. Decision point

What decision would change if prediction improved?

This is the most important section.

A model output is only useful if it changes a real decision.

### Decision owner

```text
[Engineer, operator, quality team, process owner, manufacturing lead, etc.]
```

### Decision timing

```text
[Before run, during setup, during process, after inspection, before qualification, etc.]
```

### Current decision method

```text
[Expert judgment, manual trial-and-error, historical settings, simulation, rule of thumb, etc.]
```

### AI-assisted decision

What would the system recommend?

```text
[Recommended process window, risk estimate, next experiment, accept/reject guidance, inspection priority, etc.]
```

### Action if recommendation is trusted

What would the team do differently?

```text
[Change setting, avoid region, run fewer trials, inspect differently, prioritize experiment, update process plan, etc.]
```

---

## 8. Feedback loop

How does the result of the decision return to improve future decisions?

| Feedback item | How measured? | How soon available? | Linked to decision? | Notes |
|---|---|---|---|---|
| Example: final outcome | Testing / inspection | Hours / days / weeks | Yes / partially | Used to evaluate recommendation |
| Example: operator note | Manual entry | Same day | Sometimes | May need structure |
| Example: process log | Machine data | Immediate | Yes | Requires alignment |

### Feedback-loop notes

```text
[Write here]
```

---

## 9. Readiness check

Use this section to connect the process map to the Manufacturing AI Readiness Scorecard.

| Dimension | Low / medium / high | Notes |
|---|---|---|
| Problem clarity |  |  |
| Measurability |  |  |
| Process stability |  |  |
| Controllability |  |  |
| Decision relevance |  |  |
| Feedback loop |  |  |

### Overall readiness

```text
Not ready / early structure / almost ready / pilot ready
```

### Main blocker

```text
[What needs to be clarified before an AI-assisted pilot makes sense?]
```

---

## 10. Candidate AI task

What kind of AI-assisted task might fit this process?

Possible categories:

- prediction
- classification
- anomaly detection
- process-window recommendation
- inverse design
- risk scoring
- experiment prioritization
- operator decision support
- uncertainty-aware recommendation

### Candidate task

```text
[Write here]
```

### Why this task fits

```text
[Write here]
```

### Why this task may not fit yet

```text
[Write here]
```

---

## 11. Minimal useful pilot

What is the smallest pilot that could create learning?

A good pilot should be narrow, measurable, and connected to a real decision.

### Pilot question

```text
Can better prediction or recommendation improve [specific decision] for [specific process context]?
```

### Pilot input

```text
[What data or process information is needed?]
```

### Pilot output

```text
[What recommendation, prediction, or decision support is produced?]
```

### Success metric

```text
[What would count as useful improvement?]
```

Examples:

- fewer experimental iterations
- faster process-window identification
- better defect-risk ranking
- improved yield
- reduced inspection burden
- clearer decision confidence
- better transfer across similar runs

---

## 12. Risks and assumptions

List the main assumptions that would need to be tested.

| Assumption | Risk if false | How to test |
|---|---|---|
| Example: process data is comparable across runs | Model may learn noise | Check run-to-run consistency |
| Example: output measurement is reliable | Feedback may be misleading | Compare measurement repeatability |
| Example: recommendation can change action | Model may not create value | Interview decision owner |

---

## 13. Open questions

Use this section to capture unresolved questions.

```text
1.
2.
3.
```

---

## 14. Suggested next step

Choose one.

```text
[ ] Clarify the operational bottleneck
[ ] Improve data structure
[ ] Define the decision point
[ ] Validate measurement consistency
[ ] Identify controllable variables
[ ] Build a synthetic/toy version
[ ] Run a lightweight diagnostic study
[ ] Scope a pilot
```

---

## Community feedback wanted

This template is intended to evolve.

Useful feedback includes:

- missing process-mapping fields
- better examples from specific manufacturing domains
- ways to simplify the template
- examples where the decision point was unclear
- examples where the feedback loop was the real bottleneck
- suggestions for mapping different process types, such as discrete, batch, continuous, or inspection-heavy workflows
