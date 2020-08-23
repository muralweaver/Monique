from django.urls import path, include
from .views import ContactList, UserList, JournalList
from rest_framework import routers

router = routers.DefaultRouter()
router.register("journal", JournalList),
router.register("contacts", ContactList),
# router.register("documents", DocumentUploadView, basename="document-upload")
router.register("users", UserList)

urlpatterns = [path("", include(router.urls))]
