class Counter:
    def __init__(self, win, lose, draw, play):
        self.win = win
        self.lose = lose
        self.draw = draw
        self.play = play

    def pon_judge(self, p_pon, e_pon):
        sa = (p_pon - e_pon + 3) % 3
        if sa == 0:
            self.draw += 1
            print('結果：あいこ\n')
        elif sa == -2 or sa == 1:
            self.lose += 1
            print('結果：あなたの負け\n')
        elif sa == -1 or sa == 2:
            self.win += 1
            print('結果：あなたの勝ち\n')
        self.play += 1
