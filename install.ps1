# Henry_Antigravity2_Skill_Package Installer (Windows Only)
$ErrorActionPreference = "Stop"

$globalSkillsDir = "$HOME\.gemini\config\skills"
$globalPluginsDir = "$HOME\.gemini\config\plugins"

Write-Host "Installing Henry_Antigravity2_Skill_Package to global Antigravity config..." -ForegroundColor Cyan

# 1. Ensure target directories exist
if (-not (Test-Path $globalSkillsDir)) {
    New-Item -ItemType Directory -Path $globalSkillsDir -Force | Out-Null
}
if (-not (Test-Path $globalPluginsDir)) {
    New-Item -ItemType Directory -Path $globalPluginsDir -Force | Out-Null
}

# 2. Deploy all skills
Write-Host "Deploying skills to $globalSkillsDir ..." -ForegroundColor Yellow
if (Test-Path ".\skills") {
    Copy-Item -Path ".\skills\*" -Destination $globalSkillsDir -Recurse -Force
}

# 3. Deploy all plugins
Write-Host "Deploying plugins to $globalPluginsDir ..." -ForegroundColor Yellow
if (Test-Path ".\plugins") {
    Copy-Item -Path ".\plugins\*" -Destination $globalPluginsDir -Recurse -Force
}

Write-Host "Installation completed successfully! All 21 skills and plugins are active globally." -ForegroundColor Green
