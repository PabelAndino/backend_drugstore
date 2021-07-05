from django.contrib import admin

# Register your models here.
from MedicalApp.models import Company, Medicine, MedicalDetail, Employee, Custumer, Bill, EmployeeSalary, BillDetail, \
    CustomerRequest

admin.site.register(Company)
admin.site.register(Medicine)
admin.site.register(MedicalDetail)
admin.site.register(Employee)
admin.site.register(Custumer)
admin.site.register(Bill)
admin.site.register(EmployeeSalary)
admin.site.register(BillDetail)
admin.site.register(CustomerRequest)
