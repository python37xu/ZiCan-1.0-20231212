from django.db.models.signals import post_migrate

from mysite.myuserapp.models import MyUser,MyUserManager
from django.utils import timezone

# django 信号
# post_migrate    # 执行migrate命令后，自动触发
# 定义receiver函数
def init_db(sender, **kwargs):
    if sender.name == 'myuserapp':
        if MyUser.objects.all().count() == 0:
            MyUserManager.create_user(email="admin@admin.com",date_of_birth=timezone.now,password="admin")

post_migrate.connect(init_db)