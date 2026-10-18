import FA
import time
import csv

fa = FA.Create()
fa.ComOpen(15)

FORWARD_SPEED = 20
TURN_SPEED = 20

LONG = 60     # steps
SHORT = 30
TURN_STEPS = 3

THRESHOLD = 500

def move(l, r):
    fa.SetMotors(l, r)

def stop():
    move(0, 0)

def read_sensor():
    return fa.ReadIR(2)

file = open("perfect_data.csv", "w", newline="")
writer = csv.writer(file)
writer.writerow(["sensor", "step", "action", "reward", "next_sensor", "next_step"])

print("📊 Collecting PERFECT dataset...")

step = 0

# Rectangle pattern
pattern = [
    ("forward", LONG),
    ("turn", TURN_STEPS),
    ("forward", SHORT),
    ("turn", TURN_STEPS),
    ("forward", LONG),
    ("turn", TURN_STEPS),
    ("forward", SHORT),
    ("turn", TURN_STEPS),
]

for action_type, duration in pattern:

    for _ in range(duration):

        sensor = read_sensor()

        # ======================
        # ACTION SELECTION
        # ======================
        if sensor > THRESHOLD:
            action = 3
            reward = -10
            stop()

        elif action_type == "forward":
            action = 0
            reward = +1
            move(FORWARD_SPEED, FORWARD_SPEED)

        else:
            action = 1  # turn right
            reward = +2
            move(25, 15)

        
            reward = -1
            move(15, 25)

        next_sensor = read_sensor()
        next_step = step + 1

        # completion bonus
        if step == sum([p[1] for p in pattern]) - 1:
            reward = +5

        writer.writerow([sensor, step, action, reward, next_sensor, next_step])

        step += 1
        time.sleep(0.1)

stop()
file.close()

print("✅ Perfect dataset generated")