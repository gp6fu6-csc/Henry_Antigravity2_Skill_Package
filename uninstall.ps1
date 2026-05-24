# Henry_Antigravity2_Skill_Package Uninstaller (Windows Only)

$TargetDir = "$HOME\.gemini\config\plugins\henry-skills"

if (Test-Path $TargetDir) {
    Remove-Item -Path $TargetDir -Recurse -Force
    Write-Host "Henry_Antigravity2_Skill_Package removed successfully." -ForegroundColor Green
} else {
    Write-Host "Package is not currently installed." -ForegroundColor Yellow
}
