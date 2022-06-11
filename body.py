from vpython import *

scene = canvas(width = 1200, height =800, center=vec(0, 0, 0), background=vec(0.5,0.5,0)) 
#---------調整速度-----------
dt = 0.1
dtheta = -0.5
#---------------------------

class dancer:
	def __init__(self, center):
		self.center=center
		self.head = sphere (pos = vec(center), radius = 0.1, color=color.white)	# 頭
		self.body = box(pos = vec(center)+vec(0, 0.35, 0), length=0.18, height=0.5, width=0.18, color=color.black) # 身體
		#-------------關節位置-------------------
		self.rA_joint_1 = vec(center)+vec(0.08, 0.15, 0)
		self.lA_joint_1 = vec(center)+vec(-0.08, 0.15, 0)
		self.rL_joint_1 = vec(center)+vec(0.08, 0.55, 0)
		self.lL_joint_1 = vec(center)+vec(-0.08, 0.55, 0)
		self.rA_joint_2 = vec(center)+vec(0.08, 0.3, 0)
		self.lA_joint_2 = vec(center)+vec(-0.08, 0.3, 0)
		self.rL_joint_2 = vec(center)+vec(0.08, 0.7, 0)
		self.lL_joint_2 = vec(center)+vec(-0.08, 0.7, 0)
		#-----------------------------------------
		#------------手＆腳 (左右大小手臂&腳)（1是大手臂）-----------
		self.r_arm_1 = box(pos = vec(0, 0.15/2, 0)+vec(self.rA_joint_1), length=0.06, height=0.15, width=0.06, color=color.black)
		self.r_arm_2 = box(pos = vec(0, 0.15*1.5, 0)+vec(self.rA_joint_1), length=0.06, height=0.15, width=0.06, color=color.white)
		self.r_hand = sphere(pos = vec(0, 0.3+0.04, 0)+vec(self.rA_joint_1), radius = 0.04, color=color.white)

		self.l_arm_1 = box(pos = vec(0, 0.15/2, 0)+vec(self.lA_joint_1), length=0.06, height=0.15, width=0.06, color=color.black)
		self.l_arm_2 = box(pos = vec(0, 0.15*1.5, 0)+vec(self.lA_joint_1), length=0.06, height=0.15, width=0.06, color=color.white)
		self.l_hand = sphere(pos = vec(0, 0.3+0.04, 0)+vec(self.lA_joint_1), radius = 0.04, color=color.white)

		self.r_leg_1 = box(pos = vec(0, 0.15/2, 0)+vec(self.rL_joint_1), length=0.06, height=0.15, width=0.06, color=vec(0.478, 0.388, 0.204))
		self.r_leg_2 = box(pos = vec(0, 0.15/2, 0)+vec(self.rL_joint_2), length=0.06, height=0.15, width=0.06, color=color.white)

		self.l_leg_1 = box(pos = vec(0, 0.15/2, 0)+vec(self.lL_joint_1), length=0.06, height=0.15, width=0.06, color=vec(0.478, 0.388, 0.204))
		self.l_leg_2 = box(pos = vec(0, 0.15/2, 0)+vec(self.lL_joint_2), length=0.06, height=0.15, width=0.06, color=color.white)
		#--------------------------------------------------------
	def move(self, obj, angle):		# obj:身體部位  angle: use radian
		dt = 0.1
		dtheta = -0.5
		change_sine = False
		if angle < 0:	# if 角度為負
			change_sine = True
			dtheta = -dtheta
		if obj=='r_arm_1':
			theta = 0
			while(abs(theta) <= abs(angle)):
				rate(100)
				theta += dt*dtheta
				self.r_arm_1.rotate(axis=vec(0, 0, 1), angle=dt*dtheta, origin=vec(self.rA_joint_1))
				self.r_arm_2.rotate(axis=vec(0, 0, 1), angle=dt*dtheta, origin=vec(self.rA_joint_1))
				self.rA_joint_2 = vec(self.r_arm_1.pos)+ 1.25*vec(-self.r_arm_1.axis.y, self.r_arm_1.axis.x, 0)
				self.r_arm_2.pos = vec(self.rA_joint_2) + 1.25*vec(-self.r_arm_2.axis.y, self.r_arm_2.axis.x, 0)
				self.r_hand.pos = vec(self.rA_joint_2) + 2.52*vec(-self.r_arm_2.axis.y, self.r_arm_2.axis.x, 0)
		elif obj=='l_arm_1':
			theta = 0
			while(abs(theta) <= abs(angle)):
				rate(100)
				theta += dt*dtheta
				self.l_arm_1.rotate(axis=vec(0, 0, 1), angle=-dt*dtheta, origin=vec(self.lA_joint_1))
				self.l_arm_2.rotate(axis=vec(0, 0, 1), angle=-dt*dtheta, origin=vec(self.lA_joint_1))
				self.lA_joint_2 = vec(self.l_arm_1.pos)+ 1.25*vec(-self.l_arm_1.axis.y, self.l_arm_1.axis.x, 0)
				self.l_arm_2.pos = vec(self.lA_joint_2) + 1.25*vec(-self.l_arm_2.axis.y, self.l_arm_2.axis.x, 0)
				self.l_hand.pos = vec(self.lA_joint_2) + 2.52*vec(-self.l_arm_2.axis.y, self.l_arm_2.axis.x, 0)

		elif obj=='r_leg_1':
			theta = 0
			while(abs(theta) <= abs(angle)):
				rate(100)
				theta += dt*dtheta
				self.r_leg_1.rotate(axis=vec(0, 0, 1), angle=dt*dtheta, origin=vec(self.rL_joint_1))
				self.r_leg_2.rotate(axis=vec(0, 0, 1), angle=dt*dtheta, origin=vec(self.rL_joint_1))
				self.rL_joint_2 = vec(self.r_leg_1.pos)+ 1.25*vec(-self.r_leg_1.axis.y, self.r_leg_1.axis.x, 0)
				self.r_leg_2.pos = vec(self.rL_joint_2) + 1.25*vec(-self.r_leg_2.axis.y, self.r_leg_2.axis.x, 0)
		elif obj=='l_leg_1':
			theta = 0
			while(abs(theta) <= abs(angle)):
				rate(100)
				theta += dt*dtheta
				self.l_leg_1.rotate(axis=vec(0, 0, 1), angle=-dt*dtheta, origin=vec(self.lL_joint_1))
				self.l_leg_2.rotate(axis=vec(0, 0, 1), angle=-dt*dtheta, origin=vec(self.lL_joint_1))
				self.lL_joint_2 = vec(self.l_leg_1.pos)+ 1.25*vec(-self.l_leg_1.axis.y, self.l_leg_1.axis.x, 0)
				self.l_leg_2.pos = vec(self.lL_joint_2) + 1.25*vec(-self.l_leg_2.axis.y, self.l_leg_2.axis.x, 0)
		elif obj=='r_arm_2':
			theta = 0
			while(abs(theta) <= abs(angle)):
				rate(100)
				theta += dt*dtheta
				self.r_arm_2.rotate(axis=vec(0, 0, 1), angle=dt*dtheta, origin=vec(self.rA_joint_2))
				self.r_arm_2.pos = vec(self.rA_joint_2) + 1.25*vec(-self.r_arm_2.axis.y, self.r_arm_2.axis.x, 0)
				self.r_hand.pos = vec(self.rA_joint_2) + 2.52*vec(-self.r_arm_2.axis.y, self.r_arm_2.axis.x, 0)
		elif obj=='l_arm_2':
			theta = 0
			while(abs(theta) <= abs(angle)):
				rate(100)
				theta += dt*dtheta
				self.l_arm_2.rotate(axis=vec(0, 0, 1), angle=dt*-dtheta, origin=vec(self.lA_joint_2))
				self.l_arm_2.pos = vec(self.lA_joint_2) + 1.25*vec(-self.l_arm_2.axis.y, self.l_arm_2.axis.x, 0)
				self.l_hand.pos = vec(self.lA_joint_2) + 2.52*vec(-self.l_arm_2.axis.y, self.l_arm_2.axis.x, 0)
		elif obj=='r_leg_2':
			theta = 0
			while(abs(theta) <= abs(angle)):
				rate(100)
				theta += dt*dtheta
				self.r_leg_2.rotate(axis=vec(0, 0, 1), angle=dt*dtheta, origin=vec(self.rL_joint_2))
				self.r_leg_2.pos = vec(self.rL_joint_2) + 1.25*vec(-self.r_leg_2.axis.y, self.r_leg_2.axis.x, 0)
		elif obj=='l_leg_2':
			theta = 0
			while(abs(theta) <= abs(angle)):
				rate(100)
				theta += dt*dtheta
				self.l_leg_2.rotate(axis=vec(0, 0, 1), angle=dt*-dtheta, origin=vec(self.lL_joint_2))
				self.l_leg_2.pos = vec(self.lL_joint_2) + 1.25*vec(-self.l_leg_2.axis.y, self.l_leg_2.axis.x, 0)
		elif obj == 'body':
			theta = 0
			dt = 0.045
			while(abs(theta) <= abs(angle)):
				rate(100)
				theta += dt*dtheta
				self.r_arm_1.rotate(axis=vec(0, 0, 1), angle=dt*dtheta, origin=vec(self.center))
				self.r_arm_2.rotate(axis=vec(0, 0, 1), angle=dt*dtheta, origin=vec(self.center))
				self.r_leg_1.rotate(axis=vec(0, 0, 1), angle=dt*dtheta, origin=vec(self.center))
				self.r_leg_2.rotate(axis=vec(0, 0, 1), angle=dt*dtheta, origin=vec(self.center))
				self.l_arm_1.rotate(axis=vec(0, 0, 1), angle=dt*dtheta, origin=vec(self.center))
				self.l_arm_2.rotate(axis=vec(0, 0, 1), angle=dt*dtheta, origin=vec(self.center))
				self.l_leg_1.rotate(axis=vec(0, 0, 1), angle=dt*dtheta, origin=vec(self.center))
				self.l_leg_2.rotate(axis=vec(0, 0, 1), angle=dt*dtheta, origin=vec(self.center))
				self.l_hand.rotate(axis=vec(0, 0, 1), angle=dt*dtheta, origin=vec(self.center))
				self.r_hand.rotate(axis=vec(0, 0, 1), angle=dt*dtheta, origin=vec(self.center))
				self.body.rotate(axis=vec(0, 0, 1), angle=dt*dtheta, origin=vec(self.center))
				self.head.rotate(axis=vec(0, 0, 1), angle=dt*dtheta, origin=vec(self.center))
			self.rA_joint_1 = rotate(self.rA_joint_1-vec(self.center), angle = -angle, axis = vec(0, 0, 1)) +vec(self.center)
			self.lA_joint_1 = rotate(self.lA_joint_1-vec(self.center), angle = -angle, axis = vec(0, 0, 1)) +vec(self.center)
			self.rL_joint_1 = rotate(self.rL_joint_1-vec(self.center), angle = -angle, axis = vec(0, 0, 1)) +vec(self.center)
			self.lL_joint_1 = rotate(self.lL_joint_1-vec(self.center), angle = -angle, axis = vec(0, 0, 1)) +vec(self.center)
			self.rA_joint_2 = rotate(self.rA_joint_2-vec(self.center), angle = -angle, axis = vec(0, 0, 1)) +vec(self.center)
			self.lA_joint_2 = rotate(self.lA_joint_2-vec(self.center), angle = -angle, axis = vec(0, 0, 1)) +vec(self.center)
			self.rL_joint_2 = rotate(self.rL_joint_2-vec(self.center), angle = -angle, axis = vec(0, 0, 1)) +vec(self.center)
			self.lL_joint_2 = rotate(self.lL_joint_2-vec(self.center), angle = -angle, axis = vec(0, 0, 1)) +vec(self.center)
			
		if change_sine==True:
			change_sine = False
			dtheta = -dtheta

		return angle #紀錄角度

	def rotate(self, turns):
		theta = 0
		while(abs(theta)/(2*pi) <= turns):
			theta += dt*dtheta
			rate(250) # 轉速可調
			self.r_arm_1.rotate(axis=vec(0, 1, 0), angle=dt*dtheta, origin=vec(self.center)+vec(0, self.r_arm_1.pos.y, 0))
			self.r_arm_2.rotate(axis=vec(0, 1, 0), angle=dt*dtheta, origin=vec(self.center)+vec(0, self.r_arm_2.pos.y, 0))
			self.r_leg_1.rotate(axis=vec(0, 1, 0), angle=dt*dtheta, origin=vec(self.center)+vec(0, self.r_leg_1.pos.y, 0))
			self.r_leg_2.rotate(axis=vec(0, 1, 0), angle=dt*dtheta, origin=vec(self.center)+vec(0, self.r_leg_2.pos.y, 0))
			self.l_arm_1.rotate(axis=vec(0, 1, 0), angle=dt*dtheta, origin=vec(self.center)+vec(0, self.l_arm_1.pos.y, 0))
			self.l_arm_2.rotate(axis=vec(0, 1, 0), angle=dt*dtheta, origin=vec(self.center)+vec(0, self.l_arm_2.pos.y, 0))
			self.l_leg_1.rotate(axis=vec(0, 1, 0), angle=dt*dtheta, origin=vec(self.center)+vec(0, self.l_leg_1.pos.y, 0))
			self.l_leg_2.rotate(axis=vec(0, 1, 0), angle=dt*dtheta, origin=vec(self.center)+vec(0, self.l_leg_2.pos.y, 0))
			self.l_hand.rotate(axis=vec(0, 1, 0), angle=dt*dtheta, origin=vec(self.center)+vec(0, self.l_hand.pos.y, 0))
			self.r_hand.rotate(axis=vec(0, 1, 0), angle=dt*dtheta, origin=vec(self.center)+vec(0, self.r_hand.pos.y, 0))
			self.body.rotate(axis=vec(0, 1, 0), angle=dt*dtheta, origin=vec(self.center)+vec(0, self.body.pos.y, 0))
			self.head.rotate(axis=vec(0, 1, 0), angle=dt*dtheta, origin=vec(self.center)+vec(0, self.head.pos.y, 0))

'''
johnny = dancer(vec(0.8, 0, 0))		# 傳入頭的座標
ricky = dancer(vec(-0.8, 0, 0))
johnny.move('body', -pi/5)
johnny.move('r_arm_1', pi/4)		# 傳入身體的部位&角度（名稱都可調）
# ricky.move('l_arm_1', pi/4)
johnny.move('r_arm_2',-pi/4)
# ricky.move('l_arm_2', pi/4)
johnny.move('l_arm_1', pi/2)
# ricky.move('r_arm_1', pi/2)
johnny.move('l_arm_2', pi/3)
# ricky.move('r_arm_2', pi/3)
johnny.move('r_leg_1', pi/3)
# ricky.move('r_leg_1', pi/3)
johnny.move('r_leg_2', pi/6)
# ricky.move('r_leg_2', pi/6)
johnny.move('l_leg_1', pi/3)
# ricky.move('l_leg_1', pi/3)
johnny.move('l_leg_2', pi/6)
# ricky.move('l_leg_2', pi/6)
johnny.rotate(5)					# 旋轉的圈數
# ricky.rotate(5)

'''



