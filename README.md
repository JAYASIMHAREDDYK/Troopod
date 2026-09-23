# Purelane Shopify Theme (Dawn OS 2.0)

A Shopify Online Store 2.0 implementation of the Purelane homepage prototype, built as an extension on Shopify's Dawn theme framework.

## Live Store & Access

- **Store URL:** https://purelane-dev-4enbpwjr.myshopify.com/
- **Storefront Password:** `bohyub`
- **Base Theme:** Dawn 15.x (Online Store 2.0)
- **Repository:** https://github.com/JAYASIMHAREDDYK/Troopod.git (`main` branch)

---

## Technical Overview

The objective was converting a monolithic, single-file HTML prototype (`purelane-homepage.html`) into modular, merchant-configurable Shopify sections while keeping 1:1 visual parity with the design spec and ensuring production-level performance and accessibility.

### Architecture & Directory Layout

```text
├── assets/
│   ├── purelane.css         # Scoped styling, layout geometry, responsive breakpoints, glass tokens
│   └── purelane.js          # Client-side interactions (carousels, Ajax cart additions, mobile drawer)
├── config/
│   └── settings_data.json   # Theme configuration and default preset settings
├── layout/
│   └── theme.liquid         # Global document shell, font preconnects, asset includes
├── sections/
│   ├── hero.liquid          # Hero section with 3-tier carousel stage & trust badge column
│   ├── shop.liquid          # Product grid with rating, badge pills & direct Ajax add-to-cart
│   ├── combos.liquid        # Horizontal swipeable combo rail with bundle components breakdown
│   ├── bundles.liquid       # Tiered value bundles (Starter, Most Popular, Whole Home)
│   ├── reviews.liquid       # Infinite marquee customer review rail
│   ├── ingredients.liquid   # Botanical ingredients feature section
│   ├── pillars.liquid       # Core value propositions
│   ├── proof.liquid         # Quantitative social proof metrics
│   ├── ticker.liquid        # Announcement marquee
│   ├── header.liquid        # Fixed glass navbar with mobile drawer
│   └── footer.liquid        # Footer columns, policies, newsletter signup
└── templates/
    └── index.json           # Section ordering and block schema configuration
```

---

## Key Engineering Decisions

### 1. Liquid Schemas & Merchant Editability
Instead of hardcoding product cards, prices, and copy in Liquid:
- Every section exposes a Shopify schema with typed settings (`text`, `textarea`, `image_picker`, `collection`, `product`, `url`, `color`).
- Complex components (`hero` slides, `combos`, `bundles`, `reviews`) use nested block structures (`blocks`). Merchants can add, delete, reorder, and modify cards directly in the Shopify Theme Editor without code changes.

### 2. Metafields Architecture
To pull rich product attributes dynamically from Shopify rather than hardcoding promotional tags or reviews in template code, the following metafields are defined:

| Key | Namespace | Type | Purpose |
| :--- | :--- | :--- | :--- |
| `badge` | `purelane` | `single_line_text_field` | Product pill badge ("Best seller", "Top rated", "New") |
| `rating` | `purelane` | `number_decimal` | Star rating display (e.g. `4.8`) |
| `review_count` | `purelane` | `number_integer` | Verified buyer review count (e.g. `237`) |
| `components` | `purelane` | `list.product_reference` | Sub-products included in a bundle combo |

### 3. Performance & Core Web Vitals
The raw prototype had significant frame rate bottlenecks due to CPU-heavy rendering loops. The following fixes were implemented:
- **SVG Filter Removal on Mobile/Scroll:** The prototype used continuous CSS animations over SVG `<feTurbulence>` and `<feDisplacementMap>` nodes. This caused sustained 100% thread usage on mobile and laptop GPUs. Replaced with composited CSS gradients and hardware-accelerated transforms (`translate3d`).
- **Backdrop Filter Throttling:** Stacked `backdrop-filter: blur(...)` calls across multiple nested elements were flattened. Glassmorphic backgrounds utilize optimized alpha fills with subtle border highlights to achieve identical aesthetics at 60fps.
- **Layout Shift Prevention:** Explicit aspect ratios (`aspect-ratio: ...`) and sizing clamps on product images and the hero carousel stage prevent Cumulative Layout Shift (CLS) during image loads and variant toggles.

### 4. Layout Geometry & Responsive Fixes
- **Hero Badge/Bottle Collision:** In the original prototype, both the 3-badge glass pill and the product stage were absolute-positioned at `right: 18px` and `right: 2%`, causing the badge card to physically cover the right bottle. In `sections/hero.liquid` and `assets/purelane.css`, the layout was re-budgeted: `.badges` is pinned to `right: 0`, and `.hero-prod` is offset to `right: 132px` on desktop, guaranteeing clean breathing room across all slides.
- **Dynamic Pricing Tag Docking:** The slide price pill (`.ptag`) was tightened against the product stage container to prevent awkward whitespace gaps on ultra-wide viewports.
- **Header Clearance:** Re-calibrated `.hstage` from `74svh` down to `clamp(340px, 58svh, 500px)`, eliminating vertical overflow into the sticky navbar on laptop displays.

### 5. Multi-Page Routing & Fallbacks
- Added routing logic to `sections/header.liquid` and `layout/theme.liquid`: anchor links (`#shop`, `#bundles`) automatically resolve to `/#shop` and `/#bundles` when the user navigates to `/cart`, product pages, or collection pages.
- Mobile drawer implementation with keyboard accessibility (Escape to close, focus trapped when open, ARIA expanded state).

---

## Edge Case Handling

The store contains 21 seeded products specifically validating edge cases:
1. **Sold Out Product (`available: false`):** 
   - *Copper, Bronze & Brass Cleaner* (inventory: 0).
   - "Add to Cart" button automatically disables with distinct "Sold Out" styling; prevents accidental cart submissions.
2. **Missing Image:**
   - Products without media gracefully fallback to styled brand placeholder containers, preserving grid alignment without layout breakages.
3. **Long Product Title:**
   - *Purelane Complete Home Deep-Cleaning Ritual Kit With Reusable Spray Bottles And Cotton Cloths* (93 characters).
   - Typography uses `-webkit-line-clamp` and flexible card flexboxes to ensure uniform card heights across the grid.

---

## Local Development & Deployment

Prerequisites:
- [Shopify CLI 3.x](https://shopify.dev/docs/themes/tools/cli)
- Partner account or dev store collaborator access

### Commands

```bash
# Authenticate to the dev store
shopify theme dev --store purelane-dev-4enbpwjr.myshopify.com

# Check for Liquid syntax or schema issues
shopify theme check

# Deploy directly to the live Dawn theme
shopify theme push --theme 160909131861 --allow-live
```

---

## Author

**Jayasimha Reddy K**  
Submission for Troopod AI Product Engineer Role  
Repository: [github.com/JAYASIMHAREDDYK/Troopod](https://github.com/JAYASIMHAREDDYK/Troopod)
