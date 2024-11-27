from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from converter.serializers import ConverterSerializer
from converter.services import get_current_currency


class ConverterAPI(APIView):
    """
    Представление конвертора валюты
    """

    @swagger_auto_schema(
        request_body=ConverterSerializer,
        responses= {200: "OK!", 400: "BAD_REQUEST"},
    )
    def post(self, request) -> Response:

        serializer = ConverterSerializer(data=request.data)
        if serializer.is_valid():
            amount = request.data.get("amount")
            cur_from = request.data.get("currency_from")
            cur_to = request.data.get("currency_to")
            convert = get_current_currency(cur_from, cur_to)
            if not convert:
                return Response({"message": "Введена некорректная валюта!"})
            else:
                result = round(convert * amount, 2)
                return Response({"result": result})
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

