### 1、添加了环境变量

PROFILE_TYPE = production 或者 PROFILE_TYPE = develop

### 2、来自site-packages的migrations

建议每次都drop原有的表，再migrate

## 6、2022-04-13 备注

- [Serving static files during development](https://docs.djangoproject.com/en/3.2/howto/static-files/#serving-static-files-during-development)
    - static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        - 处于DEBUG = True
        - 执行collectstatic发现并收集静态文件至STATIC_ROOT
        - 提供对访问STATIC_ROOT目录下的静态文件的访问
- [Static file development view](https://docs.djangoproject.com/en/3.2/ref/contrib/staticfiles/#static-file-development-view)
    - urls.staticfiles_urlpatterns()
        - This will return the proper URL pattern for serving static files to your already defined pattern list
- [How to make Django serve static files with Gunicorn?](https://stackoverflow.com/questions/12800862/how-to-make-django-serve-static-files-with-gunicorn)
    - 分析static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)和staticfiles_urlpatterns()的不同作用

## [dj-rest-auth](https://dj-rest-auth.readthedocs.io/en/latest/)

- dj-rest-auth接口
    - logout接口需要打开blacklist或者cookie
    - password的reset和reset confirm接口需要发送邮件
    - user put/patch接口支持的字段有问题
- dj-rest-auth增强
    - user profile接口的增强
    - 如何支持除账号密码之外的登陆方式
- simplejwt开启了blacklist app

## [cp_ws_project](https://github.com/echo1937/cp_ws_project)

- An example project demonstrating the capabilities of celery-progress

## [django-channels-tutorials](https://github.com/echo1937/django-channels-tutorials)

- An example project of YouTube
  playlist: [Django Channels tutorials, Django Real-time apps with WebSockets](https://www.youtube.com/playlist?list=PLe4mIUXfbIqYEOgfh4X_Yz767IntYUSvg)

##         

### Extensions

- [django-celery-results](https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html?highlight=django-db#extensions)
- [How to Create a Celery Task Progress Bar in Django](https://www.youtube.com/watch?v=BbPswIqn2VI)