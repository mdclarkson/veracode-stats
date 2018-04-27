# veracode-stats

## Install

`pip install veracodestats`

Create `~/.veracode/credentials` with a Veracode user account API key ID/secret:

```
[default]
veracode_api_key_id = 359edffad5......
veracode_api_key_secret = 09fafebf9e1f3490....
```

## Usage

```
usage: veracodestats [-h] [-d] report_folder

Generate interesting statistics for a Veracode account

positional arguments:
  report_folder   report save/load folder

optional arguments:
  -h, --help      show this help message and exit
  -d, --download  download all reports, may take some time for large accounts
 ```
 
 ## Example Output
 
 ```
$ veracodestats ~/reports
Loading report files: 104/104
Parsing reports: 101/101
Processing reports 101/101

Compliance Rate By Year
-----------------------
Year      %         Compliant/Scanned
2017      0         0/4
2018      43        3/7

Apps Scanned By Year By Policy
------------------------------
2017
Policy                                  Count     
No High/Very High/XSS                   4         

2018
Policy                                  Count     
No High/Very High/XSS                   7         


Apps Scanned By Year/Month By Scan Type
---------------------------------------
2017
Month     Static    Dynamic   
Oct       1         0         
Nov       2         0         
Dec       2         1         

2018
Month     Static    Dynamic   
Jan       4         0         
Feb       2         0         
Mar       1         0         
Apr       3         0 
```
