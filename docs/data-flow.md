# KitForge — Data Flow

**Version:** 0.1  
**Date:** 2026-05-03

---

## App Startup

```mermaid
flowchart TD
    A[App launches] --> B[Load catalogue.json]
    B --> C{Catalogue valid?}
    C -- No --> D[Display error and exit]
    C -- Yes --> E[Scan kits directory]
    E --> F[Load each kit JSON]
    F --> G{Kit references\nunknown item?}
    G -- Yes --> H[Skip item, flag warning]
    G -- No --> I[Kit loaded]
    H --> I
    I --> J[Display Kit List screen]
```

---

## Kit Building

```mermaid
flowchart TD
    A[User adds item] --> B{Item already\nin kit?}
    B -- Yes --> C[Increment quantity]
    B -- No --> D[Add item at default qty]
    C --> E[Recalculate stats]
    D --> E
    E --> F[Update weight bar]
    E --> G[Auto-save kit JSON]

    H[User adjusts qty] --> E
    I[User removes item] --> E
```

---

## Readiness Report

```mermaid
flowchart TD
    A[User clicks Build] --> B[Auto-save kit JSON]
    B --> C[Calculate readiness score]
    B --> D[Check missing categories]
    B --> E[Evaluate item requirements]

    C --> C1[For each category:\nscore = 1 if any item packed else 0]
    C1 --> C2[score = sum of category_score × weight / 22 × 100]

    D --> D1[List categories with score = 0\nordered by priority]

    E --> E1[For each packed item:\n  for each requirement:\n    check requirement]
    E1 --> E2{Requirement met?}
    E2 -- No --> E3[Add warning]
    E2 -- Yes --> E4[No action]

    C2 --> F[Display Readiness Report]
    D1 --> F
    E3 --> F
```

---

## Requirement Evaluation Detail

```mermaid
flowchart TD
    A[Evaluate requirement] --> B{type?}

    B -- item --> C{item_id in kit?}
    C -- No --> WARN[Generate warning]
    C -- Yes --> OK[Pass]

    B -- category --> D{exclude_self?}
    D -- Yes --> E{Any other item\nfrom category in kit?}
    D -- No --> F{Any item from\ncategory in kit?}
    E -- No --> WARN
    E -- Yes --> OK
    F -- No --> WARN
    F -- Yes --> OK

    B -- resource/water_source --> G[Show as informational note\nnever a warning\nvisually distinct from warnings]

    B -- resource/water_ml --> H{Total water_ml\nin kit >= amount?}
    H -- No --> WARN
    H -- Yes --> OK
```

---

## Persistence

```mermaid
flowchart LR
    A[Kit state in memory] -- auto-save on change --> B[kit_id.json\non disk]
    C[catalogue.json\non disk] -- read-only at startup --> D[Catalogue in memory]
    B -- loaded at startup --> A
```
