from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from .models import Occurrence
from .serializer import OccurrenceSerializer
# Create your views here.


class AllOccurrence(ListAPIView):

    permission_classes = [IsAuthenticated]
    queryset = Occurrence.objects.all()
    serializer_class = OccurrenceSerializer

    def post(self, request, format=None):
        serializer = OccurrenceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OccurrenceView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        try:
            occurrence = Occurrence.objects.get(pk=pk)
            serializer = OccurrenceSerializer(occurrence)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        occurrence = Occurrence.objects.get(pk=pk)
        occurrence.delete()
        return Response(status=status.HTTP_200_OK)