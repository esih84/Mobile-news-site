from django.db import models
from django.utils import timezone
from django.forms import ModelForm
# Create your models here.


class User(models.Model):
    user = models.TextField(default=None)

    def __str__(self):
        return self.user


class category_obshen(models.Model):
    titles = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images', verbose_name="تصویر")
    slug = models.SlugField(max_length=100, unique=True)
    status = models.BooleanField(default=True)
    position = models.IntegerField()

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.titles


class category(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images', verbose_name="تصویر")
    slug = models.SlugField(max_length=100, unique=True)
    status = models.BooleanField(default=True)
    position = models.IntegerField()

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.title


class mobile_screen(models.Model):
    screen = models.TextField(max_length=550, verbose_name="صفحه نمایش")
    slug = models.SlugField(max_length=100, unique=True)
    screen_type = models.TextField(max_length=200, verbose_name="نوع صفحه نمایش")
    dimensions = models.FloatField(max_length=100, verbose_name="ابعاد")
    refresh_rate = models.TextField(max_length=500, verbose_name="نرخ نوسازی صفحه نمایش")
    screen_saver = models.TextField(max_length=550, verbose_name='محافظ صفحه نمایش', null=True)


class camera(models.Model):
    number_of_cameras = models.IntegerField()
    slug = models.SlugField(max_length=10000, unique=True)
    information = models.TextField(max_length=2000)
    filming = models.TextField(max_length=1000)
    selfie = models.TextField(max_length=100)
    stabilization = models.TextField(max_length=500)
    filming_selfie = models.TextField(max_length=200)
    stabilization_selfie = models.TextField(max_length=500)
    attributes = models.TextField(max_length=2000)

    def __str__(self):
        return self.slug + self.filming + self.selfie + self.filming_selfie


class color(models.Model):
    name_color = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    status = models.BooleanField(default=True, )
    position = models.IntegerField()

    def __str__(self):
        return self.name_color


class mobile_body(models.Model):
    body_material = models.TextField(max_length=1000)
    slug = models.SlugField(max_length=10000, unique=True)
    weight = models.IntegerField()
    dimensions = models.FloatField(max_length=100, verbose_name="ابعاد")
    sim_card = models.TextField(max_length=100)


    def __str__(self):
        return self.slug


class processor(models.Model):
    chip = models.TextField(max_length=500)
    graphic_chip = models.TextField(max_length=500)
    information = models.TextField(max_length=2000)
    slug = models.SlugField(max_length=10000, unique=True)

    def __str__(self):
        return self.slug


class memory(models.Model):
    slug = models.SlugField(max_length=10000, unique=True)
    internal_memory = models.TextField(max_length=300, verbose_name="حافظه داخلی")
    memory_port = models.TextField(max_length=500)

    def __str__(self):
        return self.internal_memory + self.memory_port


class speaker(models.Model):
    jack = models.BooleanField(default=True)
    slug = models.SlugField(max_length=10000, unique=True)
    stereo = models.BooleanField(default=True)
    sound_volume = models.TextField(max_length=300)

    def __str__(self):
        return self.slug + self.sound_volume


# labtop


class labtop_body(models.Model):
    body_material = models.TextField(max_length=1000)
    slug = models.SlugField(max_length=10000, unique=True)
    weight = models.IntegerField()
    sim_card = models.TextField(max_length=100)
    information = models.TextField(max_length=2000)

    def __str__(self):
        return self.body_material + self.information


class connections_labtop(models.Model):
    usb = models.IntegerField()
    type_c = models.IntegerField()
    hdmi = models.IntegerField()


class mobile(models.Model):
    STATUS_CHOICES = (
        ('p', 'publish'),
        ('n', 'draft'),
    )
    mobile_name = models.CharField(max_length=200, verbose_name="نام گوشی")
    image = models.ImageField(upload_to='images', verbose_name="تصویر")
    slug = models.SlugField(max_length=200, unique=True)
    cate = models.ManyToManyField(category, related_name="category")
    cate_obshen = models.ManyToManyField(category_obshen, related_name="category_obshens")
    desc = models.TextField(verbose_name="توضیحات")
    publication_date = models.DateTimeField(verbose_name="زمان انتشار گوشی")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='قیمت')
    screen = models.TextField(max_length=5000, verbose_name='صفحه نمایش')
    color_phone = models.TextField(max_length=2000)
    cameras = models.OneToOneField(camera, related_name="camera", on_delete=models.CASCADE)
    material = models.OneToOneField(mobile_body, related_name="materials", on_delete=models.CASCADE)
    operating_system = models.TextField(max_length=300,  verbose_name='سیستم عامل')
    prcs = models.OneToOneField(processor, related_name='mobile_processors', on_delete=models.CASCADE, verbose_name="پردازنده")
    memory = models.OneToOneField(memory, related_name="memory", on_delete=models.CASCADE)
    battery = models.IntegerField()
    charging_speed = models.IntegerField()
    information = models.TextField(max_length=2000)
    speaker = models.OneToOneField(speaker, related_name="speakers", on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    publication_blog = models.DateTimeField(default=timezone.now, verbose_name="زمان انتشار")


class labtop(models.Model):

    STATUS_CHOICES = (
        ('p', 'publish'),
        ('n', 'draft'),
    )
    labtop_name = models.CharField(max_length=200,verbose_name="نام لب تاپ")
    slug = models.SlugField(max_length=200, unique=True)
    publication_date = models.DateTimeField(verbose_name="زمان انتشار لب تاپ")
    desc = models.TextField(verbose_name="توضیحات")
    image = models.ImageField(upload_to='images', verbose_name="تصویر")
    cate = models.ManyToManyField(category, related_name="categorys")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='قیمت')
    operating_system = models.TextField(max_length=300)
    cate_obshen = models.ManyToManyField(category_obshen, related_name="category_obshe")
    labtop_processor = models.OneToOneField(processor, related_name='processors', on_delete=models.CASCADE)
    color_labtop = models.ForeignKey(color, related_name="color_lobtops", on_delete=models.CASCADE)
    battery = models.IntegerField()
    charging_speed = models.IntegerField()
    screen = models.TextField(max_length=5000 ,verbose_name='صفحه نمایش')
    camera = models.TextField(max_length=500)
    finger_print = models.BooleanField(default=False)
    information = models.TextField(max_length=2000)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    connections = models.OneToOneField(connections_labtop, related_name="connections_labtop",on_delete=models.CASCADE)
    lobtop_speaker = models.OneToOneField(speaker, related_name="lobtop_speakers", on_delete=models.CASCADE)
    publication_blog = models.DateTimeField(default=timezone.now, verbose_name="زمان انتشار")

    def __str__(self):
        return self.labtop_name


class post(models.Model):
    STATUS_CHOICES = (
        ('p', 'publish'),
        ('n', 'draft'),
    )

    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.ManyToManyField(category, related_name='post')
    cate_obshen = models.ManyToManyField(category_obshen, related_name="category")
    desc = models.TextField(max_length=500)
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    photo = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


class comment(models.Model):
    email = models.EmailField()
    reply = models.ForeignKey("self", related_name='commentid', on_delete=models.CASCADE, blank=True, null=True)
    post_key = models.ForeignKey(post, related_name='post_key', on_delete=models.CASCADE)
    desc = models.TextField(max_length=700)
    date = models.DateTimeField(default=timezone.now)
    is_reply = models.BooleanField(default=False)


class comment_form(ModelForm):
    class Meta:
        model = comment
        fields = ['email', 'desc']


class reply_form(ModelForm):
    class Meta:
        model = comment
        fields = ['email', 'desc']



