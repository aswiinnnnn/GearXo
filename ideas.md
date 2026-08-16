# SwapPhone design direction

## Three initial approaches

### Theme Name: Quiet Studio
Very restrained premium technology catalogue with warm white space, editorial product photography, and a single sage accent. It should feel considered, trustworthy, and calm rather than sales-heavy.

Probability: 0.07

### Theme Name: Soft Utility
A utilitarian discovery interface with a light mineral palette, compact data panels, and clear progressive filtering. It prioritizes speed, clarity, and confident comparison.

Probability: 0.03

### Theme Name: Signal Green
A brighter, more energetic catalogue built around a vivid green signal color, floating product cutouts, and bolder promotional moments. It is more expressive while staying light and premium.

Probability: 0.08

## Chosen approach: Quiet Studio

### Design Movement
Contemporary editorial minimalism: a product-campaign language translated into a practical catalogue, with asymmetrical composition, generous negative space, and tactile photography.

### Core Principles
1. **Editorial calm:** large type, deliberate spacing, and a low-noise interface make browsing feel effortless.
2. **Proof through detail:** condition, warranty, battery, seller, and delivery information stay visible without turning cards into dashboards.
3. **Material contrast:** warm paper, graphite type, soft stone surfaces, and brushed-phone imagery create depth without heavy gradients.
4. **Progressive confidence:** filters reveal only relevant choices, guiding users from brand to model to storage to condition.

### Color Philosophy
Warm white is the canvas, not a sterile white. Near-black graphite anchors hierarchy and communicates seriousness. A muted sage green is the ownable trust signal used sparingly for active states, savings, and reassurance. Soft clay and mist neutrals separate surfaces without visual clutter.

### Layout Paradigm
Use an asymmetric editorial rhythm: hero copy sits in a narrow left rail while product imagery occupies a large, offset stage. Browse pages use a persistent left filter rail and an expansive catalog field. On mobile, information collapses into stacked sections and horizontal product shelves rather than dense centered cards.

### Signature Elements
- A small sage **signal dot** that marks warranty, verification, or active selection.
- **Gallery ribbons** that use fine rules and compact uppercase metadata under product imagery.
- **Offset product stages** where images sit slightly outside a pale surface, creating the feel of a studio set rather than a conventional card.

### Interaction Philosophy
Interactions should feel physical and immediate: buttons compress subtly, cards lift by a few pixels, filters update counts as soon as a choice is made, and sheets enter from the edge they belong to. The interface should never surprise the user with a full reset or a hidden transaction.

### Animation
Use 160–240ms ease-out transitions for controls and cards. On initial load, stagger only major hero elements and featured products by 40ms. Use transform and opacity for motion, never layout shifts. Product imagery may drift 4–6px on hover. Respect reduced-motion preferences.

### Typography System
Use **DM Sans** for body and interface copy, with **Space Grotesk** for headlines and wordmark-adjacent display moments. Headlines are medium weight with tight tracking; metadata is compact, uppercase, and slightly tracked. Prices use tabular-looking medium-weight numerals for quick scanning.

### Brand Essence
**SwapPhone makes second-hand phones feel like a smart, premium choice for design-conscious buyers who value clarity over marketplace noise.** Personality: assured, thoughtful, refreshingly direct.

### Brand Voice
Headlines are concise and declarative. CTAs are active but not pushy. Microcopy explains the next step in plain language and avoids hype.

Example headline: “Better phones. Better sense.”

Example microcopy: “Every listing shows what matters before you decide.”

### Wordmark & Logo
The mark is an abstract interlocking S made from two rounded phone silhouettes, suggesting exchange without using arrows or commerce tropes. The wordmark is a custom-spaced lowercase “swapphone” treatment with a slightly tightened “swap” and airy “phone,” paired with the mark at a clearly visible size.

### Signature Brand Color
**Swap Sage, #A6B89A**, a softened mineral green that reads as reassuring and contemporary without becoming loud.

## Implementation reminders

- Keep the light theme only.
- Keep catalog entities in editable JSON under `client/public/data/` and resolve references by IDs.
- Keep image paths in JSON; use generated assets for the hero and a small set of authentic listing photos.
- Do not add purchase, checkout, payment, authentication, or transaction flows.
- Add file-level style comments to CSS, data, and major component/page files so the Quiet Studio direction stays explicit.
