# Roadmap

This roadmap describes the near-term development plan for the Programmable Manufacturing Lab.

The goal is to build public-facing, generalized, and synthetic artifacts for Physical AI, physics-informed decision layers, and programmable manufacturing.

This repository is being built in public. The roadmap may evolve based on community feedback, examples, and contributor interest.

---

## Current focus

The current focus is to create a useful open interface for discussing manufacturing AI readiness and decision-layer design.

Near-term priorities:

- clarify what makes a manufacturing process AI-ready
- create reusable process-mapping templates
- define common manufacturing decision points
- design safe synthetic benchmarks
- collect examples of manufacturing AI failure modes
- create contribution paths for researchers, engineers, and practitioners

---

## v0.1 — Readiness framework

Status: in progress

Goal: define a lightweight framework for evaluating whether a manufacturing process is ready for an AI-assisted pilot.

Planned artifacts:

- Manufacturing AI Readiness Scorecard
- readiness dimensions
- scoring guide
- distinction between “almost ready” and “pilot ready”
- examples of readiness blockers
- community feedback on missing criteria

Key questions:

- What must be true before AI can create operational value?
- When is the process itself the bottleneck?
- When is more data useful, and when is better process structure needed first?
- What do companies often overestimate about AI readiness?

---

## v0.2 — Process mapping templates

Status: in progress

Goal: translate manufacturing problems into structured decision problems.

Planned artifacts:

- Process Mapping Template
- Pilot Definition Template
- bottleneck taxonomy
- input / output / process-state mapping
- controllable-variable mapping
- decision-point mapping
- feedback-loop mapping

Key questions:

- What is the operational bottleneck?
- What can be measured?
- What can be controlled?
- What decision would change if prediction improved?
- What feedback is available after the decision?

---

## v0.3 — Decision-layer concepts

Status: planned

Goal: define the layer between AI model outputs and real manufacturing decisions.

Planned artifacts:

- decision-point taxonomy
- decision-owner examples
- actionable output examples
- uncertainty communication examples
- feedback-loop patterns
- examples of prediction outputs that do and do not change action

Key questions:

- What does a useful AI output look like in manufacturing?
- Who acts on the recommendation?
- When is the decision made?
- How should uncertainty be communicated?
- How does the result return to improve future decisions?

---

## v0.4 — Synthetic toy benchmarks

Status: planned

Goal: create small synthetic examples for studying Physical AI decision layers without relying on private industrial data.

Planned benchmark directions:

- toy process-window recommendation
- sparse-data regression with physics priors
- uncertainty-aware decision support
- synthetic process-structure-property mapping
- simple inverse-design problem
- noisy feedback-loop simulation

Benchmark principles:

- synthetic
- educational
- easy to inspect
- safe to share publicly
- focused on decisions, not only prediction accuracy

Key questions:

- How should a benchmark evaluate decision quality?
- When does a physics prior help under sparse data?
- How should uncertainty affect recommended actions?
- How can synthetic examples represent real manufacturing constraints without exposing private context?

---

## v0.5 — Community examples

Status: planned

Goal: collect generalized examples from different manufacturing domains.

Possible domains:

- CNC machining
- metal additive manufacturing
- injection molding
- casting
- heat treatment
- inspection workflows
- materials testing
- assembly processes
- maintenance workflows

Example structure:

- operational bottleneck
- available inputs
- measurable outputs
- controllable variables
- decision point
- feedback loop
- readiness blockers
- possible AI-assisted task

Key questions:

- Which manufacturing problems are most suitable for AI-assisted decision support?
- Which ones are not ready yet?
- What kinds of process structure are needed before modeling?
- What patterns repeat across domains?

---

## v0.6 — Documentation and onboarding

Status: planned

Goal: make the repository easier for first-time contributors to understand and use.

Planned artifacts:

- glossary
- contributor guide
- example issue templates
- discussion prompts
- simplified “start here” guide
- diagrams explaining the Physical AI decision layer
- links between README, templates, discussions, and issues

Key questions:

- Can a manufacturing engineer understand the project quickly?
- Can an AI researcher see where to contribute?
- Can a student make a small useful contribution?
- Can an industrial practitioner give feedback without sharing private data?

---

## Longer-term directions

Longer-term directions may include:

- public benchmark leaderboard for synthetic tasks
- example notebooks using synthetic datasets
- workshop-style discussion materials
- community-maintained glossary
- comparison of physics-informed and data-driven approaches
- open educational modules for Physical AI in manufacturing
- structured case-study format for generalized manufacturing AI lessons

---

## What success looks like

Near-term success:

- clear public artifacts
- useful templates
- active issues and discussions
- feedback from manufacturing and AI practitioners
- examples that help people reason about AI readiness

Medium-term success:

- outside contributors suggest improvements
- practitioners use or adapt the templates
- researchers propose synthetic benchmarks
- the community develops shared language around Physical AI decision layers

Long-term success:

- this repository becomes a useful open reference for programmable manufacturing, manufacturing AI readiness, and physics-informed decision-layer design

---

## Community feedback wanted

This roadmap is open to revision.

Useful feedback includes:

- missing roadmap items
- better sequencing
- suggested first benchmarks
- examples from specific manufacturing domains
- suggestions for making the repository easier to contribute to
- ideas for safe, synthetic, public-facing artifacts

Please open an issue or discussion if you have suggestions.
