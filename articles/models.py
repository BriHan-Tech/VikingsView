from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Author(models.Model):
    name = models.CharField(max_length=1000)
    grade = models.IntegerField()

    def __str__(self) -> str:
        return "{0} - {1}".format(self.name, str(self.grade))    


class Article(models.Model):
    title = models.CharField(max_length=250)
    date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to="thumbnails")
    article = RichTextUploadingField()
    recommended_articles = models.ForeignKey('self', blank=True, null=True, related_name="recommended", on_delete=models.CASCADE)

    def __str__(self):
        return "{0} written by: {1}".format(self.title, self.author)

    class Meta:
        ordering = ("-date",)
