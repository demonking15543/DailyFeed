from django.urls import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.


class Article(models.Model):
    user=models.ForeignKey(User, verbose_name=_("Author"), 
        related_name="author", on_delete=models.CASCADE)
    title=models.CharField(_("Title"), max_length=120)  
    description=models.TextField(_("Description"))  



    

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Article_detail", kwargs={"pk": self.pk})
