from django.test import TestCase
from customers.models import Client
from products.models import Product, ProductCategory
# Create your tests here.
from django.urls import reverse
#from django.contrib.auth import get_user_model, User
from django_tenants.test.cases import TenantTestCase,FastTenantTestCase
from django_tenants.test.client import TenantClient
from datetime import datetime
from django.db import connection
from core.models import Setting
from django_tenants.utils import get_tenant_model, get_tenant_domain_model
from django_tenants.middleware import TenantMainMiddleware
from django.test.client import RequestFactory
# Create your tests here.
class BaseSetup(TenantTestCase):
    #@classmethod
    #def setup_tenant(cls, tenant):
    #    """
    #    Add any additional setting to the tenant before it get saved. This is required if you have
    #    required fields.
    #    """
    #    tenant.name = "test"
    #    tenant.paid_until = datetime.now().strftime('%Y-%m-%d')
    #    tenant.on_trial = 0
    #    return tenant
    @classmethod
    def setup_tenant(cls, tenant):
        """
        Add any additional setting to the tenant before it get saved. This is required if you have
        required fields.
        :param tenant:
        :return:
        """
        #cls.tenant_domain = cls.get_test_tenant_domain()
        tenant.paid_until="2023-05-20"
        tenant.on_trial=True
        #tenant.owner_id = 1
        #tenant.tenants = [1]
        return tenant
 
    #@staticmethod
    #def get_test_tenant_domain():
    #    return 'example02.localhost'
    #@staticmethod
    #def get_test_schema_name():
    #    return 'example02'

    def setUp(self):
        super().setUp()
        #super().setUpClass()
        #self.factory = RequestFactory()
        #self.tm = TenantMainMiddleware(lambda r: r)
        self.c = TenantClient(self.tenant)

    def tearDown(self):
        super().tearDown()
        #super().tearDownClass()

    def test_user_profile_view(self):
        setting01 = Setting.objects.create(id='zh-hant', language='中文')
        productcato01 = ProductCategory.objects.create(name='3c')
        product01 = Product.objects.create(name='phone', price=100, category=productcato01)
        #response = self.c.get('http://tenant.test.com.localhost:8000/products/')
        response = self.c.get(reverse('products:list'))
        #response = self.c.get('/products/list/')
        self.assertEqual(response.status_code, 200)