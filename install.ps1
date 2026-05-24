# Henry_Antigravity2_Skill_Package Installer (Windows Only)

$TargetDir = "$HOME\.gemini\config\plugins\henry-skills"

Write-Host "Installing Henry_Antigravity2_Skill_Package to global Antigravity config..." -ForegroundColor Cyan

# 1. Create target directory
if (-not (Test-Path "$TargetDir\skills")) {
    New-Item -ItemType Directory -Path "$TargetDir\skills" -Force | Out-Null
}

# 2. Create plugin.json
$PluginJson = @"
{
  "name": "henry-skills",
  "description": "Unified skills package for Henry (Karpathy, RTK, NotebookLM, GitHub)",
  "version": "1.0.0"
}
"@
Set-Content -Path "$TargetDir\plugin.json" -Value $PluginJson -Force

# 3. Copy skills
Copy-Item -Path ".\skills\*" -Destination "$TargetDir\skills" -Recurse -Force

Write-Host "Installation completed successfully! The skills are now active globally." -ForegroundColor Green
