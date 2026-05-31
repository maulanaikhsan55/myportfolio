@echo off
echo ========================================
echo Portfolio Website - Git Initialization
echo ========================================
echo.

REM Check if Git is installed
git --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Git is not installed!
    echo Please download and install Git from: https://git-scm.com/downloads
    echo.
    pause
    exit /b 1
)

echo Git is installed. Proceeding with initialization...
echo.

REM Initialize Git repository
echo [1/4] Initializing Git repository...
git init
if errorlevel 1 (
    echo ERROR: Failed to initialize Git repository
    pause
    exit /b 1
)
echo ✓ Git repository initialized
echo.

REM Add all files
echo [2/4] Adding all files to Git...
git add .
if errorlevel 1 (
    echo ERROR: Failed to add files
    pause
    exit /b 1
)
echo ✓ Files added to staging
echo.

REM Create initial commit
echo [3/4] Creating initial commit...
git commit -m "Initial commit: Portfolio website setup"
if errorlevel 1 (
    echo ERROR: Failed to create commit
    pause
    exit /b 1
)
echo ✓ Initial commit created
echo.

REM Set default branch to main
echo [4/4] Setting default branch to 'main'...
git branch -M main
if errorlevel 1 (
    echo WARNING: Failed to rename branch (this is okay if already named 'main')
)
echo ✓ Branch set to 'main'
echo.

echo ========================================
echo SUCCESS! Git repository is ready!
echo ========================================
echo.
echo Next steps:
echo 1. Create a new repository on GitHub: https://github.com/new
echo 2. Run these commands (replace YOUR_USERNAME):
echo.
echo    git remote add origin https://github.com/YOUR_USERNAME/portfolio-website.git
echo    git push -u origin main
echo.
echo 3. Then deploy to Vercel: https://vercel.com
echo.
echo For detailed instructions, see: DEPLOYMENT_GUIDE.md
echo.
pause
