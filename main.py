from random import randint
from counter import Counter


def player_pon():
    is_pon = True
    while is_pon == True:
        pon = input(f'何を出すか選んでください。\n0:{pon_set.get(0)}, 1: {pon_set.get(1)}, 2: {pon_set.get(2)} \n>> ')
        try:
            i_pon = int(pon)
            if -1 < i_pon < 3:
                is_pon = False
            else:
                print(f'不正値が入力されました。\n')
        except ValueError:
            print(f'不正値が入力されました。\n')

    print('')
    return i_pon


def enemy_pon():
    return randint(0, 2)


key_list = [0, 1, 2]
pon_list = ['グー', 'チョキ', 'パー']
pon_set = {}
[pon_set.update({k: v}) for k, v in zip(key_list, pon_list)]
counter01 = Counter(0, 0, 0, 0)

print(f'ジャンケンゲームを開始します\n')

while True:
    p_hand = player_pon()
    e_hand = enemy_pon()
    print(f'あなたが出した手：{pon_set.get(p_hand)}')
    print(f'あいてが出した手：{pon_set.get(e_hand)}')

    counter01.pon_judge(p_hand, e_hand)
    text = input(f'続けますか？ y/n >> ')
    if text == 'y':
        print('続行します。\n')
    elif text == 'n':
        print(f'終了します。\n')
        print(f'戦績　試合数：{counter01.play}\n勝ち：{counter01.win} 負け：{counter01.lose} あいこ：{counter01.draw}')
        break
    else:
        print(f'不正値なので続行します。\n')
