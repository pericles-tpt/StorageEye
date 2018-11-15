# DiskHistory
A tool that checks the remaining disk space every periodically (decided by the user). If the remaining disk space is reduced by more than 500MB it will look through each folder on the selected disk and compare their sizes with the folders in its data logs to find the largest change(s) (50MB or more by default but adjustable) and then gives the user a summary of the changes in disk usage of those folders in the form of their directory address so that the user can take actions on them

Features
- Intelligent folder prioritisation: Prioritises folders that  recur a lot in scans in future scans so that the program becomes less intensive as it does more scans
- See changes to drive and revert them like github???
