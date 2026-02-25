# FinMedTech Landing Pages

This folder contains the complete website for **finmedtech.co.uk** including TaxNav product pages, Privacy Policy, and Terms of Service.

## Structure

```
landing-page/
├── index.html              # Company homepage (finmedtech.co.uk)
├── taxnav/
│   ├── index.html         # TaxNav product page
│   ├── privacy.html       # Privacy Policy (required for App Store)
│   └── terms.html         # Terms of Service (required for App Store)
└── README.md              # This file
```

## URLs After Deployment

```
https://finmedtech.co.uk/                  → Company homepage
https://finmedtech.co.uk/taxnav/           → TaxNav product page
https://finmedtech.co.uk/taxnav/privacy    → Privacy Policy
https://finmedtech.co.uk/taxnav/terms      → Terms of Service
```

## Deployment Instructions

### Option 1: Vercel (Recommended - Free, Fast)

1. Go to https://vercel.com and sign up (free)

2. Click **"Add New"** → **"Project"**

3. **Import this folder:**
   - Drag and drop the entire `landing-page` folder
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

2. Drag and drop the `landing-page` folder

3. Click "Deploy"

4. Add custom domain in Settings → Domain management

### Option 3: GitHub Pages

1. Create new GitHub repo: `finmedtech-website`

2. Upload all files from `landing-page` folder

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
- ✅ **Privacy Policy URL** → `https://finmedtech.co.uk/taxnav/privacy`
- ✅ **Terms of Service URL** → `https://finmedtech.co.uk/taxnav/terms`
- ✅ **Marketing URL** (optional) → `https://finmedtech.co.uk/taxnav`
- ✅ **Support URL** (optional) → `https://finmedtech.co.uk/taxnav` (with support email link)

### HMRC Production Application

HMRC requires:
- ✅ **Organization URL** → `https://finmedtech.co.uk`

## Testing Locally

To preview before deploying:

1. Open `index.html` in your web browser
2. Click "Learn More" on TaxNav card → should open `taxnav/index.html`
3. Click "Privacy Policy" → should open `taxnav/privacy.html`
4. Click "Terms of Service" → should open `taxnav/terms.html`
5. All links should work

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
