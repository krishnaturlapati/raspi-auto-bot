import picamera
import sys


def take_picture():
    try:
        print("Taking picture")
        with picamera.PiCamera() as camera:
            camera.resolution = (1280, 720)
            camera.capture("/home/pi/test.jpg")
        print("Successfuly took picutre")
    except Exception as e:
        print("Failed to take picture" + str(e))
        sys.exit(1)

def main():
    take_picture()

if __name__=="__main__":
   main()
