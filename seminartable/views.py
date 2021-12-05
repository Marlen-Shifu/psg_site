from django.shortcuts import render

from .models import TableRow

def seminartable_page(request):
    table_rows = TableRow.objects.all()
    return render(request, 'schedule.html', {'rows': table_rows})