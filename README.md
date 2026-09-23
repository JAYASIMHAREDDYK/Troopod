# Purelane &mdash; Production Shopify Dawn 2.0 Theme

> **Submission for Troopod AI Product Engineer Assignment**  
> Taking the Purelane plant-based homecare prototype live on Shopify Dawn with 100% merchant editability, native Shopify 2.0 architecture, and 60fps performance.

---

## 🔗 Live Store & Repository Details

- **Storefront URL:** [https://purelane-dev-4enbpwjr.myshopify.com/](https://purelane-dev-4enbpwjr.myshopify.com/)
- **Storefront Password:** `bohyub`
- **Theme Base:** Official Shopify Dawn (Online Store 2.0 clean install)
- **Repository:** [https://github.com/JAYASIMHAREDDYK/Troopod.git](https://github.com/JAYASIMHAREDDYK/Troopod.git)
- **Branch:** `main`

---

## 🎯 Scope of Work

The assignment required transforming a single-file static design prototype (`purelane-homepage.html`) into production-grade, merchant-configurable Shopify Online Store 2.0 sections.

### Primary Sections Built:
1. **Hero Section (`section.hero` / `sections/hero.liquid`)**:
   - Merchant-editable headings, accent colors, and CTA buttons.
   - Dynamic slide blocks for 1, 2, and 3-product stages with dynamic pricing, compare-at prices, and discount pills.
   - Trust badge rail with custom icons (`Plant powered`, `Safe for kids & pets`, `Zero harsh chemicals`).
   - Clean column separation preventing bottle overlap and maintaining vertical header clearance.
2. **Shop / Product Grid (`#shop` / `sections/shop.liquid`)**:
   - Collection-driven and block-driven fallback modes.
   - Dynamic product cards with rating stars, review count, badge pills, pricing, and direct Ajax Add-to-Cart.
   - Full edge-case handling: sold-out state, missing images, and long titles.
3. **Best-Selling Combos (`#combos` / `sections/combos.liquid`)**:
   - Horizontal swipeable combo rail with touch-scrolling.
   - Product package components breakdown with `+` dividers.
   - Discount tag badges and live price comparisons with one-click checkout integration.
4. **Bundles (`#bundles` / `sections/bundles.liquid`)**:
   - 3-tier bundle cards (Starter, Most Popular, Whole Home).
   - Product bottle silhouettes, tier feature checkmarks, and savings indicators.
5. **Reviews Rail (`#reviews` / `sections/reviews.liquid`)**:
   - Continuous marquee ticker displaying 5-star customer reviews, verified buyer badges, and product references.

### Bonus Sections & Infrastructure:
- **Header & Mobile Drawer (`sections/header.liquid`)**: Floating glass pill navigation with search/account/cart counters and a smooth slide-out mobile navigation drawer.
- **Ticker Bar (`sections/ticker.liquid`)**: Animated announcement strip across the top.
- **Brand Pillars (`sections/pillars.liquid`)**: 3 core value proposition cards.
- **Sourced from Nature (`sections/ingredients.liquid`)**: Botanical line-art ingredients grid.
- **Proof & Stats (`sections/proof.liquid`)**: Customer proof statistics with circular visual rings.
- **Footer (`sections/footer.liquid`)**: Newsletter capture, site navigation, and policy links.
- **Multi-page & Cart Navigation**: Full routing between homepage sections, collections, product detail pages, and `/cart`.

---

## 🏷️ Metafield Definitions Created

To support rich ecommerce data natively in Shopify without hardcoding:

| Metafield Namespace & Key | Type | Description |
| :--- | :--- | :--- |
| `product.metafields.purelane.badge` | `Single line text` | Promotional badge (e.g., `"Best seller"`, `"Top rated"`, `"New"`) |
| `product.metafields.purelane.rating` | `Decimal` | Numerical star rating (e.g., `4.8`) |
| `product.metafields.purelane.review_count` | `Integer` | Total verified customer reviews count (e.g., `237`) |
| `product.metafields.purelane.components` | `List of handles / references` | Sub-products included inside pre-built combos |

---

## 🧪 Seeded Test Scenarios

The store is seeded with **21 products** specifically verifying critical ecommerce edge cases:
- **Sold-out product:** *Copper, Bronze & Brass Cleaner* (`available: false`, inventory `0`) renders disabled Add to Cart state with "Sold Out" badge.
- **Missing image product:** Gracefully falls back to stylized brand container without breaking card geometry.
- **Long title product:** *Purelane Complete Home Deep-Cleaning Ritual Kit With Reusable Spray Bottles And Cotton Cloths* (93 chars) wraps cleanly with line-clamping and zero layout shift.

---

## ⚡ Performance & Production Architecture

1. **Eliminated CPU-Bound SVG Filters**: The prototype ran infinite animated SVG turbulence and displacement filters (`feTurbulence`, `feDisplacementMap`), causing high CPU utilization and frame drops. These were replaced with lightweight, GPU-composited CSS gradients and hardware-accelerated transitions.
2. **Backdrop Filter Optimization**: Reduced excessive stacking of heavy `backdrop-filter: blur(24px)` to maintain a silky smooth 60fps scroll.
3. **Layout Stability & CLS**: All product cards, slides, and images enforce explicit aspect ratios and composite isolation to prevent Cumulative Layout Shift (CLS).
4. **Accessibility (a11y)**: Focus-visible rings, contrast-compliant typography, ARIA labels, semantic landmark elements (`<header>`, `<main>`, `<section>`, `<footer>`), and screen-reader accessible SVGs.

---

## 🛠️ Tech Stack

- **Shopify Dawn Theme Engine** (Liquid, JSON templates, Section Schemas)
- **Vanilla CSS3** (Custom Properties, Flexbox, CSS Grid, Glassmorphism)
- **Vanilla JavaScript** (Shopify Ajax API, Touch Gestures, Carousel Controllers)
- **Shopify CLI 3.x** (Theme Deployment & Validation)

---

## 👨‍💻 Author

**Jayasimha Reddy K**  
AI Product Engineer Submission &bull; [GitHub Profile](https://github.com/JAYASIMHAREDDYK)
