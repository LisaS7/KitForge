# KitForge — Task List

## Infrastructure

- [ ] Define Pydantic models for `Kit`, `KitConfig`, `PackedItem`, `CatalogueItem`, `Requirement`
- [ ] Write catalogue loader (parse `data/catalogue.json` into models)
- [ ] FR-21: Catalogue integrity check on startup (unique IDs, valid refs, no circular deps)
- [ ] FR-19: Kit persistence — save kit to `data/kits/<id>.json`
- [ ] FR-19: Auto-save with debounce (~500ms); immediate save on close/switch/report
- [ ] FR-20: Kit loader — read all `data/kits/*.json` on launch; skip missing catalogue items with warning
- [ ] Wire up screen routing (`QStackedWidget`) with navigation between Kit List and Build screens

---

## Build Screen Layout & Styling

- [ ] Refactor build screen into 3-panel layout using Qt Designer: catalogue (fixed 240px) / centre (flex) / packed items (fixed 240px)
- [ ] Split into component files: `catalogue_panel.py`, `middle_panel.py`, `kit_panel.py`
- [ ] Add `CATEGORY_ICONS` dict mapping `Category` → icon path or `QIcon` (in `icons.py`)
- [ ] Header: khaki background, kit name field (dashed border), Configure and Build buttons right-aligned
- [ ] Panel titles: uppercase (`CATALOGUE`, `KIT LIST`)
- [ ] Hard border separators between panels (via Qt stylesheet)
- [ ] Update `styles.py`: add `CATALOGUE_WIDTH`, `KIT_PANEL_WIDTH`, `TILE_SIZE`, `ICON_SIZE`
- [ ] Bag area: centred image, "Drag items here" hint text, contained in middle panel
- [ ] Stats bar shell: weight (with bar), calories, water, duration, readiness — layout only, no live data yet

---

## Catalogue Browsing

- [ ] FR-06: Category icon grid — square tiles with icon + label (`QGridLayout` of `QPushButton`)
- [ ] FR-06: Warning indicator (⚠) on category cards for uncovered categories
- [ ] FR-06: Click category → item grid view (2-column cards with icon + label)
- [ ] FR-06: Back button returns to category grid
- [ ] FR-07: Item tooltip showing weight, calories, water, notes

---

## Kit Building

- [ ] FR-08: Click item in catalogue → add to packed items at default quantity (or increment if already present)
- [ ] FR-08b: Drag item from catalogue → drop onto bag area (same add/increment logic)
- [ ] FR-09: Quantity controls (− / +) on each packed item; remove at 0
- [ ] FR-10: Explicit remove button on packed items
- [ ] FR-11: Packed items grouped by category with collapsible headers; compact −/+ qty controls

---

## Kit Management

- [ ] FR-01b: Kit List screen — 3-column card grid with name, readiness score, weight, last modified
- [ ] FR-01b: Empty state when no kits exist
- [ ] FR-01: "+ New Kit" button — opens Kit Configuration modal, then navigates to build screen
- [ ] FR-02: Inline rename on build screen header (click → text field → Enter/blur saves)
- [ ] FR-03: Copy kit from Kit List card ("Copy of [name]", new unique ID)
- [ ] FR-04: Delete kit from Kit List card (removes JSON file from disk)

---

## Kit Configuration

- [ ] FR-05: Kit Configuration modal (`QDialog`) — fields: weight limit, adults, children (6-12), young children (2-5), infants (0-1), duration
- [ ] FR-05: Validation — weight limit and duration required; at least one person specified
- [ ] FR-05: Pre-fill modal with current values when opened on an existing kit
- [ ] FR-05: Calorie/water requirement calculation (adults 2000 kcal/3L, children 1500/2L, young 1200/1.5L, infants 700/1L per day)

---

## Stats

- [ ] FR-13: Weight bar — fill proportion vs limit; green <75%, amber 75–99%, red ≥100%
- [ ] FR-14: Stats service — `get_total_weight()`, `get_calories()`, `get_water_ml()`, `get_readiness_score()`
- [ ] FR-14: Wire stats into stats bar (live update on add/remove)
- [ ] FR-14: Calories and water shown as fraction of requirement (people × duration)
- [ ] FR-14b: Warning indicator on category cards for uncovered categories (live)

---

## Readiness Report

- [ ] FR-15: Build button — saves kit and switches to Readiness Report view; back button returns to build screen
- [ ] FR-16: Readiness score — live, weighted category coverage; formula: `sum(score × weight) / 22 × 100`
- [ ] FR-16: Score displayed in stats bar on build screen and in full on Readiness Report
- [ ] FR-17: Missing category list — ordered Required → Warning → Optional
- [ ] FR-18: Dependency warnings per packed item (one warning per unmet `requires` entry)
- [ ] FR-18: `resource: water_source` shown as informational note, visually distinct, never counted as warning
