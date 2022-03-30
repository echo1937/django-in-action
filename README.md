###1、添加了环境变量
PROFILE_TYPE = production 或者 PROFILE_TYPE = develop

### 2、来自site-packages的migrations
建议每次都drop原有的表，再migrate

### 3、2022-03-29 备注
- simplejwt开启了blacklist app
- dj-rest-auth接口
  - logout接口需要打开blacklist或者cookie
  - password的reset和reset confirm接口需要发送邮件
  - user put/patch接口支持的字段有问题
- dj-rest-auth增强
  - user profile接口的增强
  - 如何支持除账号密码之外的登陆方式

### 4、2022-03-30 备注
- 安装依赖: celery、redis(~=是啥意思)
- 配置文件```django_in_action/celery.py```
- 配置文件```django_in_action/__init__.py```(重要!!)
- DJANGO_SETTINGS_MODULE的配置
  - ```settings/__init__.py```
  - ```settings/celery.py```
- 在module下添加tasks.py, celeryapp添加views.py和urls.py, django_in_action添加urls.py
- 启动命令: celery -A django_in_action worker -l INFO