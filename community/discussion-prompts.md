# Discussion Prompts

This page collects discussion prompts for the Programmable Manufacturing Lab community.

The goal is to encourage practical, public-facing discussion around Physical AI, manufacturing AI readiness, decision layers, and programmable manufacturing.

Contributions do not need to include private production data or confidential process details. Generalized examples, lessons learned, questions, and critiques are welcome.

---

## 1. What makes a manufacturing process AI-ready?

Many manufacturing AI projects fail before the model becomes the bottleneck.

Useful discussion questions:

- What must be true before an AI-assisted manufacturing pilot can work?
- What makes a process “almost ready” but not yet pilot-ready?
- What do teams often overestimate about their data or process maturity?
- What does a usable feedback loop look like in practice?
- When is better process definition more important than a better model?

Related artifact:

```text
templates/readiness-scorecard.md
```

---

## 2. What are common manufacturing AI failure modes?

Many projects struggle for reasons unrelated to model architecture.

Useful discussion questions:

- Was the problem too broad?
- Was the data inconsistent?
- Was there no decision owner?
- Was the output not actionable?
- Was the feedback loop missing?
- Was the pilot too large?
- Was success hard to measure?

Related issue idea:

```text
Collect examples of manufacturing AI failure modes
```

---

## 3. What does a useful manufacturing decision layer output?

A model output is only useful if it changes a real decision.

Useful discussion questions:

- What should the system recommend?
- Who acts on the recommendation?
- When is the recommendation available?
- What uncertainty information is needed?
- How should engineers or operators interpret the output?
- What makes an output actionable rather than merely informative?

Possible outputs:

- recommended process window
- risk-ranked candidate settings
- feasible / infeasible region
- next experiment suggestion
- inspection priority
- uncertainty-aware go / no-go guidance

Related artifact:

```text
docs/decision-layer-primer.md
```

---

## 4. How should uncertainty be communicated in manufacturing?

Manufacturing decisions often involve uncertainty, risk, and cost.

Useful discussion questions:

- Should uncertainty be shown as confidence intervals, risk categories, or decision regions?
- When should the system say “safe to try” vs. “needs validation”?
- How much uncertainty is acceptable before running a physical experiment?
- How should uncertainty affect process-window recommendations?
- How should operators or engineers use uncertain outputs?

Related issue idea:

```text
Add examples for uncertainty communication
```

---

## 5. What is the smallest useful AI pilot?

A good first pilot should be narrow, measurable, and tied to a real decision.

Useful discussion questions:

- What is the smallest pilot that could produce useful learning?
- What success metric should be used?
- How narrow should the scope be?
- What should be explicitly out of scope?
- How should a pilot connect to future deployment?

Related artifact:

```text
templates/pilot-definition-template.md
```

---

## 6. What makes a good synthetic benchmark for Physical AI?

Synthetic benchmarks can help test decision-layer ideas safely.

Useful discussion questions:

- What should a toy manufacturing benchmark include?
- Should it test prediction accuracy, decision quality, or both?
- How should constraints be represented?
- How should feedback be simulated?
- What metrics capture useful decision-making?
- How simple is too simple?

Related artifact:

```text
benchmarks/toy-process-window/README.md
```

---

## 7. What makes manufacturing programmable?

Programmable manufacturing is still an emerging category.

Useful discussion questions:

- What does it mean for a physical process to become programmable?
- Which manufacturing decisions can be structured first?
- What should remain human-in-the-loop?
- What kinds of process knowledge can transfer across contexts?
- What is the role of physics priors?
- What is the role of foundation models?

Related artifact:

```text
docs/programmable-manufacturing.md
```

---

## 8. Where should open community work stop and proprietary deployment begin?

This repository focuses on public-facing, generalized, and synthetic artifacts.

Useful discussion questions:

- What belongs in the open layer?
- What should remain deployment-specific?
- How can synthetic examples be useful without exposing sensitive context?
- What templates or benchmarks would help the community?
- What should be standardized, and what should remain domain-specific?

---

## Suggested discussion format

A useful discussion post can be short.

Suggested structure:

```text
Context:
[What manufacturing domain, workflow, or decision type are you thinking about?]

Observation:
[What pattern, challenge, or failure mode have you seen?]

Question:
[What should the community discuss or improve?]

Generalized example:
[Optional. Keep it public-facing and non-confidential.]
```

---

## Community principle

Generalized examples are useful.

You do not need to share private data, customer details, or sensitive process parameters to contribute meaningfully.

The goal is to build shared language around Physical AI decision layers and programmable manufacturing.
