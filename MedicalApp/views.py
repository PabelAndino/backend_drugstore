from django.db import IntegrityError
from django.shortcuts import render
from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication

from MedicalApp.models import Company, CompanyBank, Medicine, MedicalDetail
from MedicalApp.serializers import CompanySerializer, CompanyBankSerializers, MedicineSerializers, \
    MedicalDetailSerailizers, MedicalDetailSimpleSerailizers


class CompanyViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        company = Company.objects.all()
        serializer = CompanySerializer(company, many=True, context={"request": request})
        response_dic = {"error": False, "message": "All Company List Data", "data": serializer.data}
        return Response(response_dic)

    def create(self, request):
        try:
            serializer = CompanySerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "Company Data Saved Succesfully"}
        except:
            dict_response = {"error": True, "message": "Error During Saving Company"}
        return Response(dict_response)

    def update(self, request, pk=None):
        try:
            query_set = Company.objects.all()
            company = get_object_or_404(query_set, pk=pk)
            serializer = CompanySerializer(company, data=request.data, context={"request": request})
            serializer.is_valid()
            serializer.save()
            dict_response = {"error": False, "message": "Company Data updated Succesfully"}
        except:
            dict_response = {"error": True, "message": "Error During Updating Company"}
        return Response(dict_response)


class CompanyBankViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        try:
            serializer = CompanyBankSerializers(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "Company Bank Data Saved Succesfully"}
        except:
            dict_response = {"error": True, "message": "Error During Saving Company Bank"}
        return Response(dict_response)

    def list(self, request):
        company = CompanyBank.objects.all()
        serializer = CompanyBankSerializers(company, many=True, context={"request": request})
        response_dic = {"error": False, "message": "All Company Bank List Data", "data": serializer.data}
        return Response(response_dic)

    def retrieve(self, request, pk=None):  # Mostrara los valores al pasarle un id como dato a la URL en el navegador
        queryset = CompanyBank.objects.all()
        companybank = get_object_or_404(queryset, pk=pk)
        serializer = CompanyBankSerializers(companybank, context={"request": request})
        return Response({
            "error": False,
            "message": "Single Data Fetch",
            "data": serializer.data
        })

    def update(self, request, pk=None):
        queryset = CompanyBank.objects.all()
        companybank = get_object_or_404(queryset, pk=pk)
        serializer = CompanyBankSerializers(companybank, data=request.data, context={"request": request})
        serializer.is_valid()
        serializer.save()
        return Response({
            "error": False,
            "message": "Company Bank Updated Successfully"

        })


class CompanyNameViewSet(generics.ListAPIView):
    serializer_class = CompanySerializer

    def get_queryset(self):
        name = self.kwargs["name"]
        return Company.objects.filter(name=name)


class MedicineViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        try:
            serializer = MedicineSerializers(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()

            medicine_id = serializer.data['id']  # Get the id of the record saved
            # print(medicine_id)
            medicine_detail_list = []
            for medicine_detail in request.data['medicine_detail']:
                # print(medicine_detail)
                # Add the id recently saved to the details
                medicine_detail["medicine_id"] = medicine_id
                medicine_detail_list.append(medicine_detail)
                # print(medicine_detail)

            serializerMedicineDetail = MedicalDetailSerailizers(data=medicine_detail_list, many=True,
                                                                context={"request": request})
            serializerMedicineDetail.is_valid()
            serializerMedicineDetail.save()

            dict_response = {"error": False, "message": "Medicine Data Saved Succesfully"}
        except IntegrityError as e:
            dict_response = {"error": True, "message": "Error During Saving Medicine", "status": e}
        return Response(dict_response)

    def list(self, request):
        medicine = Medicine.objects.all()
        serializer = MedicineSerializers(medicine, many=True, context={"request": request})

        medicine_data = serializer.data
        newmedicinelist = []

        for medicine in medicine_data:
            medicine_details = MedicalDetail.objects.filter(medicine_id=medicine["id"])
            medicine_details_serializer = MedicalDetailSimpleSerailizers(medicine_details, many=True)
            medicine["medicine_details"] = medicine_details_serializer.data
            newmedicinelist.append(medicine)

        response_dic = {"error": False, "message": "All Medicine List Data", "data": newmedicinelist}
        return Response(response_dic)

    def retrieve(self, request, pk=None):  # Mostrara los valores al pasarle un id como dato a la URL en el navegador
        queryset = Medicine.objects.all()
        medicine = get_object_or_404(queryset, pk=pk)
        serializer = MedicineSerializers(medicine, context={"request": request})

        # que muestre los tambien los detalles de medicine detail
        serializer_data = serializer.data
        medicine_detail = MedicalDetail.objects.filter(medicine_id=serializer_data["id"])
        medicine_detail_serializer = MedicalDetailSimpleSerailizers(medicine_detail, many=True)
        serializer_data['detail_medicine'] = medicine_detail_serializer.data

        return Response({
            "error": False,
            "message": "Single Data Fetch",
            "data": serializer_data
        })

    def update(self, request, pk=None):
        queryset = Medicine.objects.all()
        medicine = get_object_or_404(queryset, pk=pk)
        serializer = MedicineSerializers(medicine, data=request.data, context={"request": request})
        serializer.is_valid()
        serializer.save()
        return Response({
            "error": False,
            "message": "Medicine Updated Successfully"

        })


company_list = CompanyViewSet.as_view({"get": "list"})
company_create = CompanyViewSet.as_view({"post": "create"})
company_update = CompanyViewSet.as_view({"put": "update"})
