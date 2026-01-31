# Cloud Monitoring System – Setup Guide

## Prerequisites
- Windows Server / Windows VM
- PowerShell 5.1+
- SMTP access (Office365 / Gmail)
- Azure Monitor or AWS CloudWatch (optional)

## Setup Steps
1. Clone the repository
2. Update email addresses in scripts
3. Configure SMTP permissions
4. Schedule scripts using Task Scheduler
5. Test alerts manually

## Recommended Schedule
- CPU/Disk: Every 5 minutes
- Services: Every 5 minutes
- Login failures: Every 10 minutes
- Backup status: Daily
