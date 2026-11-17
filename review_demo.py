"""Run one fictional policy review and print the resulting record."""

import argparse
import json


def review(decision):
    original = "Requests for exceptions must be documented."
    amendment = "The procurement lead must approve each exception before it takes effect."
    events = [{
        "event": "revision_proposed",
        "actor": "FELIX (simulated)",
        "finding": "The policy does not identify an approver.",
        "proposed_addition": amendment,
        "active_version": 1,
    }]
    approved = decision == "approve"
    version = 2 if approved else 1
    events.append({
        "event": "revision_approved" if approved else "revision_rejected",
        "actor": "Fictional policy owner",
        "active_version": version,
    })
    return {
        "policy_id": "DEMO-001",
        "version": version,
        "active_text": original + " " + amendment if approved else original,
        "events": events,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("decision", choices=("approve", "reject"))
    print(json.dumps(review(parser.parse_args().decision), indent=2))
