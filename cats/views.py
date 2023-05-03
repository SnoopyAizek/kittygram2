from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import OwnerOrReadOnly, ReadOnly
from .paginations import CatsPagination
from .models import Achievement, Cat, User

from .serializers import AchievementSerializer, CatSerializer, UserSerializer


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    permission_classes = (OwnerOrReadOnly,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    pagination_class = CatsPagination
    filterset_fields = ('color', 'birth_year')
    search_fields = ('achievements__name', 'owner__username')
    ordering_fields = ('birth_year',)
    ordering = ('birth_year',)

    def get_permissions(self):
        if self.action == 'retrieve':
            return (ReadOnly(),)
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
