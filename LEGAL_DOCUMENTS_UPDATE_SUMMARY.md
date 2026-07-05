# Legal Documents Update Summary
## Privacy Policy & Terms of Service - March 22, 2026

**Updated:** Privacy Policy & Terms of Service
**Reason:** Remove TrueLayer references, update to reflect current implementation
**Status:** ✅ Complete and Ready for Publication

---

## Changes Made

### 1. Privacy Policy (`landing-page/taxswipe/privacy.html`)

#### ✅ Last Updated Date
- **Changed:** "Last updated: March 22, 2026" (already correct)
- **Status:** No change needed

#### ✅ AI Provider Correction
- **OLD:** "OpenAI GPT-4"
- **NEW:** "Anthropic Claude"
- **Reason:** Actual implementation uses Anthropic Claude API
- **Locations Updated:**
  - Section 3: How We Use Your Data (line 131)
  - Section 4.3: Third-Party Services (lines 156-161)

#### ✅ No TrueLayer References Found
- **Status:** Privacy Policy was already correct - no bank connection/TrueLayer references

---

### 2. Terms of Service (`landing-page/taxswipe/terms.html`)

#### ✅ Last Updated Date
- **OLD:** "Last updated: March 2026"
- **NEW:** "Last updated: March 22, 2026"
- **Location:** Line 69

#### ✅ Description of Service (Section 2)
- **OLD:** "Connect their UK bank accounts to sync transactions"
- **NEW:** "Import transactions via PDF bank statements, CSV files, or manual entry"
- **ADDED:** "Submit End of Period Statement (EOPS) and Final Declaration to complete tax year"
- **Reason:** Reflects actual implementation (PDF upload, not bank connections)
- **Location:** Lines 84-91

#### ✅ AI Provider Correction (Section 3)
- **OLD:** "Claude by Anthropic" and "OpenAI GPT-4" (inconsistent)
- **NEW:** "Anthropic Claude" (consistent throughout)
- **Locations Updated:**
  - AI Disclaimer (line 114)
  - Section 6.2: Third-Party Services (line 167)

#### ✅ Third-Party Services (Section 6)
**REMOVED Section 6.1: TrueLayer (Bank Connection)**
- Deleted entire subsection about TrueLayer/Open Banking
- **Reason:** TrueLayer is not used - app uses PDF upload instead

**RENUMBERED Sections:**
- 6.2 HMRC Integration → 6.1 HMRC Integration
- 6.3 Anthropic Claude → 6.2 Anthropic (AI Categorisation)

#### ✅ Limitation of Liability (Section 10)
- **OLD:** "third-party service failures (TrueLayer, HMRC API downtime)"
- **NEW:** "third-party service failures (HMRC API downtime, AWS service interruptions)"
- **ADDED:** "We are NOT liable for incorrect AI categorisation suggestions"
- **Reason:** Reflects actual third-party dependencies
- **Location:** Lines 197-201

#### ✅ Data Retention and Deletion (Section 11)
- **OLD:** "Bank connections will be immediately disconnected"
- **NEW:** "HMRC connection will be immediately disconnected"
- **ADDED:** "All transaction data will be permanently deleted"
- **Reason:** No bank connections to disconnect
- **Location:** Lines 215-219

---

## Third-Party Services Verification

### ✅ Confirmed Active Services:

1. **AWS Lambda (pdfplumber)**
   - Purpose: PDF bank statement parsing
   - Verified in: `lambda/handler.py` (invoked by `supabase/functions/parse-statement`)
   - Status: ✅ Active — replaced the former AWS Textract path (removed in TSW-310)

2. **HMRC API**
   - Purpose: MTD quarterly submissions, EOPS, Final Declaration
   - Verified in: `supabase/functions/hmrc-*` Edge Functions
   - Status: ✅ Active

3. **Anthropic Claude**
   - Purpose: AI expense categorisation
   - Verified in: `supabase/functions/ai-categorise/index.ts`
   - Status: ✅ Active

4. **Supabase**
   - Purpose: Database, authentication, Edge Functions
   - Status: ✅ Active

5. **Apple/Google**
   - Purpose: In-app purchases/subscriptions
   - Status: ✅ Active (when subscriptions implemented)

### ❌ Removed Services:

1. **TrueLayer**
   - Status: ❌ Not used
   - Removed from: Terms of Service (Sections 6.1, 10, 11)

2. **OpenAI**
   - Status: ❌ Not used (was incorrectly documented)
   - Corrected to: Anthropic Claude

---

## File Locations

### Updated Files:

1. `/Users/ajaychatrath/Desktop/Financial/TaxSwipe/landing-page/taxswipe/privacy.html`
   - 2 changes (AI provider corrections)

2. `/Users/ajaychatrath/Desktop/Financial/TaxSwipe/landing-page/taxswipe/terms.html`
   - 8 changes (date, description, AI provider, TrueLayer removal, liability, deletion)

### Related Files (Not Updated):

1. `/Users/ajaychatrath/Desktop/Financial/TaxSwipe/landing-page/privacy-policy.html`
   - Parent page linking to app-specific policies
   - No changes needed

2. `/Users/ajaychatrath/Desktop/Financial/TaxSwipe/landing-page/terms-of-use.html`
   - General FinMedTech terms
   - No changes needed

---

## Publishing Checklist

### ✅ Pre-Publication Verification:

- [x] All TrueLayer references removed from Terms of Service
- [x] Bank connection references updated to PDF upload
- [x] AI provider corrected from OpenAI to Anthropic Claude
- [x] Third-party services list verified against actual codebase
- [x] Last updated dates set to March 22, 2026
- [x] All section numbers renumbered correctly after deletions
- [x] EOPS and Final Declaration mentioned in service description
- [x] Liability section updated for current services

### 📋 Deployment Steps:

**If hosting on Vercel (as indicated by vercel.json):**

```bash
cd /Users/ajaychatrath/Desktop/Financial/TaxSwipe/landing-page

# Deploy to production
vercel --prod

# Or if using Git deployment:
git add taxswipe/privacy.html taxswipe/terms.html
git commit -m "Update legal docs: Remove TrueLayer, correct AI provider to Anthropic Claude"
git push origin main
```

**URLs After Deployment:**
- Privacy Policy: `https://yourdomain.com/taxswipe/privacy`
- Terms of Service: `https://yourdomain.com/taxswipe/terms`

### 📱 Mobile App Update:

**File:** `mobile/app/(tabs)/settings.tsx`

Ensure legal document links point to the correct URLs:

```typescript
// Settings screen should have links like:
<List.Item
  title="Privacy Policy"
  onPress={() => Linking.openURL('https://yourdomain.com/taxswipe/privacy')}
/>
<List.Item
  title="Terms of Service"
  onPress={() => Linking.openURL('https://yourdomain.com/taxswipe/terms')}
/>
```

---

## Summary of Changes

### Privacy Policy:
- ✅ 2 minor corrections (AI provider: OpenAI → Anthropic)
- ✅ No TrueLayer references (was already clean)

### Terms of Service:
- ✅ 1 date update
- ✅ 1 service description update (bank connection → PDF upload)
- ✅ 1 feature addition (EOPS and Final Declaration)
- ✅ 2 AI provider corrections (OpenAI → Anthropic)
- ✅ 1 section removal (TrueLayer)
- ✅ 2 section renumberings
- ✅ 3 liability/deletion updates (remove TrueLayer, add AWS)

**Total Changes:** 13 updates across 2 documents

---

## Compliance Status

### ✅ UK GDPR Compliance:
- [x] Data controller identified (FinMedTech/Ajay Chatrath)
- [x] All data collection purposes explained
- [x] Third-party data processors listed (AWS, HMRC, Anthropic, Supabase)
- [x] Data retention periods specified
- [x] User rights explained (access, rectification, erasure, portability)
- [x] Contact information provided
- [x] ICO complaint process mentioned

### ✅ App Store Requirements:
- [x] Privacy Policy publicly accessible
- [x] Terms of Service publicly accessible
- [x] Last updated dates present
- [x] Contact information included
- [x] In-app purchase terms mentioned
- [x] Children's privacy addressed (under 18 not permitted)

### ✅ MTD Compliance:
- [x] HMRC integration explained
- [x] Data retention for tax records (6 years) specified
- [x] Quarterly submission process described
- [x] EOPS and Final Declaration mentioned
- [x] User responsibilities clearly stated

---

## Recommendations

### 1. Deploy Immediately ✅
Legal documents are now accurate and ready for production. Deploy to make them publicly accessible at:
- `https://yourdomain.com/taxswipe/privacy`
- `https://yourdomain.com/taxswipe/terms`

### 2. Update Mobile App Links
Ensure Settings screen links point to the deployed URLs.

### 3. App Store Submission
Use these URLs in App Store Connect and Google Play Console:
- Privacy Policy URL: `https://yourdomain.com/taxswipe/privacy`
- Terms of Service URL: `https://yourdomain.com/taxswipe/terms`

### 4. User Communication
No need to notify existing users of these changes since:
- TrueLayer was never used in production
- Changes are clarifications, not material policy changes
- AI provider correction is technical detail only

### 5. Future Updates
When making changes to third-party services:
1. Update Privacy Policy (Section 4: Third-Party Services)
2. Update Terms of Service (Section 6: Third-Party Services)
3. Update last updated date
4. Deploy both documents together

---

## Next Steps

1. **Deploy legal documents to production** (Vercel or hosting platform)
2. **Verify URLs are publicly accessible**
3. **Update mobile app Settings screen** with correct links
4. **Test links open correctly** from mobile app
5. **Submit URLs to App Store Connect** and Google Play Console
6. **Consider adding in-app legal document viewer** for better UX

---

**Status:** ✅ COMPLETE - Ready for Production
**Deployment:** Pending (waiting for hosting deployment)
**Compliance:** ✅ UK GDPR, App Store, MTD Ready

**Updated By:** Claude Code
**Date:** March 22, 2026
**Review:** Ready for legal review if needed
