from django.contrib import admin
from .models import Roulette, RouletteNumber, RouletteWinner
from django.core.exceptions import ValidationError

# Register your models here.
from django import forms

class RouletteNumberForm(forms.ModelForm):
    class Meta:
        model = RouletteNumber
        fields = "__all__"
        
    def clean(self): 
        super().clean()
        
        number = self.cleaned_data['number']
        roulette = self.cleaned_data['roulette']
        
        if not self.cleaned_data['id'] and RouletteNumber.objects.filter(roulette=roulette, number=number).exists():
            return self.add_error('number', ValidationError(f"O número: {number} já foi escolhido por alguém"))
        
        return self.cleaned_data
        
class RouletteNumberInline(admin.TabularInline):
    model = RouletteNumber
    min_num = 0
    extra = 0
    form = RouletteNumberForm
    
    def get_max_num(self, request, obj=None, **kwargs):
        return obj.max_numbers if obj and obj.max_numbers else 50


@admin.register(Roulette)
class RouletteAdmin(admin.ModelAdmin):
    list_display = ('name', 'max_numbers')
    list_filter = ('name', 'max_numbers')
    inlines = [
        RouletteNumberInline,
    ]
    search_fields = ('name',)
    date_hierarchy = 'created_at'
    ordering = ('created_at',)
    
@admin.register(RouletteWinner)
class RouletteWinnerAdmin(admin.ModelAdmin):
    list_display = ('winner', 'roulette', 'created_at')
    list_filter = ('roulette', )
    search_fields = ('roulette',)
    date_hierarchy = 'created_at'
    ordering = ('created_at',)
    form = RouletteNumberForm