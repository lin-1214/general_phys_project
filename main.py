from body_move import *

ricky = dancer(vec(-.8, 0, 0))
#使呈用手撐地狀態
ricky.move('r_arm_1',3*pi/4)
ricky.move('l_arm_1',3*pi/4)
ricky.move('r_arm_2',pi/4)
ricky.move('l_arm_2',pi/4)
#動作演示
#headSpin(ricky)
#time.sleep(1)
#ice(ricky)
#handSpin(ricky)
#time.sleep(1)
#airChair(ricky)
windMill(ricky)
airChair(ricky)
handSpin(ricky)
ice(ricky)
headSpin(ricky)
elbow(ricky)

cnt = 0
scene2 = graph(title = "Energy of difference movement")
Energy_bars = gvbars(graph = scene2)
scene3 = graph(title = "height of center of gravity")
height_bars = gvbars(graph = scene3)
scene4 = graph(title = "power required of movement transform")
p_bars = gvbars(graph = scene4)
# scene4 = graph(title = "height of center of gravity")
# height_bars = gvbars(graph = scene4)
for i in E_array:
    cnt+=1
    Energy_bars.plot(cnt, i)
cnt = 0
# for i in height_bars:
#     cnt+=1
#     height_bars.plot(cnt, i)
for i in h_of_center:
    cnt+=1
    height_bars.plot(cnt, i)

Energy_diff = []
height_Energy = []
for i in range(0,5):
    for j in range(1,6):
        Energy_diff.append(abs(E_array[i]-E_array[j]))
        
for i in range(0, 5):
    for j in range(1, 6):
        height_Energy.append(abs(65*9.8*(h_of_center[i]-h_of_center[j])))

total_E_diff = []
for i in range(0,6):
    total_E_diff.append(height_Energy[i]+Energy_diff[i])
cnt = 0
for i in total_E_diff:
    cnt+=1
    p_bars.plot(cnt, 2*i)
print(total_E_diff)
#print(p_of_trans)
