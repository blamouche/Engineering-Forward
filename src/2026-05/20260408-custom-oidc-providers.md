# Custom OIDC Providers for Supabase Auth
**Source**: https://supabase.com/blog/custom-oauth-oidc-providers
**Date**: 2026-04-08
**Author**: cemal_kilic
**Keywords**: OAuth, OIDC, Supabase Auth, identity providers, PKCE, authentication, open-source

## Elevator pitch
Supabase now lets you connect any standards-compliant OpenID Connect identity provider — including regional, self-hosted, and niche providers — with the same sign-in flow, client libraries, and RLS enforcement as built-in providers.

## Takeaways
- Custom OIDC Providers fill the gap for regional compliance, self-hosted (e.g., GitHub Enterprise), and niche identity providers not covered by Supabase's 20+ built-in social auth options.
- Configuration is simple: supply issuer URL, client ID/secret, and scopes — the discovery document, endpoints, and JWKS are resolved automatically from `.well-known/openid-configuration`.
- PKCE is enabled by default with automatic code challenge/verifier generation, protecting against authorization code interception without client-side logic.
- Multi-platform apps are supported via `acceptable_client_ids` for different client IDs per platform (web, iOS, Android), and email-optional providers are available for gaming or phone-based identity systems.
- Custom providers are fully manageable through both the Dashboard and Admin API (list, update, delete), with a limit of 3 per project (expandable via support).

## Synthesis
Supabase has taken a significant step toward becoming a universal authentication layer with the launch of Custom OIDC Providers. While the platform already ships with over 20 built-in social providers (Google, GitHub, Apple, etc.), this feature addresses a critical gap: any organization that uses a provider outside that curated list was previously locked out. This includes companies with SAML-to-OIDC bridges, regional identity providers mandated for compliance, self-hosted GitHub Enterprise instances, and niche platforms in gaming, healthcare, or government.

The implementation is elegantly simple from the developer's perspective. You provide your provider's issuer URL, client credentials, and scopes, and Supabase handles everything else — discovery document resolution, endpoint negotiation, JWKS verification — all automatically via the standard `.well-known/openid-configuration` endpoint. Once configured, the provider identifier uses a `custom:` prefix namespace (e.g., `custom:my-provider`) and works identically to built-in providers across all client SDKs: JavaScript, Flutter, Swift, Kotlin, and more. There's no special client-side handling required.

Security is a first-class concern. PKCE (Proof Key for Code Exchange) is enabled by default for every custom provider, with the auth server generating the code challenge and verifier automatically. This protects against authorization code interception attacks without requiring developers to implement PKCE logic on the client side. The feature also supports authorization parameters for consent screens, offline access, and login hints, plus multi-platform client ID validation through `acceptable_client_ids`.

This release complements Supabase's earlier OAuth 2.1 server capabilities, completing the identity picture: Supabase projects can now both *be* an identity provider and *consume* any external identity provider. For enterprises and organizations that have been waiting on a specific compliance or infrastructure requirement, this removes a significant adoption barrier. The 3-provider-per-project soft limit (with support-expandable options) suggests Supabase is targeting this at serious organizational use cases rather than casual experimentation. Combined with the Dashboard-based management UI and full Admin API coverage, Custom OIDC Providers positions Supabase Auth as a genuinely universal identity layer for modern applications.
