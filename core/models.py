from django.db import models

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
