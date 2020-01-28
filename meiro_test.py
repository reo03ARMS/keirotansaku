import random
import numpy as np
import pandas as pd

r = 0.8 #割引率
actions = ["A","B","C","D","E","F"]
num_train = 1000 #テスト回数
i = 0

#Rボードの作成
def create_reward_board():
    R = pd.read_csv("./action_bord.csv",header=None)
    return R
R = create_reward_board()

#Qボードの作成
def create_action_board():
    a = np.zeros((6,6),dtype=np.int16)
    Q = pd.DataFrame(a)
    return Q
Q = create_action_board()


def main():
    for i in range(num_train):
        state = start()
        action = set_action(state)
        max_num = max_action(action)
        Q[action][state] = update(state,action,max_num)
        i += 1
    print("実行回数:" + str(num_train) + "回")
    print(Q)
    print("-------------------------")
    test()


#初期セット
def start():
    hoge = random.choice(actions)
    state = actions.index(hoge)
    return state

#actionを決める
def set_action(s):
    keep = R.iloc[s]
    while True:
        hoge2 = random.choice(actions)
        action = actions.index(hoge2)
        if keep.iloc[action] >= 0:
            break
        else:
            pass
    return action

def max_action(a):
    max_num = max(Q.iloc[a])
    return max_num  

#Qボードの更新
def update(s,a,m):
    Q[a][s] = R[a][s] + 0.8 * m
    return Q[a][s]

def train(s):
    keep = Q.iloc[s]
    return keep


def test():
    hoge = random.choice(actions)
    ans_state = actions.index(hoge)
    print("テスト開始")
    print("スタート位置:"+hoge)
    a = Q.max()
    max_action_num = a.max()
    while True:
        keep = train(ans_state)
        ans_action = keep.max()
        ans_index = keep.idxmax()
        if max_action_num == ans_action:
            print("-------------------------")
            print("現在地:"+actions[ans_index])
            print("Finish!")
            break
        else:
            print("-------------------------")
            print("現在地:"+actions[ans_index])
            print("Next!")
            ans_state =  ans_index


        



if __name__ == "__main__":
    main()
