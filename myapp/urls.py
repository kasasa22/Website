from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('admin', views.admin_index, name='admin_index'),
    path('category', views.category, name='category'),
    path('supplier', views.supplier, name='supplier'),
    path('cashier', views.cashier, name='cashier'),
    path('medicine', views.medicine, name='medicine'),
    path('sales-detail', views.sales_detail, name='sales_detail'),
    path('report', views.report, name='report'),
    path('company', views.company, name='company')

]