# KitForge — Product Requirements Document

**Version:** 0.1  
**Date:** 2026-05-03  
**Status:** Draft

---

## 1. Purpose

KitForge is a desktop application for planning emergency preparedness kits. It helps users build a well-rounded bug-out bag (BOB) by selecting items from a curated catalogue, tracking weight and nutritional coverage, and generating a readiness report that identifies gaps.

---

## 2. Problem Statement

Planning a bug-out bag is time-consuming and error-prone. Most people either over-pack (too heavy to carry) or under-pack (missing critical categories). There is no dedicated tool that combines item selection, weight tracking, and gap analysis in one place.

---

## 3. Target User

A single user planning a personal or household emergency kit on a desktop computer. No account, no cloud sync, no collaboration — local-first, offline-capable.

---

## 4. MVP Scope

The MVP covers one kit type: the **bug-out bag (BOB)**. All features below are in scope for MVP unless marked otherwise.

### 4.1 Kit Management

- Create multiple named kits
- Rename a kit inline on the build screen
- Copy and delete kits from the kit list
- Each kit is saved as a local JSON file

### 4.2 Kit Configuration

- Set a weight limit (grams)
- Set number of people the kit must support
- Set duration the kit must cover (days)
- Configuration accessible on kit creation and via a button on the build screen

### 4.3 Item Catalogue

- Built-in catalogue of generic, non-brand-specific items
- 11 categories: Water, Food, Medical, Light, Fire, Shelter, Tools, Navigation, Hygiene, Communication, Documents
- Each item has: name, category, weight, calories, water provided, water purifiable, default quantity, notes, and dependency requirements
- Catalogue is read-only in the MVP (no user-added items)

### 4.4 Kit Building

- Browse catalogue by category
- Add items to the kit; each item has an adjustable quantity
- Remove items from the kit
- Visual weight capacity bar that changes colour as the limit is approached
- Drag items from the catalogue onto a bag image to add them (game-like interaction)

### 4.5 Readiness Report

- Triggered by a prominent **Build** button on the build screen
- Replaces the build view (back button returns to editing)
- Shows overall readiness score (0–100%)
- Lists warnings for:
  - Categories with no items packed (by priority: Required → Warning → Optional)
  - Item dependency requirements that are unmet (e.g. camp stove packed but no gas canister)
- Shows kit stats: total weight, calories, stored water, purifiable water

### 4.6 Readiness Score

Weighted average of category coverage:

| Priority | Categories | Weight |
|---|---|---|
| Required | Water, Food, Medical, Light | 3 |
| Warning | Fire, Shelter, Tools | 2 |
| Optional | Navigation, Hygiene, Communication, Documents | 1 |

A category scores 1 if at least one item is packed in it, otherwise 0. Maximum possible score = 22. Score does not factor in quantity, duration, or number of people — those affect the stats display only.

### 4.7 Dependency Warnings

Items can declare requirements. Each requirement is checked independently and produces its own warning if unmet. Requirement types:

| Type | Meaning |
|---|---|
| `item` | A specific other item must also be packed |
| `category` | At least one item from a given category must be packed |
| `resource: water_source` | Contextual warning — item needs access to an external water source |
| `resource: water_ml` | Sufficient stored water must be packed (amount specified) |

---

## 5. Out of Scope (MVP)

The following are explicitly deferred to future versions:

- Additional kit types (car kit, EDC, home prep, financial kit)
- Scenario-based planning
- Scenario action planner — phased Before/During/After task lists per scenario, stored as JSON
- Financial preparedness planner — a "financial kit" using the same item/score/warning structure, with inputs like monthly expenses and savings, and stats like months of coverage
- User-added or edited catalogue items
- Export to HTML checklist
- QR code / mobile transfer
- Cloud sync or multi-device support
- Sharing or collaboration

---

## 6. Non-Functional Requirements

| Requirement | Detail |
|---|---|
| Platform | Desktop (Linux primary; Windows and macOS not tested for MVP) |
| Language | Python |
| GUI framework | Flet |
| Architecture | Builder design pattern |
| Window size | Fixed, ~1200×800 |
| Offline | Fully offline; no network calls |
| Storage | Local filesystem; one JSON file per kit |
| Startup validation | Catalogue integrity checked on launch (unique IDs, valid references, no circular dependencies) |
| Resilience | If a kit references a catalogue item that no longer exists, skip it with a warning rather than crash |

---

## 7. Design Principles

- **Flat and functional** — no border-radius, drop shadows, or gradients; hard borders throughout
- **Local-first** — all data stays on the user's machine
- **Catalogue-driven** — kit files store only user decisions; item details are always looked up from the catalogue at runtime
- **Onboarding via empty states** — no dedicated onboarding screen; empty panels show placeholder text explaining what goes there

### Colour Palette

| Role | Hex |
|---|---|
| Background | `#f1f1f1` |
| Panel / surface | `#d9d9d9` |
| Border / divider | `#c7c7c7` |
| Warm accent (khaki) — used on headers | `#cfcfb5` |
| Text / borders (dark) | `#2e2e2e` |
| Primary action / covered (olive) | `#5a6e3a` |
| Warning | `#b87c00` |
| Danger / missing | `#a63030` |

---

## 8. Success Criteria (MVP)

- A user can create a kit, add items, configure it, and generate a readiness report in a single session
- The readiness report correctly identifies all missing Required categories
- All item dependency warnings are accurate
- Kit data persists between app sessions
- The app starts without errors on a clean install with no existing kit files
