# KitForge — Functional Requirements Document

**Version:** 0.1  
**Date:** 2026-05-03  
**Status:** Draft

---

## Kit Management

**FR-01: Create kit**
- User can create a new kit from the Kit List screen
- Creating a kit opens the Kit Configuration modal before navigating to the build screen
- Kit name defaults to "New Kit"

**FR-01b: Kit list display**
- Kits are displayed as cards in a 3-column grid
- Each card shows: name, readiness score (colour-coded), weight, last modified date
- Card actions: Edit (opens build screen), Copy, Delete
- An empty state is shown when no kits exist

**FR-02: Rename kit**
- Kit name is displayed as a label on the build screen header
- Clicking the name replaces it with an inline text field
- Pressing Enter or clicking away saves the new name and reverts to a label

**FR-03: Copy kit**
- User can copy a kit from the Kit List screen
- The copy is created with a new unique ID and the name "Copy of [original name]"

**FR-04: Delete kit**
- User can delete a kit from the Kit List screen
- The kit's JSON file is removed from disk

---

## Kit Configuration

**FR-05: Configure kit**
- User can set: weight limit (grams), number of adults, number of children (6-12), number of young children (2-5), number of infants (0-1), duration (days)
- Configuration modal is opened on kit creation and via a button on the build screen
- Weight limit and duration are required; age group fields default to 0 (at least one person must be specified)
- Calorie and water requirements calculated using: adults ~2000 kcal/3L, children ~1500 kcal/2L, young children ~1200 kcal/1.5L, infants ~700 kcal/1L per day

---

## Catalogue Browsing

**FR-06: Browse by category**
- The catalogue panel shows a grid of category icons
- Clicking a category icon switches the panel to show items in that category
- A back button returns to the category grid

**FR-07: View item details**
- Each item in the catalogue shows its name and weight
- Additional detail (calories, water, notes) accessible via tooltip

---

## Kit Building

**FR-08: Add item to kit**
- User can add an item from the catalogue to the kit
- The item is added with its default quantity
- If the item is already in the kit, its quantity is incremented instead

**FR-08b: Drag and drop**
- User can drag an item from the catalogue and drop it onto the kit area to add it
- Drop behavior follows same logic as FR-08 (add with default qty or increment existing)

**FR-09: Adjust quantity**
- Each packed item shows − and + controls
- When quantity reaches 0 via −, the item is removed from the kit automatically

**FR-10: Remove item**
- User can remove an item from the packed items panel
- The item is removed entirely regardless of quantity

**FR-11: Collapse/expand category**
- Packed items are grouped by category in the right panel
- Clicking a category header collapses or expands its item list

---

## Stats

**FR-13: Weight bar**
- Displays total packed weight against the configured weight limit
- Bar colour: green below 75% of limit, amber 75–99%, red at or above limit

**FR-14: Stats display**
- Displays: total weight (g), total calories, stored water (ml), purifiable water (ml)
- Stored water and purifiable water are shown separately and never summed
- Calories and water requirements calculated from age breakdown × duration; packed amounts shown as fraction of requirement

**FR-14b: Category warning indicators**
- A warning icon is shown next to any category not yet covered in the packed items panel
- This is a live indicator on the build screen, separate from the Readiness Report

---

## Readiness Report

**FR-15: Build button**
- The Build button is a view switch, not a calculation trigger
- Clicking Build saves the kit and navigates to the Readiness Report view
- A back/edit button returns to the build screen
- The readiness score and warnings are always calculated live; Build does not gate them

**FR-16: Readiness score**
- Score is calculated continuously as the kit changes (not on demand)
- Displayed in the stats bar on the build screen and in full on the Readiness Report
- Calculated as a weighted average of category coverage (0–100%)
- Each category scores 1 if at least one item is packed, otherwise 0
- Weights: Required = 3, Warning = 2, Optional = 1
- Maximum possible score = 22 points
- Formula: `score = sum(category_score × weight) / 22 × 100`
- Score does not factor in quantity, duration, or number of people

**FR-17: Missing category warnings**
- Report lists all categories with no items packed
- Ordered by priority: Required first, then Warning, then Optional

**FR-18: Dependency warnings**
- For each packed item, each `requires` entry is evaluated independently
- An unmet requirement produces a warning attributed to that item
- Requirement types and their checks:

| Type | Unmet condition |
|---|---|
| `item` | The specified item ID is not in the kit |
| `category` | No item from the specified category is in the kit (excluding self if `exclude_self: true`) |
| `resource: water_source` | Always shown as an informational note — never counted as a warning; visually distinct from warnings |
| `resource: water_ml` | Total stored `water_ml` in kit is less than the specified `amount` |

---

## Persistence

**FR-19: Save kit**
- Kit is saved to a local JSON file named by kit ID (e.g. `a3f8c1d2.json`) in `./data/kits/`
- Kit changes are auto-saved after a debounce period (~500ms after last change)
- Immediate save triggered on app close, kit switch, or navigating to readiness report
- Directory created automatically if missing

**FR-20: Load kit**
- On launch, the app reads all kit JSON files from `./data/kits/`
- Each valid kit is displayed as a card on the Kit List screen
- If a kit references a catalogue item that no longer exists, that item is skipped and a warning is shown on the build screen

---

## Startup Validation

**FR-21: Catalogue integrity check**
- On app startup, the catalogue is validated:
  - Every item has a unique ID
  - Every `requires` entry of type `item` references an existing item ID
  - Every `requires` entry of type `category` references a recognised category
  - No item requires itself
- If validation fails, the app displays an error identifying the issue and does not start
