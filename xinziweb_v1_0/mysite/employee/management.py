from django.db.models.signals import post_migrate

from mysite.employee.models import department


# django 信号
# post_migrate    # 执行migrate命令后，自动触发
# 定义receiver函数
def init_db(sender, **kwargs):
    if sender.name == 'employee':
        if department.objects.all().count() == 0:
            department(DeptName="总部门", DeptNumber='1', parent=0).save()


post_migrate.connect(init_db)