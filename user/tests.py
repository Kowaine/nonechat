from django.test import TestCase
from user.views import *
from user.models import User
from django.utils import timezone

# Create your tests here.
class UserTest(TestCase):
    def setUp(self):
        print("开始测试")
    
    def tearDown(self):
        print("测试结束")

    def test_is_exist(self):
        ''' 测试检查用户是否存在的函数 '''
        username = "Kowaine"
        wrong_username = "QWERT"
        User.objects.create(username=username, password="12345678", last_ip="127.0.0.1", register_time=timezone.now())
        result = is_exist(username)
        wrong_result = is_exist(wrong_username)
        self.assertEqual(result, True)
        self.assertEqual(wrong_result, False)

    def test_vaildate_user(self):
        ''' 测试检查用户密码是否匹配的函数 '''
        username = "Kowaine"
        password = "12345678"
        wrong_password = "12345679"
        User.objects.create(username=username, password=password, last_ip="127.0.0.1", register_time=timezone.now())
        result = vaildate_user(username, password)
        wrong_result = vaildate_user(username, wrong_password)
        self.assertEqual(result, True)
        self.assertEqual(wrong_result, False)