from django.contrib import admin

from .models import Conversation
from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):

    """ Message Admin Definition """
    
    list_display = ('__str__', 'created')


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):

    """ Conversation Admin Definition """
    
    list_display = ('__str__', 'count_messages', 'count_participants')