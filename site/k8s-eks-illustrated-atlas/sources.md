# Sources and further reading

## [S01] Kubernetes cluster architecture

https://kubernetes.io/docs/concepts/architecture/
Publisher: Kubernetes
Accessed: 2026-10-10
Kind: documentation
Supports: API server, etcd, scheduler, controllers, kubelet and runtime responsibilities
Further reading: Read the linked primary source for implementation details and current constraints.
Limits: Illustrations simplify implementation details. Customer outcomes are vendor-published, not independently reproduced.

## [S02] Kubernetes controllers

https://kubernetes.io/docs/concepts/architecture/controller/
Publisher: Kubernetes
Accessed: 2026-10-10
Kind: documentation
Supports: Controllers compare desired and observed state and act through APIs
Further reading: Read the linked primary source for implementation details and current constraints.
Limits: Illustrations simplify implementation details. Customer outcomes are vendor-published, not independently reproduced.

## [S03] Workloads

https://kubernetes.io/docs/concepts/workloads/
Publisher: Kubernetes
Accessed: 2026-10-10
Kind: documentation
Supports: Deployment, StatefulSet, DaemonSet, Job and CronJob use cases
Further reading: Read the linked primary source for implementation details and current constraints.
Limits: Illustrations simplify implementation details. Customer outcomes are vendor-published, not independently reproduced.

## [S04] Deployments

https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
Publisher: Kubernetes
Accessed: 2026-10-10
Kind: documentation
Supports: ReplicaSet ownership, rolling updates, surge and unavailable settings
Further reading: Read the linked primary source for implementation details and current constraints.
Limits: Illustrations simplify implementation details. Customer outcomes are vendor-published, not independently reproduced.

## [S05] Service

https://kubernetes.io/docs/concepts/services-networking/service/
Publisher: Kubernetes
Accessed: 2026-10-10
Kind: documentation
Supports: Service selection, stable access and EndpointSlices
Further reading: Read the linked primary source for implementation details and current constraints.
Limits: Illustrations simplify implementation details. Customer outcomes are vendor-published, not independently reproduced.

## [S06] Persistent volumes

https://kubernetes.io/docs/concepts/storage/persistent-volumes/
Publisher: Kubernetes
Accessed: 2026-10-10
Kind: documentation
Supports: PVC, PV, provisioning and reclaim lifecycle
Further reading: Read the linked primary source for implementation details and current constraints.
Limits: Illustrations simplify implementation details. Customer outcomes are vendor-published, not independently reproduced.

## [S07] Resource management

https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
Publisher: Kubernetes
Accessed: 2026-10-10
Kind: documentation
Supports: Requests, limits, scheduling, CPU throttling and memory enforcement
Further reading: Read the linked primary source for implementation details and current constraints.
Limits: Illustrations simplify implementation details. Customer outcomes are vendor-published, not independently reproduced.

## [S08] Horizontal Pod Autoscaling

https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/
Publisher: Kubernetes
Accessed: 2026-10-10
Kind: documentation
Supports: Metric ratio algorithm, CPU utilization relative to requests, metric pipeline
Further reading: Read the linked primary source for implementation details and current constraints.
Limits: Illustrations simplify implementation details. Customer outcomes are vendor-published, not independently reproduced.

## [S09] Disruptions

https://kubernetes.io/docs/concepts/workloads/pods/disruptions/
Publisher: Kubernetes
Accessed: 2026-10-10
Kind: documentation
Supports: PDB limits eviction; involuntary failure and rollout limitations
Further reading: Read the linked primary source for implementation details and current constraints.
Limits: Illustrations simplify implementation details. Customer outcomes are vendor-published, not independently reproduced.

## [S10] Liveness, readiness and startup probes

https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/
Publisher: Kubernetes
Accessed: 2026-10-10
Kind: documentation
Supports: Probe actions and startup protection
Further reading: Read the linked primary source for implementation details and current constraints.
Limits: Illustrations simplify implementation details. Customer outcomes are vendor-published, not independently reproduced.

## [S11] RBAC good practices

https://kubernetes.io/docs/concepts/security/rbac-good-practices/
Publisher: Kubernetes
Accessed: 2026-10-10
Kind: documentation
Supports: Least privilege and weak namespace boundaries
Further reading: Read the linked primary source for implementation details and current constraints.
Limits: Illustrations simplify implementation details. Customer outcomes are vendor-published, not independently reproduced.

## [S12] Network policies

https://kubernetes.io/docs/concepts/services-networking/network-policies/
Publisher: Kubernetes
Accessed: 2026-10-10
Kind: documentation
Supports: L4 policy, enforcement dependency, default allowance, DNS egress
Further reading: Read the linked primary source for implementation details and current constraints.
Limits: Illustrations simplify implementation details. Customer outcomes are vendor-published, not independently reproduced.

## [S13] Topology spread constraints

https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/
Publisher: Kubernetes
Accessed: 2026-10-10
Kind: documentation
Supports: Zone and host distribution, strict scheduling constraints
Further reading: Read the linked primary source for implementation details and current constraints.
Limits: Illustrations simplify implementation details. Customer outcomes are vendor-published, not independently reproduced.

## [S14] What is Amazon EKS?

https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html
Publisher: AWS
Accessed: 2026-10-10
Kind: documentation
Supports: Managed Kubernetes and AWS integration
Further reading: Read the linked primary source for implementation details and current constraints.
Limits: Illustrations simplify implementation details. Customer outcomes are vendor-published, not independently reproduced.

## [S15] EKS Auto Mode

https://docs.aws.amazon.com/eks/latest/userguide/automode.html
Publisher: AWS
Accessed: 2026-10-10
Kind: documentation
Supports: Managed compute, networking, load balancing and block storage
Further reading: Read the linked primary source for implementation details and current constraints.
Limits: Illustrations simplify implementation details. Customer outcomes are vendor-published, not independently reproduced.

## [S16] EKS compute options

https://docs.aws.amazon.com/eks/latest/userguide/eks-compute.html
Publisher: AWS
Accessed: 2026-10-10
Kind: documentation
Supports: Auto Mode, managed nodes, self-managed nodes, Fargate, Hybrid Nodes
Further reading: Read the linked primary source for implementation details and current constraints.
Limits: Illustrations simplify implementation details. Customer outcomes are vendor-published, not independently reproduced.

## [S17] EKS Pod Identity

https://docs.aws.amazon.com/eks/latest/userguide/pod-identities.html
Publisher: AWS
Accessed: 2026-10-10
Kind: documentation
Supports: Service account role associations, agent, SDK support and Linux EC2 scope
Further reading: Read the linked primary source for implementation details and current constraints.
Limits: Illustrations simplify implementation details. Customer outcomes are vendor-published, not independently reproduced.

## [S18] EKS access entries

https://docs.aws.amazon.com/eks/latest/userguide/access-entries.html
Publisher: AWS
Accessed: 2026-10-10
Kind: documentation
Supports: IAM principal access with EKS access policies or Kubernetes groups
Further reading: Read the linked primary source for implementation details and current constraints.
Limits: Illustrations simplify implementation details. Customer outcomes are vendor-published, not independently reproduced.

## [S19] VPC and subnet considerations

https://docs.aws.amazon.com/eks/latest/best-practices/subnets.html
Publisher: AWS
Accessed: 2026-10-10
Kind: documentation
Supports: Cluster subnets, private endpoint access, upgrade IP headroom
Further reading: Read the linked primary source for implementation details and current constraints.
Limits: Illustrations simplify implementation details. Customer outcomes are vendor-published, not independently reproduced.

## [S20] AWS Load Balancer Controller

https://docs.aws.amazon.com/eks/latest/userguide/aws-load-balancer-controller.html
Publisher: AWS
Accessed: 2026-10-10
Kind: documentation
Supports: Ingress to ALB and Service LoadBalancer to NLB integration
Further reading: Read the linked primary source for implementation details and current constraints.
Limits: Illustrations simplify implementation details. Customer outcomes are vendor-published, not independently reproduced.

## [S21] EBS CSI integration

https://docs.aws.amazon.com/eks/latest/userguide/ebs-csi.html
Publisher: AWS
Accessed: 2026-10-10
Kind: documentation
Supports: EBS support limits and different Auto Mode provisioner
Further reading: Read the linked primary source for implementation details and current constraints.
Limits: Illustrations simplify implementation details. Customer outcomes are vendor-published, not independently reproduced.

## [S22] Cluster upgrade best practices

https://docs.aws.amazon.com/eks/latest/best-practices/cluster-upgrades.html
Publisher: AWS
Accessed: 2026-10-10
Kind: documentation
Supports: Compatibility, removed APIs, node upgrades and add-on coordination
Further reading: Read the linked primary source for implementation details and current constraints.
Limits: Illustrations simplify implementation details. Customer outcomes are vendor-published, not independently reproduced.

## [S23] Amazon EKS pricing

https://aws.amazon.com/eks/pricing/
Publisher: AWS
Accessed: 2026-10-10
Kind: pricing
Supports: Standard and extended support charges and separate compute costs
Further reading: Read the linked primary source for implementation details and current constraints.
Limits: Illustrations simplify implementation details. Customer outcomes are vendor-published, not independently reproduced.

## [S24] Booking.com search ranking on Amazon EKS

https://aws.amazon.com/solutions/case-studies/booking-eks-case-study/
Publisher: AWS / Booking.com
Accessed: 2026-10-10
Kind: customer case study
Supports: Dedicated ranking cluster, phased migration and reported latency
Further reading: Read the linked primary source for implementation details and current constraints.
Limits: Illustrations simplify implementation details. Customer outcomes are vendor-published, not independently reproduced.

## [S25] Crossuite migration to EKS

https://aws.amazon.com/solutions/case-studies/crossuite-eks-case-study/
Publisher: AWS / Crossuite
Accessed: 2026-10-10
Kind: customer case study
Supports: HPA, Karpenter, ALB, RDS PostgreSQL, CloudWatch and reported outcomes
Further reading: Read the linked primary source for implementation details and current constraints.
Limits: Illustrations simplify implementation details. Customer outcomes are vendor-published, not independently reproduced.

## [S26] Karpenter best practices

https://docs.aws.amazon.com/eks/latest/best-practices/karpenter.html
Publisher: AWS
Accessed: 2026-10-10
Kind: documentation
Supports: Pending workload capacity, diversification and interruption handling
Further reading: Read the linked primary source for implementation details and current constraints.
Limits: Illustrations simplify implementation details. Customer outcomes are vendor-published, not independently reproduced.

## [S27] Kubernetes observability

https://kubernetes.io/docs/concepts/cluster-administration/observability/
Publisher: Kubernetes
Accessed: 2026-10-10
Kind: documentation
Supports: Metrics, logs, traces and resource Metrics API distinction
Further reading: Read the linked primary source for implementation details and current constraints.
Limits: Illustrations simplify implementation details. Customer outcomes are vendor-published, not independently reproduced.

## [S28] EKS control plane logs

https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html
Publisher: AWS
Accessed: 2026-10-10
Kind: documentation
Supports: Optional API, audit, authenticator, scheduler and controller logging
Further reading: Read the linked primary source for implementation details and current constraints.
Limits: Illustrations simplify implementation details. Customer outcomes are vendor-published, not independently reproduced.

## [S29] EFS CSI integration

https://docs.aws.amazon.com/eks/latest/userguide/efs-csi.html
Publisher: AWS
Accessed: 2026-10-10
Kind: documentation
Supports: Shared filesystem integration and Fargate static provisioning constraint
Further reading: Read the linked primary source for implementation details and current constraints.
Limits: Illustrations simplify implementation details. Customer outcomes are vendor-published, not independently reproduced.

## [S30] AWS Fargate for EKS

https://docs.aws.amazon.com/eks/latest/userguide/fargate.html
Publisher: AWS
Accessed: 2026-10-10
Kind: documentation
Supports: No DaemonSets, privileged containers or GPUs; private subnets and IP targets
Further reading: Read the linked primary source for implementation details and current constraints.
Limits: Illustrations simplify implementation details. Customer outcomes are vendor-published, not independently reproduced.

## [S31] Update an EKS cluster

https://docs.aws.amazon.com/eks/latest/userguide/update-cluster.html
Publisher: AWS
Accessed: 2026-10-10
Kind: documentation
Supports: Control plane and component upgrade sequencing
Further reading: Read the linked primary source for implementation details and current constraints.
Limits: Illustrations simplify implementation details. Customer outcomes are vendor-published, not independently reproduced.

## [S32] IAM roles for service accounts

https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html
Publisher: AWS
Accessed: 2026-10-10
Kind: documentation
Supports: OIDC service account tokens and STS temporary credentials
Further reading: Read the linked primary source for implementation details and current constraints.
Limits: Illustrations simplify implementation details. Customer outcomes are vendor-published, not independently reproduced.

## [S33] Kubernetes multi-tenancy

https://kubernetes.io/docs/concepts/security/multi-tenancy/
Publisher: Kubernetes
Accessed: 2026-10-10
Kind: documentation
Supports: Control and data plane isolation; shared kernels and dedicated clusters
Further reading: Read the linked primary source for implementation details and current constraints.
Limits: Illustrations simplify implementation details. Customer outcomes are vendor-published, not independently reproduced.

## [S34] Amazon VPC CNI

https://docs.aws.amazon.com/eks/latest/userguide/managing-vpc-cni.html
Publisher: AWS
Accessed: 2026-10-10
Kind: documentation
Supports: VPC private addresses per Pod and Auto Mode networking ownership
Further reading: Read the linked primary source for implementation details and current constraints.
Limits: Illustrations simplify implementation details. Customer outcomes are vendor-published, not independently reproduced.

## [S35] ConfigMaps

https://kubernetes.io/docs/concepts/configuration/configmap/
Publisher: Kubernetes
Accessed: 2026-10-10
Kind: documentation
Supports: Non-confidential runtime configuration
Further reading: Read the linked primary source for implementation details and current constraints.
Limits: Illustrations simplify implementation details. Customer outcomes are vendor-published, not independently reproduced.

## [S36] Kubernetes Secret good practices

https://kubernetes.io/docs/concepts/security/secrets-good-practices/
Publisher: Kubernetes
Accessed: 2026-10-10
Kind: documentation
Supports: Base64 is encoding, least privilege and encryption considerations
Further reading: Read the linked primary source for implementation details and current constraints.
Limits: Illustrations simplify implementation details. Customer outcomes are vendor-published, not independently reproduced.

## [S37] EKS reliability

https://docs.aws.amazon.com/eks/latest/best-practices/reliability.html
Publisher: AWS
Accessed: 2026-10-10
Kind: documentation
Supports: Control plane across three AZs; shared data plane responsibility
Further reading: Read the linked primary source for implementation details and current constraints.
Limits: Illustrations simplify implementation details. Customer outcomes are vendor-published, not independently reproduced.

## [S38] EKS version rollback

https://docs.aws.amazon.com/eks/latest/userguide/rollback-cluster.html
Publisher: AWS
Accessed: 2026-10-10
Kind: documentation
Supports: Current documented seven-day, one-minor-version rollback window and limitations
Further reading: Read the linked primary source for implementation details and current constraints.
Limits: Illustrations simplify implementation details. Customer outcomes are vendor-published, not independently reproduced.

## [S39] Amazon EBS volumes

https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volumes.html
Publisher: AWS
Accessed: 2026-10-10
Kind: documentation
Supports: Volumes and attached instances must be in the same Availability Zone
Further reading: Read the linked primary source for implementation details and current constraints.
Limits: Illustrations simplify implementation details. Customer outcomes are vendor-published, not independently reproduced.
