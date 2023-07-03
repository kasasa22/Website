from django.shortcuts import render 
from django.http import HttpResponse

# Create your views here.
def index(request):   
    return render(request, 'index.html')
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

