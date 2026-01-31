$BackupLog = "C:\Backup\last_backup.txt"

if (Test-Path $BackupLog) {
    $LastBackup = Get-Content $BackupLog | Get-Date
    if ($LastBackup -lt (Get-Date).AddDays(-1)) {
        $Message = "🚨 Backup Failure: No successful backup in last 24 hours"
    }
} else {
    $Message = "🚨 Backup Log Missing: Backup may not be running"
}

if ($Message) {
    Write-Output $Message

    Send-MailMessage `
        -To "admin@company.com" `
        -From "monitor@cloud.com" `
        -Subject "Backup Status Alert" `
        -Body $Message `
        -SmtpServer "smtp.office365.com" `
        -UseSsl
}
$TimeWindow = (Get-Date).AddMinutes(-10)
$Failures = Get-WinEvent -FilterHashtable @{
    LogName='Security'
    ID=4625
    StartTime=$TimeWindow
}