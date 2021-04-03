# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below: 
def f_to_c(f_temp):
  c_temp = (f_temp - 32) *(5/9)
  return c_temp

print(f_to_c(100))

def c_to_f(c_temp):
  f_temp = (c_temp* (9/5)) + 32
  return f_temp

print(c_to_f(1))

def get_force(mass, accel):
  return mass*accel

print("The GE train supplies " + str(get_force(train_mass, train_acceleration)) + " Newtons of force")

def get_energy(mass, c = (3*10**8)):
  return mass*c
bomb_energy = str(get_energy(bomb_mass))
print("A 1kg bomb supplies " + bomb_energy + " Joules" )

def get_work(mass, accel, dist):
  force = get_force(mass, accel)
  return force*dist

train_work = str(get_work(train_mass, train_acceleration, train_distance))

print("The GE train does " + train_work + " Joules of work over", train_distance, "meters")
