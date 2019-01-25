from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib import messages
from capture_email.core.forms import CaptureEmailForm
from capture_email.core.mailchimp import APIMailChimp


class Index(FormView):
    template_name = 'contact.html'
    form_class = CaptureEmailForm
    success_url = reverse_lazy('core:home')

    def get(self, request, *args, **kwargs):
        return render(request, 'core/index.html', {'form': self.form_class})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            try:
                id_list = '6b4a7c21ea'
                mail = APIMailChimp()
                mail.add_email(id_list,  form.cleaned_data.get('email'))
                messages.success(request, 'E-mail cadastrado com suceso!')
                return redirect(self.success_url)
            except BaseException as error:
                print(error)
                messages.error(request, 'Erro ao cadastrar E-mail.')
        return render(request, 'core/index.html', {'form': form})
