---
title: "Physical-bridge constructions (Oct 2026 catch-up)"
route: "/wiki/physical-bridge-constructions"
date: "2026-10-18"
claimStatus: "restricted"
tags: ["physical-bridge", "pruning", "observation", "receiver", "research-branch"]
dek: "Catch-up of the research-branch constructions on pruning, observation and the receiver since the 2026-10-10 compile. All restricted, not on main, native bridge NOT_DERIVED; this does not show a derived measurement event, a derived arrow of time, or a breakthrough."
---

[Wiki](index.md)

# Physical-bridge constructions (Oct 2026 catch-up)

Restricted · research branch · not on main · compiled 2026-10-18 · GitHub-only (no X source)

This page collects the work on the WetLabEngine branch
[`research/uqcf-overlapping-guard-exchange`](https://github.com/proteinfoldingengine/WetLabEngine/tree/research/uqcf-overlapping-guard-exchange/ResearchHistory/UQCF-GEM/research/physical-bridge)
(directory `ResearchHistory/UQCF-GEM/research/physical-bridge/`) since the wiki's last compile on 2026-10-10.
Branch head at compile: [`566b9b8d`](https://github.com/proteinfoldingengine/WetLabEngine/commit/566b9b8d502acbe6b1d959410f2a5eb44739769c).

!!! warning "Claim boundary"
    Every item here is **Restricted**: research branch, not on main, native bridge **NOT_DERIVED**.
    That pruning/observation occurs is an **accepted empirical input**, not something derived.
    "Gemini ACCEPTED" means one model review found no error in a frozen, pre-registered argument. It is not proof and not peer review.
    WetLabEngine `STATUS.md` did not change for these items, so no `claimStatus` on this wiki moved. scientific_breakthrough: false.

## Framing (from Aaron, 2026-10-17)

Pre-time pruning (excluding possibilities, logical dependence) is distinct from pruning that constitutes time (an actual update that changes what stays recoverable).
Time is the ordered history of compatible records of such events. The model carries the *effect* of observation, not its cause; observation is taken as a known input, with no claim about the actor.

## Inherited foundation (credited)

These constructions build on existing, separately reviewed stack work and do not replace it:

- [Genesis Pin](genesis-pin.md) (V997): a ledger, not a selector; pinned root plus append-only continuity gives each retained entry a unique ancestry address.
- [v15.12 history](v1512-history.md) and [v15.13 events](v1513-events.md); v15.14 record dependencies (read channel supplied); v15.15 copy gate (records rewind when unobserved, cannot when observed); v15.16 pinching / retention nesting; v15.17 retained-motion demo (observed vs unobserved agree exactly when motion preserves the retained structure).
- v15.10 conditional theorem (a noninjective recoverability update induces an oriented order) and V1153 / V1172 / V1472 ledger implementations.
- The GPT agent's P1/P2 pushforward machinery and accepted reviews (credited to **proteinfolding-gpt**, listed below).

## Grok-agent constructions (proteinfolding-grokbot)

### 2026-10-17 · recoverable_pruning_ledger

Badge: **Restricted** · Gemini ACCEPTED · research branch · NOT_DERIVED

- **Plain summary:** pruning in the ledger redistributes retained content to ancestors; it never creates information. Under a stated survivor-selection contract, the retained records form a decreasing, record-compatible chain, and the loss of recoverability has a definite direction.
- **Does NOT show:** that pruning actually occurs natively, native receiver access, or a derived arrow of time. Witness D depends on supplied premise J.
- **Sources:** freeze [`0fbea1c3`](https://github.com/proteinfoldingengine/WetLabEngine/commit/0fbea1c3), scientific SHA [`a61bac8c`](https://github.com/proteinfoldingengine/WetLabEngine/commit/a61bac8c); review [run 39070100916](https://github.com/proteinfoldingengine/WetLabEngine/actions/runs/39070100916) (ACCEPTED, no findings, native_bridge NOT_DERIVED). Incorporates two GPT adverse-review corrections.

### 2026-10-17 · preparability_branch_split

Badge: **Restricted** · draft revised by GPT; corrected packet ACCEPTED · NOT_DERIVED

- **Plain summary:** looks at whether two distinguishable preparations can be built as a split from a common pinned root, rather than supplied by hand.
- **Does NOT show:** native preparability. The GPT review found that the V997 hash chain gives no permission to append to the carrier tree, that two-coordinate access was unearned, and that the complete-fiber contraction is allowed, not forced. Those gaps remain.
- **Sources:** draft 1 [`526b3af7`](https://github.com/proteinfoldingengine/WetLabEngine/commit/526b3af7); GPT revision and review record [`153af9dd`](https://github.com/proteinfoldingengine/WetLabEngine/commit/153af9dd); first review [run 39075699709](https://github.com/proteinfoldingengine/WetLabEngine/actions/runs/39075699709) (REVISE), corrected packet [run 39076009238](https://github.com/proteinfoldingengine/WetLabEngine/actions/runs/39076009238) (ACCEPTED).

### 2026-10-17 · pruning_occurrence

Badge: **Not claimed** · conditional candidate · unreviewed

- **Plain summary:** a conditional candidate for what an actual pruning occurrence would look like (monotone retention along provenance, including appends), reconciled against V997, V1172, V1472, P1/P2 and v15.16.
- **Does NOT show:** that pruning must occur; it was never frozen or reviewed. Per Aaron's later rule, occurrence is now treated as an accepted input instead.
- **Sources:** drafts [`229bdf27`](https://github.com/proteinfoldingengine/WetLabEngine/commit/229bdf27) and [`aab5f7c4`](https://github.com/proteinfoldingengine/WetLabEngine/commit/aab5f7c4). No review run.

### 2026-10-18 · record_access

Badge: **Not claimed** · draft · unreviewed on its own

- **Plain summary:** readability equals centrality. In executed v15.16, pinching on the record bits is the same as a Lüders read of the receiver's own register, it is repeatable, and the register-local state is unchanged.
- **Does NOT show:** a native write. The write is still the supplied v15.15 CNOT, so access is through a supplied interface. Its central-algebra results were later used inside receiver_identification sections 14 and 19.
- **Sources:** draft 1 [`352fac2d`](https://github.com/proteinfoldingengine/WetLabEngine/commit/352fac2d). No standalone review run.

### 2026-10-18 · observation_effect

Badge: **Restricted** · Gemini ACCEPTED · research branch · NOT_DERIVED

- **Plain summary:** observing changes later outcomes exactly when the next motion breaks the retained structure (this generalizes v15.17). In the which-path example the *unobserved* receiver keeps a full bit about the source and the observed one keeps none. A keep-or-reveal trade-off: for blurring (pinching) observations, a trace of size C that an observation happened costs a disturbance of about C² to the earlier record (sharp). The ledger's absorption step escapes this because it moves content instead of blurring it.
- **Does NOT show:** why observation happens (an accepted input), the receiver link, or a derived bridge. Gemini labeled the bridge "derived" while listing hand-supplied inputs; that label was recorded, not adopted. The underlying quantity is the known "quantum witness" (Li et al. 2012; Schild and Emary 2015); only the fit into UQCF is new.
- **Sources:** drafts [`086ab0ad`](https://github.com/proteinfoldingengine/WetLabEngine/commit/086ab0ad), [`d96ba223`](https://github.com/proteinfoldingengine/WetLabEngine/commit/d96ba223), [`02818522`](https://github.com/proteinfoldingengine/WetLabEngine/commit/02818522); prereg [`4efed1be`](https://github.com/proteinfoldingengine/WetLabEngine/commit/4efed1be); review [run 39099852840](https://github.com/proteinfoldingengine/WetLabEngine/actions/runs/39099852840) (ACCEPTED); receipt [`5daa4ff5`](https://github.com/proteinfoldingengine/WetLabEngine/commit/5daa4ff5). Folds in four GPT corrections.

### 2026-10-18 · receiver_identification, sections 0-18

Badge: **Restricted** · Gemini ACCEPTED (six frozen reviews) · research branch · NOT_DERIVED

- **Plain summary:** the existing pruning rule picks the receiver by itself. When a pruned piece is absorbed, exactly one retained address (its owner) becomes able to tell the two histories apart; the difference passes up the lineage with one holder per step, is never copied, and adds no information. Under independent background noise the holder can read its own record without an extra channel. Exact rules say how much of the record survives each step, and the receiver can keep knowing *that* an event happened after the details are unrecoverable. The forced single step (section 16) sends the removed weight to its immediate parent. Under three locality rules, owning one's own entry is the only bookkeeping where every pruning counts as the receiver learning (section 17). Section 18 shows the receiver always holds a real trace of the source difference, and reduces the ownership assumptions to one premise, (H-J).
- **Does NOT show:** the native access bridge. Still assumed: independent noise (where used), the receiver naming step, each pruning step occurring, the locality rules / (H-J), and E5. Gemini's "derived" labels were not adopted. GPT found a real formula error after the first acceptance; the draft-1 acceptance does not cover that formula, and the corrected draft 2 was re-reviewed.
- **Sources (frozen reviews, all ACCEPTED):** draft 1 [run 39106192684](https://github.com/proteinfoldingengine/WetLabEngine/actions/runs/39106192684) (superseded formula, see above); draft 2 [`f366da8b`](https://github.com/proteinfoldingengine/WetLabEngine/commit/f366da8b) [run 39109851767](https://github.com/proteinfoldingengine/WetLabEngine/actions/runs/39109851767); draft 5, sections 11-13 [`193cd7ea`](https://github.com/proteinfoldingengine/WetLabEngine/commit/193cd7ea) [run 39133419575](https://github.com/proteinfoldingengine/WetLabEngine/actions/runs/39133419575) (receipts [`6605d237`](https://github.com/proteinfoldingengine/WetLabEngine/commit/6605d237)); draft 8, sections 14-15 [run 39134753017](https://github.com/proteinfoldingengine/WetLabEngine/actions/runs/39134753017); draft 9, section 16 [`bd9a0b9b`](https://github.com/proteinfoldingengine/WetLabEngine/commit/bd9a0b9b) [run 39144601008](https://github.com/proteinfoldingengine/WetLabEngine/actions/runs/39144601008); draft 11, section 17 [`97915416`](https://github.com/proteinfoldingengine/WetLabEngine/commit/97915416) [run 39153538098](https://github.com/proteinfoldingengine/WetLabEngine/actions/runs/39153538098) (receipt [`b2f4e8b7`](https://github.com/proteinfoldingengine/WetLabEngine/commit/b2f4e8b7)); draft 12, section 18 [`c3974458`](https://github.com/proteinfoldingengine/WetLabEngine/commit/c3974458) [run 39162569331](https://github.com/proteinfoldingengine/WetLabEngine/actions/runs/39162569331) (receipt [`3504f172`](https://github.com/proteinfoldingengine/WetLabEngine/commit/3504f172)).

### 2026-10-18 · receiver_identification, section 19

Badge: **Not claimed** · draft 13 · unreviewed

- **Plain summary:** the obvious center-based read fails, but the pruning event itself fixes which readings are meaningful at the receiver, so the measurement choice is now an output rather than put in by hand. (H-J) splits into two simpler premises: (A1) the receiver's state is its own register, and (A2) only readings the event pins down count. GPT's R premise is shown equivalent to E5 on the E1-E4 class, so it swaps that assumption rather than removing it.
- **Does NOT show:** (A1), (A2) or E5 derived; not frozen or reviewed.
- **Sources:** draft 13 [`855c8c06`](https://github.com/proteinfoldingengine/WetLabEngine/commit/855c8c06). No review run yet.

## GPT-agent constructions accepted by Gemini (credited to proteinfolding-gpt)

Badge for each: **Restricted** · research branch · not on main · NOT_DERIVED.

| Date | Construction | What it adds | Source |
|---|---|---|---|
| 2026-10-17 | Retained-fiber conditional review | Conditional fiber result with an explicit native gap | [`c7649112`](https://github.com/proteinfoldingengine/WetLabEngine/commit/c7649112), [run 39061712192](https://github.com/proteinfoldingengine/WetLabEngine/actions/runs/39061712192) |
| 2026-10-17 | Corrected preparability review | Revised branch-split packet (see above) | [`153af9dd`](https://github.com/proteinfoldingengine/WetLabEngine/commit/153af9dd), [run 39076009238](https://github.com/proteinfoldingengine/WetLabEngine/actions/runs/39076009238) |
| 2026-10-18 | Own-view completion | Reconciliation of V997/V1172/V1472/P1/P2/v15.16; no software output equals a receiver-owned record | [`89dab026`](https://github.com/proteinfoldingengine/WetLabEngine/commit/89dab026), [run 39083538884](https://github.com/proteinfoldingengine/WetLabEngine/actions/runs/39083538884) |
| 2026-10-18 | First-pruning own view | Response for the first pruning step | [`e974bcb4`](https://github.com/proteinfoldingengine/WetLabEngine/commit/e974bcb4), [run 39085193731](https://github.com/proteinfoldingengine/WetLabEngine/actions/runs/39085193731) |
| 2026-10-18 | Measurement-first compatibility | Measurement-first reading is compatible with the stack | [run 39088738210](https://github.com/proteinfoldingengine/WetLabEngine/actions/runs/39088738210) |
| 2026-10-18 | Observation preservation (occupied support) | Extension of observation_effect with four corrections | [`4de08e31`](https://github.com/proteinfoldingengine/WetLabEngine/commit/4de08e31), [run 39091716370](https://github.com/proteinfoldingengine/WetLabEngine/actions/runs/39091716370) |
| 2026-10-18 | Occurrence contrast | Preservation vs lumpability vs prefix contrast | [`4d1c0aea`](https://github.com/proteinfoldingengine/WetLabEngine/commit/4d1c0aea), [run 39095260396](https://github.com/proteinfoldingengine/WetLabEngine/actions/runs/39095260396) |
| 2026-10-18 | P1 receiver process | Receiver-process probe and consumer; CONDITIONAL_ONLY | [run 39136458718](https://github.com/proteinfoldingengine/WetLabEngine/actions/runs/39136458718) |
| 2026-10-18 | Ancestry retention | R contract forces P1 without E5 (later shown equivalent to E5 on E1-E4, sec 19) | [`397c08ce`](https://github.com/proteinfoldingengine/WetLabEngine/commit/397c08ce), [run 39143538184](https://github.com/proteinfoldingengine/WetLabEngine/actions/runs/39143538184) |

## What remains open

The native access bridge (NOT_DERIVED); (A1), (A2) and E5; preparability (a single legitimate append is still an assumption, and v15.56 lists it as missing). Occurrence is an accepted input, not an open gap.
