from django.shortcuts import render
from .models import Coin

# Create your views here.
def index(request):
    # Get the first 10 coins ordered by social score descending
    coins = Coin.objects.order_by('-social_score')[:10]
    fields = [f.name for f in Coin._meta.get_fields()]
    context = {
        "coins" : coins,
        "fields" : fields
    }
    return render(request, 'coins/index.html', context = context)


def load_coins(request):
    page = request.POST.get('page')
    coins = Coin.objects.order_by('-social-score')

    results_per_page = 10
    paginator = Paginator(coins, results_per_page)
    try:
        coins = paginator.page(page)
    except PageNotAnInteger:
        coins = paginator.page(2)
    except EmptyPage:
        coins = paginator.page(paginator.num_pages)

    # Build a html coins list with the paginated posts
    coins_html = loader.render_to_string('coins/coins.html', {'coins': coins})

    # Package output data and return it as a JSON object
    output = {'coins_html': coins_html, 'has_another': posts.has_next()}
    return JsonResponse(output)
