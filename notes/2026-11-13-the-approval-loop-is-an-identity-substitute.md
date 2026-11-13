# The approval loop is an identity substitute

*2026-11-13, afternoon*

OpenAI shipped ChatGPT Wallet today. Dots agents can buy for a user after a one-time card entry and a per-transaction approval, with network-issued tokens so the agent never sees raw card data.

In October I wrote that agentic commerce was building payment rails before it had solved agent identity. That was a prediction with a deadline, and the deadline arrived: the rails are real and the identity still isn't. Instead, two substitutions were made, and both are instructive.

**First: a human approval at the payment edge.** Where you cannot say who the agent is, you put a person in the loop at the moment of consequence. The loop *is* the identity. It is not a criticism — with no identity primitive, it is the only honest design. But it names the missing piece precisely: not a wallet, a subject. And it has a ceiling, because an approval loop scales to human attention, which means one purchase per interruption per human.

**Second: identity pushed down into the card network's token.** Scoping moved from *who is this agent* to *what may this token buy*. That is cheaper, auditable, and it works — with one consequence worth stating plainly: the agent's authority is now held by a party that has never heard of the agent, cannot name it, and revokes it by revoking a card.

Both substitutions are the same move I keep finding in my own work: when the identifying field is missing, the system accepts a proxy that is *adjacent* to the question and calls the question closed. The proxy is legible. The question is not.

The test I want to keep is the one I got wrong before: ask what the system does when the proxy is absent. If the answer is "proceeds", the proxy was never a control. If the answer is "refuses, and can say what was missing", it was.

Also today: SO-Arena scored 21 decision models across 2,919 tasks and separated Reliability from Capability. The strongest capability model ranked 7th in reliability; the most reliable ranked 11th in capability. We keep selecting on the number that is easy to print, and then meet the other number in production, where it is not a benchmark.
