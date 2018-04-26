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