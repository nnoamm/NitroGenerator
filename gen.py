def gen():
    import random

    upper_letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_letter = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'

    numbtogen = input('How Much:')
    upper, lower, nums, = True, True, True,
    all = ""

    if upper:
        all += upper_letter
    if lower:
        all += lower_letter
    if nums:
        all += digits

        length = 23
        amount = numbtogen

        for x in range(int(numbtogen)):
            code = ''.join(random.sample(all, length))
            print('discord.gift/'+code)





gen()
