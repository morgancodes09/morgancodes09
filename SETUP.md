# Setup — Abhay's Goku / Saiyan GitHub Profile

## Upload
1. Create or open the public profile repository `morgancodes09/morgancodes09`.
2. Upload the contents of this bundle to the repository root, preserving `.github/workflows/profile-3d.yml`.
3. Open Actions, enable workflows if prompted, and run **Planet Namek 3D Contribution Skyline** once.

## Only remaining personal edits
- Add a public email address if you want one displayed.
- Add LinkedIn and Instagram URLs if you want those cards linked.
- Replace the five project repository links with their exact repository URLs. The current links open your repository list and do not pretend to know individual repo names.
- Confirm whether Ghaziabad is the location you want publicly displayed; it is currently used as your KIET campus location.
- Add actual GitHub counts (repositories, followers, stars, contributions) if you want numeric dashboard values. They were not available in the provided context.

## Included files
- `hero.svg` — personalized animated hero with Abhay's name, role rotation, college and location.
- `saiyan-way.svg` — personal development values.
- `techniques-stack.svg` — skills grid.
- `zfighter-id.svg` — ID badge and dashboard.
- `connect.svg` — Goku-inspired pointing mascot with `@morgancodes09`.
- `goku-walk.gif`, `goku-dance.gif`, `goku-kamehameha-run.gif` — three looping 8-frame chibi GIFs.
- `.github/workflows/profile-3d.yml` — daily contribution skyline workflow.

## Character art regeneration prompts
**ID portrait:** Original anime-inspired Saiyan developer portrait, waist-up, cheerful confident young adult with dramatic spiky black hair, expressive eyes, orange martial-arts gi over a deep-blue undershirt, blue wrist wraps, golden energy aura, crisp original cel-shaded fan-art aesthetic, transparent background, centered composition, no logos, no text, high resolution.

**Connect pose:** Original anime-inspired Saiyan developer mascot, full body, smiling and pointing toward a neon sign that reads `@morgancodes09`, orange gi with blue undershirt and wristbands, spiky black hair with subtle orange rim light, three glowing orange-gold energy orbs and sparkles, sticker-style outline, transparent background, high resolution.

**Chibi sprite frames:** Eight-frame horizontal sprite strip, same original chibi Saiyan developer in orange gi and blue wristbands, consistent scale and proportions, transparent background, no borders or text. Make separate strips for an eight-pose walk cycle, an eight-pose dance with a blue-armored rival and purple-haired young fighter, and a run/energy-sphere cycle. Each cell should be 480×480.

## Notes
- Personal details filled from information previously supplied: Abhay Singh, `morgancodes09`, KIET Group of Institutions, known skills, hobbies and five known projects.
- Email, direct social URLs, exact project repository URLs and current GitHub counts were not available, so they are intentionally not fabricated.
- SVGs use embedded PNG artwork and CSS/SMIL only; no JavaScript or remote image/font dependencies are required inside the SVGs.


## Dashboard count note
The animated dashboard uses known profile facts rather than fabricated live GitHub statistics: 5 listed projects, semester 5, 5 programming languages (C, C++, Java, Python and Dart), and 16 listed tools/technologies. If your project list or skills change, update the values in `zfighter-id.svg` and the explanatory note in `README.md`.


## Hero character motion

The hero SVG uses sixteen separate, embedded transparent Goku frame images. They are opacity-cycled with SVG SMIL animations, following the same layered-frame technique used by the original reference profile. Goku himself gently breathes, sways and shifts through a continuous idle loop; the aura and scanner are separate animations. `assets/hero-motion.gif` is a matching preview of the same character motion. The small badge portrait elsewhere in the profile remains static by design.

GitHub may cache SVG images. If the updated hero does not appear immediately after committing, bump the local image query version in `README.md` (for example `hero.svg?v=3`).

## Contribution skyline

The workflow is named `GitHub-Profile-3D-Contrib`. After uploading the repository, open **Actions → GitHub-Profile-3D-Contrib → Run workflow** once. The generated `profile-3d-contrib/profile-night-view.svg` is created by the action; it is not included in the ZIP before the first successful run. The workflow then refreshes it daily.
