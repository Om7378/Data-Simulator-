from django.contrib import admin
from .models import PostgreSQLConfiguration, PostgreSQLDataMapping, PostgreSQLColumnMapping


@admin.register(PostgreSQLConfiguration)
class PostgreSQLConfigurationAdmin(admin.ModelAdmin):
    list_display = ('id', 'connection_name', 'host', 'port', 'database_name', 'username')


@admin.register(PostgreSQLDataMapping)
class PostgreSQLDataMappingAdmin(admin.ModelAdmin):
    list_display = ('id', 'connection', 'output_type', 'target_table', 'timestamp_column')


@admin.register(PostgreSQLColumnMapping)
class PostgreSQLColumnMappingAdmin(admin.ModelAdmin):
    list_display = ('id', 'data_mapping', 'output_name', 'column_name')