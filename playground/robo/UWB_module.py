import time
import math
import random

class UWBRobotSystem:
    def __init__(self):
        # Positions in 2D space (x, y)
        self.master_pos = [0.0, 10.0]  # Master starts 10m ahead
        self.robot_pos = [0.0, 0.0]    # Robot starts at origin
        
        # 4 Tags: 1 Master (Remote), 3 Slaves (On Robot: Left, Center, Right)
        self.slaves_offset = [(-0.5, 0), (0, 0), (0.5, 0)] # Local offsets on robot
        
        self.velocity = 0.0
        self.max_speed = 5.0  # m/s
        self.follow_dist = 2.0 # Target distance to keep from Master

    def get_uwb_ranges(self):
        """Mimics UWB distance pinging from 3 Slaves to 1 Master."""
        ranges = []
        for offset in self.slaves_offset:
            # Calculate actual distance with UWB noise (approx +/- 10cm accuracy)
            actual_x = self.robot_pos[0] + offset[0]
            actual_y = self.robot_pos[1] + offset[1]
            
            dist = math.sqrt((self.master_pos[0] - actual_x)**2 + 
                             (self.master_pos[1] - actual_y)**2)
            
            # Add UWB signal noise/jitter
            noisy_dist = dist + random.uniform(-0.1, 0.1)
            ranges.append(noisy_dist)
        return ranges

    def update_master_movement(self, t):
        """Simulates the person/master moving away and slowing down."""
        # Master moves forward but varies speed
        speed = 1.5 + math.sin(t * 0.5) # Oscillates speed
        self.master_pos[1] += speed * 0.1 

    def calculate_motor_response(self, ranges):
        """Simple P-Controller to mimic robot response based on UWB data."""
        avg_range = sum(ranges) / len(ranges)
        error = avg_range - self.follow_dist
        
        # Acceleration logic
        if error > 0.5:
            accel = 1.5  # Catch up
        elif error < -0.5:
            accel = -3.0 # Brake (don't hit the master!)
        else:
            accel = 0.0  # Maintain
            
        return accel

    def run(self, iterations=20):
        print(f"{'Time':<5} | {'Master Y':<10} | {'Robot Y':<10} | {'Avg Range':<10} | {'Status'}")
        print("-" * 60)
        
        for i in range(iterations):
            t = i * 0.5
            self.update_master_movement(t)
            
            ranges = self.get_uwb_ranges()
            accel = self.calculate_motor_response(ranges)
            
            # Update robot physics
            self.velocity += accel * 0.5
            self.velocity = max(0, min(self.velocity, self.max_speed))
            self.robot_pos[1] += self.velocity * 0.5
            
            status = "FAST" if accel > 0 else "BRAKING" if accel < 0 else "STABLE"
            
            print(f"{t:<5.1f} | {self.master_pos[1]:<10.2f} | {self.robot_pos[1]:<10.2f} | {sum(ranges)/3:<10.2f} | {status}")
            time.sleep(0.1)

# Run Simulation
sim = UWBRobotSystem()
sim.run()