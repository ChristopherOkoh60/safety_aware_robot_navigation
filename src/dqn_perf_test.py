import FA
import time
import torch
import torch.nn as nn

# =========================
# INITIALIZE ROBOT
# =========================
fa = FA.Create()
fa.ComOpen(15)

THRESHOLD = 500

# =========================
# DQN MODEL (SAME AS TRAINING)
# =========================
class DQN(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(2, 64),   # sensor + step
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 4)
        )

    def forward(self, x):
        return self.net(x)

model = DQN()
model.load_state_dict(torch.load("dqn_perfect_model.pth"))
model.eval()

# =========================
# ROBOT CONTROL FUNCTIONS
# =========================
def move(l, r):
    fa.SetMotors(l, r)

def stop():
    move(0, 0)

def read_sensor():
    return fa.ReadIR(2)

# =========================
# TEST PARAMETERS
# =========================
step = 0
MAX_STEPS = 200   # enough to complete rectangle

print("🤖 Rectangle-aware DQN started...")

try:
    while step < MAX_STEPS:

        sensor = read_sensor()

        # =========================
        # NORMALIZE INPUT (same as training)
        # =========================
        sensor_norm = sensor / 4095.0
        step_norm = step / MAX_STEPS

        state = torch.tensor([[sensor_norm, step_norm]], dtype=torch.float32)

        # =========================
        # PREDICT ACTION
        # =========================
        with torch.no_grad():
            action = torch.argmax(model(state)).item()

        print(f"Step: {step}, Sensor: {sensor}, Action: {action}")

        # =========================
        # EXECUTE ACTION
        # =========================
        if action == 0:
            move(20, 20)   # forward

        elif action == 1:
            move(30, 0)    # right

        elif action == 2:
            move(0, 30)    # left

        elif action == 3:
            stop()         # stop

        # =========================
        # SAFETY OVERRIDE (OBSTACLE)
        # =========================
        if sensor > THRESHOLD:
            print("⚠️ Obstacle detected! Stopping...")
            stop()
            time.sleep(1)

        step += 1
        time.sleep(0.1)

    print("✅ Rectangle path completed")

# =========================
# SAFE SHUTDOWN
# =========================
except KeyboardInterrupt:
    print("🛑 Interrupted by user")

finally:
    stop()
    print("✅ Robot safely stopped")