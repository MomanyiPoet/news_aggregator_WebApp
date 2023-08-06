from django.db import models

# Create your models here.
class headline(models.Model):
  title = models.CharField(max_length=200)
  image = models.URLField(null=True, blank=True)
  url = models.TextField()

  class Meta:
    db_table = "tblheadline"

  def __str__(self):
    return self.title