import asyncio
class RobotSensor:
    async def read_temperature(self):
        await asyncio.sleep(0.1)  # Sensor delay
        return 37.2
    
    async def read_pressure(self):
        await asyncio.sleep(0.15)
        return 1013

async def robot_monitoring():
    sensor = RobotSensor()
    
    # BAD: Sequential = slow
    # temp = await sensor.read_temperature()
    # pressure = await sensor.read_pressure()
    
    # GOOD: Parallel = 100Hz monitoring
    while True:
        temp, pressure = await asyncio.gather(
            sensor.read_temperature(),
            sensor.read_pressure()
        )
        print(f"Temp: {temp}, Pressure: {pressure}")
        await asyncio.sleep(0.01)  # 100Hz
