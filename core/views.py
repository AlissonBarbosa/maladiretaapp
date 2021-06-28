from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from leadership.models import Leadership
from employees.models import Employee
from customers.models import Customer
from candidates.models import Candidate
from authorities.models import Authoritie
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile
from statistics.generate import Generate

from fpdf import FPDF

import io
from django.http import FileResponse
import pdfkit

@login_required
def handler404(request, exception):
    return render(request, '404.html', status=404)

@login_required
def index(request):
    generate = Generate()
    customers = generate.statistic_customers()
    leadership = generate.statistic_leadership()
    authorities = generate.statistic_authorities()
    candidates = generate.statistic_candidates()
    solicitations = generate.statistic_solicitations()
    context = {'customers': customers,
                'leadership': leadership,
                'authorities': authorities,
                'candidates': candidates,
                'solicitations': solicitations}
    return render(request, 'index.html', context)

def export_pdf(html_string, filename):
    html = HTML(string=html_string)
    result = html.write_pdf()

    response = HttpResponse(content_type='application/pdf;')
    response['Content-Disposition'] = 'inline; filename={}.pdf'.format(filename)
    response['Content-Transfer-Encoding'] = 'binary'
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())

    return response

def export_leadership_pdf(query): 
    html_string = render_to_string('reports/leadership_template.html', {'leaderships': query})
    options = {
        'page-size': 'A4',
        'encoding': "UTF-8",
        'orientation': 'Landscape',
        'margin-top': '1cm',
        'margin-right': '1cm',
        'margin-bottom': '1cm',
        'margin-left': '1cm',
        'footer-left': "Mala Direta - Romero Rodrigues",
        'footer-font-size':'8',
        'footer-right': '[page] de [topage]',
        'footer-font-name': 'Dosis',
    }

    output = pdfkit.from_string(html_string, False, options)
    response = HttpResponse(output, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment;filename="Relatorio_Lideranças.pdf"'

    return response

# def export_leadership_pdf(query):
#     html_string = render_to_string('reports/leadership_template.html', {'leaderships': query})
#     return export_pdf(html_string=html_string, filename="Relatorio Lideranças")

def export_employee_pdf(query):
    html_string = render_to_string('reports/employee_template.html', {'employees': query})
    options = {
        'page-size': 'A4',
        'encoding': "UTF-8",
        'orientation': 'Landscape',
        'margin-top': '1cm',
        'margin-right': '1cm',
        'margin-bottom': '1cm',
        'margin-left': '1cm',
        'footer-left': "Mala Direta - Romero Rodrigues",
        'footer-font-size':'8',
        'footer-right': '[page] de [topage]',
        'footer-font-name': 'Dosis',
    }

    output = pdfkit.from_string(html_string, False, options)
    response = HttpResponse(output, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment;filename="Relatorio_Funcionários.pdf"'

    return response

def export_customer_pdf(query):
    html_string = render_to_string('reports/customer_template.html', {'customers': query})
    options = {
        'page-size': 'A4',
        'encoding': "UTF-8",
        'orientation': 'Landscape',
        'margin-top': '1cm',
        'margin-right': '1cm',
        'margin-bottom': '1cm',
        'margin-left': '1cm',
        'footer-left': "Mala Direta - Romero Rodrigues",
        'footer-font-size':'8',
        'footer-right': '[page] de [topage]',
        'footer-font-name': 'Dosis',
    }

    output = pdfkit.from_string(html_string, False, options)
    response = HttpResponse(output, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment;filename="Relatorio_Clientes.pdf"'

    return response

def export_candidate_pdf(query):
    html_string = render_to_string('reports/candidate_template.html', {'candidates': query})
    options = {
        'page-size': 'A4',
        'encoding': "UTF-8",
        'orientation': 'Landscape',
        'margin-top': '1cm',
        'margin-right': '1cm',
        'margin-bottom': '1cm',
        'margin-left': '1cm',
        'footer-left': "Mala Direta - Romero Rodrigues",
        'footer-font-size':'8',
        'footer-right': '[page] de [topage]',
        'footer-font-name': 'Dosis',
    }

    output = pdfkit.from_string(html_string, False, options)
    response = HttpResponse(output, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment;filename="Relatorio_Candidatos.pdf"'

    return response

def export_authoritie_pdf(query):
    html_string = render_to_string('reports/authoritie_template.html', {'authorities': query})
    options = {
        'page-size': 'A4',
        'encoding': "UTF-8",
        'orientation': 'Landscape',
        'margin-top': '1cm',
        'margin-right': '1cm',
        'margin-bottom': '1cm',
        'margin-left': '1cm',
        'footer-left': "Mala Direta - Romero Rodrigues",
        'footer-font-size':'8',
        'footer-right': '[page] de [topage]',
        'footer-font-name': 'Dosis',
    }

    output = pdfkit.from_string(html_string, False, options)
    response = HttpResponse(output, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment;filename="Relatorio_Autoridades.pdf"'

    return response

def generate_report(request):
    origin = request.session.get("query_origin")
    query_filter = request.session.get("query_filter")

    if origin == "Leadership":
        if query_filter:
            return export_leadership_pdf(Leadership.objects.search(query_filter))
        else:
            return export_leadership_pdf(Leadership.objects.all())
    elif origin == "Employee":
        if query_filter:
            return export_employee_pdf(Employee.objects.search(query_filter))
        else:
            return export_employee_pdf(Employee.objects.all())
    elif origin == "Customer":
        if query_filter:
            return export_customer_pdf(Customer.objects.search(query_filter))
        else:
            return export_customer_pdf(Customer.objects.all()[:5000])
    elif origin == "Candidate":
        if query_filter:
            return export_candidate_pdf(Candidate.objects.search(query_filter))
        else:
            return export_candidate_pdf(Candidate.objects.all())
    elif origin == "Authoritie":
        if query_filter:
            return export_authoritie_pdf(Authoritie.objects.search(query_filter))
        else:
            return export_authoritie_pdf(Authoritie.objects.all())

def export_customer_tags(query):
    pdf = FPDF(orientation ='P', unit = 'mm', format='Letter')
    pdf.set_margins(left=4, top=8, right=5)
    pdf.set_auto_page_break(auto = True, margin = 10)
    pdf.add_page()
    pdf.set_font('Arial', '', 10)

    x_ref = pdf.get_x()
    width_tag = 69.6
    count = 0
    y_ref = pdf.get_y()
    count_tag = 0
    for customer in query:
        if count_tag % 30 == 0 and count_tag > 0:
            pdf.add_page()
        #text = 'Prezado Alisson Barbosa\nRua das Orquídeas, 57\nJardim das Plantas\nCampina Grande - PB\n58415-000'
        text = '{}\n{}, {}\n{}\n{}\n{}'.format(customer.name, customer.street, customer.number, customer.neighborhood, customer.city, customer.cep)
        if count == 0:
            x_ref = pdf.get_x()
            y_ref = pdf.get_y()
            count += 1
        elif count == 1:
            x_ref += width_tag
            count += 1
        elif count == 2:
            x_ref += width_tag
            count = 0
        pdf.set_xy(x = x_ref, y = y_ref)
        pdf.multi_cell(width_tag, 5.195, text, 0, 'L')
        count_tag += 1
            

    response = HttpResponse(pdf.output(dest='S').encode('latin-1'))
    response['Content-Disposition'] = 'attachment;filename="Etiquetas.pdf"'
    return response

def generate_tags(request):
    origin = request.session.get("query_origin")
    query_filter = request.session.get("query_filter")

    if origin == "Customer":
        if query_filter:
            return export_customer_tags(Customer.objects.search(query_filter))
        else:
            return export_customer_tags(Customer.objects.all())