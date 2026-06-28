# Git auto sync script
# Usage: powershell -File git_sync.ps1

$vault = "H:\转录"
$msg = "chore(kb): auto sync - $(Get-Date -Format 'yyyy-MM-dd HH:mm')"

Write-Host "=== GitHub Sync ===" -ForegroundColor Green
Set-Location $vault

$status = git status --porcelain
if (-not $status) {
    Write-Host "No changes. Pulling..." -ForegroundColor Green
    git pull origin main --ff-only 2>&1
    return
}

git add -A
git commit -m $msg
git pull origin main --ff-only 2>&1
git push origin main 2>&1
Write-Host "== Sync Complete ==" -ForegroundColor Green
