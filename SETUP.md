# Abhay Singh — Gojo Theme GitHub Profile Setup

## Included in this package

- `README.md` — complete profile page: animated hero, about card, skill constellation, hanging ID dashboard, featured missions, repository cards, contribution skyline and connect section.
- `gojo-hero-motion.gif` — animated hero where **Abhay Singh types in** while Gojo moves. `gojo-pointing.gif` and `gojo-chibi.png` are supporting character art.
- `about.svg`, `skills.svg`, `dashboard.svg`, `missions.svg`, `connect.svg` — custom blue / violet / gold panels. The dashboard ID swings from a lanyard; the about artwork floats.
- `01-…` to `05-…` `.svg` — one clickable illustrated card per project.
- `hobbies.svg` (animated hobby cards), `quote.svg` (Six Eyes quote banner), `typing-intro.gif`, plus self-generated GitHub stats cards (`scripts/gojo_stats.py` + `profile-stats/`), views counter and a Gojo-coloured contribution snake.
- `.github/workflows/profile-3d.yml` — scheduled 3D contribution skyline workflow.
- `profile-3d-contrib/` — contribution skyline SVG (placeholder until the workflow runs).
- `PROJECT-INVENTORY.md` — project list and a copy-ready card template.

## Upload / replace the profile

1. Open `https://github.com/morgancodes09/morgancodes09` (the repo named exactly like your username).
2. Extract this ZIP on your computer.
3. Open the extracted folder, select **all files and folders**, including hidden `.github`.
4. Upload them to the **root** of the repository using **Add file → Upload files**. Keep the folder structure; the README uses root-relative paths.
5. Commit the upload, then hard-refresh your profile with `Ctrl + Shift + R`.
6. Open **Actions → Gojo's 3D Skyline + Snake → Run workflow** once and wait for a green run. This creates the 3D skyline and the snake (published to the `output` branch). Until then the snake image shows as broken.
7. Delete obsolete files from your earlier upload only after the new profile looks right (old `*-motion.gif`, `typing-intro.gif`, `badges/`, `hobby-*.gif`, `connect-banner.svg`, `divider.gif`, `gojo-contribution-skyline.gif`, `skills-six-eyes.gif`, `about-motion-v2.gif`, `dashboard-motion.gif`, `connect-motion.gif`).

## Add a new repository later

1. Copy an existing `NN-name.svg` card, rename it, and edit the title, one-line description and technology chips.
2. In `README.md`, add a new `<td>` with the linked image inside the grid in **Repository Collection**.
3. To promote it, add a card to `missions.svg` and a bar in `dashboard.svg`.
4. If the public repository count changes, update `14+` in `dashboard.svg`.

## Notes

- If GitHub caches an image, bump the `?v=` number on it in `README.md`.
- SVG motion may vary by client; the layout stays readable if animation does not play.
- Hospital Readmission Prediction and SkyPulse have no repository link yet. Once you have the URLs, wrap their images in `<a href>` in `README.md` and `missions.svg`.
