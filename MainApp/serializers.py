from rest_framework import serializers
from .models import CsvUpload

class CsvUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = CsvUpload
        fields = '__all__'