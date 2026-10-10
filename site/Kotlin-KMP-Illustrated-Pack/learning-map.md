# Kotlin & KMP — Illustrated Field Guide

Depth: Best practices

Level 2 · fundamentals and best practices for a software engineer. Twelve topic sheets cover language contracts, collections, models, functions, coroutines, flows, Android/iOS compilation, platform seams, UI sharing, Swift interop, memory, and validation. Official rolling documentation checked on 9 October 2026; current Swift export is Alpha. Code is illustrative and reasoned through, not compiled or executed on Android/iOS. This is a focused mobile introduction, not a complete Kotlin course or ecosystem comparison.

## 1. Nullability: make absence explicit

Stage: Fundamentals
Prerequisites: basic programming
Takeaway: Treat missing data as a modeled case, not a surprise hidden behind !!.
Sheet: topics/01-nullability.html

## 2. val, collections, and ownership

Stage: Fundamentals
Prerequisites: 01-nullability
Takeaway: val fixes a binding; immutability is a property of the reachable object graph.
Sheet: topics/02-ownership.html

## 3. Data classes and sealed state models

Stage: Fundamentals
Prerequisites: 02-ownership
Takeaway: Use data classes for payloads and sealed variants for a closed set of outcomes.
Sheet: topics/03-models.html

## 4. Functions, lambdas, and readable transformations

Stage: Fundamentals
Prerequisites: 03-models
Takeaway: Short code earns its keep only when the next reader can see the rule.
Sheet: topics/04-functions.html

## 5. Coroutines: suspension with owned lifetimes

Stage: Fundamentals
Prerequisites: 04-functions
Takeaway: Every long-lived task needs an owner, a cancellation path, and cleanup.
Sheet: topics/05-coroutines.html

## 6. Flow and StateFlow: work versus state

Stage: Applications
Prerequisites: 05-coroutines
Takeaway: StateFlow describes what is true now; it does not preserve every event.
Sheet: topics/06-flows.html

## 7. KMP: source sets become platform binaries

Stage: Applications
Prerequisites: 05-coroutines
Takeaway: commonMain is shared source compiled per target, not a runtime shared between phones.
Sheet: topics/07-compilation.html

## 8. Platform capabilities: contracts and adapters

Stage: Applications
Prerequisites: 07-compilation
Takeaway: Name the capability in common code; choose its concrete implementation at composition.
Sheet: topics/08-ports.html

## 9. Choose the UI sharing boundary deliberately

Stage: Best practices
Prerequisites: 08-ports, 06-flows
Takeaway: Share the behavior that benefits the team; validate the experience on each OS.
Sheet: topics/09-ui-boundary.html

## 10. Swift interop: exported APIs need design

Stage: Best practices
Prerequisites: 05-coroutines, 06-flows, 08-ports
Takeaway: An API that is pleasant in Kotlin may need a narrower Swift-facing facade.
Sheet: topics/10-swift-interop.html

## 11. Native memory, callbacks, and performance

Stage: Best practices
Prerequisites: 10-swift-interop, 02-ownership
Takeaway: Compiled native code still has a runtime, allocation costs, and ownership obligations.
Sheet: topics/11-memory.html

## 12. Validate on both targets, then expand

Stage: Further improvements
Prerequisites: 11-memory, 09-ui-boundary
Takeaway: Optimize the amount of trustworthy sharing, not the percentage of shared lines.
Sheet: topics/12-validation.html
