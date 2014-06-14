# dropbox-backup

use dropbox to backup database

## supported database

* postgresql (requirements: postgresql-clients)
* mongodb (requirements: mongodb-clients)
* ...

## usage

```bash
pip install -r requirements.txt
cp config.sample.py config.py
vi config.py
python dbacker.py
```

## cron

```
0 * * * * python :path/dbacker.py # every hour
```

## todo

* add more database support
* add more cloud storage support
* restore cli
