# Manufacturing AI Readiness Scorecard

A lightweight framework for evaluating whether a manufacturing process is ready for an AI-assisted pilot.

Many manufacturing AI projects fail before the model itself becomes the bottleneck. The issue is often that the process, data, decision point, or feedback loop is not structured enough for AI to create operational value.

This scorecard is designed to help distinguish between:

- an interesting AI idea
- an almost-ready manufacturing use case
- a pilot-ready manufacturing use case
- a process that needs more operational structuring first

The goal is not to require perfect data or a fully mature digital system. The goal is to determine whether there is enough structure to anchor a focused AI-assisted intervention.

---

## How to use this scorecard

For each dimension, assign a score from 0 to 3.

```text
0 = Not defined
1 = Partially defined
2 = Mostly defined
3 = Pilot ready
```

A process does not need a perfect score to begin exploration. However, a strong pilot usually needs clear evidence across problem clarity, measurability, controllability, and feedback.

---

## Readiness dimensions

### 1. Problem clarity

Can the manufacturing problem be defined in operational terms?

| Score | Description |
|---|---|
| 0 | The problem is described only in vague terms, such as “too much scrap” or “low yield.” |
| 1 | The pain is known, but the location, timing, frequency, or operating conditions are unclear. |
| 2 | The problem is tied to a specific process step, product family, material, machine, or operating regime. |
| 3 | The problem is clearly defined with operational scope, baseline performance, and measurable impact. |

Example questions:

- Where does the problem occur?
- When does it occur?
- Under what process conditions does it occur?
- What is the current baseline?
- What would count as improvement?

---

### 2. Measurability

Are the relevant inputs, outputs, and process states captured consistently enough to compare runs or decisions?

| Score | Description |
|---|---|
| 0 | Data is missing, informal, paper-based, or not linked to process outcomes. |
| 1 | Some data exists, but it is inconsistent, incomplete, or difficult to compare across runs. |
| 2 | Key inputs and outputs are captured with enough consistency to support analysis. |
| 3 | Inputs, outputs, process states, and outcomes are consistently recorded and traceable. |

Example questions:

- What inputs are recorded?
- What outputs are measured?
- Are timestamps, part IDs, machine IDs, or batch IDs available?
- Can two people interpret the same data trail in the same way?
- Can historical decisions be compared against outcomes?

---

### 3. Process stability

Is the process repeatable enough that output changes mean something?

| Score | Description |
|---|---|
| 0 | The process is highly unstable or poorly understood. |
| 1 | Variation exists, but the main sources are not well separated. |
| 2 | The process is repeatable enough that major changes in output can be meaningfully interpreted. |
| 3 | The process has enough stability to support prediction, comparison, and controlled intervention. |

Example questions:

- Are repeated runs comparable?
- Are changes in output caused by known process variables or by uncontrolled noise?
- Is there enough repeatability to evaluate whether a recommendation helped?
- Are there known operating regimes where the process behaves differently?

---

### 4. Controllability

Are there practical levers that engineers or operators can adjust?

| Score | Description |
|---|---|
| 0 | There are no clear controllable variables. |
| 1 | Some variables can be adjusted, but their relationship to outcomes is unclear. |
| 2 | Key controllable variables are known and can be changed within practical limits. |
| 3 | The process has well-defined control levers, constraints, and feasible adjustment ranges. |

Example questions:

- What can be changed?
- Who can change it?
- How often can it be changed?
- What are the safe or feasible operating ranges?
- What constraints must be respected?

---

### 5. Decision relevance

Would a better prediction actually change a real manufacturing decision?

| Score | Description |
|---|---|
| 0 | The model output would be interesting but would not affect action. |
| 1 | A possible decision exists, but it is not yet connected to workflow or ownership. |
| 2 | There is a clear decision point where better prediction could influence action. |
| 3 | The decision, owner, timing, and expected operational impact are clearly defined. |

Example questions:

- What decision would change if prediction improved?
- Who owns that decision?
- When is the decision made?
- What would the system recommend?
- What would engineers or operators do differently?

---

### 6. Feedback loop

Can the result of a decision be observed and used to improve future decisions?

| Score | Description |
|---|---|
| 0 | Outcomes are not measured or not connected to previous decisions. |
| 1 | Outcomes are sometimes observed, but feedback is slow or inconsistent. |
| 2 | Outcomes can be linked back to process conditions and decisions. |
| 3 | There is a repeatable feedback loop from decision to physical outcome to updated knowledge. |

Example questions:

- What happens after a recommendation is used?
- How is the result measured?
- Can the result be connected back to the original inputs and decision?
- How quickly is feedback available?
- Can the feedback improve the next decision?

---

## Scoring guide

| Total score | Interpretation |
|---|---|
| 0–6 | Not ready. The process likely needs operational definition, data structuring, or measurement work first. |
| 7–11 | Early structure. The pain is real, but the use case may need more scoping before an AI pilot. |
| 12–15 | Almost ready. The process has enough structure for focused discovery or a lightweight diagnostic study. |
| 16–18 | Pilot ready. There is likely enough structure to test whether AI-assisted prediction or decision support can create value. |

This score is not meant to be rigid. A low score in one critical dimension, especially decision relevance or feedback loop, may block a pilot even if the total score is high.

---

## Almost ready vs. pilot ready

### Almost ready

A manufacturing use case is almost ready when:

- the pain is real
- the team can describe the problem
- some data exists
- key process variables are known
- there is interest in better prediction or optimization

However, the process may still need clearer measurement, decision ownership, or feedback structure.

### Pilot ready

A manufacturing use case is pilot ready when:

- there is a specific operational bottleneck
- relevant inputs and outputs are consistently captured
- the process is stable enough for comparison
- there are controllable variables
- a better prediction could change a real decision
- outcomes can be observed and linked back to the decision

In short:

```text
Almost ready = real pain + emerging structure

Pilot ready = real pain + usable data trail + actionable decision point + feedback loop
```

---

## Example use cases

This scorecard can be applied to manufacturing problems such as:

- scrap reduction
- yield improvement
- process-window development
- parameter tuning
- defect risk reduction
- qualification acceleration
- material or process development
- inspection and monitoring workflows
- operator decision support

---

## Community feedback wanted

This framework is intentionally lightweight and evolving.

Useful feedback includes:

- missing readiness dimensions
- better scoring criteria
- examples from specific manufacturing domains
- differences between discrete, batch, and continuous processes
- cases where AI failed because readiness was overestimated
- cases where simple process structuring mattered more than model complexity

Please open an issue or discussion if you have suggestions.
