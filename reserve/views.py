from django.shortcuts import render, redirect
from .models import Reserve
from django.shortcuts import get_object_or_404

# from .forms import ResForm
from .forms import ReserveForm


# 予約一覧
def index(request):
    reserves = Reserve.objects.all().order_by('-datetime')
    return render(request, 'reserve/index.html', {'reserves': reserves})


# 予約詳細
def detail(request, reserve_id):
    reserve = get_object_or_404(Reserve, id=reserve_id)
    return render(request, 'reserve/detail.html', {'reserve': reserve})


# 新規予約
def reserve_new(request):
    if request.method == "POST":
        form = ReserveForm(request.POST)
        if form.is_valid():
            # form.save()
            return redirect('reserve:confirm_reserve')
    else:
        form = ReserveForm()
    return render(request, 'reserve/reserve_new.html', {'form': form})

# 予約変更


# 予約取消

# 予約前確認画面
def reserve_confirm(request):
    form = ReserveForm(request.POST)
    return render(request, 'reserve/reserve_confirm.html', {'form': form})
