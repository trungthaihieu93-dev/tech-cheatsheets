# Example review notes

These are teaching specimens, not a complete infrastructure project. YAML parsing and cross-object selectors were checked locally. No cluster API validation or cloud deployment was performed.

## quote-api.yaml

Supply your own non-root image and implement the three HTTP health endpoints on port 3000. Prefer an immutable image digest for an actual release. Requests, limits, probe budgets, HPA bounds and shutdown grace are illustrative values, not measured recommendations.

The image must tolerate a read-only root filesystem and the configured UID/GID. `/tmp` is writable. Add any required other writable paths deliberately. Handle termination in the application and test load-balancer draining; the grace period alone does not make shutdown correct.

The HPA requires a compatible resource Metrics API provider. Strict zone/host spread can leave Pods Pending and does not ensure an independently selected minimum number of eligible zones. Review node placement, spare surge capacity, and dependency capacity. PDB controls eligible evictions; it does not constrain Deployment rollouts or protect against zone failure.

The Service is internal. An ALB/NLB/controller configuration, VPC, node capacity, identity association, data services and telemetry are intentionally outside this specimen. Configure those for your chosen standard-EKS or Auto-Mode contract. The ServiceAccount alone grants no AWS role. Pod Identity or IRSA needs its own platform setup.

## network-policy-specimen.yaml

This exercise only denies traffic and allows a specific CoreDNS label/namespace path. It deliberately does NOT allow the API ingress, database, AWS APIs, identity-agent endpoint or other egress. Applying it can interrupt service. Confirm policy enforcement, actual DNS labels and whether NodeLocal DNS changes the path. Add all required flows before using a deny policy beyond a disposable lab.

## Verification you still need

After adapting the examples, use target-cluster server-side validation, verify admission policy and security-context compatibility, observe probe behavior, load-test HPA and dependencies, and test allowed/denied permissions. No blanket claim of production readiness is made.

Relevant sources: S04, S05, S07–S13, S17, S20, S30 and S36 in the atlas ledger.
