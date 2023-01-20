from django.contrib import admin
from .models import Project


class ProjectAdmin (admin.ModelAdmin):
##последовательность имен полей, которые должны выводиться в списке записей
    list_display = ('title', 'technology')
#последовательность имен полей, которые должны быть
#преобразованы в гиперссылки, ведущие на страницу правки записи;
    list_display_links = ('title', 'technology')
#последовательность имен полей, по которым должна выпоняться фильтрация
    search_fields = ('title', 'technology')


admin.site.register(Project, ProjectAdmin)

