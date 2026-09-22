# Common Ground Creative

A pnpm workspace starter for a TypeScript full-stack application.

## Packages

- `apps/web` — Next.js App Router frontend
- `apps/api` — Fastify HTTP API
- `packages/shared` — shared Zod schemas and inferred TypeScript types

## Prerequisites

- Node.js 20.9 or later
- pnpm 10 or later

## Getting started

```bash
cp .env.example .env
pnpm install
pnpm dev
```

The web app runs at `http://localhost:3000`; the API runs at `http://localhost:3001`.

For a deterministic demo, set `LLM_ENABLED=false` in `.env`. This returns mock data for
the document-analysis endpoint only; it does not disable or change the realtime voice module.

## Synthesia avatar setup

Create an API key in the [Synthesia developer settings](https://app.synthesia.io/#/developers/api-keys), then add it to `SYNTHESIA_API_KEY` in your local `.env`. Set `SYNTHESIA_AVATAR_ID` once the avatar has been selected, and enable `SYNTHESIA_SESSIONS_ENABLED` when the Interactive Avatar session integration is ready. Do not expose the API key through `NEXT_PUBLIC_` variables or commit it to the repository.

## Commands

```bash
pnpm dev           # start web and API in parallel
pnpm build         # build shared package, web, and API
pnpm typecheck     # type-check every workspace package
pnpm lint          # lint every workspace package
pnpm format        # format source files
pnpm format:check  # verify formatting
```

## API

`GET /health` returns a typed health response using the schema exported by `@common-ground/shared`.
