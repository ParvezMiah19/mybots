import pyrosim.pyrosim as pyrosim

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Ground", pos=[0, 0, 0], size=[10, 10, 0.5])  # Adding a ground plane for better visualization
    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[1, 1, 1])
    pyrosim.Send_Cube(name="BackLeg", pos=[-1, 0, 0.5], size=[1, 1, 1])
    pyrosim.Send_Cube(name="FrontLeg", pos=[1, 0, 0.5], size=[1, 1, 1])
    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[-0.5, 0, 0.5])
    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[0.5, 0, 0.5])
    pyrosim.End()

Create_World()
Create_Robot()
