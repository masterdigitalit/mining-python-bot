warningMessage = 'прошло 10 минут, просим вас подтвердить выполнение'

admins = [5273914742, 6214632131]

confirmationStates = ['not-activated', 'waiting', 'warning', 'not-done', 'success']


listOfTemky = [
    # {'name': 'hamster combat', 'link': 'https://t.me/hamSter_kombat_bot/'},
    {'name': 'blum', 'link': 'https://t.me/BlumCryptoBot/app?startapp=to_home', 'daily': True},
    {'name': 'BullApp', 'link':'https://t.me/BullApp_bot?start=822611494_3347', 'daily': True}
    # {'name': 'tapswap', 'link': 'https://t.me/tapswap_mirror_1_bot'},
]


times = {
    'hamster combat':{'periodic':None,'daily':{'type':'by-time'}},
    'BullApp': {'periodic':10},
    'blum':{'periodic':10}

}
