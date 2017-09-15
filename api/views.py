from imagesearch_app.models import Image, ImageSearch
from .serializers import ImageSerializer, ImageSearchSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination


# Create your views here.
class ImageListAPIView(APIView):

    def get(self, request, format=None, *args, **kwargs):
        term = str(kwargs['term'])
        image_search = ImageSearch(term=term)
        image_search.save()
        paginator = LimitOffsetPagination()
        images = Image.objects.filter(snippet__contains=term)
        result_page = paginator.paginate_queryset(images, request)
        serializer = ImageSerializer(result_page, many=True, context={'request': request})

        return Response(serializer.data)


class ImageSearchListAPIView(APIView):

    def get(self, request, format=None):
        image_search = ImageSearch.objects.all().order_by('-when')
        serializer = ImageSearchSerializer(image_search, many=True)

        return Response(serializer.data)
