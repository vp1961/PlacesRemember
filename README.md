[![Build Status](https://travis-ci.org/vp1961/PlacesRemember.svg?branch=master)](https://travis-ci.org/vp1961/PlacesRemember)
[![Coverage Status](https://coveralls.io/repos/github/vp1961/PlacesRemember/badge.svg?branch=master)](https://coveralls.io/github/vp1961/PlacesRemember?branch=master)

Веб-приложение, с помощью которого люди смогут хранить свои впечатления о посещённых местах.
## Запуск
- Git clone or download
- Установите зависимости командой `pip install -r requirements.txt`
- В приложении используется SpatiaLite — расширение SQLite для пространственных данных. Необходимо установить spatialite выполнив `sudo apt install libsqlite3-mod-spatialite` или установить из исходников https://www.gaia-gis.it/fossil/libspatialite/index 
- Перенесите миграции в БД командой `python3 manage.py migrate`
- Запустите сервер командой `python3 manage.py runserver` и перейдите по ссылке `http://127.0.0.1:8000/admin/`
- Необходимо создать приложение на сайте "Facebook для разработчиков", по ссылке: https://developers.facebook.com/. После создания приложения, нужно его добавить в интерфейс "Django admin", по вкладке "Social applications".
