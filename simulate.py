import pybullet as p
import pybullet_data
import time
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.8)
planeId = p.loadURDF("plane.urdf")
worldId = p.loadSDF("world.sdf")
robotId = p.loadURDF("body.urdf")
while p.isConnected():
    p.stepSimulation()
    time.sleep(1./240.)
