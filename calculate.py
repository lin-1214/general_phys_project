from body import *
E_array = []
g = 9.8
MOI = []
h_of_center = []
#angle_frequency = dtheta/dt
def moment_of_inertia(dancer):
    center = dancer.center
     #r_leg_1, l_leg_pos, r_arm_pos, l_arm_pos, body_pos, head_pos=dancer.r_leg_1,dancer.r_leg_2
    len_const = 4/3
    mg_leg_1, mg_leg_2, mg_arm_1, mg_arm_2, mg_head, mg_body = 7,  1, 1.5, 0.5,  5, 40 
    I = len_const**2*(1/2*(mg_leg_1*abs(center.x-dancer.l_leg_1.pos.x)**2)+1/2*(mg_leg_2*abs(center.x-dancer.l_leg_2.pos.x)**2)\
        +1/2*(mg_leg_1*abs(center.x-dancer.r_leg_1.pos.x)**2)+1/2*(mg_leg_2*abs(center.x-dancer.r_leg_2.pos.x)**2)\
        +1/2*(mg_arm_1*abs(center.x-dancer.l_arm_1.pos.x)**2)+1/2*(mg_arm_2*abs(center.x-dancer.l_arm_2.pos.x)**2)\
        +1/2*(mg_arm_1*abs(center.x-dancer.r_arm_1.pos.x)**2)+1/2*(mg_arm_2*abs(center.x-dancer.r_arm_2.pos.x)**2)\
        +1/2*(mg_head*abs(center.x-dancer.head.pos.x)**2)\
        +1/2*(mg_body*abs(center.x-dancer.body.pos.x)**2))
    MOI.append(I)
    print("moment of inertia", I)
    return I #0.5mr**2

def rotate_energy(dancer):
    E = moment_of_inertia(dancer)*(dtheta/dt)**2
    print("Energy: ", E)
    E_array.append(E)
    return E
def lever_force(dancer):
        len_const = 4/3
        center = dancer.l_arm_2.pos
        mg_leg_1, mg_leg_2, mg_arm_1, mg_arm_2, mg_head, mg_body = 7, 1, 1.5, 0.5,  5, 40
        leg_torch =  mg_leg_1*abs(dancer.l_leg_1.pos.x-center.x)+mg_leg_2*abs(dancer.l_leg_2.pos.x-center.x)\
                            +mg_leg_1*abs(dancer.r_leg_1.pos.x-center.x)+mg_leg_2*abs(dancer.r_leg_2.pos.x-center.x)
        arm_torch = mg_arm_1*abs(dancer.r_arm_1.pos.x-center.x)+mg_arm_2*abs(dancer.r_arm_2.pos.x-center.x) 
        body_torch = mg_body*abs(dancer.body.pos.x-center.x)
        F_torch = len_const*(leg_torch+arm_torch+body_torch)
        print(center.x-dancer.body.pos.x)
        F = F_torch/abs(dancer.body.pos.x-dancer.l_arm_2.pos.x)/len_const
        print("Lever force", F)
        return F #newton

def gravity_center(dancer):
    mg_leg_1, mg_leg_2, mg_arm_1, mg_arm_2, mg_head, mg_body = 7*g, g, 1.5*g, 0.5*g, 5*g, 40*g
    grav_center = (mg_leg_1*(dancer.l_leg_1.pos+dancer.r_leg_2.pos)+mg_leg_2*(dancer.l_leg_2.pos+dancer.r_leg_2.pos)\
                            +mg_arm_1*(dancer.l_leg_1.pos+dancer.r_leg_1.pos)+mg_arm_2*(dancer.l_leg_2.pos+dancer.r_leg_2.pos)\
                            +mg_body*(dancer.body.pos)+mg_head*(dancer.head.pos))/65/g
    
    h_of_center.append(grav_center.y)
    print("Gravity center:  ",grav_center)
    

#turn_energy = 1/2*moment_of_inertia(ricky)*angle_frequency**2
#print(turn_energy)
    
    
