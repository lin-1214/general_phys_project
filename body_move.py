from vpython import *
from body import *
import time
from calculate import *
r_arm_theta1, r_arm_theta2, r_leg_theta1, r_leg_theta2, l_arm_theta1, l_arm_theta2, l_leg_theta1, l_leg_theta2, b_theta = 0,0,0,0,0,0,0,0,0

#使舞者回復初始動作
def initialize(dancer,r_a1,r_a2,l_a1,l_a2,r_l1,r_l2,l_l1,l_l2,b):
        global r_arm_theta1, r_arm_theta2, r_leg_theta1, r_leg_theta2, l_arm_theta1, l_arm_theta2, l_leg_theta1, l_leg_theta2, b_theta
        dancer.move('l_leg_1',-l_l1)
        dancer.move('r_leg_1',-r_l1)
        dancer.move('l_leg_2',-l_l2)
        dancer.move('r_leg_2',-r_l2)
        dancer.move('r_arm_1',-r_a1)
        dancer.move('r_arm_2',-r_a2)
        dancer.move('l_arm_1',-l_a1)
        dancer.move('l_arm_2',-l_a2)
        dancer.move('body',-b)
        r_arm_theta1,r_arm_theta2,l_arm_theta1,l_arm_theta2,r_leg_theta1,r_leg_theta2,l_leg_theta1,l_leg_theta2,b_theta = 0,0,0,0,0,0,0,0,0
        

def headSpin(dancer):
        global r_arm_theta1, r_arm_theta2, r_leg_theta1, r_leg_theta2, l_arm_theta1, l_arm_theta2, l_leg_theta1, l_leg_theta2, b_theta
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
        rotate_energy(dancer)
        gravity_center(dancer)
        dancer.rotate(7)
        initialize(dancer,r_arm_theta1, r_arm_theta2, l_arm_theta1, l_arm_theta2, r_leg_theta1, r_leg_theta2, l_leg_theta1, l_leg_theta2, b_theta)
        
def handSpin(dancer):
        global r_arm_theta1, r_arm_theta2, r_leg_theta1, r_leg_theta2, l_arm_theta1, l_arm_theta2, l_leg_theta1, l_leg_theta2, b_theta
        r_arm_theta1 += dancer.move('r_arm_1',pi/8)
        l_arm_theta1 += dancer.move('l_arm_1',pi/8)
        r_leg_theta1 += dancer.move('r_leg_1',-pi/16)
        l_leg_theta1 += dancer.move('l_leg_1',-pi/16)
        rotate_energy(dancer)
        gravity_center(dancer)
        dancer.rotate(7)
        initialize(dancer,r_arm_theta1, r_arm_theta2, l_arm_theta1, l_arm_theta2, r_leg_theta1, r_leg_theta2, l_leg_theta1, l_leg_theta2,b_theta)

def ice(dancer):
        global r_arm_theta1, r_arm_theta2, r_leg_theta1, r_leg_theta2, l_arm_theta1, l_arm_theta2, l_leg_theta1, l_leg_theta2, b_theta
        r_arm_theta1 += dancer.move('r_arm_1',pi/7)
        l_arm_theta2 += dancer.move('l_arm_2',-pi/4)
        l_arm_theta1 += dancer.move('l_arm_1',-pi/4)
        b_theta += dancer.move('body',pi/7)
        r_leg_theta1 += dancer.move('r_leg_1',pi/4)
        l_leg_theta1 += dancer.move('l_leg_1',pi/4)
        r_leg_theta2 += dancer.move('r_leg_2',-pi/4)
        rotate_energy(dancer)
        gravity_center(dancer)
        lever_force(dancer) 
        time.sleep(2) #定格
        initialize(dancer,r_arm_theta1, r_arm_theta2, l_arm_theta1, l_arm_theta2, r_leg_theta1, r_leg_theta2, l_leg_theta1, l_leg_theta2, b_theta)

def airChair(dancer):
        global r_arm_theta1, r_arm_theta2, r_leg_theta1, r_leg_theta2, l_arm_theta1, l_arm_theta2, l_leg_theta1, l_leg_theta2, b_theta
        r_arm_theta1 += dancer.move('r_arm_1',-pi/4)
        b_theta += dancer.move('body',2*pi/5)
        r_arm_theta2 += dancer.move('r_arm_2',pi/4)
        l_arm_theta2 += dancer.move('l_arm_2',-pi/6)
        l_arm_theta1 += dancer.move('l_arm_1',-2*pi/3)
        l_leg_theta1 += dancer.move('l_leg_1',2*pi/5)
        r_leg_theta1 += dancer.move('r_leg_1',pi/5)
        r_leg_theta2 += dancer.move('r_leg_2',-3*pi/4)
        rotate_energy(dancer)
        gravity_center(dancer)
        lever_force(dancer)
        time.sleep(2)  #定格
        initialize(dancer,r_arm_theta1, r_arm_theta2, l_arm_theta1, l_arm_theta2, r_leg_theta1, r_leg_theta2, l_leg_theta1, l_leg_theta2, b_theta)



def windMill(dancer):
        global r_arm_theta1, r_arm_theta2, r_leg_theta1, r_leg_theta2, l_arm_theta1, l_arm_theta2, l_leg_theta1, l_leg_theta2, b_theta
        
        r_arm_theta1 += dancer.move('r_arm_1',-pi/4)
        b_theta += dancer.move('body',2*pi/5)
        r_arm_theta2 += dancer.move('r_arm_2',pi/4)
        l_arm_theta2 += dancer.move('l_arm_2',-pi/3)
        l_arm_theta1 += dancer.move('l_arm_1',-3*pi/2)
        r_leg_theta1 += dancer.move('r_leg_1',pi/5)
        l_leg_theta1 += dancer.move('l_leg_1',pi/5)
        moment_of_inertia(dancer)
        rotate_energy(dancer)

        gravity_center(dancer)
        
        for i in range(2):
                dancer.rotate(5)
                l_arm_theta2 += dancer.move('l_arm_2',2*pi/3)
                l_arm_theta1 += dancer.move('l_arm_1',3*pi/4)
                r_arm_theta1 += dancer.move('r_arm_1',-2*pi/3)
                r_arm_theta2 += dancer.move('r_arm_2',-pi)
                r_leg_theta1 += dancer.move('r_leg_1',-pi/5)
                l_leg_theta2 += dancer.move('l_leg_2',-pi/5)
                r_leg_theta2 += dancer.move('r_leg_2',-pi/5)
                b_theta += dancer.move('body',pi/10)
                dancer.rotate(5)
                b_theta += dancer.move('body',-pi/10)
                r_leg_theta2 += dancer.move('r_leg_2',+pi/5)
                l_leg_theta2 += dancer.move('l_leg_2',+pi/5)
                r_leg_theta1 += dancer.move('r_leg_1',+pi/5)
                r_arm_theta2 += dancer.move('r_arm_2',pi)
                r_arm_theta1 += dancer.move('r_arm_1',2*pi/3)
                l_arm_theta1 += dancer.move('l_arm_1',-3*pi/4)
                l_arm_theta2 += dancer.move('l_arm_2',-2*pi/3)
                
        initialize(dancer,r_arm_theta1, r_arm_theta2, l_arm_theta1, l_arm_theta2, r_leg_theta1, r_leg_theta2, l_leg_theta1, l_leg_theta2, b_theta)

def elbow(dancer):
        global r_arm_theta1, r_arm_theta2, r_leg_theta1, r_leg_theta2, l_arm_theta1, l_arm_theta2, l_leg_theta1, l_leg_theta2, b_theta
        r_arm_theta1 += dancer.move('r_arm_1',pi/10)
        r_arm_theta2 += dancer.move('r_arm_2',pi/10)
        b_theta += dancer.move('body',pi/10)
        l_arm_theta1 += dancer.move('l_arm_1',pi/10)
        l_arm_theta2 += dancer.move('l_arm_2',-pi/10)
        l_leg_theta1 += dancer.move('l_leg_1',pi/2)
        r_leg_theta1 += dancer.move('r_leg_1',pi/10)
        r_leg_theta2 += dancer.move('r_leg_2',pi/3)
        rotate_energy(dancer)
        gravity_center(dancer)
        time.sleep(2)
        initialize(dancer,r_arm_theta1, r_arm_theta2, l_arm_theta1, l_arm_theta2, r_leg_theta1, r_leg_theta2, l_leg_theta1, l_leg_theta2, b_theta)
        
#應該可以做為編舞範例
# ricky = dancer(vec(-.8, 0, 0))
# #使呈用手撐地狀態
# ricky.move('r_arm_1',3*pi/4)
# ricky.move('l_arm_1',3*pi/4)
# ricky.move('r_arm_2',pi/4)
# ricky.move('l_arm_2',pi/4)
# #動作演示
# #headSpin(ricky)
# #time.sleep(1)
# #ice(ricky)
# #handSpin(ricky)
# #time.sleep(1)
# #airChair(ricky)
# headSpin(ricky)
# ice(ricky)
# handSpin(ricky)
# airChair(ricky)
# windMill(ricky)
# elbow(ricky)





