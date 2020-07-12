from django.http import HttpResponse
 
from TestModel.models import TestTable
 
# 数据库操作
def testdb(request):
    # test1 = TestTable(name='runoob')
    # test1.save()
    test = TestTable.objects.all().filter(name='runoob')
    return HttpResponse(str(test[0].id))