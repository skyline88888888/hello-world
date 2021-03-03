#2_order_determinant.py
coefficientarr=[]
for i in range(4):
    coefficientarr.append(eval(input("系数"+str(i)+":")))
for i in range(2):
    coefficientarr.append(eval(input("常数"+str(i)+":")))
denominator=coefficientarr[0]*coefficientarr[3]-coefficientarr[1]*coefficientarr[2]
molecule_x1=coefficientarr[4]*coefficientarr[3]-coefficientarr[1]*coefficientarr[5]
molecule_x2=coefficientarr[0]*coefficientarr[5]-coefficientarr[4]*coefficientarr[2]
print("x1:{} x2:{}".format(molecule_x1/denominator,molecule_x2/denominator))
