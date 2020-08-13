from django.urls import path, include
from .views import NoteList, DebtList, ContactList, DocumentUploadView, UserList
from rest_framework import routers

router = routers.DefaultRouter()
router.register('notes', NoteList),
router.register('contacts', ContactList),
router.register('debts', DebtList),
router.register('documents', DocumentUploadView, basename='document-upload')
router.register('users', UserList)

urlpatterns = [
    path('', include(router.urls))

]
