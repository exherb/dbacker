# dropbox-backup

use dropbox to backup database

## supported database

* postgresql
* mongodb (requirements: mongodb-clients)
* ...

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
