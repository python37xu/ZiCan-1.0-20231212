from django.db import models

# Create your models here.
ASCRIPTION_CHOICES = (
    ('0', '固定资产'),
    ('1', '低值易耗品'),
)

# 资产类别
class AssetClass(models.Model):
    code = models.CharField(max_length=20, null=False, blank=False, editable=True, verbose_name='类别编码')
    name = models.CharField(max_length=50, null=True, blank=True, editable=True, verbose_name='类别名称')
    symbol = models.CharField(max_length=30, null=True, blank=True, editable=True, verbose_name='类别符号')
    ascription = models.CharField(max_length=2, choices=ASCRIPTION_CHOICES, null=True, blank=False,verbose_name='类别归属')
    pidparent = models.IntegerField(db_column='pidparent', null=True, blank=True, editable=True,verbose_name= '上级类别')
    attach_code = models.IntegerField(null=True, blank=True, default=0, editable=False)  # 资产编号自增时参考使用（临时 使用）
    deltag = models.IntegerField(null=False, blank=False, default=0, editable=False, verbose_name='删除')

    class Admin:
        search_fields = ['code', 'name']

    @staticmethod
    def initial_data():
        if AssetClass.objects.all().count() == 0:
            AssetClass(code="1", name='资产类别', pidparent=0).save()

    class Meta:
        db_table = 'assetclass'
        verbose_name = "资产类别"
        verbose_name_plural = verbose_name
        unique_together = (("code",),)
        default_permissions = ('add', 'change', 'delete', 'export')