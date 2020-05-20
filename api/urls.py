from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import NoteList, DebtList, ContactList
from rest_framework import routers

router = routers.DefaultRouter()
router.register('notes', NoteList),
router.register('contacts', ContactList),
router.register('debts', DebtList)

urlpatterns = [
    path('', include(router.urls)),

]
