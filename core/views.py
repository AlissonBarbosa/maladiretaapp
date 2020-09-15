from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from leadership.models import Leadership
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile

def index(request):
    return render(request, 'index.html')

def export_leadership_pdf(query): 
    html_string = render_to_string('reports/leadership_template.html', {'leaderships': query})
    
    html = HTML(string=html_string)
    result = html.write_pdf()

   # Creating http response
    response = HttpResponse(content_type='application/pdf;')
    response['Content-Disposition'] = 'inline; filename=Relatorio_Liderancas.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())

    return response

def generate_report(request):
    origin = request.session.get("query_origin")
    query_filter = request.session.get("query_filter")

    if origin == "Leadership":
        if query_filter:
            return export_leadership_pdf(Leadership.objects.search(query_filter))
        else:
            return export_leadership_pdf(Leadership.objects.all())