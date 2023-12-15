from django.db.models.signals import post_migrate

from mysite.asset.models import AssetClass


# django 信号
# post_migrate    # 执行migrate命令后，自动触发
# 定义receiver函数
def init_db(sender, **kwargs):
    if sender.name == 'mysite.asset':
        if AssetClass.objects.all().count() == 0:
            AssetClass(code="1", name='资产类别', pidparent=0).save()


post_migrate.connect(init_db)