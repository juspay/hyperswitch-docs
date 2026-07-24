---
description: >-
  Compare two routing strategies on a live split of your traffic, with
  guardrails and statistical significance - so you only roll out a change once
  the data proves it wins.
icon: flask
---

# A/B Testing

A/B testing runs two routing strategies side by side on a **live split** of your own traffic - a
**control** arm (what you do today) and a **variant** arm (the change you're evaluating) - measures
how each performs, and tells you whether the difference is **statistically significant** or just
noise. A built-in **guardrail** flags the experiment the moment the variant starts hurting
approvals, so you catch a bad change early.

Use it whenever you change how payments are routed - turning on Multi-Objective Routing, letting
[Autopilot](autopilot.md) self-tune, adjusting an auth-rate setting - to prove the change helps
**before** it touches all your traffic. A change that quietly lowers your approval rate costs far
more than any fee it saves.

> **Note.** An experiment compares *routing strategies*, not payment providers. Each arm is a
> routing configuration. The connectors are still chosen by that arm's logic per payment.

## The core idea - control vs variant

An experiment has exactly two arms.

- **Control** - your baseline strategy (typically your current live routing).
- **Variant** - the change you want to prove out. Always the **minority** arm - it takes a small,
  capped share of traffic so a bad change can only ever affect a fraction of payments.

You choose what share of traffic the variant sees (the **variant split**). In the dashboard builder
this is a slider capped at **5-30%**. Everything else goes to control. Because the variant is always
the minority, control stays the majority - the safe side.

Each arm is one of two things.

- **An Auth-Rate Routing strategy** with its own settings (auth-rate scoring, optionally with
  [Multi-Objective Routing](multi-objective-routing.md) and/or [Autopilot](autopilot.md)).
  This is the common case.
- **An existing named routing algorithm** - a single connector, a priority list, a volume split, or
  an advanced rule tree you've already built.

<figure><img src="../../../.gitbook/assets/routing-ab-test-setup.png" alt="A/B test setup screen showing Control and Variant arm selectors and the variant split slider"><figcaption></figcaption></figure>

## Setting up an experiment

You build an experiment in the dashboard's A/B test builder, with the following pieces.

| Setting | What it does |
| --- | --- |
| **Experiment type** | **Algorithm comparison** (pick any two strategies as arms) or **Auth-rate config tuning** (same strategy both arms, variant changes one or two settings). |
| **Control strategy** | The baseline arm. |
| **Variant strategy** | The arm you're testing. |
| **Variant split %** | Share of traffic sent to the variant (builder slider, 5-30). The rest goes to control. |
| **Sample target (minimum sample size)** | How many transactions each arm needs before results are treated as meaningful (builder presets 1,000 / 5,000 / 10,000 / 50,000, default 5,000). Until then the verdict is "collecting data". |
| **Guardrail threshold (pp)** | If the variant's approval rate falls this many percentage points below control, the experiment is flagged **guardrail breached** (default 3 pp). |

### Strategy presets

For the **Algorithm comparison** type, the builder offers ready-made auth-rate strategies so you
don't have to hand-tune each arm - two independent dials (Multi-Objective Routing × self-tuning).

| Preset | What it is |
| --- | --- |
| **Maximize approvals · manual tuning** | Pure auth-rate routing - pick the connector most likely to approve. |
| **Maximize approvals · auto-tuned** | The same, with [Autopilot](autopilot.md) self-tuning the auth-rate settings. |
| **Approvals + save on fees · manual** | Adds Multi-Objective Routing - cheapest among equally-reliable connectors, settings you control. |
| **Approvals + save on fees · auto-tuned** | Multi-Objective Routing with Autopilot self-tuning. |

You can also pick a **saved routing algorithm** (a single connector, a priority list, a volume
split, or an advanced rule tree) as either arm.

> **Note.** The "save on fees" presets only appear if you have
> [**Multi-Objective Routing**](multi-objective-routing.md) enabled, and the "auto-tuned" presets
> only if **Autopilot / auto-calibration** is on.

A typical first experiment is **control = Maximize approvals** vs **variant = Approvals + save on
fees** - i.e. "does Multi-Objective Routing save money without hurting approvals?"

## How traffic is split

Arm assignment is **deterministic per payment**. Each payment's id is hashed and taken **modulo 100**
against the variant split - so a given payment always lands in the **same arm**, including on
retries. This matters - a payment retried after a decline is scored consistently, never split across
arms. (At the platform level the split is capped below 50%, so the variant is always the minority
arm. The dashboard builder narrows that to a 5-30% slider.)

There are two places this assignment is used.

- **Real payments** - your live routing decisions route into the assigned arm. This only happens
  once you explicitly enable **real-payment interception** for the merchant (the
  `ab-test-real-payments` feature). It's **off by default**, so creating and activating an
  experiment does **not** touch live traffic until you opt in.
- **Simulation / Decision Explorer** - you can preview what each arm *would* do for any payment
  context without a real transaction, using the routing simulator. This works even before
  real-payment interception is on, so you can sanity-check an experiment before it ever sees a
  customer.

> **Info.** An experiment must also be **activated** (like any routing algorithm) to run. And an
> experiment can only be **edited or deleted while inactive** - deactivate it first if it's live.

## Guardrails

The variant is the risky arm, so it's watched. Once each arm has enough data, before any
significance test runs, the results check the guardrail first - if the variant's **approval rate is
more than the guardrail threshold** (in percentage points) below control, the verdict short-circuits
to **guardrail breached** and the dashboard shows a red banner - "Variant auth rate dropped X pp
below control. Consider stopping the experiment."

This is a **flag, not an automatic stop** - you decide whether to stop it (there's a **Stop**
button). Combined with the capped minority split, it means a bad variant only ever affects a small
share of traffic and is surfaced clearly.

## Reading the results

Once both arms have traffic, the results view runs a **statistical significance test** between them
and returns a verdict. For a Multi-Objective Routing experiment it tests **net expected value**
(approvals *and* fees together) with a two-sample z-test. For an approvals-only experiment it
collapses to a plain **approval-rate** test.

**Per-arm metrics**

| Metric | Meaning |
| --- | --- |
| **Transactions** | How many payments the arm handled. |
| **Outcome** | Approved vs declined counts. |
| **Net auth rate (NAR)** | Overall approval rate - any attempt succeeded. |
| **First-attempt rate (FAAR)** | Approval rate on the first try, before retries. |
| **Cost saved (TCS)** | Total fees saved versus baseline (Multi-Objective Routing arms only). |
| **Avg chosen cost / avg cost saved (bps)** | Average fee of the connector picked, and the per-txn saving. |
| **Avg latency (ms)** | Average routing-decision latency for the arm. |
| **Net EV (bps)** | Net expected value - the combined approvals-and-cost score the winner is judged on. |

For an **approvals-only** experiment (neither arm uses Multi-Objective Routing), the cost fields -
cost saved, avg cost saved, and Net EV - are empty, and the winner is judged on approval rate alone.

**Overall stats**

| Field | Meaning |
| --- | --- |
| **delta_pp** | The variant's approval-rate difference vs control, in percentage points. |
| **p_value** | Probability the observed difference is chance. Lower = more confident. |
| **confidence_interval** | The plausible range of the true difference. |
| **net_delta_bps** | The net expected-value difference between arms. |
| **verdict** | The bottom line (see below). |

### Verdicts

| Verdict | Meaning | What to do |
| --- | --- | --- |
| **Collecting data** | At least one arm hasn't hit the minimum sample size yet. | Wait for more traffic. |
| **Not significant** | Enough data, but the difference is within noise. | The change is neutral. Keep or drop it on other grounds. |
| **Variant wins** | The variant significantly beats control on net expected value. | Roll the variant out. |
| **Variant loses** | The variant significantly underperforms control. | Keep control. Discard the variant. |
| **Guardrail breached** | The variant's approval rate fell too far below control. | Stop - the variant is hurting approvals. |

You can also open the **per-transaction log** to see exactly which arm each payment landed in and
how it turned out - useful for spot-checking arm assignment or debugging a specific payment.

## A typical workflow

1. **Build the experiment.** Pick control (your current routing) and variant (the change), set a
   modest variant split (e.g. 10-20%), a sample target, and a guardrail threshold.
2. **Preview in the simulator.** Confirm each arm does what you expect on sample payments.
3. **Activate it.** Activating prompts you to **enable live-traffic testing** at the same time. If
   you activate without it, the experiment shows as **Not collecting** (an amber banner reminds you
   to turn on live traffic). Switch it on when you're ready for the variant to take its split of
   real payments.
4. **Watch the results.** The status reads **Active** once it's live and collecting. The verdict
   starts at "collecting data" and firms up as traffic accrues (statistical significance is declared
   at p < 0.05).
5. **Decide.** On **variant wins**, promote the variant to your live routing. On **variant loses**
   or **guardrail breached**, keep control (hit **Stop**). An experiment must be **inactive** to be
   edited or deleted - you can also **duplicate** one to iterate.

## Relationship to other features

- [**Multi-Objective Routing**](multi-objective-routing.md) - a variant arm can turn this on to
  A/B test whether it pays off for you.
- [**Autopilot**](autopilot.md) - a variant arm can enable Autopilot self-tuning, scoped to just
  that arm, to test self-tuning against your manual settings.
- **Merchant features** - where `ab-test-real-payments` is toggled (Dashboard → merchant features).
