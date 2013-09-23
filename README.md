# dropbox-backup

use dropbox to backup database

## supported database

* postgresql
* mongodb (requirements: mongodb-clients)
* ...

## usage (first time)

```bash
pip install dropbox
cp config.sample.py
vi config.py
python dbacker.py
```

## cron

```
0 * * * * "python :path/dbacker.py" # every hour
```

## todo

* add more database support
* add more cloud storage support
* restore cli
