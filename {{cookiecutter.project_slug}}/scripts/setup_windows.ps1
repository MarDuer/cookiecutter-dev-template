# PowerShell script to install just on Windows
# Requires Git Bash to be installed

$ErrorActionPreference = "Stop"

Write-Host "Installing just command runner..." -ForegroundColor Green

# Check if just is already installed
if (Get-Command just -ErrorAction SilentlyContinue) {
    Write-Host "just is already installed!" -ForegroundColor Yellow
    just --version
    exit 0
}

# Download and install just
$justVersion = "1.25.2"
$downloadUrl = "https://github.com/casey/just/releases/download/$justVersion/just-$justVersion-x86_64-pc-windows-msvc.zip"
$tempDir = "$env:TEMP\just-install"
$installDir = "$env:LOCALAPPDATA\just"

# Create directories
New-Item -ItemType Directory -Force -Path $tempDir | Out-Null
New-Item -ItemType Directory -Force -Path $installDir | Out-Null

try {
    # Download
    Write-Host "Downloading just $justVersion..." -ForegroundColor Cyan
    $zipFile = "$tempDir\just.zip"
    Invoke-WebRequest -Uri $downloadUrl -OutFile $zipFile

    # Extract
    Write-Host "Extracting..." -ForegroundColor Cyan
    Expand-Archive -Path $zipFile -DestinationPath $tempDir -Force

    # Move to install directory
    Move-Item -Path "$tempDir\just.exe" -Destination "$installDir\just.exe" -Force

    # Add to PATH if not already there
    $userPath = [Environment]::GetEnvironmentVariable("Path", "User")
    if ($userPath -notlike "*$installDir*") {
        Write-Host "Adding to PATH..." -ForegroundColor Cyan
        [Environment]::SetEnvironmentVariable(
            "Path",
            "$userPath;$installDir",
            "User"
        )
        $env:Path = "$env:Path;$installDir"
    }

    Write-Host "`n✓ just installed successfully!" -ForegroundColor Green
    Write-Host "Version: " -NoNewline
    & "$installDir\just.exe" --version

    Write-Host "`nNote: You may need to restart your terminal for PATH changes to take effect." -ForegroundColor Yellow

} catch {
    Write-Host "Error: $_" -ForegroundColor Red
    exit 1
} finally {
    # Cleanup
    Remove-Item -Path $tempDir -Recurse -Force -ErrorAction SilentlyContinue
}
