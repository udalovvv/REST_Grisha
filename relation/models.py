from django.db import models


class Mod(models.Model):
    title_of_mod = models.CharField(max_length=100)
    text_of_mod = models.CharField(max_length=1000)
    # comments = models.ManyToManyField(Comment)
    def __str__(self):
        return f"{self.title_of_mod}"


class Comment(models.Model):
    text_of_comment = models.CharField(max_length=1000)
    mod = models.ForeignKey(Mod, on_delete=models.PROTECT, null=True, blank=True, related_name="comments")
    # mod = models.ManyToManyField(Mod, related_name="comments")
    def __str__(self):
        return f"{self.text_of_comment}"


class Like(models.Model):
    counter = models.IntegerField()
    comment = models.OneToOneField(Comment, on_delete=models.CASCADE)















