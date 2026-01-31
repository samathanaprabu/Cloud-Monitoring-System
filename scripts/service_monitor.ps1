$Services = @("W3SVC", "MSSQLSERVER")

foreach ($ServiceName in $Services) {
    $Service = Get-Service -Name $ServiceName -ErrorAction SilentlyContinue

    if ($Service.Status -ne "Running") {
        $Message = "🚨 Service Down: $ServiceName is not running"
        Write-Output $Message

        Send-MailMessage `
            -To "admin@company.com" `
            -From "monitor@cloud.com" `
            -Subject "Service Down Alert" `
            -Body $Message `
            -SmtpServer "smtp.office365.com" `
            -UseSsl
    }
}
