height=float(input("身長(cm)を入力して下さい"))
bmi=22
std_weight=bmi*(height/100)**2
print("身長: "+str(height)+"cm →",end="") #改行なし
print("標準体重"+str(std_weight)+"kg")