from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect, FileResponse
# from django.template import loader
from django.urls import reverse

from .models import Plantilla
import datetime

import io
from reportlab.pdfgen import canvas

# Create your views here.


def some_view(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")
    p.drawString(0, 400, "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc ullamcorper urna et erat aliquet sollicitudin. Morbi faucibus nibh sodales, convallis ante eget, venenatis ex. Vivamus interdum ultricies dapibus. Nam tempus, turpis a porta aliquet, est ex pulvinar diam, sit amet convallis turpis ex a metus. Praesent tincidunt hendrerit pellentesque. Pellentesque quis feugiat odio, a varius augue. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nunc pharetra, enim vel interdum pharetra, magna nunc malesuada dui, vitae tincidunt est diam a odio. Nulla vitae maximus mi. Nunc eget felis tortor. Nulla rhoncus rutrum felis, a placerat magna lacinia at. Curabitur eget urna metus. In accumsan ipsum in diam aliquet euismod. Vivamus ante nunc, pharetra et. ")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')


def saludo(request):
    fecha = datetime.datetime.now().year
    texto = '<h3>Hola estamos a %s </h3>' % fecha
    return HttpResponse(texto)


def inicio(request):
    context = {

    }
    return render(request, 'plantillas/base.html', context)


def index(request):
    latest_question_list = Plantilla.objects.order_by('-nombre')[:5]
    # template = loader.get_template('plantillas/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'plantillas/index.html', context)


def detail(request, id):
    question = get_object_or_404(Plantilla, pk=id)
    return render(request, 'plantillas/detail.html', {'question': question})

    # return HttpResponse("Estas  viendo el detalle de una plantilla determinada %s. " % id)


def results(request, id):
    response = "Estas buscando resultados para la palabra %s. "
    question = get_object_or_404(Plantilla, pk=id)
    return render(request, 'plantillas/results.html', {'question': question})
    # return HttpResponse(response % id)


def vote(request, id):
    question = get_object_or_404(Plantilla, pk=id)
    try:
        selected_choice = question
    except (KeyError, Plantilla.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'plantillas/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.tipo = request.POST['tipo']
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('plantillas:results', args=(question.id,)))

        # return HttpResponse("Esto es otra cosa %s." % id)
