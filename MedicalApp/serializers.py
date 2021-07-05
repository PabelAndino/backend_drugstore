from rest_framework import serializers

from MedicalApp.models import Company, CompanyBank, Medicine, MedicalDetail, Employee, Custumer, Bill, CustomerRequest, \
    CompanyAccount, EmployeeBank


class CompanySerializer(serializers.ModelSerializer):  # .HyperlinkedModelSerializer
    class Meta:
        model = Company
        fields = "__all__"  # ["name", "address", "email", "ruc"]


class CompanyBankSerializers(serializers.ModelSerializer):
    class Meta:
        model = CompanyBank
        fields = "__all__"

    def to_representation(self, instance):  # show all data that correspond to the foreing Key Value
        response = super().to_representation(instance)
        response['company'] = CompanySerializer(instance.company_id).data
        return response


class MedicineSerializers(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = '__all__'

    def to_representation(self, instance):
        response = super(MedicineSerializers, self).to_representation()
        response['company'] = CompanySerializer(instance.company_id).data
        return response


class MedicalDetailSerailizers(serializers.ModelSerializer):
    class Meta:
        model = MedicalDetail
        fields = '__all__'

    def to_representation(self, instance):
        response = super(MedicalDetailSerailizers, self).to_representation()
        response['medicine'] = MedicineSerializers(instance.medicine_id).data
        return response


class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Custumer
        fields = '__all__'


class BillSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'

    def to_representation(self, instance):
        response = super(BillSerializers, self).to_representation()
        response['custumer'] = CustomerSerializers(instance.custumer_id).data
        return response


class CustomerRequestSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomerRequest
        fields = '__all__'


class CompanyAccountSerializers(serializers.ModelSerializer):
    class Meta:
        model = CompanyAccount
        fields = '__all__'

    def to_representation(self, instance):
        response = super(CompanyAccountSerializers, self).to_representation()
        response['company'] = CompanySerializer(instance.company_id).data
        return response


class EmployeeBankSerializers(serializers.ModelSerializer):
    class Meta:
        model = EmployeeBank
        fields = '__all__'

    def to_representation(self, instance):
        response = super(EmployeeBankSerializers, self).to_representation()
        response['employee'] = EmployeeSerializers(instance.employee.id).data
        return response