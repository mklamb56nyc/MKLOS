# Microsite photo sources

`index.html` is self-contained — all seven photos are embedded as base64 JPEG
data URIs (compressed to ~1MB total), so the page works as a repo file, a
claude.ai artifact, or an email attachment with no external requests.

Published artifact (private link, share from its menu):
https://claude.ai/code/artifact/d1c97b65-a8c2-45f5-b69e-6b4a1c29c9a4

Also published on the live site as `/private/sintra19.html` in
`received-wisdom-site` ("The study" hub links it). The site copy is this
file plus a standard document head, `<meta name="robots" content="noindex">`
(the `private/` convention there), and one line changed: the kids' names are
removed from the fine print, per the "family details stay out of anything
published" rule. Cover headline "Play with me!?" and the
"Mr & Mrs Active Man and Wife" masthead line are Mike's (2026-07-23).

All images are from Wikimedia Commons, scaled via the Commons thumbnail API
(hero 1400px, others 1000px), recompressed with Pillow (q≈68–76):

| Slot | File on Commons | Author | License |
|---|---|---|---|
| Hero (cover) | Cliffs at Cabo da Roca, Portugal, 20250606 1522 0263.jpg | Jakub Hałun | CC BY 4.0 |
| The address | GOLF DE PENHA LONGA Portugal (1413021987).jpg | lele3100 | CC BY 2.0 |
| The address | Palácio Nacional da Pena, Sintra, Portugal, 20250606 1159 0132.jpg | Jakub Hałun | CC BY 4.0 |
| Friday | Marina de Cascais (Portugal).jpg | Vitor Oliveira | CC BY 2.0 |
| Saturday golf | Guincho Dunes near Cascais.jpg | Walterpeitz | CC BY-SA 4.0 |
| Saturday wine | Autumn vineyards (38013421512).jpg | Frayle | CC0 |
| Sunday | Beach at sunset, Praia D'El Rey, Amoreira, Portugal julesvernex2.jpg | Jules Verne Times Two | CC BY-SA 4.0 |

Honesty notes (also in the page footer): the Guincho-dunes frame shows the
dune coast Oitavos plays through, not the course itself; the Praia D'El Rey
frame is the beach below West Cliffs. No Commons photos exist of either
course proper. Attribution is printed in the page footer as the licenses
require.

To swap a photo: find a replacement on Commons, download a scaled thumb via
the API (`iiurlwidth`), recompress, and replace the corresponding
`data:image/jpeg;base64,…` blob in `index.html` (each `<img>`'s `alt` text
identifies the slot).
