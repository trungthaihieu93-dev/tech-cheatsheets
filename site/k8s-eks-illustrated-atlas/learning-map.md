# Kubernetes + AWS EKS Illustrated Atlas

Depth: Best practices

Depth 2: fundamentals, applications, production decisions and further improvements for a software practitioner. Fourteen topics, twenty-two editable SVG illustrations, two published customer cases and one hypothetical insurance API scenario. Stable API examples; no claim to exhaustive ecosystem or cluster-version coverage. No AWS deployment or measured performance result.

## 1. Kubernetes: APIs, control loops and execution

Stage: Fundamentals
Prerequisites: Basic technical literacy
Takeaway: Kubernetes continually tries to converge on your declared state; convergence and business correctness are different promises.
Sheet: topics/01-control-loops.html

## 2. Workloads, configuration and ownership

Stage: Fundamentals
Prerequisites: 01-control-loops
Takeaway: Choose the workload controller for the lifecycle you need, then separate configuration from the image.
Sheet: topics/02-objects.html

## 3. Networking: DNS, Services, routing and VPC IPs

Stage: Fundamentals
Prerequisites: 01-control-loops, 02-objects
Takeaway: Separate the configuration path from the request path, and treat IP space as a capacity constraint.
Sheet: topics/03-networking.html

## 4. EKS responsibility boundaries and compute choices

Stage: Fundamentals
Prerequisites: 01-control-loops
Takeaway: Select how much infrastructure AWS operates, without giving away application ownership.
Sheet: topics/04-eks-model.html

## 5. IAM, Kubernetes RBAC and workload identity

Stage: Applications
Prerequisites: 04-eks-model, 02-objects
Takeaway: Keep engineer-to-cluster, Pod-to-AWS and user-to-product authorization separate.
Sheet: topics/05-identities.html

## 6. Storage, state and recovery

Stage: Applications
Prerequisites: 02-objects, 04-eks-model
Takeaway: Persistence, replication and backup solve different failure cases.
Sheet: topics/06-data.html

## 7. Worked case: a multi-tenant insurance API on EKS

Stage: Applications
Prerequisites: 03-networking, 05-identities, 06-data
Takeaway: Keep the API stateless, bound downstream concurrency and make asynchronous work safe to retry.
Sheet: topics/07-insurtech.html

## 8. Published cases: healthcare SaaS and ML search ranking

Stage: Applications
Prerequisites: 04-eks-model, 03-networking, 06-data
Takeaway: Transfer the decision pattern; do not copy the published performance number as your own forecast.
Sheet: topics/08-customer-cases.html

## 9. Probes, rollouts, disruption and availability

Stage: Best practices
Prerequisites: 02-objects, 03-networking, 04-eks-model
Takeaway: Readiness controls participation; liveness restarts; placement and rollout controls govern other failure paths.
Sheet: topics/09-release-reliability.html

## 10. Capacity: requests, HPA and node provisioning

Stage: Best practices
Prerequisites: 04-eks-model, 09-release-reliability
Takeaway: Measure the bottleneck, then scale the layer that can relieve it.
Sheet: topics/10-scaling.html

## 11. Tenancy, least privilege and network policy

Stage: Best practices
Prerequisites: 05-identities, 03-networking
Takeaway: A namespace is an organizational boundary; build the actual trust boundary explicitly.
Sheet: topics/11-security.html

## 12. Observe and diagnose the right layer

Stage: Best practices
Prerequisites: 03-networking, 09-release-reliability, 10-scaling
Takeaway: Start from user-visible failure, then follow evidence down the request path.
Sheet: topics/12-observability.html

## 13. Upgrades, recovery paths and the full bill

Stage: Further improvements
Prerequisites: 04-eks-model, 09-release-reliability, 12-observability
Takeaway: Budget compatibility work and recovery before the support calendar makes the decision for you.
Sheet: topics/13-lifecycle.html

## 14. A practical learning path and improvement experiments

Stage: Further improvements
Prerequisites: 13-lifecycle, 11-security, 10-scaling
Takeaway: Make every improvement a hypothesis with a measured success condition.
Sheet: topics/14-practice.html
