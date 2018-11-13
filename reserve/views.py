from django.shortcuts import render, redirect
from .models import Res
from django.shortcuts import get_object_or_404
from .forms import ResForm


# 予約一覧
def index(request):
    reserves = Res.objects.all().order_by('datetime')
    return render(request, 'reserve/index.html', {'reserves': reserves})


# 予約詳細
def detail(request, reserve_id):
    reserve = get_object_or_404(Res, id=reserve_id)
    if request.method == 'POST':
        reserve.delete()
        return redirect('reserve:index')
    return render(request, 'reserve/detail.html', {'reserve': reserve, 'reserve_id': reserve_id})


# 新規予約
def reserve_new(request):
    form = ResForm(request.POST or None)
    if form.is_valid():
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
def edit(request, reserve_id):
    reserve = get_object_or_404(Res, pk=reserve_id)

    if request.method == 'POST':
        form = ResForm(request.POST)
        if form.is_valid():
            res = Res()
            res.name = form.cleaned_data['name']
            res.datetime = form.cleaned_data['datetime']
            res.num = form.cleaned_data['num']
            res.course = form.cleaned_data['course']
            res.comment = form.cleaned_data['comment']

            Res.objects.filter(pk=reserve_id).update(
                name=res.name,
                datetime=res.datetime,
                num=res.num,
                course=res.course,
                comment=res.comment,
            )
            reserve = get_object_or_404(Res, pk=reserve_id)
            return render(request, 'reserve/detail.html', {'reserve': reserve})

    else:
        data = {
            'name': reserve.name,
            'datetime': reserve.datetime.strftime('%Y-%m-%dT%H:%M'),  # 日時と時刻の間にTを入れる
            'num': reserve.num,
            'course': reserve.course,
            'comment': reserve.comment,
            }
        form = ResForm(data)

    return render(request, 'reserve/edit.html', {'form': form, 'reserve_id': reserve_id})


# 予約取消
def delete(request, reserve_id):
    reserve = get_object_or_404(Res, id=reserve_id)
    if request.method == 'POST':
        reserve.delete()
        return redirect('reserve:index')
    return render(request, 'reserve/delete.html', {'reserve': reserve})

