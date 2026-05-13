# Manufacturing AI Pilot Definition Template

A lightweight template for defining a focused AI-assisted manufacturing pilot.

This template is designed to help translate a broad manufacturing opportunity into a narrow, measurable, decision-focused pilot.

A good pilot should not start with “we want to use AI.”  
A good pilot should start with a specific operational decision that could improve if better prediction, recommendation, or uncertainty awareness were available.

---

## 1. Pilot summary

### Pilot name

```text
Example: Process-window recommendation for reducing trial iterations
```

### Manufacturing context

```text
[Briefly describe the process area, material family, machine type, workflow, or production context.]
```

### Core pilot question

```text
Can better prediction or recommendation improve [specific decision] for [specific process context]?
```

Example:

```text
Can better prediction reduce the number of experimental iterations needed to identify a feasible process window?
```

---

## 2. Operational bottleneck

What specific bottleneck is the pilot trying to address?

Avoid broad descriptions such as:

```text
Improve quality
Use AI
Optimize production
Reduce cost
```

Prefer narrow operational descriptions such as:

```text
Reduce trial-and-error iterations when selecting process settings for a new material or part family.
```

### Bottleneck

```text
[Write here]
```

### Current baseline

What happens today?

```text
[Current workflow, number of trials, time required, cost, defect rate, yield, or decision method.]
```

### Why now?

Why is this bottleneck worth addressing now?

```text
[Business need, qualification pressure, production scale-up, recurring defects, high experiment cost, etc.]
```

---

## 3. Decision to improve

A pilot is useful only if it can change a real decision.

### Decision owner

```text
[Engineer, operator, process owner, quality team, manufacturing lead, etc.]
```

### Decision timing

```text
[Before run, during setup, during process, after inspection, before qualification, etc.]
```

### Current decision method

```text
[Expert judgment, manual trial-and-error, historical setting, simulation, rule of thumb, etc.]
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

## 4. Pilot input

What information is available before the decision?

| Input | Type | Source | Available when? | Notes |
|---|---|---|---|---|
| Example: process setting A | Numeric | Machine / engineer | Before run | Controllable |
| Example: material descriptor | Numeric / categorical | Material record | Before run | May vary by batch |
| Example: process signal | Time-series / image | Sensor / monitoring | During process | May require preprocessing |

### Input notes

```text
[Write here]
```

---

## 5. Pilot output

What should the pilot produce?

Possible outputs:

- predicted outcome
- feasible / infeasible classification
- defect-risk score
- recommended process window
- next experiment recommendation
- uncertainty estimate
- decision table
- operator or engineer guidance

### Expected output

```text
[Write here]
```

### Output format

```text
[Dashboard, table, report, notebook, API output, recommendation list, process map, etc.]
```

### How the output will be used

```text
[Describe how the output connects to the real manufacturing decision.]
```

---

## 6. Success metric

What would count as a useful pilot result?

A success metric should be measurable and connected to the bottleneck.

Possible success metrics:

- fewer experimental iterations
- faster process-window identification
- improved yield
- reduced defect-risk region
- better ranking of candidate settings
- reduced inspection burden
- improved confidence in decision-making
- clearer go / no-go decision
- better transfer across similar runs

### Primary success metric

```text
[Write here]
```

### Secondary success metrics

```text
1.
2.
3.
```

### Minimum useful result

What is the smallest result that would still make the pilot valuable?

```text
[Write here]
```

---

## 7. Data and feedback

What data is needed, and how will the result be evaluated?

### Historical data available

```text
[Describe what historical data exists, if any.]
```

### New data needed

```text
[Describe what new measurements, tests, or runs may be needed.]
```

### Feedback signal

How will the pilot know whether a recommendation was good?

```text
[Inspection result, test result, yield, defect indicator, process signal, engineer review, etc.]
```

### Feedback timing

```text
[Immediate, hours, days, weeks, months.]
```

### Link between decision and outcome

Can the outcome be connected back to the recommendation?

```text
[Yes / partially / no / unknown. Explain briefly.]
```

---

## 8. Scope

A good pilot should be narrow.

### In scope

```text
[Specific process, material, machine, product family, decision type, or data source.]
```

### Out of scope

```text
[What this pilot will not attempt to solve.]
```

Examples of useful boundaries:

- one material family
- one machine type
- one process step
- one quality outcome
- one decision point
- one data stream
- one engineering workflow

---

## 9. Assumptions

List the assumptions behind the pilot.

| Assumption | Why it matters | How to test |
|---|---|---|
| Example: output measurements are reliable | Bad labels weaken feedback | Compare repeated measurements |
| Example: controllable variables can be changed | Recommendation must be actionable | Confirm with process owner |
| Example: process data is comparable across runs | Model needs consistent patterns | Check run-to-run structure |

---

## 10. Risks

What could make the pilot fail?

Possible risks:

- problem is not clearly defined
- data is inconsistent
- process is unstable
- output measurement is unreliable
- no controllable variables
- recommendation cannot change action
- feedback is too slow
- decision owner is unclear
- pilot scope is too broad
- success metric is not measurable

### Main risks

```text
1.
2.
3.
```

### Risk mitigation

```text
[How can these risks be reduced before or during the pilot?]
```

---

## 11. Readiness check

Use the Manufacturing AI Readiness Scorecard before starting the pilot.

| Dimension | Score 0–3 | Notes |
|---|---:|---|
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
[What must be clarified before the pilot can create value?]
```

---

## 12. Pilot plan

### Phase 1: Define

```text
[Clarify bottleneck, decision owner, inputs, outputs, and success metric.]
```

### Phase 2: Prepare

```text
[Organize data, define synthetic or historical baseline, align measurements.]
```

### Phase 3: Model / analyze

```text
[Build baseline prediction, risk score, recommendation logic, or process map.]
```

### Phase 4: Evaluate

```text
[Compare recommendation against outcome, historical baseline, or expert judgment.]
```

### Phase 5: Decide next step

```text
[Stop, refine, expand, collect more data, or scope deployment.]
```

---

## 13. Minimal pilot artifact

What should be produced at the end of the pilot?

Possible artifacts:

- pilot report
- process map
- readiness assessment
- baseline model
- synthetic benchmark
- recommendation table
- uncertainty visualization
- decision workflow proposal
- next-experiment plan

### Final artifact

```text
[Write here]
```

---

## 14. Expansion path

If the pilot works, what comes next?

Possible expansion paths:

- expand to more process settings
- expand to more materials
- expand to more machines
- connect to live data
- add uncertainty-aware recommendations
- build operator-facing workflow
- create repeatable deployment template
- convert pilot into production decision support

### Next expansion step

```text
[Write here]
```

---

## 15. Open questions

```text
1.
2.
3.
```

---

## Suggested use

This template works best when used together with:

```text
templates/readiness-scorecard.md
templates/process-mapping-template.md
```

Recommended sequence:

```text
1. Use the readiness scorecard to assess whether the process is ready.
2. Use the process-mapping template to structure the manufacturing problem.
3. Use this pilot-definition template to scope the smallest useful pilot.
```

---

## Community feedback wanted

This template is intentionally lightweight and evolving.

Useful feedback includes:

- missing pilot-definition fields
- better success metrics
- examples from different manufacturing domains
- warning signs that a pilot is too broad
- ways to define a minimum useful result
- examples where the decision point was unclear
- examples where feedback timing made the pilot difficult
