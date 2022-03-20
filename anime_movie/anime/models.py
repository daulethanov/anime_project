from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField('Категория', max_length=140)
    url = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Genre(models.Model):
    name = models.CharField('Имя', max_length=100)
    url = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = 'Жанры'


class Actor(models.Model):
    name = models.CharField("Имя", max_length=100)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    description = models.TextField("Описание", null=True, blank=True)
    image = models.ImageField("Изображение", upload_to="actors/", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Режиссеры"
        verbose_name_plural = "Режиссеры"


class Anime(models.Model):
    SERIAL = 'serial'
    FILM = 'film'
    OVA = 'ova'
    SPECIAL = 'special'

    CHOICE_CATEGORY = {
        (SERIAL, 'Сериал'),
        (FILM, 'Фильм'),
        (OVA, 'OVA'),
        (SPECIAL, 'Special')
    }

    title = models.CharField('Аниме', max_length=255)
    description = models.TextField('Описание')
    hep = models.TextField('видео')
    genres = models.ManyToManyField(Genre, verbose_name='Жанры')
    actors = models.ManyToManyField(Actor, verbose_name='Режиссер')
    category = models.CharField(choices=CHOICE_CATEGORY, verbose_name='Категория', max_length=50, null=True)
    url = models.SlugField(max_length=140, unique=True)
    draft = models.BooleanField('Черновик', default=False)
    poster = models.ImageField('Изоброжение', upload_to='anime/')
    year = models.PositiveSmallIntegerField("Дата выхода", default=2019)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('anime_detail', kwargs={'slug': self.url})

    class Meta:
        verbose_name = 'Аниме'
        verbose_name_plural = 'Аниме'


class RatingStar(models.Model):
    value = models.FloatField('Значение', default=0)

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"


class Rating(models.Model):
    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="звезда")
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, verbose_name='Аниме')

    def __str__(self):
        return f"{self.star} - {self.anime}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class Reviews(models.Model):
    """Отзывы"""
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True
    )
    anime = models.ForeignKey(Anime, verbose_name="Аниме", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.anime}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

