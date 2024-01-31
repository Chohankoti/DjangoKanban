from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from .models import Users, Tasks, CCode, AccessControl
from .serializers import UsersSerializer, TasksSerializer, CCodeSerializer, AccessControlSerializer

class UsersListCreateView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class UsersRetrieveUpdateDeleteView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    def get(self, request, **kwargs):
        return self.retrieve(request, **kwargs)

    def put(self, request, **kwargs):
        return self.update(request, **kwargs)

    def delete(self, request, **kwargs):
        return self.destroy(request, **kwargs)

class TasksListCreateView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class TasksRetrieveUpdateDeleteView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer

    def get(self, request, **kwargs):
        return self.retrieve(request, **kwargs)

    def put(self, request, **kwargs):
        return self.update(request, **kwargs)

    def delete(self, request, **kwargs):
        return self.destroy(request, **kwargs)

class CCodeListCreateView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = CCode.objects.all()
    serializer_class = CCodeSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class CCodeRetrieveUpdateDeleteView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = CCode.objects.all()
    serializer_class = CCodeSerializer

    def get(self, request, **kwargs):
        return self.retrieve(request, **kwargs)

    def put(self, request, **kwargs):
        return self.update(request, **kwargs)

    def delete(self, request, **kwargs):
        return self.destroy(request, **kwargs)

class AccessControlListCreateView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = AccessControl.objects.all()
    serializer_class = AccessControlSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class AccessControlRetrieveUpdateDeleteView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = AccessControl.objects.all()
    serializer_class = AccessControlSerializer

    def get(self, request, **kwargs):
        return self.retrieve(request, **kwargs)

    def put(self, request, **kwargs):
        return self.update(request, **kwargs)

    def delete(self, request, **kwargs):
        return self.destroy(request, **kwargs)
