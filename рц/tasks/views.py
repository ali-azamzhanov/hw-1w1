from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    search_fields = ['title']

    def get_queryset(self):
        qs = super().get_queryset()
        completed = self.request.query_params.get('completed')
        if completed is not None:
            if completed.lower() == 'true':
                qs = qs.filter(completed=True)
            elif completed.lower() == 'false':
                qs = qs.filter(completed=False)
        return qs
