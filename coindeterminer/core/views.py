from django.shortcuts import render
from core.coindeterminer import CoinDeterminer


def home(request):
    context = {}

    if request.method == 'POST':

        # Instance of CoinDeterminer
        coins = CoinDeterminer()

        coins_total_list = []

        # Calc of the total of coins of the field "Amount"
        if 'amount' in request.POST:
            amount = request.POST.get('amount')

            if amount:
                coins_total = coins.get_coins_total(amount)

                # If result 'None' returned - Return this warning message below
                if not coins_total:
                    coins_total_list.append([u'Invalid value. Please try again.',])
                else:
                    coins_total_list.append(coins_total,)


        # Calc of the total of coins of the content of uploaded file
        if 'attachment' in request.FILES:
            attachment = request.FILES['attachment']

            # Read each line of the file
            lines = attachment.read().split('\n')
            for line in lines:
                coins_total_list.append(coins.get_coins_total(line))

        # Context var (list) to show results
        context['coins_total_list'] = coins_total_list

        # Context var to show the results DIV
        context['result'] = True


    return render(request, 'home.html', context)

