from django.utils.translation import gettext_lazy as _
from portfolio.core.models import AbstractBaseModel, models


class Category(AbstractBaseModel):
    name = models.CharField(verbose_name=_('name'), max_length=50)
    slug = models.SlugField(verbose_name=_('slug'), max_length=50, unique=True)

    def __str__(self):
        return f'{self.name}'