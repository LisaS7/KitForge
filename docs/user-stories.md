# KitForge — User Stories & Acceptance Criteria

**Version:** 0.1  
**Date:** 2026-05-03  
**Status:** Draft

---

## Kit Management

**US-01: Create a new kit**  
As a user, I want to create a new kit so that I can start planning my bug-out bag.

- Given I am on the Kit List screen, when I click "+ New Kit", then the Kit Configuration modal opens
- When I complete configuration and confirm, then I am taken to the build screen with an empty kit named "New Kit"
- When I am taken to the build screen, then the kit JSON file has been created on disk

**US-02: Rename a kit**  
As a user, I want to rename my kit so that I can identify it easily.

- Given I am on the build screen, when I click the kit name, then it becomes an editable text field
- When I press Enter or click away, then the name is saved and reverts to a label
- When the name is saved, then the kit JSON file is updated

**US-03: Copy a kit**  
As a user, I want to copy an existing kit so that I can use it as a starting point for a new one.

- Given I am on the Kit List screen, when I click Copy on a kit card, then a new kit is created with a new unique ID and the name "Copy of [original name]"
- Then the copy appears on the Kit List screen

**US-04: Delete a kit**  
As a user, I want to delete a kit I no longer need.

- Given I am on the Kit List screen, when I click Delete on a kit card, then the kit is removed from the list
- Then the kit's JSON file is deleted from disk

---

## Kit Configuration

**US-05: Configure a kit**  
As a user, I want to set my kit's weight limit, number of people, and duration so that the app can give me relevant feedback.

- Given the Kit Configuration modal is open, when I enter valid values and confirm, then the kit is updated with those values
- When duration is entered, then it is accepted as a plain number of days
- When I open the modal on an existing kit, then the current values are pre-filled

---

## Catalogue Browsing

**US-06: Browse items by category**  
As a user, I want to browse items by category so that I can find what I need quickly.

- Given I am on the build screen, when I view the catalogue panel, then I see a grid of category icons
- When I click a category, then the panel shows items in that category
- When I click the back button, then I return to the category grid

**US-07: View item details**  
As a user, I want to see details about an item before adding it so that I can make an informed choice.

- Given I am viewing a category's items, when I hover over an item, then a tooltip shows its weight, calories, water, and notes

---

## Kit Building

**US-08: Add an item to my kit**  
As a user, I want to add items to my kit so that I can build it out.

- Given I am viewing a category's items, when I click an item, then it is added to the packed items panel at its default quantity
- When the item is already in the kit, then its quantity is incremented by 1 instead

**US-09: Drag and drop an item**  
As a user, I want to drag items onto the bag so that adding items feels intuitive.

- Given I am viewing a category's items, when I drag an item icon onto the bag image and release, then the item is added to the kit
- Then the packed items panel updates immediately

**US-10: Adjust item quantity**  
As a user, I want to adjust how many of each item I'm packing.

- Given an item is in my kit, when I click +, then its quantity increases by 1
- When I click −, then its quantity decreases by 1
- When the quantity reaches 0, then the item is removed from the kit automatically

**US-11: Remove an item**  
As a user, I want to remove an item from my kit entirely.

- Given an item is in my kit, when I click Remove, then the item is removed from the packed items panel regardless of quantity

**US-12: Collapse and expand categories**  
As a user, I want to collapse category sections in the packed items panel so that I can focus on what I'm working on.

- Given the packed items panel has items in multiple categories, when I click a category header, then its item list collapses
- When I click it again, then it expands

---

## Stats

**US-13: See my kit's weight**  
As a user, I want to see how heavy my kit is so that I know if it's within my limit.

- Given I have items in my kit, then the stats panel shows total weight in grams
- Then a weight bar shows fill proportion relative to the configured weight limit
- When weight is below 75% of the limit, then the bar is green
- When weight is between 75% and 99% of the limit, then the bar is amber
- When weight is at or above the limit, then the bar is red

**US-14: See my kit's nutritional and water coverage**  
As a user, I want to see total calories and water so that I know if my kit covers my needs.

- Given I have items in my kit, then the stats panel shows total calories and total stored water (ml)
- Then purifiable water is shown separately and never added to stored water
- Then calories and water are shown in context of the configured number of people and duration

---

## Readiness Report

**US-15: Switch to the readiness report view**  
As a user, I want to switch to a focused report view so that I can review my kit's completeness without distraction.

- Given I am on the build screen, when I click Build, then the kit is saved and the Readiness Report replaces the build view
- When I click the back/edit button, then I return to the build screen
- Then the report shows the same score that was already visible in the stats bar — clicking Build does not trigger a new calculation

**US-16: See my readiness score**  
As a user, I want to see an always-current score so that I can gauge how prepared I am as I build.

- Given I have items in my kit, then the readiness score is shown live in the stats bar on the build screen
- Then the score updates immediately whenever an item is added, removed, or its quantity changes
- Then the score reflects weighted category coverage (Required × 3, Warning × 2, Optional × 1)
- When all Required and Warning categories are covered, then the score is at least 77%
- When no items are packed, then the score is 0%

**US-17: See missing category warnings**  
As a user, I want to know which categories I haven't covered so that I can fill the gaps.

- Given the Readiness Report is displayed, then any category with no items packed is listed as a warning
- Then warnings are ordered Required first, then Warning, then Optional

**US-18: See item dependency warnings**  
As a user, I want to know when a packed item is missing something it depends on so that my kit is actually usable.

- Given the Readiness Report is displayed, when a packed item has an unmet requirement, then a warning is shown for that item
- When multiple requirements are unmet on the same item, then each produces a separate warning
- When a requirement is of type `resource: water_source`, then it is shown as an informational note, never counted as a warning, and is visually distinct from warnings

---

## Persistence

**US-19: Kit is saved automatically**  
As a user, I want my kit to be saved without me having to think about it.

- Given I make any change to a kit (name, config, items), then the kit is saved to disk automatically
- When I relaunch the app, then all previously saved kits are present on the Kit List screen

**US-20: Graceful handling of missing catalogue items**  
As a user, I don't want the app to crash if the catalogue has changed since I last used it.

- Given a kit references an item that no longer exists in the catalogue, when the kit is loaded, then that item is skipped
- Then a warning is shown on the build screen indicating which items could not be loaded
