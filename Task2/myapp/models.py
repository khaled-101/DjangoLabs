from django.db import models

class School(models.Model):
    name = models.CharField(verbose_name="School", max_length=50, unique=True)
    number_of_classes = models.IntegerField(verbose_name="Number of Classes")  # Changed from CharField to IntegerField
    area = models.DecimalField(verbose_name="Area", max_digits=10, decimal_places=2, default=0.00, editable=False)

    def calculate_area(self):
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
    area = models.DecimalField(verbose_name="Area", max_digits=10, decimal_places=2, default=0.00)  # Ensure default is properly handled

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  
        if self.school:
            self.school.area = self.school.calculate_area()  
            self.school.save()

    def delete(self, *args, **kwargs):
        """Ensure the school's area updates when a classroom is deleted."""
        school = self.school
        super().delete(*args, **kwargs)
        if school:
            school.save()
