# FinMedTech Landing Pages

This repo is the complete website for **finmedtech.co.uk** — the company homepage, the company-level Privacy Policy and Terms of Use, and the BP Tracker product pages.

**TaxSwipe is not served from here.** Its product page and legal documents live on `taxswipe.co.uk`, which is a separate Vercel project deployed from a different repo. The `/taxswipe/*` routes here are 301 redirects only.

## Structure

```
├── index.html              # Company homepage (finmedtech.co.uk)
├── privacy-policy.html     # FinMedTech company Privacy Policy
├── terms-of-use.html       # FinMedTech company Terms of Use
├── bp-tracker/             # BP Tracker product page + its legal documents
├── .well-known/            # security.txt
├── vercel.json             # Headers and redirects
└── README.md               # This file
```

## URLs After Deployment

```
https://finmedtech.co.uk/                  → Company homepage
https://finmedtech.co.uk/privacy           → FinMedTech Privacy Policy
https://finmedtech.co.uk/terms-of-use      → FinMedTech Terms of Use
https://finmedtech.co.uk/bp-tracker        → BP Tracker product page
```

### Legacy TaxSwipe routes (301 → taxswipe.co.uk)

`taxswipe.co.uk` is the single source of truth for TaxSwipe's legal documents. These routes exist only so older
App Store Connect and HMRC references keep resolving — nothing is served from this repo under `/taxswipe`:

```
/taxswipe/terms    → https://taxswipe.co.uk/terms
/taxswipe/privacy  → https://taxswipe.co.uk/privacy
/taxswipe/*        → https://taxswipe.co.uk/
/taxswipe          → https://taxswipe.co.uk/
/taxnav/*          → the matching taxswipe.co.uk URL (older brand name)
```

Do not re-add TaxSwipe HTML under `/taxswipe` in this repo. Two copies of a legal document is exactly the defect
TSW-620 fixed: the copy here drifted to a version missing its refund clause while `taxswipe.co.uk` carried the
current one.

## Current Deployment

This site is deployed via **Vercel**, connected to a **separate** GitHub repo: `chatrath02/finmedtech-website` (connected Feb 25).

- **Vercel project name:** `finmedtech-website`
- **GitHub repo:** `chatrath02/finmedtech-website` (separate from the main TaxSwipe repo)
- **Domain:** `finmedtech.co.uk`
- **Deploys automatically** on push to the connected branch

### This repo is the only source

`chatrath02/finmedtech-website` is the sole source for finmedtech.co.uk. The Vercel project's root directory
is unset — it deploys this repo's root. Pushing to the connected branch is all that is needed to go live.

There is no second copy to keep in sync. If you find `landing-page/` in the TaxSwipe repo, it is a stale
leftover that is deployed nowhere — do not edit it and do not treat it as this site's source.

## Deployment Instructions

### Option 1: Vercel (Recommended - Free, Fast)

1. Go to https://vercel.com and sign up (free)

2. Click **"Add New"** → **"Project"**

3. **Import this folder:**
   - Drag and drop this repo's root folder
   - OR connect GitHub repo and select this folder

4. **Deploy:**
   - Click "Deploy"
   - Wait ~30 seconds

5. **Connect your domain:**
   - In Vercel project → **Settings** → **Domains**
   - Click "Add Domain"
   - Enter: `finmedtech.co.uk`
   - Follow DNS instructions (add A record or CNAME)
   - Wait 5-60 mins for DNS propagation

6. **Verify:**
   - Visit https://finmedtech.co.uk
   - Check all pages work

### Option 2: Netlify (Alternative - Also Free)

1. Go to https://netlify.com and sign up

2. Drag and drop this repo's root folder

3. Click "Deploy"

4. Add custom domain in Settings → Domain management

### Option 3: GitHub Pages

1. Create new GitHub repo: `finmedtech-website`

2. Upload all files from this repo's root

3. Go to repo **Settings** → **Pages**

4. Set source to `main` branch, `/` (root)

5. Add custom domain: `finmedtech.co.uk`

6. Update DNS:
   ```
   A record: @ → 185.199.108.153
   A record: @ → 185.199.109.153
   A record: @ → 185.199.110.153
   A record: @ → 185.199.111.153
   CNAME: www → yourusername.github.io
   ```

## DNS Configuration (for any hosting)

**At your domain registrar** (where you bought finmedtech.co.uk):

### For Vercel:
```
A record: @ → 76.76.21.21
CNAME: www → cname.vercel-dns.com
```

### For Netlify:
```
A record: @ → 75.2.60.5
CNAME: www → your-site-name.netlify.app
```

Vercel/Netlify will show you exact DNS records after you add the domain.

## What These Pages Are For

### App Store Submission Requirements

Apple and Google require:
- ✅ **Privacy Policy URL** → `https://taxswipe.co.uk/privacy`
- ✅ **Terms of Service URL** → `https://taxswipe.co.uk/terms`
- ✅ **Marketing URL** (optional) → `https://taxswipe.co.uk/`
- ✅ **Support URL** (optional) → `https://taxswipe.co.uk/`

Use the `taxswipe.co.uk` URLs directly. The `finmedtech.co.uk/taxswipe*` equivalents still resolve via 301, but
they are a compatibility shim for already-submitted references, not the addresses to give out.

### HMRC Production Application

HMRC requires:
- ✅ **Organization URL** → `https://finmedtech.co.uk`

## Testing Locally

To preview before deploying:

1. Open `index.html` in your web browser
2. Click "Learn More" on the TaxSwipe card → should leave the site for `https://taxswipe.co.uk/`
3. Click "Learn More" on the BP Tracker card → should open `bp-tracker/index.html`
4. All links should work

Redirects live in `vercel.json` and are not exercised by opening files locally. Verify them against the Vercel
preview deployment instead:

```bash
curl -sIL https://finmedtech.co.uk/taxswipe/terms   # must end at https://taxswipe.co.uk/terms, 301 in the chain
curl -sIL https://finmedtech.co.uk/taxswipe/privacy
curl -sIL https://finmedtech.co.uk/taxswipe
```

## Next Steps

**After Deployment:**

1. ✅ Verify all URLs work
2. ✅ Set up email forwarding: `hello@finmedtech.co.uk` → your personal email
3. ✅ Submit HMRC production application with `https://finmedtech.co.uk`
4. ✅ Use these URLs in App Store Connect submission

## Updating Content

To update any page:
1. Edit the HTML file locally
2. Re-upload to Vercel/Netlify (automatic deployment)
3. OR push to GitHub (if using GitHub Pages)

## Need Help?

- Vercel Docs: https://vercel.com/docs
- Netlify Docs: https://docs.netlify.com
- GitHub Pages: https://pages.github.com
