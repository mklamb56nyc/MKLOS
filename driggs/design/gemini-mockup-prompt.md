# Gemini image prompts — Crossed Arrows Lot 3 mockup

Copy a prompt below into Gemini (Nano Banana / Gemini image / "Imagine"). Start with
**Prompt A**. Ask for **16:9**, generate 3–4 variations, then iterate conversationally
("keep everything, make the roofs flatter / the glass taller / more snow").

## Should you feed it the site plan and inspiration images? — yes, selectively
Gemini blends text + reference images. Use references where they help and keep the count low
(1–3); too many muddy it.

- **Inspiration photos (High Horse Ranch) → YES, always.** This is the single biggest quality
  lever. Text like "Cor-Ten + reclaimed wood + floor-to-ceiling glass" gets you *near* the look;
  a real photo locks the exact weathered-steel tone, wood warmth, roof proportion, and mood. Grab
  2–3 High Horse Ranch exterior photos (Dezeen / Architectural Record / the KieranTimberlake page)
  and attach them: *"Match the materials, roof, and mood of these reference photos."*
- **The site-plan schematic (`site-plan-schematic.svg`) → only for the aerial (Prompt B), and
  label it.** Image models don't reliably turn a 2D diagram into a correct 3D eye-level scene — and
  may try to *redraw* the diagram. For the aerial it's useful as a layout guide; attach it and say:
  *"Use the attached top-down plan only to place the three buildings, the fire pit, and the
  driveway — render a photorealistic aerial, do not reproduce the diagram or its labels."* For
  eye-level shots (A, C, D), skip it and let the text carry the composition.
- **The garage section (`garage-section.svg`) → only with Prompt E**, same "reference for the
  roof/door geometry, don't draw the diagram" caveat.
- **Workflow:** run a **text-only baseline first**, then add the High Horse Ranch photos and
  regenerate — you'll immediately see the reference lock the look. Iterate by editing, not
  restarting ("keep this exact image but add snow / lower the sun").

The prompts below are written to stand on their own (prompt carries the weight); the reference
photos make them *faithful* rather than merely *plausible*.

---

## Prompt A — hero exterior, dusk (start here)  ·  attach: High Horse Ranch photos
> Photorealistic architectural visualization, wide cinematic three-quarter view at golden-hour
> dusk, camera low and to one side. **Three separate low, single-story modern buildings set on a
> very gentle arc and angled slightly inward so they all aim at the same distant point** across a
> high-desert sagebrush meadow in Idaho's Teton Valley (~6,200 ft), the jagged snow-capped **Teton
> Range on the horizon** catching pink alpenglow. A larger main house in the center, a 3-car garage
> to one side and a two-bedroom bunkhouse to the other. **Each building opens a full-height,
> full-width wall of glass toward the mountains, glowing warm from within**, sheltered by a **flat,
> low-slope single-pitch (shed) roof that is tall over the glass and slopes down to a low far edge,
> with a deep cantilevered overhang and wood-clad soffit**; low-profile flush solar panels on the
> roofs. In the foreground between the buildings, a **circular stone fire pit with a curved
> stone-bench amphitheater**, fire lit. Side and back elevations clad in **weathering Cor-Ten steel
> and warm reclaimed wood**, minimal openings. KieranTimberlake High Horse Ranch design language:
> contemporary-rustic, warm earth tones, industrial precision, long horizontal lines hugging the
> land. Dusting of snow, big sky, calm and minimal. Full-frame camera, 35mm, f/8, crisp
> architectural photography, high dynamic range. 16:9.
>
> Negative: no pitched/gabled roofs, no suburban houses, no visible power lines, no fussy ornament,
> no railings or clutter, no people, not cartoonish, not a gray clay render.

## Prompt B — the arrangement, aerial oblique  ·  attach: High Horse Ranch photos + site-plan-schematic.svg (layout guide only)
> Photorealistic aerial oblique (drone, ~150 ft up) of **three low flat-shed-roof modern detached
> buildings on a very gentle arc, each turned slightly inward so all three face a shared point
> toward a mountain range** (sightlines converge). Center main house, a 3-car garage at one end and
> a bunkhouse at the other. Flat single-slope roofs (high on the mountain/glass side, low on the
> back), deep overhangs, flush roof solar; full-height glass on the mountain-facing side, Cor-Ten
> steel and reclaimed wood on the other faces. **The 3 garage doors are on the back (low, road)
> side, flush-clad to match.** **In the courtyard on the mountain side, a circular stone fire pit
> ringed by a tight curved stone bench.** A gravel driveway curves in from the road side to a small
> motor court behind the buildings; open sagebrush meadow between the buildings and the snow-capped
> Teton Range. Warm low sun, long shadows, KieranTimberlake High Horse Ranch aesthetic, minimalist.
> 16:9. Negative: no pitched roofs, no fences, no suburbia, no clutter, do not render a diagram.

## Prompt C — the western approach / arrival (shows the garage doors)  ·  attach: High Horse Ranch photos
> Photorealistic eye-level view of the **quiet back (west) side of a three-building modern compound
> at the end of a gravel driveway and motor court**, the snow-capped Teton Range rising behind the
> low rooflines. The buildings present **understated façades of weathering Cor-Ten steel and warm
> reclaimed wood with few, recessed openings**, under **flat low-slope shed roofs that rise away
> from the viewer** (low eave on this near side, taller behind). The nearest building is a garage
> with **three flush garage doors clad in the same Cor-Ten/wood so they nearly disappear into the
> façade**, set under a ~10-ft low eave. Deep overhangs, thin fascia, a stacked-firewood nook.
> Overcast soft light, calm, minimal, KieranTimberlake High Horse Ranch style. 16:9.
> Negative: no pitched roofs, no big glass on this side, no suburban roll-up doors, no clutter.

## Prompt D — interior, looking out the view wall  ·  attach: High Horse Ranch interior photos
> Photorealistic interior of a warm minimalist single-story home, standing in an open living space
> looking out through a **full-height, full-width wall of glass** at the snow-capped Teton Range.
> **Reclaimed Douglas-fir ceiling that slopes up toward the glass** with exposed structure and a
> deep overhang shading the view, polished concrete floor, Cor-Ten and wood accents, a low
> fireplace, spare furnishings. Warm morning light, alpenglow on the peaks. KieranTimberlake High
> Horse Ranch aesthetic. 16:9. Negative: no clutter, no ornate furniture, no small punched windows.

## Prompt E — the garage, three-quarter (roof + doors correct)  ·  attach: garage-section.svg (geometry ref, don't draw it) + High Horse Ranch photos
> Photorealistic three-quarter exterior of a **single modern 3-car garage** in a sagebrush meadow.
> **Flat single-slope (shed) roof, low on the door side and rising to a taller far edge**; on the
> low front side, **three garage doors flush-clad in weathering Cor-Ten steel and reclaimed wood**
> under a ~10-ft eave, reading as quiet planes. The tall far (mountain) side carries a **band of
> clerestory glass**. Deep overhang, thin fascia, wood soffit, flush roof solar. Gravel apron in
> front. Snow-capped Teton Range beyond. KieranTimberlake High Horse Ranch material palette,
> minimalist, warm earth tones. 16:9. Negative: no pitched roof, no suburban raised-panel doors,
> no clutter, do not render a diagram.

---

## Reference notes to keep the model on-brief
- **Massing:** three *detached* rectangular volumes, single story, long and low; very gentle arc,
  end buildings toed slightly inward so all sightlines converge toward the mountains.
- **Roofs:** flat / very-low single slope (**high edge on the glass/mountain side, low edge on the
  back/road side**), deep cantilevered overhangs, wood soffits, low-profile flush solar.
- **Garage:** doors on the **low back (road) side**, flush-clad to match; clerestory glass on the
  tall mountain side.
- **Foreground:** circular stone fire pit + tight curved stone bench, between the buildings and the
  view.
- **Materials:** Cor-Ten weathering steel (rusted-warm), reclaimed wood, floor-to-ceiling glass,
  concrete plinth/piers. Warm earth palette.
- **Setting:** Teton Valley sagebrush meadow, ~6,200 ft, big sky, snow-capable, Teton Range to view.
- **Mood:** quiet, minimal, contemporary-rustic — High Horse Ranch, not "mountain lodge."
