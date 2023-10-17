from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View,CreateView, ListView, UpdateView, TemplateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Computer, ComputerGeneration, ComputerBrand
from .forms import ComputerBrandForm, ComputerGenerationForm
# from django.contrib.auth.mixins import LoginRequiredMixin


# class IndexView(TemplateView):
#     template_name= "computer/index.html"


#USING VIEW CLASS ONLY.
class ComputerBrandView(View):
    def get(self,request):
        form= ComputerBrandForm()
    
        return render(request,'computer/computerbrand_form.html',{
            'form':form,
        })
    
    def post(self,request):
        form= ComputerBrandForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
        return redirect('chub:brand-list')
    
        # return render(request,'computer/computerbrand_list.html', {
        #     'form': form,
        # })
    

class ComputerBrandUpdateView(View):
    def get(self, request, pk):
        item= get_object_or_404(ComputerBrand, pk=pk)
        form= ComputerBrandForm(instance=item)

        return render (request, 'computer/computerbrand_form.html', {
            'form':form,
        })

    def post(self, request, pk):
        item = get_object_or_404(ComputerBrand, pk= pk)

        form= ComputerBrandForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('chub:brand-list')
        
        return render(request,'computer/computerbrand_form.html', {
            'form': form,
        })
    

class ComputerBrandDeleteView(View):
    def get(self,request, pk):
        form= get_object_or_404(ComputerBrand, pk=pk)

        return render(request, 'computer/computerbrand_confirm_delete.html',{
            'form':form,
        })

    def post(self,request, pk):
        form=get_object_or_404(ComputerBrand, pk=pk)
        form.delete()

        return redirect('chub:brand-list')
        

# to show list of computer brand
class ComputerBrandPageView(View):
    def get(self, request):
        form = ComputerBrand.objects.all()

        return render(request, 'computer/computerbrand_list.html', {
            'brand_list':form,
        })


class ComputerGenerationView(View):
    def get(self, request):
        form= ComputerGenerationForm()

        return render(request,'computer/computergeneration_form.html',{
            'form':form,
        })

    def post(self, request):
        form=ComputerGenerationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chub:genlist')
        
        return render(request, 'computer/computergeneration_form.html', {
            'form': form,
        })


class ComputerGenerationUpdateView(View):
    def get(self,request,pk):
        item= get_object_or_404(ComputerGeneration, pk=pk)
        form= ComputerGenerationForm(instance=item)

        return render(request, 'computer/computergeneration_form.html', {
            'form':form
        })
        
    def post(self, request, pk):
        item= get_object_or_404(ComputerGeneration,pk=pk)
        form= ComputerGenerationForm(request.POST, instance=item)

        if form.is_valid():
            form.save()
            return redirect('chub:genlist')
        
        return render (request,'computer/computergeneration_form.html', {
            'form': form,
        })
    

class ComputerGenerationDeleteView(View):
    def get(self, request, pk):
        item= get_object_or_404(ComputerGeneration,pk=pk)
        
        return render (request, 'computer/computergeneration_confirm_delete.html', {
            'form':item
        })
    
    def post(self, request, pk):
        item= get_object_or_404(ComputerGeneration, pk=pk)
        item.delete()

        return redirect('chub:genlist')


class ComputerGenerationPageView(View):
    def get(self, request):
        form= ComputerGeneration.objects.all()

        return render(request,'computer/computergeneration_list.html', {
            'gen_list':form,
        })
    


# USING CREATEVIEW 

# class CompBrandCreateView(CreateView):
#     model=ComputerBrand
#     fields="__all__"
#     success_url= reverse_lazy("chub:brand-list")

class CompGenerationCreateView(CreateView):
    model=ComputerGeneration
    fields= "__all__"
    success_url= reverse_lazy('chub:genlist')

class ComputerCreateView(CreateView):
    model= Computer
    fields= "__all__"
    success_url= reverse_lazy('chub:index')   
    

#using ListView

# class CompBrandListView(ListView):
#     model= ComputerBrand
#     context_object_name= "brand_list"

class CompGenListView(ListView):
    model= ComputerGeneration
    context_object_name= 'gen_list'

class ComputerListView(ListView):
    model= Computer
    context_object_name= 'comp_list'


# using UpdateView

# class CompBrandUpdateView(UpdateView):
#     model= ComputerBrand
#     fields= "__all__"
#     success_url= reverse_lazy('chub:brand-list')

class CompGenUpdateView(UpdateView):
    model=ComputerGeneration
    fields="__all__"
    success_url= reverse_lazy('chub:genlist')

class ComputerUpdateView(UpdateView):
    model= Computer
    fields= "__all__"
    success_url= reverse_lazy('chub:index')


# using DeleteView

# class CompBrandDeleteView(DeleteView):
#     model= ComputerBrand
#     success_url= reverse_lazy('chub:brand-list')

class ComputerDeleteView(DeleteView):
    model= Computer
    success_url= reverse_lazy('chub:index')

class CompGenDeleteView(DeleteView):
    model= ComputerGeneration
    success_url= reverse_lazy('chub:genlist')