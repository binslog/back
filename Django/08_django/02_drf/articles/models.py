from rest_framework.response import Response
from rest_framework.decorator import api_view
from rest_framework import status

from .models import Article, Comment
from .serializers import ~~~~

@api_view(['GET','POST'])
def Article_list(request):
    if request.method == "GET":
        articles=Article.objects.all()
        serializer=ArticleListSerializer(articles,many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer=ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status=status.http~~~~)


def Article_detail(request,article_pk):
    comment=Comment.Article.get(pk=article_pk)

    if request.method == "GET":
        serializer=Commentserializer(comment)
        return Response(serializer.data)
    
    elif request.method == "DELETE":
        comment.delete()
        return Response(status=stauts.http~~~)

    elif request.method == "PUT":
        serializer=CommentSerializer(comment,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status=status.http~ created 201)


