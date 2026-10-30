# MBERRY BURO website: free hosting guide

A single-page static site. No build step and no server needed. All copy, prices, projects and contact details live in `content.json`.

## 1. Put it online for free (about 5 minutes)

**Option A: Netlify Drop (fastest, no Git)**
1. Go to https://app.netlify.com/drop and sign up free.
2. Drag this whole folder onto the page. You get a link like `https://mberry-buro.netlify.app` (HTTPS included).
3. Rename the site under *Site configuration → Change site name*.

**Option B: GitHub Pages (recommended, enables the free CMS)**
1. Create a free GitHub account and a new public repository, e.g. `mberry-buro`.
2. *Add file → Upload files*, drop in everything from this folder (including `.pages.yml`), commit.
3. *Settings → Pages → Source: Deploy from branch → main / root*. Live at `https://<username>.github.io/mberry-buro/`.

Cloudflare Pages and Vercel also work the same way (import the repo, no build command, output directory `/`).

## 2. Turn on the enquiry form (free)

The form uses FormSubmit (https://formsubmit.co), free, no account, supports file attachments.
1. In `content.json` set `"form": { "endpoint": "https://formsubmit.co/ajax/YOUR-EMAIL" }`.
2. Submit one test enquiry from the live site. FormSubmit emails an activation link; click it.
3. Optional: replace your email in the URL with the random alias FormSubmit gives you, so the address is not visible in the code.

Spam protection: honeypot field + minimum fill time. Each email includes the selected package and the lead source (which button the visitor clicked).

## 3. Edit content without code (free CMS)

With Option B: go to https://app.pagescms.org, sign in with GitHub, open the repo. You get forms to edit projects and photos, copy, prices, package details and contact info. Each save commits to GitHub and the site updates within a minute.

## 4. Before launch checklist (from the brief)

- Replace placeholder images in `img/` with approved project photos (WebP, about 2000px wide for galleries, 1200px for cards). Update names, types, verified locations.
- Remove the grey preview bar (`<div class="preview-bar">`) and the project disclaimer paragraph in `index.html`. Remove the "Draft for legal review" tag once the privacy text is approved.
- Real email, phone, WhatsApp and Instagram in `content.json`.
- Set your domain in `sitemap.xml`, `robots.txt` and add `<link rel="canonical">` / `og:url` in `index.html`.
- Confirm public site language(s), prices and currencies.

If you edit `content.json` by hand, also run `python3 build.py` (optional) to refresh the copy embedded in `index.html` for search engines. The live site always loads the latest `content.json` anyway.
