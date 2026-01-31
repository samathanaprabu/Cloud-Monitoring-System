$Threshold = 80
$CpuUsage = (Get-Counter '\Processor(_Total)\% Processor Time').CounterSamples.CookedValue

if ($CpuUsage -gt $Threshold) {
    $Message = "🚨 High CPU Usage Alert: $([math]::Round($CpuUsage,2))%"
    Write-Output $Message

    Send-MailMessage `
        -To "admin@company.com" `
        -From "monitor@cloud.com" `
        -Subject "High CPU Usage Alert" `
        -Body $Message `
        -SmtpServer "smtp.office365.com" `
        -UseSsl
}   
