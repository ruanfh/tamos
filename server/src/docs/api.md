
# TAMOS Server API

The TAMOS Server exposes a minimal HTTP API for submitting gems and accessing the public archive.  
This API is intentionally small and predictable. It demonstrates how a TAMOS‑compatible node can accept new gems, validate them, and publish them as static JSON files.  
This is a reference implementation, not a full platform.  
Platforms may extend this API, but the core protocol remains unchanged.

---

## Base URL

`http://your-tamos-server.com/`

All endpoints are relative to this root.

---

## Endpoints

### 1. POST `/submit`

Submit a new gem to the server.

**Request:**

```http
POST /submit
Content-Type: application/json
```

**Body:**

```json
{
  "url": "https://example.com/resource",
  "description": "A short description of the resource.",
  "author": "Name or handle",
  "date": "2026-01-08"
}
```

**Validation:**

The server validates the payload against `gem.schema.json`.
If invalid, the server returns:

```http
400 Bad Request
```
```json
{
  "error": "Validation failed",
  "details": { ... }
}
```

**Success Response:**

If valid, the server:
- Allocates the next numeric ID
- Writes the gem to `archive/{id}.json`
- Returns the assigned ID

```http
201 Created
```
```json
{
  "id": 42
}
```

---

### 2. GET `/archive/`

List all gems in the archive.

**Behavior:**
Returns a directory listing or a JSON index (implementation‑dependent).  
This endpoint exists primarily for convenience; AI crawlers can also enumerate files directly.

**Example Response** (optional JSON index):

```json
{
  "gems": [
    { "id": 1, "path": "/archive/1.json" },
    { "id": 2, "path": "/archive/2.json" }
  ]
}
```

---

### 3. GET `/archive/{id}`

Retrieve a single gem by ID.

**Example:**

```http
GET /archive/42
```

**Response:**

```json
{
  "url": "https://example.com/resource",
  "description": "A short description.",
  "author": "Author",
  "date": "2026-01-08"
}
```

**Errors:**

```http
404 Not Found
```
```json
{
  "error": "Gem not found"
}
```

---

### 4. GET `/health`

Simple health check endpoint.

**Response:**

```http
200 OK
```
```json
{
  "status": "ok"
}
```

Used for monitoring, uptime checks, and deployment verification.

---

## API Philosophy

The TAMOS Server API is intentionally minimal:

- No authentication
- No deletion
- No editing
- No ranking
- No sync
- No federation
- No metadata beyond the gem schema

The server’s only job is to accept valid gems and publish them as static files.  
Everything else — discovery, indexing, ranking, linking — is handled by AI crawlers following the protocol.

---

## Example Workflow

1. Client submits a gem
   ```http
   POST /submit
   ```
2. Server validates and stores it
   ```text
   archive/17.json
   ```
3. AI crawlers fetch the archive
   ```http
   GET /archive/
   GET /archive/17.json
   ```
4. AI follows the gem’s URL
   The AI explores the resource, builds semantic understanding, and connects it to other gems.

---

## Non‑Goals

This API does **not** attempt to:

- synchronize nodes
- federate servers
- manage users
- moderate content
- provide search
- provide analytics
- provide dashboards

These are platform‑level concerns, not protocol concerns.

---

## Summary

The TAMOS Server API provides:

- a clean way to submit gems
- a predictable archive structure
- a minimal surface area
- a fully TAMOS‑compliant node

It is designed to be forked, extended, or replaced by platforms — while keeping the core protocol pure.
