# Glossary

A working glossary for Physical AI, physics-informed decision layers, and programmable manufacturing.

This glossary is intentionally lightweight and evolving. The goal is to create shared language for researchers, engineers, practitioners, and builders working at the intersection of AI and physical manufacturing systems.

---

## Physical AI

**Physical AI** refers to AI systems that reason about, interact with, or support decisions in the physical world.

In manufacturing, Physical AI systems must account for:

- material behavior
- process constraints
- equipment limits
- uncertainty
- measurement noise
- sparse data
- feedback from physical outcomes
- human engineering and operator workflows

Physical AI is different from purely digital AI because actions in the physical world can carry cost, delay, safety risk, and qualification implications.

---

## Physical AI Stack

The **Physical AI Stack** is a conceptual stack for connecting AI capability to real-world physical systems.

A simplified version:

```text
Physical execution
        ↑
Decision layer
        ↑
Industrial data + physics
        ↑
Foundation models / AI models
        ↑
Compute + infrastructure
```

This repository focuses mainly on the decision-layer and public-facing artifacts around manufacturing readiness, process mapping, and synthetic benchmarks.

---

## Decision Layer

A **Decision Layer** is the system layer that connects AI outputs to real physical decisions.

It translates:

```text
data + physics + constraints + uncertainty
```

into:

```text
actionable decisions
```

Examples of decision-layer outputs:

- recommended process window
- next experiment recommendation
- defect-risk ranking
- feasible / infeasible region
- uncertainty-aware go / no-go guidance
- inspection priority
- operator or engineer decision support

The key question is:

```text
What decision changes because this system exists?
```

---

## Programmable Manufacturing

**Programmable Manufacturing** is the idea that manufacturing systems can become more structured, adaptive, and decision-driven.

It does not mean factories become fully autonomous immediately.

It means manufacturing workflows become easier to reason about, update, and improve through explicit representations of:

- bottlenecks
- inputs
- outputs
- process states
- controllable variables
- decision points
- feedback loops
- constraints
- success metrics

The goal is to move from repeated trial-and-error toward reusable decision workflows.

---

## Manufacturing AI Readiness

**Manufacturing AI Readiness** describes whether a manufacturing process is structured enough for AI-assisted prediction, recommendation, or decision support to create value.

A process is more AI-ready when it has:

- a clear operational bottleneck
- measurable inputs and outputs
- enough process stability for comparison
- controllable variables
- a real decision point
- a feedback loop from action to outcome

AI readiness does not require perfect data.

It requires enough structure for AI to improve a real decision.

---

## Pilot Ready

A manufacturing use case is **pilot ready** when there is enough structure to test whether AI-assisted prediction or recommendation can improve a specific decision.

A pilot-ready use case usually has:

- specific bottleneck
- usable data trail
- measurable outcome
- controllable variables
- decision owner
- feedback mechanism
- narrow scope
- measurable success metric

---

## Almost Ready

A use case is **almost ready** when the pain is real and some structure exists, but the workflow is not yet ready for a focused pilot.

Common missing pieces:

- unclear measurement
- inconsistent data trail
- unclear decision owner
- unstable process
- missing feedback loop
- too broad pilot scope

In short:

```text
Almost ready = real pain + emerging structure

Pilot ready = real pain + usable data trail + actionable decision point + feedback loop
```

---

## Process Mapping

**Process Mapping** is the act of translating a manufacturing problem into a structured decision problem.

A process map should identify:

- operational bottleneck
- inputs
- outputs
- process states
- controllable variables
- decision point
- decision owner
- constraints
- feedback loop
- success metric

This helps determine whether AI should be used, what kind of AI task may fit, and whether the process is ready for a pilot.

---

## Process Window

A **Process Window** is a region of process settings that is expected to produce acceptable outcomes while respecting constraints.

For example, a process window may describe combinations of controllable settings that are likely to satisfy:

- quality requirements
- property targets
- defect limits
- equipment constraints
- stability requirements
- safety limits

A decision layer may recommend a process window rather than a single setting, especially when uncertainty is important.

---

## Physics Priors

**Physics Priors** are domain-informed assumptions, constraints, or relationships that help guide learning or decision-making.

Examples:

- feasible operating ranges
- known physical trends
- conservation relationships
- monotonic behavior
- material behavior assumptions
- process constraints
- simplified surrogate equations
- dimensional reasoning

Physics priors are useful when manufacturing data is sparse, noisy, expensive, or difficult to transfer.

They do not need to replace data-driven models.  
They can help structure the search space and make recommendations more realistic.

---

## Physics-Informed AI

**Physics-Informed AI** refers to AI systems that combine data-driven methods with physical knowledge.

In manufacturing, this may involve:

- using physics-informed features
- constraining model outputs
- combining models with simplified physical equations
- guiding optimization with physical feasibility
- incorporating domain priors
- using physical feedback to improve predictions

The goal is not only higher prediction accuracy, but better physical decision-making.

---

## Industrial Data

**Industrial Data** refers to data generated by real-world industrial processes.

Examples:

- machine logs
- process settings
- sensor data
- inspection results
- test data
- material records
- batch records
- operator notes
- production outcomes

Industrial data is often:

- sparse
- noisy
- incomplete
- inconsistent
- expensive to collect
- difficult to transfer across settings

This makes process structure and physics priors especially important.

---

## Feedback Loop

A **Feedback Loop** connects a decision to a physical action, then connects the measured result back to future decisions.

A simplified feedback loop:

```text
recommendation
        ↓
physical action
        ↓
measured outcome
        ↓
updated knowledge
        ↓
better future recommendation
```

Without feedback, an AI system may produce outputs but cannot learn whether those outputs improved the physical process.

---

## Decision Point

A **Decision Point** is the moment where a person or system chooses an action.

Examples in manufacturing:

- selecting process parameters
- choosing the next experiment
- accepting or rejecting a part
- prioritizing inspection
- adjusting a process plan
- selecting a material
- deciding whether a process window is acceptable
- choosing whether to scale or qualify a process

A model is more useful when its output is tied to a clear decision point.

---

## Decision Owner

A **Decision Owner** is the person or team responsible for acting on a recommendation.

Examples:

- process engineer
- manufacturing engineer
- quality engineer
- operator
- production lead
- materials engineer
- qualification team
- maintenance team

If the decision owner is unclear, AI output may not change action.

---

## Actionable Output

An **Actionable Output** is a model or system output that can change a real decision.

Less actionable:

```text
Predicted value = 0.73
```

More actionable:

```text
This setting is high risk. Try the lower-risk region between A and B, or run experiment C next to reduce uncertainty.
```

Actionable outputs usually include:

- recommendation
- uncertainty
- constraints
- decision context
- expected impact
- next step

---

## Uncertainty-Aware Recommendation

An **Uncertainty-Aware Recommendation** accounts for uncertainty when suggesting an action.

In manufacturing, uncertainty matters because physical experiments may be expensive, slow, or risky.

Examples:

- safe-to-try region
- uncertain region requiring validation
- high-risk region to avoid
- confidence interval around predicted outcome
- next experiment that reduces uncertainty
- recommendation with expected risk level

---

## Synthetic Benchmark

A **Synthetic Benchmark** is a simplified public benchmark generated from artificial data or toy functions.

Synthetic benchmarks are useful because they can test concepts without requiring private industrial data.

In this repository, synthetic benchmarks may explore:

- process-window recommendation
- sparse-data learning
- physics-prior usefulness
- uncertainty-aware decisions
- feedback-loop simulation
- decision quality metrics

A synthetic benchmark should be educational, inspectable, and safe to share publicly.

---

## Toy Benchmark

A **Toy Benchmark** is a deliberately simple benchmark designed for learning, discussion, or early testing.

Toy benchmarks should not be mistaken for production systems.

They are useful for asking focused questions such as:

- Does uncertainty affect the recommendation?
- Does a physics prior help under sparse data?
- Can the system find a feasible process window?
- Can decision quality be evaluated separately from prediction accuracy?

---

## Decision Quality

**Decision Quality** measures whether a system helps make better decisions, not only whether it predicts accurately.

Possible decision-quality metrics:

- feasible recommendation rate
- target-window hit rate
- false-safe rate
- false-reject rate
- number of experiments needed
- regret relative to best known setting
- reduction in trial iterations
- improvement in decision confidence

A model can have good prediction accuracy but poor decision usefulness if its output does not change action.

---

## Sparse Data

**Sparse Data** means there are few examples relative to the complexity of the process.

Sparse data is common in high-value manufacturing because experiments may be expensive, slow, or difficult to repeat.

Physics priors and process structure can help when data is sparse.

---

## Operational Bottleneck

An **Operational Bottleneck** is the specific practical constraint or pain point that limits performance.

Weak description:

```text
Improve manufacturing.
```

Stronger description:

```text
Reduce the number of trial iterations required to identify a feasible process window.
```

Clear bottlenecks make AI pilots easier to scope and evaluate.

---

## Minimal Useful Pilot

A **Minimal Useful Pilot** is the smallest focused test that can produce meaningful learning.

A good pilot should define:

- bottleneck
- decision point
- inputs
- outputs
- feedback
- scope
- success metric
- minimum useful result

The goal is not to solve everything at once.  
The goal is to test whether better prediction or recommendation improves a real decision.

---

## Human-in-the-Loop

**Human-in-the-Loop** means that engineers, operators, or other domain experts remain part of the decision workflow.

In manufacturing, this is often necessary because:

- physical decisions have cost and risk
- domain expertise matters
- workflows vary by site
- recommendations need interpretation
- qualification and safety may require human review

Human-in-the-loop systems can still be highly valuable if they improve decision quality.

---

## Open Layer

The **Open Layer** refers to the public-facing, generalized, and synthetic artifacts that can be shared safely.

Examples:

- readiness scorecards
- process-mapping templates
- pilot-definition templates
- glossary
- synthetic benchmarks
- educational notes
- community discussions

The open layer helps build shared language and community adoption.

---

## Deployment Layer

The **Deployment Layer** refers to real-world implementation in a specific industrial context.

It may involve:

- site-specific data
- partner workflows
- production constraints
- real process parameters
- deployment feedback
- integration with operational systems

This repository focuses on the open layer.

---

## Guiding principle

Start from the decision, not the model.

A model is useful when it helps someone make a better decision in the physical world.
