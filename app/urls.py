from django.urls import path, include
from .views import BlogCreateView, BlogDeleteView, BlogListView, BlogUpdateView, CommentViewSet, TagViewSet, CategoryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'comment', CommentViewSet, basename='comment')
router.register(r'tag', TagViewSet, basename='tag')
router.register(r'category', CategoryViewSet, basename='category')


urlpatterns = [
    path('', include(router.urls)),
    path('blog-list/', BlogListView.as_view(), name="blog-list"),
    path('blog-create/', BlogCreateView.as_view(), name="blog-create"),
    path('blog-update/', BlogUpdateView.as_view(), name="blog-update"),
    path('blog-delete/', BlogDeleteView.as_view(), name="blog-delete"),
]