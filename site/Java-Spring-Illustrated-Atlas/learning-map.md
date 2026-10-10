# Java & Spring — Illustrated Engineering Atlas

Depth: Best practices

Depth 2: fundamentals and best practices for a working software engineer. 32 topics cover Java contracts and runtime, Framework core, Boot, web/data/security, messaging/integration/batch, Cloud, testing/observability and optional Modulith/AI/native/specialist capabilities. This is a broad mechanism atlas, not exhaustive documentation of every Spring API or cloud subproject. Java examples use non-preview constructs from modern Java (records require 16+; virtual threads 21+). Research anchors Java SE 25 and live Spring documentation retrieved 2026-10-09. The retrieved Boot system-requirements page reports Boot 4.1.1, Framework 7.0.9+, Java 17–26. Use the matching BOM and supported project generations; do not combine displayed individual project versions arbitrarily. Code snippets are illustrative and were not compiled as a complete application. Choices and improvements marked synthesis are reasoned recommendations, not measured performance results.

## 1. Java, Framework, Boot: find the layers

Stage: Fundamentals
Prerequisites: Basic technical literacy
Takeaway: Know the owner of a behavior before debugging its annotations.
Sheet: topics/01-ecosystem.html

## 2. Types, objects, records and domain invariants

Stage: Fundamentals
Prerequisites: 01-ecosystem
Takeaway: A type should make the wrong state harder to represent.
Sheet: topics/02-types.html

## 3. Collections, generics and equality

Stage: Fundamentals
Prerequisites: 01-ecosystem
Takeaway: Collection contracts are part of your domain contract.
Sheet: topics/03-collections.html

## 4. Lambdas, streams and honest parallelism

Stage: Fundamentals
Prerequisites: 01-ecosystem
Takeaway: Readable transformation beats decorative functional syntax.
Sheet: topics/04-streams.html

## 5. Resource ownership and decimal money

Stage: Fundamentals
Prerequisites: 01-ecosystem
Takeaway: Memory, resources and money each need their own ownership rules.
Sheet: topics/05-resources-money.html

## 6. Concurrency, visibility and virtual threads

Stage: Fundamentals
Prerequisites: 01-ecosystem
Takeaway: Cheap waiting is not unlimited throughput.
Sheet: topics/06-concurrency.html

## 7. JVM, JIT, garbage collection and diagnosis

Stage: Fundamentals
Prerequisites: 01-ecosystem
Takeaway: Observe the bottleneck before tuning the JVM.
Sheet: topics/07-jvm.html

## 8. IoC, constructor injection and bean definitions

Stage: Fundamentals
Prerequisites: 01-ecosystem
Takeaway: The container should assemble your design, not become your design.
Sheet: topics/08-ioc.html

## 9. Scopes, lifecycle and thread-safe singleton design

Stage: Fundamentals
Prerequisites: 01-ecosystem
Takeaway: Scope controls lifetime; it does not grant thread safety.
Sheet: topics/09-bean-lifecycle.html

## 10. AOP proxies: why annotations sometimes vanish

Stage: Fundamentals
Prerequisites: 01-ecosystem
Takeaway: An annotation is metadata; the invocation path makes it operational.
Sheet: topics/10-proxies.html

## 11. Spring Boot: conditional assembly, not sorcery

Stage: Fundamentals
Prerequisites: 01-ecosystem
Takeaway: Auto-configuration is conditional code you can inspect.
Sheet: topics/11-boot.html

## 12. Configuration, profiles and secret boundaries

Stage: Applications
Prerequisites: 01-ecosystem
Takeaway: Debug the effective configuration, not just the file you edited.
Sheet: topics/12-config.html

## 13. MVC request flow, DTO validation and errors

Stage: Applications
Prerequisites: 01-ecosystem
Takeaway: Validate syntax at transport boundaries and invariants in the domain.
Sheet: topics/13-mvc.html

## 14. MVC, WebFlux and virtual threads: choose by constraints

Stage: Applications
Prerequisites: 01-ecosystem
Takeaway: Choose an execution model for your dependencies, not your fashion sense.
Sheet: topics/14-reactive.html

## 15. Spring Data: repositories, aggregates and fetch plans

Stage: Applications
Prerequisites: 01-ecosystem
Takeaway: Repository convenience does not cancel database physics.
Sheet: topics/15-data.html

## 16. Transactions, rollback and propagation boundaries

Stage: Applications
Prerequisites: 01-ecosystem
Takeaway: A local transaction is a precise boundary, not a universal undo button.
Sheet: topics/16-transactions.html

## 17. Security filters, JWT and domain authorization

Stage: Applications
Prerequisites: 01-ecosystem
Takeaway: Authentication names the caller; authorization constrains the action.
Sheet: topics/17-security.html

## 18. Sessions, browser credentials and CSRF

Stage: Applications
Prerequisites: 01-ecosystem
Takeaway: Understand how credentials travel before disabling protections.
Sheet: topics/18-sessions.html

## 19. Caching: keys, freshness and invalidation

Stage: Applications
Prerequisites: 01-ecosystem
Takeaway: Every cache needs an owner, a key contract and a freshness promise.
Sheet: topics/19-cache.html

## 20. Kafka, AMQP and Pulsar: delivery boundaries

Stage: Applications
Prerequisites: 01-ecosystem
Takeaway: Assume retries can repeat business work unless your boundary proves otherwise.
Sheet: topics/20-messaging.html

## 21. Spring Integration: adapters, channels and routing

Stage: Applications
Prerequisites: 01-ecosystem
Takeaway: A diagrammed integration flow still needs a capacity model.
Sheet: topics/21-integration.html

## 22. Spring Batch: chunk commits and safe restarts

Stage: Applications
Prerequisites: 01-ecosystem
Takeaway: Restartability is a data contract, not a checkbox.
Sheet: topics/22-batch.html

## 23. Spring Cloud: select distributed capabilities

Stage: Applications
Prerequisites: 01-ecosystem
Takeaway: Distribute deliberately; pay the network bill consciously.
Sheet: topics/23-cloud.html

## 24. REST, GraphQL, gRPC and hypermedia

Stage: Applications
Prerequisites: 01-ecosystem
Takeaway: Transport changes the contract shape; business rules still need enforcement.
Sheet: topics/24-api-contracts.html

## 25. Tests that catch wiring, persistence and HTTP failures

Stage: Best practices
Prerequisites: 01-ecosystem
Takeaway: Test the boundary where the defect can actually occur.
Sheet: topics/25-testing.html

## 26. Actuator, observations, metrics and traces

Stage: Best practices
Prerequisites: 01-ecosystem
Takeaway: A dashboard earns its place by answering a failure question.
Sheet: topics/26-observability.html

## 27. Timeouts, retries, bulkheads and scheduled work

Stage: Best practices
Prerequisites: 01-ecosystem
Takeaway: Resilience protects a budget; it does not promise eventual success.
Sheet: topics/27-resilience.html

## 28. Modulith: enforce domain boundaries before distribution

Stage: Further improvements
Prerequisites: 01-ecosystem
Takeaway: Make boundaries real before making them remote.
Sheet: topics/28-modulith.html

## 29. Spring AI: retrieval and tools with controlled authority

Stage: Further improvements
Prerequisites: 01-ecosystem
Takeaway: The model can suggest an action; the application must authorize it.
Sheet: topics/29-ai.html

## 30. AOT and native images: optimize the deployment case

Stage: Further improvements
Prerequisites: 01-ecosystem
Takeaway: Optimize the lifecycle that dominates your real cost.
Sheet: topics/30-native.html

## 31. Specialist Spring projects: choose the protocol

Stage: Applications
Prerequisites: 01-ecosystem
Takeaway: Use the smallest set of projects that honors your actual contracts.
Sheet: topics/31-specialists.html

## 32. A production learning loop and migration compass

Stage: Further improvements
Prerequisites: 01-ecosystem
Takeaway: Learn the mechanism, state the constraint, measure the change.
Sheet: topics/32-improvement-loop.html
