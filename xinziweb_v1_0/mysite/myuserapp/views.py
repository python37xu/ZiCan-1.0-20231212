# coding=utf-8
from django.contrib.auth.backends import ModelBackend
#django的Q对象将SQL表达式封装在Python对象中，该对象可用于与数据库相关的操作。使用Q对象，我们可以使用更少和更简单的代码进行复杂查询。
from django.db.models import Q
from django.contrib.auth import get_user_model

User = get_user_model()

# 自定义登录 查询
class MyCustomBackend(ModelBackend):
    print("11111111111111111111111111111")
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            print("22222222222222222222")
            print(User)
            print(request.POST)

            user = User.objects.get(Q(email=email))
            print(user)
            if user.check_password(password):
                return user
        except Exception as e:
            return None

