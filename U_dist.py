### U-distribution Plot & visualize ###
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm import tqdm_notebook as tqdm

num = 225
ball = 9000

def coma_plot(square):
    s = int(np.sqrt(square.shape[0]))
    square = square.reshape((s, s))
    loc_ball = []
    for i in tqdm(range(square.shape[0])):  # 同じコマでもボールの位置をちょっとランダムに割り振る
        for j in range(square.shape[1]):
            for z in range(int(square[i, j])):
                loc_ball.append([np.random.uniform(i, i + 1), np.random.uniform(j, j + 1)])  # <- 同じコマ内で適当に
    loc_ball = np.array(loc_ball)

    plt.figure(figsize=(10, 10))
    plt.scatter(loc_ball[:, 0], loc_ball[:, 1], s=10, color="black")

    plt.title("Distribution")

    # 　縦と横線を入れる。
    x = range(s + 1)
    y = range(s + 1)
    for i in range(s + 1):
        plt.plot(x, np.repeat(y[i], s + 1), color="black")
        plt.plot(np.repeat(x[i], s + 1), y, color="black")

    plt.show()


def init(num, ball):  # <- 最初のランダム配置
    square = np.zeros(num)
    for i in range(ball):
        square[np.random.randint(num)] += 1
    return square


def invisible(num, ball):

    square = init(num, ball)

    coma_plot(square)
    plt.show()

    sns.distplot(square)
    plt.title("Initial Distribution")
    plt.show()

    for i in range(1000000):  # exchange()をrange(...)回繰り返す

        x_from = np.random.randint(num)  # 0~10の数字からランダムに1つ抜く
        x_to = np.random.randint(num)  # 0~10の数字からランダムに1つ抜く
        if square[x_from] != 0:  # もしsquareのx_from番目の数字が0でなかったら
            square[x_from] = square[x_from] - 1  # quareのx_from番目から1を引く
            square[x_to] = square[x_to] + 1  # squareのx_to番目に1を加える
    return square


def main():
    square = invisible(num, ball)
    coma_plot(square)
    sns.distplot(square)
    plt.title("Final Distribution")
    plt.show()


if __name__ == "__main__":
    main()