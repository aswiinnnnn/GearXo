# SwapPhone Apple-inspired revision

## Downloadable project archive

- [ ] Package the complete frontend project source and configuration into a ZIP, excluding generated dependencies and transient logs.
- [ ] Validate the archive contents and deliver it to the user.


- [x] Replace the current typography with an Apple-like system font stack and confirm the visual hierarchy.
- [x] Show original-colour brand icon artwork in horizontally scrollable brand filters, with a graceful fallback when an icon is unavailable.
- [x] Add multi-select model, storage, condition, warranty, battery, and colour filter state and controls.
- [x] Add a dual-thumb min/max price range slider and active filter summary.
- [x] Remove the mobile hamburger and show current-page state in header and bottom navigation.
- [x] Add a minimal global scroll progress indicator, skeleton loaders, custom 404, empty, and error states.
- [x] Add markdown-capable product descriptions and a sticky price/purchase bar on product details.
- [x] Remove marketplace seller/review language and simplify the single-store sell flow to a contact CTA.
- [x] Rebuild the mobile hero composition.
- [x] Add non-blank product recommendations ranked by model, brand, specs, and price proximity.
- [x] Validate desktop/mobile routes and save a new checkpoint.

## Focused UI cleanup

- [x] Hide the default browser scrollbar while retaining the custom top scroll progress indicator.
- [x] Remove colour selection from the filter taxonomy and filter state.
- [x] Convert product recommendations into a horizontally scrollable rail.
- [x] Move the saved/wishlist action to the top-right of product details.
- [ ] Verify the changes at mobile and desktop sizes, then save a checkpoint.

## Sort control fix

- [x] Replace the native sort select with a shadcn-style dropdown menu.
- [x] Verify keyboard, outside-click, and responsive behavior, then checkpoint the fix.

## Hero background refinement

- [x] Use the generated phone image as the hero section background rather than a separate image column.
- [x] Add responsive overlay treatment so the copy and actions remain readable.
- [x] Verify the hero on mobile and desktop, then save a checkpoint.

## Final mobile chrome cleanup

- [x] Hide native scrollbars inside the mobile filter drawer and all nested horizontal scrollers.
- [x] Pin the mobile wishlist/favourite icon to the far top-right edge of the header.
- [x] Verify the narrow mobile drawer/header and save a checkpoint.

## Mobile hero framing

- [x] Add a mobile-specific background size and position so the phone imagery is visible at the intended scale.
- [x] Verify mobile and desktop hero framing, then save a checkpoint.

## Reference-aligned mobile hero

- [x] Keep the phone artwork as a CSS background image and structure the mobile hero as an upper copy zone with a lower image reveal.
- [x] Match the reference’s mobile spacing, image crop, and rounded container treatment.
- [x] Verify mobile and desktop hero layouts, then save a checkpoint.

## Continuous mobile hero background

- [x] Make the mobile phone artwork read as one continuous CSS background behind the copy and CTAs.
- [x] Remove the lower-block visual impression while keeping text contrast and image visibility.
- [x] Verify mobile and desktop hero composition, then save a checkpoint.

## Seamless mobile hero crop

- [x] Enlarge and reposition the mobile CSS background so phone artwork is present across the full hero height.
- [x] Soften the mobile overlay transition to remove the horizontal seam while preserving text contrast.
- [x] Verify the mobile hero and save a checkpoint.

## Proper seamless mobile hero fix

- [x] Replace the seam-producing mobile hero composition with a seamless background treatment or mobile-specific asset.
- [x] Keep the image visually behind the full hero content with no horizontal panel boundary.
- [x] Verify against the supplied mobile reference and save a checkpoint.

## Mobile-only hero verification

- [x] Inspect and verify the mobile viewport only, using the dedicated mobile background asset.
- [x] Confirm the image is visually behind the full mobile hero content with no lower panel impression.
- [x] Save a checkpoint after mobile verification.

## Deployed mobile asset binding

- [ ] Ensure the mobile breakpoint requests and renders the dedicated seamless hero asset instead of the old desktop asset.
- [ ] Verify the actual mobile asset request and visual output after rebuild.
- [ ] Save a checkpoint only after the deployed mobile view is confirmed.

## Compact hero height

- [x] Add responsive max-height limits to the hero without clipping copy or CTAs.
- [x] Verify the shorter hero on mobile and desktop, then save a checkpoint.

## Tighter mobile hero

- [ ] Reduce mobile hero max height and internal padding so it occupies less of the first screen.
- [ ] Verify headline, supporting copy, and both CTAs remain visible, then save a checkpoint.

## 360px mobile hero

- [x] Reduce the mobile hero max height to approximately 360px and tighten its internal spacing.
- [x] Verify the trust strip enters the first screen sooner without clipping the CTAs, then save a checkpoint.

## Supplied logo and shorter mobile hero

- [ ] Prepare optimized transparent logo variants from the supplied app logo.
- [ ] Replace the existing mark everywhere in the app and update favicon metadata.
- [ ] Reduce the mobile hero height further and preserve readable content and CTAs.
- [ ] Verify logo rendering and mobile hero, then save a checkpoint.

## Homepage CTA order

- [x] Move the “Ready to look around? / Browse all 8 mobiles” section below featured phones at the bottom of the homepage.
- [x] Verify the homepage order and save a checkpoint.

## Simplified homepage

- [x] Remove the warranty, delivery, returns, and quality trust strip from the homepage only.
- [x] Verify the homepage spacing and save a checkpoint.

## Care Plus rebrand

- [x] Replace visible SwapPhone app naming with “Care Plus” across the website.
- [x] Show “Care Plus” beside the supplied logo in the top-left header and update page metadata.
- [x] Verify the rebrand and save a checkpoint.

## More expressive mobile hero

- [x] Improve the compact mobile hero’s image-led composition and visual hierarchy without increasing height.
- [x] Strengthen CTA grouping and overlay contrast while keeping both actions visible.
- [x] Verify the mobile hero and save a checkpoint.

## Homepage category rail

- [x] Add editable category data for popular phone browsing paths.
- [x] Build visual category cards with direct filtered-catalogue navigation.
- [x] Make the category row horizontally scrollable on mobile and spacious on desktop.
- [x] Verify category navigation and save a checkpoint.

## Balanced mobile hero

- [x] Add intentional vertical rhythm between eyebrow, headline, description, and CTA row.
- [x] Remove the empty-feeling lower hero area by balancing content placement with the background image crop.
- [x] Verify the mobile hero and save a checkpoint.

## Homepage order and punctuation cleanup

- [x] Move Shop by mood directly above Featured phones.
- [x] Remove every em dash character from visible website copy and editable content data.
- [x] Verify the homepage order and copy, then save a checkpoint.

## Copy cleanup and catalogue expansion

- [x] Search the complete codebase for em dash characters and rewrite affected website copy naturally.
- [x] Preserve Nothing and Motorola brands and their existing catalogue paths.
- [x] Add 20 additional realistic device listings with valid existing brand, model, image, condition, pricing, and filter references.
- [x] Validate the expanded catalogue, remove all em dashes, and save a checkpoint.

## Apply researched homepage copy

- [x] Replace the generic hero headline, eyebrow, description, and CTA labels with specific buyer-focused messaging.
- [x] Rewrite category, featured, and final catalogue CTA copy to be concrete and conversion-oriented.
- [x] Preserve Nothing and Motorola references and verify the 28-device catalogue after the copy update.
- [x] Save a checkpoint after homepage copy verification.

## Remove Nothing and Motorola

- [ ] Remove Nothing and Motorola products, models, and brand entries from the JSON catalogue.
- [ ] Remove Nothing and Motorola from visible homepage, filters, brand navigation, and searchable content.
- [ ] Validate the remaining catalogue count and save a checkpoint.

## Latest iPhone model browse section

- [x] Replace the post-brand section with latest iPhone model cards driven by catalogue data.
- [x] Add direct model links into the filtered catalogue.
- [x] Verify mobile and desktop model browsing, then save a checkpoint.

## Home and sell hero copy

- [ ] Replace the home hero headline and supporting copy with a sharper buyer outcome and clear proof.
- [ ] Replace the sell hero headline and supporting copy with a clear valuation and contact action.
- [ ] Verify both pages and save a checkpoint.

## Compact home and sell hero copy

- [ ] Shorten the home hero headline and supporting copy so it fits cleanly on mobile.
- [ ] Shorten the sell hero headline and supporting copy so it fits cleanly on mobile.
- [ ] Verify both hero sections and save a checkpoint.

## Focused sell page

- [x] Remove the oversized sell hero treatment.
- [x] Replace it with a compact explanation of the estimate flow above the form.
- [x] Verify the sell page form on mobile and desktop, then save a checkpoint.

## Expand homepage featured phones

- [x] Show more phone listings in the final Featured phones section.
- [x] Preserve a compact mobile rail and a fuller desktop grid.
- [x] Verify the homepage and save a checkpoint.

## Navigation brand name

- [x] Add “Care Plus” beside the logo in the global navigation bar.
- [x] Verify the header on mobile and desktop, then save a checkpoint.

## Favicon-only correction

- [x] Remove the white rounded background from the navigation logo.
- [x] Apply the rounded white-square treatment only to the favicon asset.
- [x] Verify both treatments and save a checkpoint.

## Favicon visibility correction

- [ ] Enlarge and increase contrast of the Care Plus mark inside the favicon.
- [ ] Verify the favicon asset and save a checkpoint.

## Natural punctuation cleanup

- [x] Search the full codebase for em dash characters.
- [x] Rewrite affected copy with natural punctuation and verify none remain.
- [x] Save a checkpoint after verification.

## Product detail share and mobile purchase bar

- [x] Make the share action use the native share sheet with a copy-link fallback.
- [x] Restore visible price and purchase controls in the mobile sticky bar.
- [x] Verify product detail behavior on mobile and desktop, then save a checkpoint.

## Route scroll restoration

- [x] Reset scroll to the top whenever the route changes.
- [x] Verify page and product navigation scroll positions, then save a checkpoint.

## Reliable route scroll restoration

- [ ] Handle every route transition, including history navigation and reused-shell routes.
- [ ] Verify all major pages start at the top, then save a checkpoint.

## Visible device codes

- [x] Show each listing’s unique device code on product cards.
- [x] Show the device code prominently on product details.
- [x] Verify readability on mobile and desktop, then save a checkpoint.

## Simplified product-card pricing

- [x] Remove crossed-out original prices from product cards.
- [x] Use the secondary price area to show the unique device code clearly.
- [x] Verify product cards on mobile and desktop, then save a checkpoint.

## Direct Browse back navigation

- [x] Make the Product Detail back control navigate directly to Browse.
- [ ] Verify the control and save a checkpoint.

## Code-only product identifiers

- [x] Remove the “Device code” label from product cards and product details.
- [x] Verify the shorter identifiers and save a checkpoint.

## Curved sticky purchase bar

- [x] Add curved outer ends to the sticky price and purchase component.
- [x] Verify the rounded bar on mobile and desktop, then save a checkpoint.

## Simplified sticky purchase bar

- [x] Remove warranty details from the sticky price and purchase component, while keeping Free delivery.
- [x] Verify the simplified bar and save a checkpoint.

## Buy now purchase label

- [x] Rename the sticky purchase action to “Buy now”.
- [x] Verify the label and save a checkpoint.

## Favourite scroll preservation

- [x] Prevent favourite actions from resetting the current scroll position.
- [x] Verify saving from Browse and Product Detail, then save a checkpoint.

## Reload-free favourite toggles

- [x] Prevent add and remove favourite actions from reloading or remounting the page.
- [x] Verify both toggle states and save a checkpoint.

## Final favourite scroll-jump fix

- [x] Separate wishlist rerenders from route scroll restoration.
- [x] Verify add and remove at a scrolled position, then save a checkpoint.

## Mobile Saved count badge

- [x] Show the saved-device count on the mobile bottom-nav Saved item.
- [x] Verify the badge updates with favourites and save a checkpoint.

## Flicker-free favourite updates

- [x] Prevent product images from reloading when favourite state changes.
- [x] Verify cards and product details without image flicker, then save a checkpoint.

## Hide homepage brand selection

- [x] Comment out the homepage brand-selection section without deleting it.
- [x] Verify homepage flow and save a checkpoint.

## Refine Saved badge and toast

- [x] Move the mobile saved-count badge closer to the heart icon.
- [x] Apply a light toast surface with dark text and a subtle shadow.
- [x] Verify the mobile navigation and toast, then save a checkpoint.

## Remove header favourite

- [x] Remove the top-right favourite control from the global header.
- [x] Verify header spacing and saved-phone access, then save a checkpoint.

## WhatsApp sell enquiry

- [ ] Replace the estimate action with a WhatsApp enquiry button.
- [ ] Pass selected device details in the prefilled WhatsApp message.
- [ ] Confirm the Care Plus WhatsApp number and save a checkpoint.

## Replace app logo

- [x] Replace navigation, favicon, and branding references with a visible high-contrast treatment of the user-provided logo.
- [x] Verify the new logo at mobile and desktop sizes, then save a checkpoint.
- [x] Ensure the white logo remains legible on the navigation background and favicon.

## First-visit Browse tour

- [x] Show a homepage tour prompt after five seconds only for the first visit.
- [x] Add Skip and Browse now actions that persist dismissal/completion.
- [x] Verify timing, navigation, and mobile layout, then save a checkpoint.

## Compact Browse coachmark

- [x] Replace the large tour modal with a small coachmark anchored above mobile Browse.
- [x] Explain that Browse opens all devices and filters, with Maybe later and Browse now actions.
- [x] Verify coachmark placement and save a checkpoint.

## Coachmark pointer and wordmark size

- [x] Align the coachmark pointer with the actual mobile Browse item.
- [x] Increase the Care Plus wordmark size in the top navigation.
- [x] Verify mobile and desktop header treatment, then save a checkpoint.

## Closer Browse coachmark

- [x] Move the coachmark downward closer to the Browse bottom-nav button.
- [x] Verify the spacing and save a checkpoint.

## Repeatable homepage tour

- [x] Show the Browse tour again after refreshes and repeat homepage visits.
- [x] Limit dismissal to the current homepage visit and save a checkpoint.

## Icon-free tour card

- [x] Remove the decorative icon from the homepage tour card.
- [x] Verify the simplified card and save a checkpoint.

## Compact tour sizing

- [x] Reduce the homepage Browse tour card to the minimum useful size.
- [x] Verify the compact coachmark and save a checkpoint.

## Recently viewed homepage rail

- [ ] Show Recently viewed after more than three devices have been viewed.
- [ ] Use a horizontal scrolling product rail and verify it, then save a checkpoint.

## Narrower tour width

- [x] Reduce the homepage Browse coachmark to a centered max width.
- [x] Verify the narrower coachmark and save a checkpoint.

## Detailed device descriptions

- [x] Add detailed Markdown descriptions to every device listing.
- [x] Verify descriptions render correctly on Product Detail pages and save a checkpoint.

## Full-width purchase bar

- [x] Replace the floating curved price and Buy now component with a full-width square-ended bar.
- [x] Verify mobile and desktop Product Detail layouts, then save a checkpoint.

## Connect purchase bar to bottom navigation

## Remove remaining purchase-bar seam

## Further purchase-bar overlap

- [x] Move the mobile purchase bar farther down so the navigation fully covers the seam.
- [x] Verify the adjustment and save a checkpoint.

- [x] Overlap the fixed purchase bar and mobile bottom navigation to eliminate the remaining visible strip.
- [x] Verify the seam-free result at the reported mobile width and save a checkpoint.

- [x] Remove the gap between the mobile purchase bar and bottom navigation.
- [x] Verify the connected surfaces and save a checkpoint.

## Transparent navigation logo

- [ ] Create a black transparent navigation logo variant.
- [ ] Keep the rounded dark favicon unchanged.
- [ ] Verify both logo treatments and save a checkpoint.

## Rounded white favicon

- [ ] Create a white rounded-square favicon background around the Care Plus logo.
- [ ] Bind the new favicon asset and verify it in the app metadata.
- [ ] Verify the result and save a checkpoint.

## Navigation lockup alignment

- [x] Correct the visual baseline and spacing between the logo and Care Plus name.
- [x] Verify the header on mobile and desktop, then save a checkpoint.
