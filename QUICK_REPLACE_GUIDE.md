# ⚡ Quick Replace Guide

Gunakan Find & Replace (Ctrl+H) di VS Code untuk mengganti konten dengan cepat.

## 🔄 Global Replacements (All Files)

### 1. Email Address
**Find:** `uxmushfq@gmail.com`  
**Replace:** `maulanamuhammadikhsanxap2@gmail.com`  
**Files:** All HTML files

### 2. Website Title
**Find:** `Portfolica - Personal Portfolio Website Template`  
**Replace:** `Maulana Muhammad Ikhsan - Finance Automation & Full-Stack Developer`  
**Files:** All HTML files

### 3. Meta Description
**Find:** `Personal portfolio website, showcasing selected projects, case studies, and professional experience in design and development.`  
**Replace:** `Finance automation specialist and full-stack developer. Building production-grade ERP integrations, reconciliation systems, and SaaS platforms. Laravel, React, TypeScript, Python.`  
**Files:** All HTML files

### 4. Calendar Link (Book a Call)
**Find:** `https://cal.com`  
**Replace:** `mailto:maulanamuhammadikhsanxap2@gmail.com`  
**Files:** All HTML files

### 5. Profile Image URL
**Find:** `https://framerusercontent.com/images/GLrXdyCPhNqdGXFCIVsn5gnaXvE.png`  
**Replace:** `[YOUR_PROFILE_IMAGE_URL]` (upload your photo to Imgur/Cloudinary first)  
**Files:** All HTML files

---

## 📄 Page-Specific Replacements

### index.html (Homepage)

#### Hero Section Name
**Find:** Look for text near hero section (you'll need to search manually)  
**Replace:** `Maulana Muhammad Ikhsan`

#### Tagline/Title
**Find:** Designer/Developer title text  
**Replace:** `Finance Automation & Full-Stack Developer`

#### Bio/Summary
**Find:** Existing bio paragraph  
**Replace:** 
```
Accounting Information Systems student specializing in finance automation, 
ERP integration, and full-stack development. Building production-grade systems 
that bridge accounting domain knowledge with modern software engineering.
```

---

### about (About Page)

#### Full Bio
**Replace with:**
```
I'm an Accounting Information Systems student at Telkom University (GPA 3.81/4.00) 
with hands-on experience delivering production-grade finance automation systems, 
ERP integrations, and reconciliation workflows.

I specialize in building systems that bridge accounting domain knowledge with 
modern software engineering—from multi-tenant SaaS platforms to bank reconciliation 
APIs and ERP integrations with Accurate Online and SAP.

My work spans Laravel, React, TypeScript, Python FastAPI, and PostgreSQL, with 
applied knowledge of financial systems, cost accounting, and process automation.
```

#### Skills Section
**Add these skill categories:**
- ERP & Accounting: Accurate Online, SAP FI/CO, Zahir Accounting
- Finance Automation: n8n, Webhook Integration, Bank Statement Parsing
- Web Development: Laravel, React, TypeScript, Next.js, Python FastAPI
- Tools: Git, Postman, Railway, Figma, Google APIs

---

### contact (Contact Page)

#### Contact Information
**Replace:**
- Email: `maulanamuhammadikhsanxap2@gmail.com`
- Phone: `+62 857-0117-4347`
- Location: `Bandung, Indonesia`
- LinkedIn: `linkedin.com/in/maulanamuhammadikhsan`
- GitHub: `github.com/maulanaikhsan55`

---

## 🎨 Project Pages Mapping

### Project 1: tomoro-bridging
**Title:** Tomoro Bridging Internal  
**Subtitle:** Finance Operations System  
**Tech:** Laravel, FastAPI, PostgreSQL, Accurate Online  
**Description:** Production finance operations web app integrated with Accurate Online ERP, automating sales invoicing and purchase order processing across 2 stores and 5 transaction channels.

### Project 2: zeirec
**Title:** Zeirec  
**Subtitle:** Multi-Tenant Finance Automation SaaS  
**Tech:** Laravel, React, TypeScript, PostgreSQL  
**Description:** Multi-tenant finance automation platform supporting 3+ client workspaces with reimbursement approval flows and reconciliation modules used by finance teams.

### Project 3: api-bank-reconcile
**Title:** API Bank Reconcile  
**Subtitle:** Bank Statement Parser & Reconciliation API  
**Tech:** Next.js, React, TypeScript, PostgreSQL, Railway  
**Description:** REST API service that parses bank statements (PDF, HTML, CSV) and returns normalized JSON for reconciliation systems, supporting BCA, BRI, and Mandiri.

### Project 4: duckcost
**Title:** DuckCost  
**Subtitle:** COGS & Production Cost Calculator  
**Tech:** Flutter, Cost Accounting  
**Description:** Mobile app enabling SMEs to calculate COGS and manage production cost records. Top 165/750+ entries, Rp14,000,000 funding (Innovillage 2024).

### Project 5: agriduck
**Title:** AgriDuck  
**Subtitle:** Financial Recording Platform for Farmers  
**Tech:** Laravel, SQL  
**Description:** Cash recording platform with automated cash flow reports, date-range filters, and PDF export. National finalist from 30+ universities.

### Project 6: cellupay
**Title:** CelluPay  
**Subtitle:** Digital Financial Application (UX Design)  
**Tech:** Figma, UX Research  
**Description:** End-to-end UX design for digital transaction app. Copyright Certificate from DJKI (Ministry of Law and Human Rights).

---

## 🖼️ Image Placeholders

You'll need to upload these images and replace URLs:

1. **Profile Photo** - Professional headshot
2. **Project Screenshots:**
   - Tomoro Bridging dashboard
   - Zeirec interface
   - API Bank Reconcile demo
   - DuckCost app screens
   - AgriDuck platform
   - CelluPay Figma designs

**Recommended Image Hosts:**
- [Imgur](https://imgur.com) - Free, easy
- [Cloudinary](https://cloudinary.com) - Free tier, CDN
- [GitHub](https://github.com) - Use your repo's assets folder

---

## 🔍 How to Use This Guide

### In VS Code:

1. Open the entire folder: `File > Open Folder` → select `portfolica.framer.website`
2. Press `Ctrl + Shift + H` (Find and Replace in Files)
3. Enter **Find** text
4. Enter **Replace** text
5. Click "Replace All" or review each match
6. Save all files: `Ctrl + K, S`

### Tips:
- ✅ Do global replacements first (email, title, etc.)
- ✅ Test in browser after each major change
- ✅ Commit to git after each successful update
- ✅ Keep backup of original files (already in git history)

---

## ⚠️ Important Notes

1. **Don't break HTML structure** - Only replace text content, not HTML tags
2. **Test after changes** - Open in browser to verify
3. **Backup first** - Git commit before major changes
4. **Case sensitive** - Some replacements are case-sensitive
5. **URLs** - Make sure all URLs are valid and working

---

## 🎯 Recommended Order

1. ✅ Global replacements (email, title, meta tags)
2. ✅ Homepage (index.html)
3. ✅ About page
4. ✅ Contact page
5. ✅ Projects listing (all-projects)
6. ✅ Individual project pages (6 pages)
7. ✅ Upload and replace images
8. ✅ Final testing
9. ✅ Deploy to Vercel

---

**Ready to start? Begin with the global replacements!** 🚀
