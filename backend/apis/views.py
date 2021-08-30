from rest_framework.generics import ListAPIView, RetrieveAPIView
from apis.models import Article
from apis.serializers import  ArticleSerializer
# Create your views here.

class ArticleListView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class =  ArticleSerializer


class ArticleDetailView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class =  ArticleSerializer    