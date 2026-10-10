# Inside React Native: Hermes, Fabric, Modules and Native APIs

Depth: Best practices

Second volume to the React Native + Expo JS/native boundary illustrated pack. Engineer-focused deeper mechanisms in Hermes, Fabric, TurboModules, Expo Modules, Kotlin and Swift platform APIs. Android/iOS thread, ownership, lifecycle, release and diagnosis practices. Conceptual examples; no unverified performance benchmarks or exhaustive SDK tutorial.

## 1. Hermes: build-time bytecode to a running JS heap

Stage: Fundamentals
Prerequisites: Basic technical literacy
Takeaway: Hermes executes the app’s JS; the release bundle is normally compiled to Hermes bytecode at build time.
Sheet: topics/01-hermes-pipeline.html

## 2. Fabric: three trees and three phases

Stage: Fundamentals
Prerequisites: Basic technical literacy
Takeaway: React elements, C++ shadow nodes, and native host views are related representations with different owners.
Sheet: topics/02-fabric-trees.html

## 3. Two authoring paths over one runtime boundary

Stage: Fundamentals
Prerequisites: Basic technical literacy
Takeaway: TurboModules use RN typed specs and Codegen; Expo Modules use a Swift/Kotlin DSL above JSI-related primitives.
Sheet: topics/03-module-interface-map.html

## 4. Kotlin and Swift meet the OS

Stage: Fundamentals
Prerequisites: Basic technical literacy
Takeaway: Native module code runs inside real Android/iOS app lifecycles; a JS Promise cannot erase their rules.
Sheet: topics/04-platform-ownership.html

## 5. Hermes and JSI: runtime versus interface

Stage: Applications
Prerequisites: 01-hermes-pipeline, 03-module-interface-map
Takeaway: Hermes is an engine; JSI is an interface for native code to work with a JS runtime.
Sheet: topics/05-hermes-jsi.html

## 6. Fabric native view: props down, events up

Stage: Applications
Prerequisites: 02-fabric-trees
Takeaway: A native visual surface needs a component contract, host view implementation and event path.
Sheet: topics/06-fabric-native-view.html

## 7. TurboModule Codegen across Android and iOS

Stage: Applications
Prerequisites: 03-module-interface-map
Takeaway: A TS/Flow spec is the shared contract; Codegen and platform implementations fill different layers.
Sheet: topics/07-turbo-codegen.html

## 8. Expo Module DSL in Kotlin and Swift

Stage: Applications
Prerequisites: 03-module-interface-map, 04-platform-ownership
Takeaway: A module definition publishes functions, views and events while choosing native execution queues.
Sheet: topics/08-expo-dsl.html

## 9. Hermes memory: JS heap is only part of the story

Stage: Best practices
Prerequisites: 01-hermes-pipeline, 05-hermes-jsi
Takeaway: Separate JS heap growth from native allocation and resource retention before blaming GC.
Sheet: topics/09-hermes-memory.html

## 10. Fabric scheduling: JS, layout and UI are different budgets

Stage: Best practices
Prerequisites: 02-fabric-trees
Takeaway: The render pipeline can span threads, but host-view mutation remains a UI-thread operation.
Sheet: topics/10-fabric-scheduling.html

## 11. Module call threading and payload shape

Stage: Best practices
Prerequisites: 07-turbo-codegen, 08-expo-dsl
Takeaway: A Promise is an API result, not proof that no work blocks a critical thread.
Sheet: topics/11-module-queues.html

## 12. Android Activity and iOS app lifecycle are not interchangeable

Stage: Best practices
Prerequisites: 04-platform-ownership, 08-expo-dsl
Takeaway: Expose a common JS result but respect different native lifecycle and permission paths.
Sheet: topics/12-platform-lifecycle.html

## 13. Hermes diagnosis lab: startup, long tasks and heap

Stage: Further improvements
Prerequisites: 09-hermes-memory
Takeaway: Treat engine tuning as a measured hypothesis in the app’s full startup and interaction path.
Sheet: topics/13-hermes-diagnosis.html

## 14. Fabric diagnosis lab: render, commit or mount?

Stage: Further improvements
Prerequisites: 10-fabric-scheduling
Takeaway: Optimize the phase that consumes the frame, not the phase whose name is most familiar.
Sheet: topics/14-fabric-diagnosis.html

## 15. Choose the module boundary and ownership model

Stage: Further improvements
Prerequisites: 11-module-queues, 12-platform-lifecycle
Takeaway: Pick the smallest public API that expresses required behavior, then select a module mechanism.
Sheet: topics/15-module-design-choice.html

## 16. Cross-platform contract and native release safety

Stage: Further improvements
Prerequisites: 15-module-design-choice
Takeaway: A JS update can target only a binary containing compatible native modules and configuration.
Sheet: topics/16-release-contract.html
