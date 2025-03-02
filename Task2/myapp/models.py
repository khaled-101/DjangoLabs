from django.db import models

class School(models.Model):
    name = models.CharField(verbose_name="School", max_length=50, unique=True)
    number_of_classes = models.IntegerField(verbose_name="Number of Classes")  # Changed from CharField to IntegerField
    area = models.FloatField(verbose_name="Area", default=0.0, editable=False)

    def calculate_area(self):
        # If the instance hasn't been saved yet, return 0
        if not self.pk:
            return 0
        # Otherwise, sum up the areas of related classrooms
        return sum(classroom.area for classroom in self.classroom_set.all())    
    def save(self, *args, **kwargs):
        self.area = self.calculate_area()
        super().save(*args, **kwargs)   
class Classroom(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)  
    name = models.CharField(verbose_name="Classroom", max_length=50, unique=True)
    area = models.FloatField(verbose_name="Area", default=0.0)

    def save(self, *args, **kwargs):
        """Save and update the school's area calculation."""
        super().save(*args, **kwargs)
        if self.school:
            self.school.save()

    def delete(self, *args, **kwargs):
        """Ensure the school's area updates when a classroom is deleted."""
        school = self.school
        super().delete(*args, **kwargs)
        if school:
            school.save()
