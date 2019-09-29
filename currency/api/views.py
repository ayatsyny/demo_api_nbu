import requests
from drf_yasg.openapi import Schema, TYPE_OBJECT, TYPE_INTEGER, TYPE_STRING, FORMAT_FLOAT, FORMAT_DATE
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class ListCurrencies(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={403: 'detail: Authentication credentials were not provided.',
                                    404: 'Error: external service not correct work',
                                    200: Schema(
                                        type=TYPE_OBJECT,
                                        properties={
                                            'r030': Schema(type=TYPE_INTEGER, description='кодова назва у системі'),
                                            'txt': Schema(type=TYPE_STRING,
                                                          description='назва валюти української мовою'),
                                            'rate': Schema(type=FORMAT_FLOAT, description='обмінний рейд'),
                                            'cc': Schema(type=TYPE_STRING, description='міжнародний стандарт iso-3'),
                                            'exchangedate': Schema(type=FORMAT_DATE,
                                                                   description='прогноз до даної дати'),
                                        }
                                    )
                                    }
                         )
    def get(self, request, format=None):
        url = 'http://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
        res = requests.get(url)
        if res.status_code != 200:
            return Response('Error: external service not correct work', status=status.HTTP_404_NOT_FOUND)
        return Response(res.json(), status=status.HTTP_200_OK)
