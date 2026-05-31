# 🚀 Deployment Guide - Vercel

## Quick Start (5 Minutes)

### Step 1: Initialize Git Repository

```bash
cd d:\xampp_new\htdocs\portfolica.framer.website
git init
git add .
git commit -m "Initial commit: Portfolio website setup"
```

### Step 2: Create GitHub Repository

1. Go to [github.com/new](https://github.com/new)
2. Repository name: `portfolio-website` (or any name you prefer)
3. Keep it **Public** or **Private** (your choice)
4. **DO NOT** initialize with README (we already have files)
5. Click "Create repository"

### Step 3: Push to GitHub

```bash
git remote add origin https://github.com/maulanaikhsan55/portfolio-website.git
git branch -M main
git push -u origin main
```

### Step 4: Deploy to Vercel

#### Option A: Via Vercel Dashboard (Recommended)

1. Go to [vercel.com](https://vercel.com)
2. Sign in with GitHub
3. Click "Add New Project"
4. Import your `portfolio-website` repository
5. **Project Settings:**
   - Framework Preset: **Other**
   - Root Directory: `./`
   - Build Command: (leave empty)
   - Output Directory: (leave empty)
6. Click "Deploy"
7. Wait 1-2 minutes ✨
8. Your site is live!

#### Option B: Via Vercel CLI

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
cd d:\xampp_new\htdocs\portfolica.framer.website
vercel

# Follow prompts:
# - Set up and deploy? Y
# - Which scope? (your account)
# - Link to existing project? N
# - Project name? portfolio-website
# - Directory? ./
# - Override settings? N

# Deploy to production
vercel --prod
```

---

## 🔧 Post-Deployment Configuration

### Custom Domain (Optional)

1. Go to Vercel Dashboard → Your Project → Settings → Domains
2. Add your custom domain (e.g., `maulanaikhsan.com`)
3. Follow DNS configuration instructions
4. Wait for DNS propagation (5-30 minutes)

### Environment Variables (If Needed Later)

1. Vercel Dashboard → Your Project → Settings → Environment Variables
2. Add any API keys or secrets here
3. Redeploy to apply changes

---

## 📝 Content Update Workflow

### After Deployment, Update Content:

1. **Edit files locally** (in VS Code or any editor)
2. **Test locally** via XAMPP: `http://localhost/portfolica.framer.website`
3. **Commit changes:**
   ```bash
   git add .
   git commit -m "Update: [describe what you changed]"
   git push
   ```
4. **Vercel auto-deploys** (30-60 seconds)
5. **Check live site** at your Vercel URL

---

## 🎯 Priority Content Updates

### Phase 1: Critical (Do First)
- [ ] Replace email: `uxmushfq@gmail.com` → `maulanamuhammadikhsanxap2@gmail.com`
- [ ] Update meta titles and descriptions
- [ ] Change profile image URL
- [ ] Update social links (LinkedIn, GitHub)

### Phase 2: Important (Do Next)
- [ ] Homepage hero section (name, title, tagline)
- [ ] About page content
- [ ] Project titles and descriptions
- [ ] Contact page information

### Phase 3: Polish (Do Later)
- [ ] Project detail pages (all 6 projects)
- [ ] Add project screenshots/images
- [ ] Update footer links
- [ ] SEO optimization (robots.txt, sitemap)

---

## 🔍 Testing Checklist

Before going live, test:

- [ ] All navigation links work
- [ ] Contact form/email links work
- [ ] Social media links are correct
- [ ] Mobile responsive (test on phone)
- [ ] All images load properly
- [ ] No broken links (404 errors)
- [ ] Page load speed is good

---

## 🐛 Troubleshooting

### Issue: Vercel build fails
**Solution**: Check `vercel.json` configuration, ensure no syntax errors

### Issue: Links don't work after deployment
**Solution**: Vercel's `cleanUrls: true` handles extensionless URLs automatically

### Issue: Images not loading
**Solution**: Check image URLs, ensure they're absolute paths or hosted externally

### Issue: Changes not showing on live site
**Solution**: 
1. Hard refresh browser (Ctrl + Shift + R)
2. Check Vercel deployment logs
3. Verify git push was successful

---

## 📊 Analytics (Optional)

### Add Vercel Analytics

1. Vercel Dashboard → Your Project → Analytics
2. Enable Vercel Analytics (free tier available)
3. View traffic, performance, and user data

### Add Google Analytics

1. Get GA4 tracking ID from [analytics.google.com](https://analytics.google.com)
2. Add tracking code to `<head>` section of all HTML files
3. Commit and push changes

---

## 🎉 You're Done!

Your portfolio is now:
- ✅ Live on the internet
- ✅ Auto-deployed on every git push
- ✅ Fast and globally distributed (Vercel CDN)
- ✅ HTTPS enabled by default
- ✅ Ready to share with recruiters!

**Next Steps:**
1. Share your Vercel URL on LinkedIn
2. Add to your CV/resume
3. Keep updating with new projects
4. Monitor analytics to see visitors

---

**Need Help?**
- Vercel Docs: [vercel.com/docs](https://vercel.com/docs)
- Vercel Support: [vercel.com/support](https://vercel.com/support)
- GitHub Issues: Create issue in your repo

**Good luck! 🚀**
