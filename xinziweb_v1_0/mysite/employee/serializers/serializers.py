from rest_framework import serializers

from mysite.employee.models import department,UserEmp

# 部门数据序列化
class DepartmentSerializers(serializers.Serializer):
    DeptID = serializers.CharField(required=False)
    DeptNumber = serializers.CharField()
    DeptName = serializers.CharField()
    parent = serializers.CharField()
    DeptAddr = serializers.CharField()

    # 序列化
    def to_representation(self, instance):
        ret = super(DepartmentSerializers, self).to_representation(instance)
        return ret

    def create(self, validated_data):
        """
        根据提供的验证过的数据创建并返回一个新的`Snippet`实例。

        """
        print("create=========================================")
        return department.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        根据提供的验证过的数据更新和返回一个已经存在的`Snippet`实例。
        """
        print("-------update------------------------")
        # instance.DeptID = validated_data.get('DeptID', instance.DeptID)
        instance.DeptNumber = validated_data.get('DeptNumber', instance.DeptNumber)
        instance.DeptName = validated_data.get('DeptName', instance.DeptName)
        instance.parent = validated_data.get('parent', instance.parent)
        instance.DeptAddr = validated_data.get('DeptAddr', instance.DeptAddr)
        instance.save()

        return instance

# 人员部门查询序列化器
class DeptUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = department
        fields = ['DeptID', 'DeptNumber', 'DeptName']

# 人员数据序列化
class UserEmpSerializers(serializers.ModelSerializer):
    # defaultdeptid 字段的嵌套序列化器
    defaultdeptid = DeptUserSerializers(read_only=True)
    # 外间关联
    defaultdeptid_id = serializers.PrimaryKeyRelatedField(queryset=department.objects.all(), source='defaultdeptid', write_only=True)
    badgenumber = serializers.CharField()

    class Meta:
        model = UserEmp
        # 序列化字段
        fields = ['id','badgenumber', 'ename', 'defaultdeptid', 'isstaff', 'isactive', 'isadmin', 'empemail', 'phono','defaultdeptid_id']
        # 只读
        read_only_fields = ['id']

    def create(self, validated_data):
        """
        根据提供的验证过的数据创建并返回一个新的`Snippet`实例。

        """
        print("create=========================================")
        print(validated_data["badgenumber"])
        return UserEmp.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        根据提供的验证过的数据更新和返回一个已经存在的`Snippet`实例。
        """
        print("-------update------------------------")
        # instance.DeptID = validated_data.get('DeptID', instance.DeptID)
        # instance.badgenumber = validated_data.get('badgenumber', instance.badgenumber)
        instance.ename = validated_data.get('ename', instance.ename)
        instance.defaultdeptid = validated_data.get('defaultdeptid', instance.defaultdeptid)
        instance.isstaff = validated_data.get('isstaff', instance.isstaff)
        instance.isactive = validated_data.get('isstaff', instance.isactive)
        instance.isadmin = validated_data.get('isstaff', instance.isadmin)
        instance.empemail = validated_data.get('isstaff', instance.empemail)
        instance.phono = validated_data.get('isstaff', instance.phono)
        instance.save()

        return instance