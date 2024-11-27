from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from converter.serializers import ConverterSerializer
from converter.services import get_current_currency


class ConverterAPI(APIView):
    """
    Представление конвертора валюты
    """

    def post(self, request):

        serializer = ConverterSerializer(data=request.data)
        if serializer.is_valid():
            amount = request.data.get("amount")
            cur_from = request.data.get("currency_from")
            cur_to = request.data.get("currency_to")
            convert = get_current_currency(cur_from, cur_to)
            result = round(convert * amount, 2)
            return Response({"result": result})
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

