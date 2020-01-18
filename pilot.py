'''
Рисует полет противника по заданным траекториям
'''


from Content import Content
from Enemy_1 import Enemy_1
from Conduct import Conduct
from LineMovement import LineMovement
from Trajectory import Trajectory


def getPilotContent(pygame, gameDisplay, gameParams):
    enemy = Enemy_1(pygame, gameDisplay, gameParams)
    lineM = LineMovement(90, 300)
    lineM2 = LineMovement(45, 300)
    lineM3 = LineMovement(270, 300)
    lineM4 = LineMovement(0, 300)
    movements = []
    movements.append(lineM)
    movements.append(lineM2)
    movements.append(lineM3)
    movements.append(lineM4)
    trajectory = Trajectory(gameParams, movements, (gameParams.getWidth() // 2,-50), incr=3)
    trajectories = []
    trajectories.append(trajectory)
    conduct = Conduct(trajectories)
    content = Content(enemy, conduct, 5)
    contents = []
    contents.append(content)
    return contents
