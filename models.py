from django.db import models


class PostgreSQLConfiguration(models.Model):
    connection_name = models.CharField(
        max_length=255,
        unique=True
    )

    host = models.CharField(max_length=255)
    port = models.IntegerField(default=5432)
    database_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.host}:{self.port} - {self.database_name}"


class PostgreSQLDataMapping(models.Model):

    OUTPUT_CHOICES = [
        ('temperature', 'Temperature'),
        ('vibration', 'Vibration'),
    ]

    connection = models.ForeignKey(
        PostgreSQLConfiguration,
        on_delete=models.CASCADE,
        related_name='data_mappings'
    )

    output_type = models.CharField(
        max_length=50,
        choices=OUTPUT_CHOICES
    )

    target_table = models.CharField(max_length=255)

    timestamp_column = models.CharField(max_length=255)

    def __str__(self):
        return (
            f"{self.connection.connection_name} - "
            f"{self.output_type}"
        )


class PostgreSQLColumnMapping(models.Model):

    data_mapping = models.ForeignKey(
        PostgreSQLDataMapping,
        on_delete=models.CASCADE,
        related_name='column_mappings'
    )

    output_name = models.CharField(max_length=100)

    column_name = models.CharField(
        max_length=255,
        blank=True
    )

    def __str__(self):
        return f"{self.output_name} → {self.column_name}"