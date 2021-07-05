
from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication

from MedicalApp.models import Company, CompanyBank
from MedicalApp.serializers import CompanySerializer, CompanyBankSerializers


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




company_list = CompanyViewSet.as_view({"get": "list"})
company_create = CompanyViewSet.as_view({"post": "create"})
company_update = CompanyViewSet.as_view({"put": "update"})
