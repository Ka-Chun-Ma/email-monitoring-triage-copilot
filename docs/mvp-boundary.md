# MVP Boundary

## Purpose
This document defines what the first version of email-monitoring-triage-copilot will and will not do.

The goal is to protect focus, avoid premature complexity, and keep the MVP aligned with the real workflow problem.

## Product position
This project is a deterministic-first, human-in-the-loop, AI-assisted operational workflow prototype.

It is not:
- a flashy AI demo
- a fully autonomous agent
- a replacement for expert judgment
- a full enterprise integration platform

## In scope for MVP
The first version will focus on the smallest useful operational slice.

### 1. Input ingestion
- load sample monitoring issues from a structured file
- use a stable schema for source issue data

### 2. Message normalization
- normalize raw issue text into a consistent format for downstream matching
- preserve source text while creating a derived normalized field

### 3. Deterministic first-pass pattern matching
- compare normalized issues against known patterns
- separate exact or rule-based matching from fuzzy reasoning

### 4. First-pass triage output
The system should assign one of:
- likely recurring
- likely new
- review needed

The system should also provide a reason and confidence level.

### 5. Candidate hint enrichment
Where mappings exist, the system should provide candidate:
- KB reference
- ticket reference
- owner hint

These are suggestions only, not final decisions.

### 6. Structured email draft scaffolding
The system should generate a daily monitoring draft with a fixed section structure:
1. New issues
2. Recurring issues
3. Follow-up items
4. Missing mappings / review needed

### 7. Minimal observability
The system should output a minimal run log such as:
- processed count
- likely recurring count
- likely new count
- review needed count
- missing mapping count
- draft generated or not

## Explicitly out of scope for MVP
The first version will NOT do the following:

### 1. Autonomous outbound action
- no auto-send email
- no auto-update ticket
- no auto-write-back to operational systems

### 2. Direct internal system integration
- no live enterprise database integration
- no direct LDW, Tableau, API, or monitoring system connection
- no production credentials or operational execution

### 3. Full agentic autonomy
- no multi-step autonomous agent that decides and acts without review
- no background loop with independent execution authority

### 4. Advanced LLM dependency
- no bare-LLM-first design
- no requirement for LLM to function in the core path
- no reliance on ungrounded generation for critical classification

### 5. Multimodal enrichment
- no screenshot understanding
- no chart interpretation
- no document image parsing

### 6. Rich UI and workflow polish
- no dashboard UI
- no web app interface
- no polished analyst console
- no user management or permissions system

### 7. Full retrieval architecture
- no RAG stack
- no vector database
- no semantic retrieval platform
- no local model hosting requirement

## Boundary principles
The MVP should follow these principles:
- workflow-first
- deterministic-first
- grounded before generative
- human-in-the-loop
- assessment before trust
- observability before scale

## Decision rule for new ideas
If a new feature idea appears, ask:
1. Does it directly reduce first-pass triage or email packaging effort?
2. Does it preserve or improve reviewability?
3. Can it be observed and assessed cheaply?
4. Does it increase autonomy before trust is established?
5. Does it belong in this MVP or in a later architecture map?

If the idea adds complexity without improving the core workflow slice, it should be deferred.

## The core promise of MVP
The MVP promises only this:
- take a sample set of issues
- structure them
- triage them conservatively
- enrich them where possible
- draft a stable email scaffold
- preserve human judgment

That is enough for version 1.

## Version
v1.0