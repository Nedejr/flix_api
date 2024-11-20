from rest_framework import generics
from reviews.models import Review
from reviews.serializers import ReviewSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission


# Algumas classes de permissões
# IsAdminUser
# IsAuthenticated
# IsAuthenticatedOrReadOnly
class ReviewCreateListView(generics.ListCreateAPIView):

    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView, GlobalDefaultPermission):

    permission_classes = (IsAuthenticated,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
