from django.conf.urls import re_path
from mysite.myuserapp.views import *
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns =[
    re_path(r'api/token/', obtain_jwt_token,name='token_obtain_pair'),
]

