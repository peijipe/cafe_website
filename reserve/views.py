from django.shortcuts import render, redirect
from .models import Reserve, Res
from django.shortcuts import get_object_or_404

from .forms import ResForm

# 予約一覧
def index(request):
    reserves = Res.objects.all().order_by('datetime')
    return render(request, 'reserve/index.html', {'reserves': reserves})


# 予約詳細
def detail(request, reserve_id):
    reserve = get_object_or_404(Res, id=reserve_id)
    return render(request, 'reserve/detail.html', {'reserve': reserve})


# 新規予約
def reserve_new(request):
    form = ResForm(request.POST or None)
    if form.is_valid():
        print('form_validation')
        res = Res()
        res.name = form.cleaned_data['name']
        res.datetime = form.cleaned_data['datetime']
        res.num = form.cleaned_data['num']
        res.course = form.cleaned_data['course']
        res.comment = form.cleaned_data['comment']

        Res.objects.create(
            name=res.name,
            datetime=res.datetime,
            num=res.num,
            course=res.course,
            comment=res.comment,
        )
        return redirect('reserve:index')

    return render(request, 'reserve/reserve_new.html', {'form': form})


# 予約変更

# 予約取消

# 予約前確認画面
