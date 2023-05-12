from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from .serializers import FileSerializer
from rest_framework import status, generics
from .models import File
import mysql.connector

class FileView(generics.CreateAPIView):
  queryset = File.objects.all()
  serializer_class = FileSerializer
  parser_classes = (MultiPartParser, FormParser)

  def post(self, request, *args, **kwargs):
    file_serializer = FileSerializer(data=request.data)

    def name():
      if file_serializer.is_valid():
        file_serializer.save()
        f = file_serializer.validated_data
        for key, value in f.items():
          return value

    text = ""
    file_obj = request.FILES['file']
    for c in file_obj.chunks():
      text = text + " " + c.decode("UTF-8")

    connection = mysql.connector.connect(
      host='localhost', user='admin', password='Vineetha@123', port='3306', database='api_db')
    cursor = connection.cursor()
    filename=name()
    query="INSERT INTO ram1234 (content, file) VALUES (%s, %s)"
    cursor.execute(query, (text, str(filename)))
    cursor.close()
    connection.commit()
    if file_serializer.is_valid():
      return Response(file_serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)