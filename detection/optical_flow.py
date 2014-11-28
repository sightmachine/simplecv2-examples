import time

from simplecv.api import Camera, Motion


def movement_check(x=0, y=0, t=1):
    directionX = ""
    directionY = ""
    if x > t:
        directionX = "Right"
    if x < - 1 * t:
        directionX = "Left"
    if y < -1 * t:
        directionY = "Up"
    if y > t:
        directionY = "Down"

    direction = directionX + " " + directionY
    if direction is not "":
        return direction
    else:
        return "No Motion"

def main():
    scale_amount = (200, 150)
    cam = Camera(0)
    prev = cam.get_image().resize(scale_amount[0], scale_amount[1])
    time.sleep(0.5)
    t = 0.5
    buffer = 20
    count = 0

    while True:
        current = cam.get_image()
        current = current.resize(scale_amount[0], scale_amount[1])
        if count < buffer:
            count = count + 1
        else:
            fs = current.find(Motion, prev, window=15, method="BM")
            length_of_fs = len(fs)
            if fs:
                dx = 0
                dy = 0
                for f in fs:
                    dx = dx + f.dx
                    dy = dy + f.dy

                dx = dx / length_of_fs
                dy = dy / length_of_fs
                motion_str = movement_check(dx, dy, t)
                current.dl().text(motion_str, (10, 10))

        prev = current
        time.sleep(0.01)
        current.show()


if __name__ == '__main__':
    main()
