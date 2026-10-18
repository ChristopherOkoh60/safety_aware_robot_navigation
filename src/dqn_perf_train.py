import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
import numpy as np

# =========================
# LOAD DATASET
# =========================
data = pd.read_csv("perfect_data.csv")

states = torch.tensor(data[["sensor", "step"]].values, dtype=torch.float32)
actions = torch.tensor(data["action"].values, dtype=torch.long)
rewards = torch.tensor(data["reward"].values, dtype=torch.float32)
next_states = torch.tensor(data[["next_sensor", "next_step"]].values, dtype=torch.float32)

# =========================
# NORMALIZATION (VERY IMPORTANT)
# =========================
states[:, 0] /= 4095.0
next_states[:, 0] /= 4095.0

states[:, 1] /= states[:, 1].max()
next_states[:, 1] /= next_states[:, 1].max()

# =========================
# DQN MODEL
# =========================
class DQN(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(2, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 4)  # 4 actions
        )

    def forward(self, x):
        return self.net(x)

model = DQN()
target_model = DQN()
target_model.load_state_dict(model.state_dict())

# =========================
# TRAINING SETUP
# =========================
optimizer = optim.Adam(model.parameters(), lr=0.001)
loss_fn = nn.MSELoss()

gamma = 0.9
EPOCHS = 100

# =========================
# TRAINING LOOP
# =========================
for epoch in range(EPOCHS):

    # Forward pass
    q_values = model(states)

    # Q(s,a)
    q_selected = q_values.gather(1, actions.unsqueeze(1)).squeeze()

    # Q(s',a')
    with torch.no_grad():
        next_q_values = target_model(next_states)
        max_next_q = torch.max(next_q_values, dim=1)[0]

    # Bellman target
    target = rewards + gamma * max_next_q

    # Loss
    loss = loss_fn(q_selected, target)

    # Backprop
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    # Update target network
    if epoch % 10 == 0:
        target_model.load_state_dict(model.state_dict())

    print(f"Epoch {epoch+1}: Loss = {loss.item():.4f}")

# =========================
# SAVE MODEL
# =========================
torch.save(model.state_dict(), "dqn_perfect_model.pth")

print("✅ DQN training complete and model saved")