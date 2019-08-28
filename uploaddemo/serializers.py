# -*- coding:utf-8 -*-
from rest_framework import serializers
from uploaddemo.models import Airticle


class AirticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airticle
        fields = '__all__'


class AirticlePicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airticle
        fields = ['image']