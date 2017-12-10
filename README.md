# ���������� ���� ���� � ������

��������� ��� ����������� � �������� �����, ��� ���� ���� ������������ � ������

## ���������

��������� ������������ ������� Mac OS, Linux

### ���������

��������� ��������� �������

```
git clone https://github.com/ivan-uskov/faces
cd faces
apt-get install python2.7
apt-get install python-opencv
apt-get install python-tk
pip install -r requirements.txt
```

### ��������� ����

* ��������� ������ django, ������������ ����� � ������� �� �������������� ������
* ��������� ������ nginx, ���� �������� ��������� root � ��������� server_name � ����� nginx.conf � �������� ��� � /etc/nginx/conf.d
* �������� ������ � ����� static ������������ www-data
* ���� �� ������� ������� ���� �����, ����� ���������� ������ � ����� /app

## ������

* ������������� nginx
* ��������� ./run_server.sh

## ������ ��� ������� �����������

���� ���������� ��������� ��� windows ��� ��� linux c 3 ������� opencv 
���������� ������� stasm_util �� ����������
https://github.com/alyssaq/stasm_build

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## FAQ

* ������ ������ � 404, ������ ����������� �� timout ��������� ������� ������� ����������, ����� ������� ����������� ��������� ��� ��������� timeout
* ����� �� ��������������� python-tk, ������ ����� ��-�� ������ ������ ���� linux

## �����������

* alyssaq/face_morpher