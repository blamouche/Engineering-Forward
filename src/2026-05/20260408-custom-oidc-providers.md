# Custom OIDC Providers for Supabase Auth
**Source**: https://supabase.com/blog/custom-oauth-oidc-providers
**Date**: 2026-04-08
**Author**: cemal_kilic
**Keywords**: auth, oauth, oidc, openid-connect, security, identity-provider, enterprise, PKCE

## Elevator pitch
Supabase Auth now supports custom OpenID Connect providers, letting developers connect any standards-compliant identity provider — from GitHub Enterprise to regional compliance-mandated IdPs — with the same sign-in flow as built-in providers.

## Takeaways
- Custom OIDC providers work exactly like Supabase's 20+ built-in providers: same `signInWithOAuth` flow, same client libraries, same RLS enforcement
- Configuration is simple: supply an issuer URL, client credentials, and scopes — Supabase automatically resolves the discovery document, endpoints, and JWKS from `/.well-known/openid-configuration`
- PKCE (Proof Key for Code Exchange) is enabled by default for every custom provider, protecting against authorization code interception with zero client-side work
- Supports advanced scenarios: multi-platform apps with per-platform client IDs, email-optional providers for gaming/device-based identity, and custom authorization parameters
- Limited to 3 custom providers per project by default, with more available on request

## Synthesis
Supabase Auth ships with over 20 built-in social providers (Google, GitHub, Apple, etc.), but that catalog could never cover every use case. Companies with GitHub Enterprise Server, regional identity providers mandated for compliance, SAML-to-OIDC bridges, or niche gaming/healthcare identity networks were stuck. Custom OIDC Providers closes that gap.

The implementation is clean. Developers call `supabase.auth.admin.customProviders.createProvider()` with a provider type, identifier (prefixed with `custom:`), client credentials, issuer URL, and requested scopes. Supabase handles the rest — it resolves the OIDC discovery document from the issuer's well-known endpoint, verifies ID tokens against the provider's JWKS, and automatically includes the `openid` scope. Client-side usage is identical to built-in providers: `supabase.auth.signInWithOAuth({ provider: 'custom:my-provider' })` works across JavaScript, Flutter, Swift, and all other supported SDKs.

PKCE is enabled by default with no client-side logic required — the auth server generates and manages the code challenge and verifier automatically. This is a meaningful security win, as PKCE is often overlooked in custom integrations. Additional features include authorization params for consent screens and login hints, `acceptable_client_ids` for multi-platform apps that use different client IDs per platform, and an `email_optional` flag for providers that don't return email addresses (gaming platforms, device-based identity).

Providers are fully manageable through both the Dashboard and the Admin API: list, update (rotate secrets, change scopes, toggle enabled/disabled), and delete. The only immutable fields are `provider_type` and `identifier`. This release completes a two-sided picture for Supabase Auth: last year's OAuth 2.1 server capabilities let projects *be* identity providers; custom OIDC providers now let them *consume* any external identity provider.
