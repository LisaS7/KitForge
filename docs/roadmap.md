# KitForge — Development Roadmap

## Phase 1: App Skeleton + Data
**Goal: See catalogue in UI**

- [x] Define core Pydantic models
- [x] Load `catalogue.json`
- [x] Minimal Flet app (single screen)
- [x] Render catalogue items

---

## Phase 2: Basic Kit Building
**Goal: Add/remove items in memory**

- [x] Create in-memory kit
- [x] Add item (FR-08)
- [x] Increment existing item (FR-08)
- [x] Decrement/remove item (FR-09, FR-10)
- [x] Display packed items list

---

## Phase 3: Build Screen Layout & Styling
**Goal: Match wireframe structure and visual language**

- [ ] Refactor `build.py` into 3-panel layout (catalogue / centre / packed items)
- [ ] Split into component files: `catalogue_panel.py`, `centre_panel.py`, `kit_panel.py`
- [ ] Add category metadata (icons, priority) to `models.py` or a constants module
- [ ] Khaki header bar with kit name and action buttons (Configure / Build)
- [ ] Panel titles: uppercase, small, letter-spaced (`CATALOGUE`, `PACKED ITEMS`)
- [ ] Hard 2px dark borders between panels (matching wireframe)
- [ ] Category icon grid in catalogue panel (2-column, square cards)
- [ ] Catalogue view state: category grid → item grid → back button (FR-06)
- [ ] Bag area: centred 🎒 with dashed border and drop hint
- [ ] Stats bar shell: weight, calories, water, duration, readiness score (layout only)
- [ ] Packed items grouped by category with collapsible headers (FR-11)
- [ ] Compact qty controls (small −/+ buttons, no icon buttons)
- [ ] Update `styles.py` with missing tokens: `KHAKI`, `PANEL_TITLE_STYLE`, `MUTED`, `SUCCESS`

---

## Phase 4: Stats Layer
**Goal: App feels "alive"**

- [ ] Stats service: `get_total_weight()`, `get_calories()`, `get_water_ml()` (FR-14)
- [ ] Wire stats into stats bar (live update on add/remove)
- [ ] Weight bar with colour thresholds: green <75%, amber 75–99%, red ≥100% (FR-13)
- [ ] Calories and water shown as fraction of requirement (people × duration) (FR-14)
- [ ] Warning indicator on category cards for uncovered categories (FR-14b)

---

## Phase 5: Persistence
**Goal: Data survives reboot**

- [ ] Save kit to `data/kits/<id>.json` (FR-19)
- [ ] Auto-save with debounce (~500ms); immediate save on close/switch/report (FR-19)
- [ ] Load all kits from `data/kits/*.json` on launch (FR-20)
- [ ] Catalogue integrity check on startup (FR-21)

---

## Phase 6: Kit List Screen
**Goal: Multiple kits usable**

- [ ] Screen routing / `AppController` (Kit List ↔ Build Screen ↔ Report)
- [ ] Kit list UI — 3-column card grid with name, readiness score, weight, last modified (FR-01b)
- [ ] Empty state (FR-01b)
- [ ] "+ New Kit" → Kit Configuration modal → build screen (FR-01)
- [ ] Kit Configuration modal — weight limit, people, duration; validation (FR-05)
- [ ] Inline rename on build screen header (FR-02)
- [ ] Copy kit from card (FR-03)
- [ ] Delete kit from card (FR-04)

---

## Phase 7: Readiness System
**Goal: Identify gaps in kit coverage**

- [ ] Readiness score calculation — weighted category coverage (FR-16)
- [ ] Score live in stats bar and full display on report screen (FR-16)
- [ ] Missing category list ordered Required → Warning → Optional (FR-17)
- [ ] Dependency warnings per packed item (FR-18)
- [ ] `water_source` shown as informational note, not warning (FR-18)
- [ ] Readiness Report screen (FR-15)

---

## Phase 8: UX Polish
**Goal: Smooth, complete experience**

- [ ] Item tooltips: weight, calories, water, notes (FR-07)
- [ ] Drag & drop: catalogue → bag area (FR-08b)
- [ ] Debounced auto-save
- [ ] Rename/copy/delete polish
