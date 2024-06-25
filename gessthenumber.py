import random
serect_number=random.randint(1,20)
print("1から20までの数字を当ててください")

#6回聞く
for guesses_taken in range(1,7):
          print("数を入力して下さい")
          guess=int(input())

          if guess < serect_number:
                  print("あなたの推定値は小さいです")
          elif guess > serect_number:
                  print("あなたの推定値は大きいです")
          else:
                  break

if guess == serect_number:
        print("当たり！"+str(guesses_taken)+"回で当たりました")
else:
        print("残念。正解は"+str(serect_number)+"でした")