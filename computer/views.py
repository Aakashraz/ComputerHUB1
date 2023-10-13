from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, TemplateView, DeleteView
from django.urls import reverse_lazy
from .models import Computer, ComputerGeneration, ComputerBrand

# from django.contrib.auth.mixins import LoginRequiredMixin


# class IndexView(TemplateView):
#     template_name= "computer/index.html"


class CompBrandCreateView(CreateView):
    model=ComputerBrand
    fields="__all__"
    success_url= reverse_lazy("chub:brand-list")

    

class CompGenerationCreateView(CreateView):
    model=ComputerGeneration
    fields= "__all__"
    success_url= reverse_lazy('chub:genlist')

class ComputerCreateView(CreateView):
    model= Computer
    fields= "__all__"
    success_url= reverse_lazy('chub:index')   
    


class CompBrandListView(ListView):
    model= ComputerBrand
    context_object_name= "brand_list"

class CompGenListView(ListView):
    model= ComputerGeneration
    context_object_name= 'gen_list'

class ComputerListView(ListView):
    model= Computer
    context_object_name= 'comp_list'



class CompBrandUpdateView(UpdateView):
    model= ComputerBrand
    fields= "__all__"
    success_url= reverse_lazy('chub:brand-list')

class CompGenUpdateView(UpdateView):
    model=ComputerGeneration
    fields="__all__"
    success_url= reverse_lazy('chub:genlist')

class ComputerUpdateView(UpdateView):
    model= Computer
    fields= "__all__"
    success_url= reverse_lazy('chub:index')



class CompBrandDeleteView(DeleteView):
    model= ComputerBrand
    success_url= reverse_lazy('chub:brand-list')

class ComputerDeleteView(DeleteView):
    model= Computer
    success_url= reverse_lazy('chub:index')

class CompGenDeleteView(DeleteView):
    model= ComputerGeneration
    success_url= reverse_lazy('chub:genlist')