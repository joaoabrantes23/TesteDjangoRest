from rest_framework import viewsets
from testeDjango.serializers import ToDoSerializer
from testeDjango.models import ToDo

class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
