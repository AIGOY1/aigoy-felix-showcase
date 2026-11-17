# AIGOY and FELIX | Who approves a policy change?

I built AIGOY, a governance, risk and compliance platform for European SMEs, and FELIX, its compliance agent. One product decision was where to draw the line between drafting a change and authorising it.

This standalone example uses a fictional policy and scripted decisions to illustrate that boundary. The sample runs locally with Python 3 and uses no services, credentials or customer data.

## Follow one amendment

A procurement team uses this policy: “Requests for exceptions must be documented.” During review, FELIX flags a missing detail: who can approve an exception? It proposes adding: “The procurement lead must approve each exception before it takes effect.”

| Step | Active policy | What the reviewer can trace |
| --- | --- | --- |
| FELIX submits its draft | Original wording | Proposed amendment and finding |
| Policy owner rejects it | Original wording | Rejection and reviewer |
| Policy owner approves it instead | Amended wording | Approval, reviewer and new version |

## Try both outcomes

Run these commands separately. Each starts a fresh fictional case. Compare the policy version, active text and event history in the JSON output.

```sh
python3 review_demo.py reject
python3 review_demo.py approve
```

The reviewer identity is fixed for illustration. The output is an in-memory example of an audit record. Production authentication, storage and model calls are outside this sample.

## The customer conversation

Before proposing a pilot, I would ask the policy owner to walk me through the last amendment. How long went into drafting? How long did it wait for approval? If review is the bottleneck, faster drafting alone will do little for lead time. I would agree on the baseline with the owner and check that every accepted amendment can be traced to its reviewer.

Tom Brandt · [AIGOY product overview](https://www.aigoy.de/)
