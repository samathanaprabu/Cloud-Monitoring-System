$TimeWindow = (Get-Date).AddMinutes(-10)
$Failures = Get-WinEvent -FilterHashtable @{
    LogName='Security'
    ID=4625
    StartTime=$TimeWindow
}

if ($Failures.Count -gt 5) {
    $Message = "🚨 Security Alert: $($Failures.Count) failed login attempts detected"
    Write-Output $Message

    Send-MailMessage `
        -To "admin@company.com" `
        -From "monitor@cloud.com" `
        -Subject "Login Failure Alert" `
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