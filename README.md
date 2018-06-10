# django个人博客

使用django1.11.9  + python3.6.5制作的一个个人简易博客

确保自己电脑上已经安装python3.6.5及以上版本和mysql数据库

将项目拉到本地后，通过cmd命令行进入项目根目录

输入 pip install -r requirement.txt 将项目所需第三方库全部安装好

打开myblog/settings.py文件，在85行开始找到以下代码：
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myblog',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'CHARSET': 'utf8'
    }
}

上述代码配置的数据库用户USER和密码PASSWORD请根据自己电脑mysql数据库的配置信息修改

使用数据库创建一个utf8字符集数据库名为‘myblog’

在cmd命令行输入python manage.py createsuperuser创建超级管理员账号，邮箱可以随意填写，输入密码时是不会显示的

创建完超级管理员账号后输入 python manage.py runserver 启动项目

打开浏览器，输入localhost:8000即可在本地访问博客

访问localhost:8000/admin使用刚刚创建的超级管理员账号登入后台，即可添加文章
