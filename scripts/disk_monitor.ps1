$Threshold = 15  # Free space percentage

Get-PSDrive -PSProvider FileSystem | ForEach-Object {
    $FreePercent = ($_.Free / $_.Used + $_.Free) * 100

    if ($FreePercent -lt $Threshold) {
        $Message = "🚨 Low Disk Space on drive $($_.Name): $([math]::Round($FreePercent,2))% free"
        Write-Output $Message

        Send-MailMessage `
            -To "admin@company.com" `
            -From "monitor@cloud.com" `
            -Subject "Low Disk Space Alert" `
            -Body $Message `
            -SmtpServer "smtp.office365.com" `
            -UseSsl
    }
}
$TimeWindow = (Get-Date).AddMinutes(-10)
$Failures = Get-WinEvent -FilterHashtable @{
    LogName='Security'
    ID=4625
    StartTime=$TimeWindow
}