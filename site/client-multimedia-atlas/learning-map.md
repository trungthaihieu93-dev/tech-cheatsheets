# Client Multimedia Libraries — Illustrated Atlas

Depth: Libs/frameworks/stacks

Depth 3 · All eight pictured libraries · 18 illustrated topics · 3 worked reference architectures. Covers browser-side playback with React-oriented examples and framework-neutral engines. Current primary documentation was reviewed on 10 October 2026; v10 example targets @videojs/react 10.0.1. Other snippets describe documented interfaces and need a project lockfile/device test. Worked cases are proposed designs, not published customer outcomes. Popularity/download counts in the screenshot are intentionally not used as evidence. Code was not executed against live media; no performance measurements are claimed. Clappr component repositories are historical and point to its monorepo.

## 1. Name the layer before choosing the library

Stage: Fundamentals
Prerequisites: Basic technical literacy
Takeaway: Player UI, provider integration, streaming engine and video infrastructure are separate decisions.
Sheet: topics/01-layer-map.html

## 2. A video URL is only the beginning

Stage: Fundamentals
Prerequisites: 01-layer-map
Takeaway: A successful fetch does not prove that the browser can decode the media.
Sheet: topics/02-browser-pipeline.html

## 3. HLS, DASH, ABR and the buffer budget

Stage: Fundamentals
Prerequisites: 02-browser-pipeline
Takeaway: ABR trades quality against the risk of draining the playback buffer.
Sheet: topics/03-adaptive-streaming.html

## 4. Video.js: mature ecosystem, new v10 model

Stage: Applications
Prerequisites: 03-adaptive-streaming
Takeaway: Treat v8 → v10 as an integration migration, not a package-version bump.
Sheet: topics/04-videojs.html

## 5. ReactPlayer: one façade, several providers

Stage: Applications
Prerequisites: 01-layer-map
Takeaway: Normalize integration, but preserve provider-specific capabilities and failures.
Sheet: topics/05-reactplayer.html

## 6. React YouTube: keep the iframe contract small

Stage: Applications
Prerequisites: 05-reactplayer
Takeaway: Use the provider API after readiness; do not treat the iframe as your own video DOM.
Sheet: topics/06-react-youtube.html

## 7. Mux Player: optimized for the Mux path

Stage: Applications
Prerequisites: 03-adaptive-streaming
Takeaway: Mux Player reduces integration work when delivery and analytics already use Mux.
Sheet: topics/07-mux-player.html

## 8. Vidstack: a useful architecture with a maintenance boundary

Stage: Applications
Prerequisites: 04-videojs
Takeaway: Study Vidstack’s separation of state and providers, but include its maintenance status in adoption decisions.
Sheet: topics/08-vidstack.html

## 9. hls.js: HLS engine, not a complete branded player

Stage: Applications
Prerequisites: 03-adaptive-streaming
Takeaway: Own initialization, fallback, cleanup and error reporting when using a low-level engine.
Sheet: topics/09-hlsjs.html

## 10. dash.js: reference MPEG-DASH implementation

Stage: Applications
Prerequisites: 03-adaptive-streaming
Takeaway: MPD, browser capabilities, packaging and license setup must agree.
Sheet: topics/10-dashjs.html

## 11. Clappr: an extensible player for plugin-based products

Stage: Applications
Prerequisites: 09-hlsjs
Takeaway: Extensibility is useful only when plugin versions and lifecycle ownership remain clear.
Sheet: topics/11-clappr.html

## 12. Worked case: mixed-provider learning portal

Stage: Applications
Prerequisites: 05-reactplayer, 06-react-youtube
Takeaway: A shared catalog model is more durable than pretending every provider has the same features.
Sheet: topics/12-case-portal.html

## 13. Worked case: protected enterprise training

Stage: Applications
Prerequisites: 07-mux-player, 12-case-portal
Takeaway: Own tenant authorization on the backend; deliver media through a constrained playback capability.
Sheet: topics/13-case-protected.html

## 14. Worked case: live event with chat and replay

Stage: Applications
Prerequisites: 09-hlsjs, 10-dashjs
Takeaway: Reducing player buffer alone cannot remove upstream live latency.
Sheet: topics/14-case-live.html

## 15. Lifecycle, SSR, accessibility and user intent

Stage: Best practices
Prerequisites: 11-clappr, 14-case-live
Takeaway: A correct player survives remounts and remains operable without a mouse.
Sheet: topics/15-lifecycle-accessibility.html

## 16. Signed media, CORS, DRM and delivery boundaries

Stage: Best practices
Prerequisites: 13-case-protected
Takeaway: Separate authorization, cross-origin access, encryption and device compatibility.
Sheet: topics/16-security-delivery.html

## 17. QoE: measure what the viewer experiences

Stage: Best practices
Prerequisites: 15-lifecycle-accessibility, 16-security-delivery
Takeaway: Player success is first-frame success plus sustained viewing, not a green API response.
Sheet: topics/17-qoe-diagnostics.html

## 18. Choose, migrate and improve with evidence

Stage: Further improvements
Prerequisites: 17-qoe-diagnostics, 08-vidstack
Takeaway: Optimize the complete viewing path under your constraints, then measure the change.
Sheet: topics/18-selection-migration.html
