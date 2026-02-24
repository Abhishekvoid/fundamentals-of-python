import time
import random

class RobotServoSimulator:
    def __init__(self):
        # Initial states for 4 wheels: [Front-Left, Front-Right, Rear-Left, Rear-Right]
        self.velocities = [0.0, 0.0, 0.0, 0.0] 
        self.accelerations = [0.0, 0.0, 0.0, 0.0]
        self.wheel_names = ["FL", "FR", "RL", "RR"]
        
        # Physics Constants
        self.max_accel = 2.5  # m/s^2
        self.max_brake = -4.0 # m/s^2
        self.friction = 0.05  # Natural slowdown
        
    def update_physics(self, target_accel, noise_level=0.05):
        """Calculates the realistic movement of wheels with slight mechanical variance."""
        for i in range(4):
            # Add a tiny bit of random 'jitter' to simulate real-world motor variance
            jitter = random.uniform(-noise_level, noise_level)
            actual_accel = target_accel + jitter
            
            # Update Velocity: V = u + at
            self.accelerations[i] = actual_accel
            self.velocities[i] += self.accelerations[i]
            
            # Apply friction and limits
            if self.velocities[i] < 0: self.velocities[i] = 0
            
    def run_simulation(self, duration_sec=10):
        print(f"{'Time (s)':<10} | {'Phase':<12} | {'FL Accel':<10} | {'RR Accel':<10} | {'Avg Velocity'}")
        print("-" * 70)
        
        start_time = time.time()
        
        while (time.time() - start_time) < duration_sec:
            elapsed = time.time() - start_time
            
            # Logic for Realistic Movement Phases
            if elapsed < 3:
                phase = "Accelerating"
                cmd_accel = self.max_accel
            elif elapsed < 7:
                phase = "Cruising"
                cmd_accel = 0.0
            else:
                phase = "Braking"
                cmd_accel = self.max_brake
                
            self.update_physics(cmd_accel)
            
            # Print data for the first (FL) and last (RR) wheels to show the variance
            avg_v = sum(self.velocities) / 4
            print(f"{elapsed:10.2f} | {phase:12} | {self.accelerations[0]:10.2f} | {self.accelerations[3]:10.2f} | {avg_v:.2f} m/s")
            
            time.sleep(0.5)

# Initialize and Run
bot = RobotServoSimulator()
bot.run_simulation()