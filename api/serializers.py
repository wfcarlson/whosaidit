from rest_framework import serializers

from api.models import *

class GameRoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = GameRoom
        fields = '__all__'

class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = '__all__'
        depth = 1

class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = '__all__'
        depth = 1

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = '__all__'
        depth = 1