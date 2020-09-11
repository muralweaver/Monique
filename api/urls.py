from django.urls import path, include
from .views import ContactList, UserList, JournalList, DebtList, NoteList, TaskList, FoodPrefList
from rest_framework import routers

# This router is similar to SimpleRouter, but additionally includes a default API root view, that returns a
# response containing hyperlinks to all the list views - https://www.django-rest-framework.org/api-guide/routers/

router = routers.DefaultRouter()
router.register("journal", JournalList),
router.register("contacts", ContactList),
router.register("notes", NoteList),
router.register("tasks", TaskList),
router.register("foodpref", FoodPrefList),
router.register("debts", DebtList),
# router.register("documents", DocumentUploadView, basename="document-upload")
router.register("users", UserList)

urlpatterns = [path("", include(router.urls))]
