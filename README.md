# Превращаем одно лицо в другое

Загружаем два изображения и получаем гифку, как одно лицо превращается в другое

## Установка

Выполните следующие действия, доступные операционные системы Mac OS, Linux

### Окружение

Выполните следующие команды

```
git clone https://github.com/ivan-uskov/faces
cd faces
apt-get install python2.7
apt-get install python-opencv
apt-get install python-tk
pip install -r requirements.txt
```

### Настройка прав

* Поправьте конфиг django, относительно папки в которую вы устанавливаете проект
* Поправьте конфиг nginx, надо обновить директиву root и директиву server_name в файле nginx.conf и добавить его в /etc/nginx/conf.d
* Сделайте доступ к папке static пользователю www-data

## Запуск

* Перезапускаем nginx
* запускаем ./run_server.sh

## Запуск под другими платформами

Если необходимо запускать под windows или под linux c 3 версией opencv 
Необходимо собрать stasm_util по инструкции
https://github.com/alyssaq/stasm_build

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* alyssaq/face_morpher