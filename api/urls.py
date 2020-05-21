from django.urls import path, include
from .views import NoteList, DebtList, ContactList, DocumentUploadView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('notes', NoteList),
router.register('contacts', ContactList),
router.register('debts', DebtList),
router.register('documents', DocumentUploadView, basename='document-upload')

urlpatterns = [
    path('', include(router.urls))

]
