from django.contrib import admin

from django.db import models
from django.forms import Textarea

from .models import Meeting, Meeting_Item



class MeetingItemInline(admin.StackedInline):

		model = Meeting_Item
		extra = 0


class MeetingAdmin(admin.ModelAdmin):

	formfield_overrides = {
        models.CharField: {'widget': Textarea(
                           attrs={'rows': 5,
                                  'cols': 40,
                                  'style': 'height: 10em;'})},
    }

	inlines = [MeetingItemInline]

	list_display = ('description', 'meeting_type','pub_date', 'was_published_recently')

	list_filter = ['pub_date']

admin.site.register(Meeting, MeetingAdmin)