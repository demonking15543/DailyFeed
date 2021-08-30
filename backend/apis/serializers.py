from django.db.models import fields
from rest_framework import serializers
from apis import models
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = ('id', 'title', 'description',)


