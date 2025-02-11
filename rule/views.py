from django.shortcuts import render
from .forms import RuleForm
from django.views import View


class AddRule(View):

    def get(self, request):
        form = RuleForm(initial={'user': request.user})
        return render(request, 'rule/add_rule.html', {'form': form, 'error': ''})

    def post(self, request):
        form = RuleForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return render(request, 'rule/add_rule.html', {'form': form, 'error': ''})
        else:
            error = 'Форма не правильно заповнена'
            return render(request, 'rule/add_rule.html', {'form': form, 'error': error})


