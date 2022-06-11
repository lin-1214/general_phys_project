from vpython import *
from body import *

r_arm_theta1, r_arm_theta2, r_leg_theta1, r_leg_theta2, l_arm_theta1, l_arm_theta2, l_leg_theta1, l_leg_theta2 = 0,0,0,0,0,0,0,0

def initialize(dancer,r_a1,r_a2,l_a1,l_a2,r_l1,r_l2,l_l1,l_l2):
        global r_arm_theta1, r_arm_theta2, r_leg_theta1, r_leg_theta2, l_arm_theta1, l_arm_theta2, l_leg_theta1, l_leg_theta2
        dancer.move('l_leg_1',-l_l1)
        dancer.move('r_leg_1',-r_l1)
        dancer.move('l_leg_2',-l_l2)
        dancer.move('r_leg_2',-r_l2)
        dancer.move('r_arm_1',-r_a1+3*pi/4)
        dancer.move('r_arm_2',-r_a2+pi/4)
        dancer.move('l_arm_1',-l_a1+3*pi/4)
        dancer.move('l_arm_2',-l_a2+pi/4)
        r_arm_theta1,r_arm_theta2,l_arm_theta1,l_arm_theta2,r_leg_theta1,r_leg_theta2,l_leg_theta1,l_leg_theta2 = 0,0,0,0,0,0,0,0

def headspin(dancer):
        global r_arm_theta1, r_arm_theta2, r_leg_theta1, r_leg_theta2, l_arm_theta1, l_arm_theta2, l_leg_theta1, l_leg_theta2
        r_arm_theta1 += dancer.move('r_arm_1',3*pi/4)
        l_arm_theta1 += dancer.move('l_arm_1',3*pi/4)
        r_arm_theta2 += dancer.move('r_arm_2',pi/4)
        l_arm_theta2 += dancer.move('l_arm_2',pi/4)
        r_leg_theta1 += dancer.move('r_leg_1',2*pi/5)
        l_leg_theta1 += dancer.move('l_leg_1',2*pi/5)
        dancer.rotate(1)
        r_leg_theta2 += dancer.move('r_leg_2',-3*pi/5)
        dancer.rotate(2)
        r_arm_theta1 += dancer.move('r_arm_1',-pi/4)
        r_arm_theta2 += dancer.move('r_arm_2',-pi/4)
        dancer.rotate(2)
        l_arm_theta1 += dancer.move('l_arm_1',-pi/4)
        l_arm_theta2 += dancer.move('l_arm_2',-pi/4)
        dancer.rotate(3)
        r_leg_theta2 += dancer.move('r_leg_2',2*pi/7)
        r_leg_theta1 += dancer.move('r_leg_1',-pi/7)
        l_leg_theta1 += dancer.move('l_leg_1',-pi/5)
        l_leg_theta2 += dancer.move('l_leg_2',-pi/4)
        dancer.rotate(7)
        



johnny = dancer(vec(0.8, 0, 0))		# 傳入頭的座標
ricky = dancer(vec(-0.8, 0, 0))
headspin(ricky)
initialize(ricky,r_arm_theta1,r_arm_theta2,l_arm_theta1,l_arm_theta2,r_leg_theta1,r_leg_theta2,l_leg_theta1,l_leg_theta2)





