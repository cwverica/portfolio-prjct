from django.db import models

# Create blog model
# title
# publication timestamp
# body
# image

class Blog(models.Model):
    title = models.CharField(max_length=250)
    timestamp = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/blog/')
# add blog app to the settings
# create a migration
# migrate
# add to the admin
