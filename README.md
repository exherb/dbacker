# dropbox-backup

use dropbox to backup database

## usage

```bash
cp config.sample.py
vi config.py
python dbacker.py
```

## cron

```
0 * * * * "python :path/dbacker.py" # every hour
```
