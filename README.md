# Python_Django_DRF_Vue.js_MariaDB

```
docker exec -it python_django_drf_vuejs_mariadb-server-1 bash
```

```
python manage.py shell
```

```
from django.core.management.utils import get_random_secret_key
```

```
get_random_secret_key()
```

上記4コマンドで、コンテナに入り、shellの対話モードに入る。
その後、SECRET_KEYを再生成して、hogehogeから出力された任意のSECRET_KEYに
再設定してください。

settings_local.py

```
SECRET_KEY = 'hogehoge'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_sample',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'db',
        'PORT': '3306',
    }
}
```

その後、frontendディレクトリまで潜り、node_modulesを作成
```
npm i
```

アプリケーション起動
```
npm start
```
