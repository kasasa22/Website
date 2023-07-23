from django.shortcuts import render 
from django.http import HttpResponse

# Create your views here.
def welcome(request):   
    return render(request, 'welcome.html')
def admin_index(request):
    return render(request, 'admin-index.html')
def category(request):
    return render(request, 'category.html')
def supplier(request):
    return render(request, 'supplier.html')
def cashier(request):
    return render(request, 'cashier.html')
def medicine(request):
    return render(request, 'medicine.html')
def sales_detail(request):
    return render(request, 'sales-detail.html')
def report(request):
    return render(request, 'report.html')
def company(request):
    return render(request, 'company.html')

def add_category(request):
    return render(request, 'add-category.html',)
def add_supplier(request):
    return render(request, 'add-supplier.html',)
def add_cashier(request):
    return render(request, 'add-cashier.html',)
def add_medicine(request):
    return render(request, 'add-medicine.html',)
def cashier_index(request):
    return render(request, 'cashier-index.html')
def sales(request):
    return render(request, 'sales.html')
def daily_sales(request):
    return render(request, 'daily-sales.html')
def profile(request):
    return render(request, 'profile.html')