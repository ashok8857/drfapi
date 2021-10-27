from django.db.models import fields
from rest_framework import routers, serializers
from . models import StuInfo


class StuSerializers(serializers.ModelSerializer):
    class Meta:
        model=StuInfo
        fields='__all__'

