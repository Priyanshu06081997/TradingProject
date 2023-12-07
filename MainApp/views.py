from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CsvUploadSerializer
from .models import CsvUpload
import pandas as pd
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import render 
import json
  
# Create your views here. 

class candle:
        id = ''
        open = ''
        high = ''
        low = ''
        close = ''
        date = ''
        def __init__(self, id, open, high, low, close, date):  
            self.id = str(id ) 
            self.open = str(open)
            self.high = str(high)
            self.low = str(low)
            self.close = str(close)
            self.date = str(date)

class CsvViewSet(viewsets.ModelViewSet):
    queryset            = CsvUpload.objects.all()
    serializer_class    = CsvUploadSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            
            file = serializer.validated_data['file']
            df = pd.read_csv(file , skipinitialspace = True)
            df = df.fillna('')
            l=[]
            for index, row in df.iterrows():
                obj = candle(row['id'],row['open'],row['high'],row['low'],row['close'],row['date'])
                l.append(obj.__dict__)

            serializer.validated_data['data'] = json.dumps(l)
            serializer.save()
            return Response({'data':serializer.data}, status=200)
        except Exception as e:
            return Response({'message':e}, status=500)
                 
                 
