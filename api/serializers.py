from rest_framework import serializers
from api.models import Message


class MessageSerializer(serializers.ModelSerializer):
	author = serializers.SerializerMethodField()
	
	class Meta:
		model = Message
		fields = ('email', 'message', 'author', 'created', 'updated')

	def get_author(self, obj):
		# if user.is_authenticated:
		# 		return username
		return 'Unauthenticated user'
