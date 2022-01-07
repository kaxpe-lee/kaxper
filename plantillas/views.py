from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
# from django.template import loader
from django.urls import reverse

from .models import Plantilla

# Create your views here.


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
