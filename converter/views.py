from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from converter.serializers import ConverterSerializer


class ConverterAPI(APIView):
    """
    Представление конвертора валюты
    """

    def post(self, request):

        serializer = ConverterSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.amount)
            print(serializer.currency_from)
            print(serializer.currency_into)
            return Response({"result":"OK!"})
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

