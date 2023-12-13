from django.conf.urls import re_path
from mysite.employee.views import *

urlpatterns =[
    re_path(r'department/$',DepartmentList.as_view()),
    re_path(r'department/(?P<id>\d+)/$',DepartmentListDlite.as_view()),
    re_path(r'useremp/$',UsermepList.as_view()),
    re_path(r'useremp/(?P<id>\d+)/$',UsermepListDilte.as_view())
]

