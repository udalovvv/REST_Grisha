from django.urls import path

from relation.views import index, show, create, comment_delete

urlpatterns = [
    path('', index),
    path('<int:id>', show),
    path('<int:id>/create', create),
    path("comment/<int:id>/delete", comment_delete)
]