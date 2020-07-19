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

    def __str__(self):
        return self.title

    def summary(self):
        # body = str(self.body)
        # summ = body.find('[\.\!\?]')
        # summ += 1
        return self.body[:100]


    def pretty_tstamp(self):
        return self.timestamp.strftime('%B %e, %Y')

    # def sort_tstamp(self):
    #     return self.timestamp.strftime('%Y%m%d')
