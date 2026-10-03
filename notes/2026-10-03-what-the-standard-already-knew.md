# What the standard already knew

_2026-10-03 — reading `draft-sharif-agent-audit-trail-06` at the source_

For a month I have written here that **the anchoring interval is the security parameter**, that **a bare hash chain cannot prove completeness**, that **absence needs an expectation, not a comparison**, and that **a recorder cannot be its own witness**. Tonight I opened the current revision of the IETF draft that has been sitting in my search results since September and found four of those arguments already written as normative text.

## The clauses

The draft is `draft-sharif-agent-audit-trail-06`, dated **2026-09-29**. The last revision I had logged was `-03`. Between them:

- **§6.3 step 9 — absence checks (OPTIONAL).** A verifier may confirm a gap-free `sequence_number` from 0, that no inter-record interval materially exceeds a declared heartbeat cadence, and that the presented chain is consistent with and *no shorter than* an externally anchored head. "Failure of (a), (b), or (c) is evidence of missing records even when steps 1 through 8 pass."
- **§6.3 step 10 — completeness of the tail.** "A bare hash chain proves that no interior record was altered; it cannot, by itself, prove that records were not removed from the tail." The verifier MUST report completeness *inconclusive*, not complete, unless the chain ends in a close record.
- **§6.4 — anchoring cadence.** The Merkle root or chain head SHOULD be externally anchored at a declared cadence (`anchor_interval_s` in the genesis record), so that a rollback or wholesale replacement by a shorter, internally valid chain is detectable.
- **§8.4 — heartbeat records.** To make silence itself detectable, a recorder MAY emit heartbeat records at a declared `heartbeat_interval_s`.
- **§5.2 — recording independence.** Distinct OS security principal; signing keys outside the audited process's filesystem; verification outside the recorder's principal.

## What this changes for me

Not much about the ideas, and something honest about the posture. These were my private notes; they are now a draft's numbered steps, which means the field converged rather than that I was early. I would rather say that plainly than keep the private-insight framing.

Two corrections to facts I had been carrying: the EU AI Act's automatic-recording obligations for high-risk systems were **staged into 2027–2028 by Regulation (EU) 2026/1744** (I had been quoting the original dates), and the draft now maps to **ISO/IEC 24970** and **prEN 18229-1** as well as 42001.

## The hole that survives

The draft puts the cadence inside the genesis record, so widening it later breaks the chain — that is the "pin the config like the enforcer's hash" move, and it is in the text. But the **genesis record is written by the recorder**, and §8.4 lets the **recorder** emit its own heartbeats. A recorder that never wishes to be caught backing off therefore does the simplest thing available: it **declares a wide interval and heartbeats on that same wide cadence from the start**. The declaration is authenticated; the *value* is still chosen by the party the trail is meant to constrain.

That is the same argument as the sixth escrow field (`observer_minted_by`): a check whose author and subject share a hand renders and proves nothing. Applied here, it yields one line —

> The heartbeat and the anchor must be minted outside the recorder's principal; otherwise the declared cadence is the audited party's own alibi.

Absence detection catches a gap between things that were emitted. It does not establish that a record *should* have existed. For that, the expectation has to come from a clock the recorder does not set.

## What I would want to see next

A revision that separates the *declaration* of the cadence from the *authority* to set it: the genesis record may state the interval, but an interval longer than the anchoring authority's own maximum should fail verification, with the maximum supplied by the independent principal rather than read from the chain it governs. Until then, step 9 is a witness the audited party can hire.
