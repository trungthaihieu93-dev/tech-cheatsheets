# React Native + Expo: across the JS/native boundary

Depth: Best practices

For software engineers. New Architecture, Hermes, Fabric, TurboModules and Expo Modules; Android/iOS call paths, threading, lifecycle, development builds and update compatibility. Conceptual API examples; no pinned SDK version or benchmark claims. Legacy bridge is historical context.

## 1. One app, three layers

Stage: Fundamentals
Prerequisites: Basic technical literacy
Takeaway: React Native is a JS application coordinated with a C++ renderer and platform code; Expo supplies a higher-level module and build workflow.
Sheet: topics/01-three-layers.html

## 2. What JSI changed

Stage: Fundamentals
Prerequisites: 01-three-layers
Takeaway: JSI allows direct runtime bindings and native object references, but synchronous calls still consume caller time.
Sheet: topics/02-jsi-versus-bridge.html

## 3. Fabric: from JSX to pixels

Stage: Fundamentals
Prerequisites: 01-three-layers
Takeaway: Render creates a C++ shadow tree, commit computes layout, and mount changes host views on the UI thread.
Sheet: topics/03-fabric-path.html

## 4. TurboModule: typed service API

Stage: Applications
Prerequisites: 02-jsi-versus-bridge
Takeaway: A typed JS specification and Codegen tie a native service contract to Android and iOS implementations.
Sheet: topics/04-turbomodule-contract.html

## 5. Expo Modules: one API, two platforms

Stage: Applications
Prerequisites: 02-jsi-versus-bridge
Takeaway: Expo’s Swift/Kotlin DSL exposes Function, AsyncFunction, events and views over React Native’s low-level primitives.
Sheet: topics/05-expo-module-contract.html

## 6. Threads: keep the caller responsive

Stage: Best practices
Prerequisites: 03-fabric-path, 05-expo-module-contract
Takeaway: Decide on a queue from the work itself: short sync work on JS, platform UI mutations on main, slow work away from both.
Sheet: topics/06-thread-ownership.html

## 7. Native events need a lifecycle

Stage: Best practices
Prerequisites: 04-turbomodule-contract, 05-expo-module-contract
Takeaway: Events are a subscription with cleanup and throughput policy, not an unlimited stream of JS callbacks.
Sheet: topics/07-events-and-lifecycle.html

## 8. The native binary is an API contract

Stage: Best practices
Prerequisites: 05-expo-module-contract
Takeaway: A JS update can only use native APIs already compiled into a compatible binary.
Sheet: topics/08-builds-and-ota.html

## 9. Measure before moving work native

Stage: Further improvements
Prerequisites: 06-thread-ownership, 07-events-and-lifecycle
Takeaway: Measure JS frames, UI frames, payload size and native work before deciding which boundary to change.
Sheet: topics/09-profile-the-boundary.html

## 10. One JS API, honest platform behavior

Stage: Further improvements
Prerequisites: 05-expo-module-contract, 08-builds-and-ota
Takeaway: Share the public contract, then test platform-specific permission, lifecycle, threading and error behavior independently.
Sheet: topics/10-platform-contract.html
