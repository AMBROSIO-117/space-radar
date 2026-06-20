# F2T2EA / OODA Duck.ai Operating Playbooks

Date: 2026-06-20
Purpose: Use a simple LLM like Duck.ai to prepare for open-ended questions, case studies, presentations, and strategic conversations without turning the process into job-search machinery.

## 1. Operating Principle

Duck.ai is best used as a **low-friction rehearsal partner**:

- Fast decomposition
- Counterarguments
- Clarifying questions
- Drill practice
- First-pass structure
- Red-team pressure

Do not use it as:

- A memory system
- A source of verified facts
- A place for secrets, credentials, or sensitive personal material
- A substitute for your own judgment

DuckDuckGo says Duck.ai does not record or store chats, removes personal metadata before sending prompts to model providers, and has model-provider agreements limiting retention. Still, operationally, write prompts as if they might be seen by a reviewer. Keep them clean.

## 2. The Core Loop

Use OODA inside each F2T2EA phase.

```text
FIND      -> What is the real question?
FIX       -> What do I know, not know, and need to constrain?
TRACK     -> What signals, assumptions, and options am I watching?
TARGET    -> What is the highest-leverage answer or action?
ENGAGE    -> Deliver the answer, slide, question, or move.
ASSESS    -> What worked, what failed, what changes next?
```

Each phase runs:

```text
Observe   -> What is in front of me?
Orient    -> What does it mean?
Decide    -> What is my next move?
Act       -> Produce the next artifact.
```

The point is speed with reflection: move, check, adjust.

## 3. The 15-Minute Duck.ai Drill

Use this when you feel stuck before a meeting, case, pitch, or open-ended question.

### Minute 0-2: Frame

Paste:

```text
You are my thinking sparring partner. Use F2T2EA and OODA.

Context:
[one paragraph]

Question:
[the actual open-ended question]

Constraints:
- Do not invent facts.
- Ask clarifying questions first if the task is ambiguous.
- Separate facts, assumptions, options, and risks.
- Give me a concrete next move.
```

### Minute 2-5: Find / Observe

Ask:

```text
What is the real question underneath this prompt? Give me:
1. The explicit question
2. The hidden question
3. The decision-maker's likely concern
4. The trap answer to avoid
```

### Minute 5-8: Fix / Orient

Ask:

```text
Constrain this problem. What are the 3-5 variables that matter most?
For each variable, tell me:
- Why it matters
- What assumption I am making
- What evidence would change my mind
```

### Minute 8-11: Target / Decide

Ask:

```text
Give me three possible answers:
1. Safe answer
2. Contrarian but defensible answer
3. Best answer under uncertainty

Then recommend one and explain why.
```

### Minute 11-14: Engage / Act

Ask:

```text
Turn the recommended answer into a 90-second spoken response.
Use this structure:
- Bottom line
- Reasoning
- Trade-off
- Concrete next step
```

### Minute 14-15: Assess

Ask:

```text
Red-team my answer. What is the strongest objection, and how should I respond in one sentence?
```

## 4. Open-Ended Question Playbook

Use this for questions like:

- "How would you solve X?"
- "What would you do first?"
- "How do you think about this market?"
- "What is your view on this product?"
- "How would you handle ambiguity?"

### FIND

Goal: identify the real decision.

Duck.ai prompt:

```text
Analyze this open-ended question:
[paste question]

Use FIND:
- What is being asked literally?
- What capability is being tested?
- What would a weak answer do?
- What would a strong answer demonstrate?
```

### FIX

Goal: constrain the problem before answering.

Prompt:

```text
Help me ask 3 clarifying questions.
They should reduce ambiguity without sounding evasive.
Then give me the assumptions I can state if no clarification is available.
```

### TRACK

Goal: keep the moving parts visible.

Prompt:

```text
Create a signal tracker for this question:
- Stakeholders
- Constraints
- Risks
- Metrics
- Unknowns
- Decision deadline
```

### TARGET

Goal: choose an answer angle.

Prompt:

```text
Give me a decision matrix with 3 options.
Score each on impact, speed, reversibility, risk, and evidence needed.
Then choose the best option.
```

### ENGAGE

Goal: answer clearly.

Prompt:

```text
Write my answer in this format:
1. My answer in one sentence
2. The reasoning
3. The trade-off
4. What I would do first
5. What I would measure
Keep it spoken, not essay-like.
```

### ASSESS

Goal: improve after rehearsal.

Prompt:

```text
Grade this answer from 1-10 for clarity, structure, originality, and credibility.
Then rewrite it one level better.
```

## 5. Case Study Playbook

Use this for business, product, strategy, or operations cases.

### Case Frame

```text
Case:
[paste case]

Use F2T2EA/OODA. Do not solve immediately.
First produce:
- Problem statement
- Decision-maker
- Objective function
- Constraints
- Missing facts
- Assumptions
```

### Case Structure

```text
Build a case tree with 3-5 branches.
For each branch:
- What question does it answer?
- What evidence would support it?
- What would falsify it?
- What metric would I use?
```

### Hypothesis First

```text
Give me an initial hypothesis and the fastest way to test it.
Use:
- Hypothesis
- Why it might be true
- What would prove it wrong
- First analysis to run
- First question to ask the interviewer/audience
```

### Recommendation

```text
Turn this into a final case recommendation:
- Recommendation
- 3 reasons
- Main risk
- Mitigation
- Next 7-day action plan
```

## 6. Presentation Playbook

Use this for decks, demos, talks, or stakeholder updates.

### FIND: Audience Need

```text
My audience is [audience].
My topic is [topic].
Use FIND:
- What do they already believe?
- What do they need to decide?
- What are they worried about?
- What would make them trust me?
```

### FIX: Message Spine

```text
Create a message spine:
1. Opening claim
2. Evidence
3. Tension or bottleneck
4. Proposed move
5. What I need from the audience
```

### TRACK: Slide Ledger

```text
Create a slide ledger.
For each slide, give:
- Slide title
- One-sentence point
- Evidence needed
- Visual idea
- Risk if this slide is weak
```

### TARGET: Sharpest Argument

```text
What is the one slide that must land?
Give me:
- The core claim
- The strongest supporting evidence
- The likely objection
- The response
```

### ENGAGE: Delivery Script

```text
Write a 3-minute spoken version.
Tone: clear, direct, thoughtful.
No corporate filler.
```

### ASSESS: Pressure Test

```text
Act as a skeptical audience member.
Ask me 7 hard questions.
Then give model answers that are concise and defensible.
```

## 7. Zero-to-One Question Playbook

Use this when the goal is not to answer correctly, but to find a non-obvious position.

### Prompt

```text
I am trying to find a zero-to-one position.

Thesis:
[paste thesis]

Arena:
[domain]

Use this structure:
1. What is the current consensus?
2. What is the lazy contrarian answer?
3. What is the deeper non-consensus answer?
4. What would make this thesis credible?
5. What is the smallest proof artifact I can build?
6. What would change my mind?
```

### Follow-up

```text
Now red-team this thesis.
Do not be polite.
Separate:
- Unsupported claim
- Weak evidence
- Overreach
- Better narrower version
- First proof artifact
```

## 8. Daily Practice Routine

Do this once per day for 20 minutes.

### 5 minutes: One Question

Pick one open-ended question:

- "What do I believe that is still under-proven?"
- "Where is the bottleneck?"
- "What would I do first?"
- "What is the non-obvious but defensible view?"

### 5 minutes: Duck.ai Drill

Run:

```text
Use F2T2EA/OODA to decompose this question.
Give me a first answer, a better answer, and a sharper answer.
```

### 5 minutes: Speak

Say the answer out loud. Do not read. Record if useful.

### 5 minutes: Assess

Ask:

```text
What was unclear, generic, unsupported, or too abstract?
Rewrite as a 60-second answer with one concrete example.
```

## 9. "Do Not Drift" Rules

- Always start with the decision question.
- Always separate facts from assumptions.
- Always ask what evidence would change your mind.
- Always produce an artifact: answer, diagram, slide spine, case tree, proof spec.
- Never let the model replace your judgment.
- Never paste sensitive personal, account, or credential data.

## 10. Fast Templates

### Template A: Open Question

```text
Use F2T2EA/OODA.
Question: [question]
Context: [context]
Output:
1. Real question
2. Clarifying questions
3. Assumptions
4. 3 options
5. Recommended answer
6. 90-second response
7. Strongest objection
```

### Template B: Case

```text
Use F2T2EA/OODA for this case:
[case]

Output:
1. Problem statement
2. Objective
3. Case tree
4. Hypothesis
5. Analysis plan
6. Recommendation
7. Risks and next steps
```

### Template C: Presentation

```text
Build a presentation spine.
Audience: [audience]
Goal: [goal]
Topic: [topic]

Output:
1. Opening claim
2. 5-slide outline
3. Evidence needed
4. Likely objections
5. 3-minute script
```

### Template D: Zero-to-One

```text
Test this thesis for originality and credibility:
[thesis]

Output:
1. Consensus
2. Lazy contrarian version
3. Deeper non-consensus version
4. Evidence needed
5. First proof artifact
6. Red-team critique
```

## 11. How To Start Acting Today

1. Pick one real open-ended question you expect to face.
2. Run Template A in Duck.ai.
3. Speak the answer out loud once.
4. Ask Duck.ai to red-team it.
5. Rewrite it as a 60-90 second answer.
6. Save the final answer in your own notes, not only in the chat.
7. Repeat with one case and one presentation question.

By the end of three loops, you will have:

- One answer
- One case structure
- One presentation spine
- One red-team list
- One proof artifact idea

That is enough to start moving.

