from django.db import models

# Create your models here.

# 部门数据表
class department(models.Model):
    DeptID = models.AutoField(db_column="deptid", primary_key=True, null=False, editable=False)
    DeptNumber = models.CharField(verbose_name='部门编号', blank=False, db_column='deptnumber', null=False,
                                  max_length=40, help_text="最大长度不超过40个字符,修改部门编号后不会改变人员所在的部门。")  # 用于显示的编号
    DeptName = models.CharField(verbose_name='部门名称', max_length=40, db_column='deptname')
    parent = models.IntegerField(db_column="supdeptid", verbose_name="父部门编号", null=False, blank=True, default=0)
    DeptAddr = models.CharField(verbose_name="部门地址", max_length=50, blank=True, null=True, db_column='deptaddr')
    DeptPerson = models.CharField(verbose_name="联系人", max_length=20, blank=True, null=True, db_column='deptperson')
    DeptPhone = models.CharField(verbose_name="电话", max_length=20, blank=True, null=True, db_column='deptphone')
    email = models.EmailField(verbose_name="邮箱", blank=True, null=True)
    DelTag = models.IntegerField(verbose_name="删除标记", default=0, editable=False, null=True, blank=True, db_column='deltag')

    class Admin:
        search_fields = ['DeptNumber', 'DeptName']
        
    @staticmethod
    def initial_data():
        if department.objects.all().count() == 0:
            department(DeptName="总部门", DeptNumber='1', parent=0).save()

    class Meta:
        db_table = 'departments'
        verbose_name = "部门"
        verbose_name_plural = verbose_name
        unique_together = (("DeptNumber",),)
        default_permissions = ('add', 'change', 'delete', 'export')

# 人员数据表
class UserEmp(models.Model):

    id=models.AutoField(db_column="userid", primary_key=True, null=False,editable=False)
    badgenumber = models.CharField(verbose_name='人员编号',db_column="badgenumber",null=False,max_length=24)
    ename = models.CharField(verbose_name='人员姓名',db_column="ename",null=True,max_length=24, blank=True, default="")
    defaultdeptid = models.ForeignKey(department, db_column="defaultdeptid", verbose_name='部门',editable=True, null=True,on_delete=models.DO_NOTHING)
    isstaff = models.BooleanField(verbose_name="是否可以登陆状态", default=False,db_column="isstaff")
    isactive = models.BooleanField(verbose_name="是否有所有权限", default=False,db_column="isactive")
    isadmin = models.BooleanField(verbose_name="是否是管理员", default=False,db_column="isadmin")
    empemail = models.EmailField(verbose_name="邮箱", blank=True,db_column="empemail",null=True,default="")
    phono = models.CharField(verbose_name="邮箱", blank=True,db_column="email",null=True,default="",max_length=24)


    def __str__(self):
        return self.ename

    class Meta:
        db_table = 'userinfo'
        verbose_name="人员"
        verbose_name_plural=verbose_name
        unique_together = (("badgenumber",),)
        default_permissions = ('browse','add', 'change', 'delete', 'export')
