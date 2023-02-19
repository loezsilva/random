from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Roulette, RouletteWinner, RouletteNumber
from roulette.clients.models import Client


class IndexListView(ListView):
    template_name = 'core/index.html'
    queryset = Roulette.objects.filter(roulettenumber__isnull=False).distinct()

# Create your views here.
class RouletteDetailView(DetailView):
    template_name = 'core/roulette.html'
    queryset = Roulette.objects.all()
    
    def dispatch(self, request, *args, **kwargs):
        if self.request.GET.get('number'):
            roulette_number = RouletteNumber.objects.get(pk=self.request.GET.get('number'))
            RouletteWinner.objects.update_or_create(
                roulette=self.get_object(),
                defaults={
                    "number": roulette_number.number,
                    "winner": roulette_number.client
                }
            )
        
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["numbers"] = self.get_object().roulettenumber_set.all().order_by('number')
        
        
        
        return context