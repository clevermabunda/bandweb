from django.db import models

class Band(models.Model):
    """
    Represents a music band.

    Attributes:
        band_name (str): The name of the band.
        number_of_members (int): The number of members in the band.
        year_formed (date): The year the band was formed.
        genre (str): The musical genre of the band.
        about_the_band (str, optional): A description of the band. Can be null.
    """

    band_name = models.CharField(max_length=50)
    number_of_members = models.IntegerField()
    year_formed = models.DateField()
    genre = models.CharField(max_length=50)
    about_the_band = models.CharField(max_length=10000, null=True)

    def __str__(self) -> str:
        """
        Returns a string representation of the Band instance.

        Returns:
            str: The name of the band.
        """
        return self.band_name
