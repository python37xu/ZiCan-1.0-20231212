from mysite.employee.models import department,UserEmp
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,AllowAny

from mysite.employee.serializers.serializers import DepartmentSerializers,UserEmpSerializers


# 查询,新增部门api
class DepartmentList(APIView):

    # IsAuthenticated 仅通过认证的用户
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        queryset = department.objects.all()
        serializer = DepartmentSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializers = DepartmentSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors)

# 修改部门api
class DepartmentListDlite(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request,id):
        queryset = department.objects.filter(DeptID = id)
        serializer = DepartmentSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self,request,id):
        queryset = department.objects.get(DeptID = id)
        serializer = DepartmentSerializers(instance=queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class UsermepList(APIView):
    # IsAuthenticated 仅通过认证的用户
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        queryset = UserEmp.objects.all()
        serializer = UserEmpSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self,requets):
        serializers = UserEmpSerializers(data=requets.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors)


class UsermepListDilte(APIView):
    # IsAuthenticated 仅通过认证的用户
    permission_classes = (IsAuthenticated,)

    def get(self,request,id):
        queryset = UserEmp.objects.filter(defaultdeptid = id)
        serializer = UserEmpSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self,request,id):
        queryset = UserEmp.objects.get(id = id)
        print(queryset)
        print(request.data)
        serializer = UserEmpSerializers(instance=queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)