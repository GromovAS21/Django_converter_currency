from rest_framework import serializers


class ConverterSerializer(serializers.Serializer):
    """
    Сериализатор для класса ConverterAPI
    """

    amount = serializers.IntegerField(required=True)
    currency_from = serializers.CharField(required=True, min_length=3, max_length=3)
    currency_to = serializers.CharField(required=True, min_length=3, max_length=3)