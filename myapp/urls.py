from django.urls import path
from . import views
urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('admin', views.admin_index, name='admin_index'),
    path('category', views.category, name='category'),
    path('supplier', views.supplier, name='supplier'),
    path('cashier', views.cashier, name='cashier'),
    path('medicine', views.medicine, name='medicine'),
    path('sales-detail', views.sales_detail, name='sales_detail'),
    path('report', views.report, name='report'),
    path('company', views.company, name='company'),
    path('add-category', views.add_category, name='add-category'),
    path('add-supplier', views.add_supplier, name='add-supplier'),
    path('add-cashier', views.add_cashier, name='add-cashier'),
    path('add-medicine', views.add_medicine, name='add-medicine'),
    path('cashier-index', views.cashier_index, name='cashier_index'),
    path('sales', views.sales, name='sales'),
    path('daily-sales', views.daily_sales, name='daily_sales'),
    path('profile', views.sales, name='profile')

]