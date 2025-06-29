from django.db import models

class CarouselItem(models.Model):
    image = models.ImageField(upload_to='carousel/')
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    button_text = models.CharField(max_length=50, blank=True)
    button_link = models.URLField(blank=True)

    def __str__(self):
        return self.title

class AboutImage(models.Model):
    image = models.ImageField(upload_to='about/')

    def __str__(self):
        return f"About Image {self.id}"

class AboutInfo(models.Model):
    heading = models.CharField(max_length=200)
    description = models.TextField()
    years_experience = models.PositiveIntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    features = models.JSONField(default=list)  # list of strings like ["Power & Energy", ...]

    def __str__(self):
        return self.heading

class Fact(models.Model):
    icon_class = models.CharField(max_length=100)
    number = models.PositiveIntegerField()
    label = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.label} ({self.number})"

class FeatureImage(models.Model):
    image = models.ImageField(upload_to='features/')

    def __str__(self):
        return f"Feature Image {self.id}"

class Feature(models.Model):
    icon_class = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='services/')

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='projects/')
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='team/')
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.position}"

class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='testimonials/')
    text = models.TextField()

    def __str__(self):
        return f"{self.client_name} ({self.profession})"

class ContactInfo(models.Model):
    phone_number = models.CharField(max_length=30)
    email = models.EmailField()
    office_address = models.TextField()
    map_link = models.URLField()
    map_iframe_src = models.TextField()

    def __str__(self):
        return f"Contact Info ({self.email})"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
