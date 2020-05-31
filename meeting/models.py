from django.db import models
from django.conf import settings
import datetime
from django.utils import timezone


TYPE = ['MANCO', 'Finance', 'Project Team Leaders']

class Meeting(models.Model):
	ref_number = models.CharField(u"Meeting Ref. No", max_length=35,
            unique=True, blank=True, db_index=True)
	meeting_type = models.CharField(u"Meeting Type", max_length=50, choices=[(i, i)
            for i in sorted(TYPE)], db_index=True, blank=True, null=True)
	pub_date = models.DateTimeField('Published Date')
	date_from = models.DateTimeField('date from')
	date_to = models.DateTimeField('date_to')
	description = models.CharField(max_length=200)

	def __str__(self):
		return self.description

	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'

class Meeting_Item(models.Model):
	meeting = models.ForeignKey(Meeting)
	item_status = models.CharField(max_length=200)
	item_description = models.CharField(max_length=200)
	item_due_date = models.DateTimeField('due date')
	item_user = models.ForeignKey(settings.AUTH_USER_MODEL)

	def __str__(self):
		return self.item_description