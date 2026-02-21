from django.contrib import admin
from .models import Listing, UserProfile, Conversation, Message


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'created_at')
    search_fields = ('title', 'description', 'owner__username')


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', 'gender', 'city')
    search_fields = ('user__username', 'city')


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('id', 'listing', 'created_at', 'updated_at')
    search_fields = ('listing__title',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'conversation', 'sender', 'created_at')
    search_fields = ('text', 'sender__username')
