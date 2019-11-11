from django.db import models

class Link(models.Model):
	mvp_code = models.CharField(max_length=250, default="")
	brand = models.CharField(max_length=250, default="")
	channel = models.CharField(max_length=250, default="")
	vendor = models.CharField(max_length=250, default="")
	placement_type = models.CharField(max_length=250, default="")
	audience = models.CharField(max_length=250, default="")
	placement_name = models.CharField(max_length=250, default="")
	fallback_url = models.CharField(max_length=250, default="")
	deeplink_path = models.CharField(max_length=250, default="")
	utm_source = models.CharField(max_length=250, default="")
	utm_campaign = models.CharField(max_length=250, default="")
	desktop_url = models.CharField(max_length=250, default="")


