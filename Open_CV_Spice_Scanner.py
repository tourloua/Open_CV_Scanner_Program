import cv2
import time
from playsound import playsound

# An object called "camera" is used with the CV2 library
camera = cv2.VideoCapture(-1)

# Notify the user that the scanner is on
playsound('/home/alexandros/Downloads/Scanner_Activated.mp3')

# QR code detection method
detector = cv2.QRCodeDetector()
last_contact = int(time.time())

# This makes the camera constantly scan for QR codes
while True:
    # This finds the image
    _, img = camera.read()

    try:
        # This makes a box around our QR code and uses the pre-built libraries to retrieve the information for the QR code
        data, bbox, _ = detector.detectAndDecode(img)
    except:
        _, img = camera.read()
        data, bbox, _ = detector.detectAndDecode(img)#resets the code if we run into the elusive bounding box error

    if bbox is not None:
        if data:
            if int(time.time()) % 3 == 0:#gives the device enough time to read each spice
                print(f"This QR code reads: {data}")
                if data == "1":
                    playsound('/home/alexandros/Downloads/1_salt.mp3')#change this to your audio file path
                    last_contact = int(time.time())
                elif data == "2":
                    playsound('/home/alexandros/Downloads/2_Black_Pepper.mp3')
                    last_contact = int(time.time())
                elif data == "3":
                    playsound('/home/alexandros/Downloads/3_Garlic_Powder.mp3')
                    last_contact = int(time.time())
                elif data == "4":
                    playsound('/home/alexandros/Downloads/4_Chili_Powder.mp3')
                    last_contact = int(time.time())
                elif data == "5":
                    playsound('/home/alexandros/Downloads/5_Onion_Powder.mp3')
                    last_contact = int(time.time())
                elif data == "6":
                    playsound('/home/alexandros/Downloads/6_Cinnamon.mp3')
                    last_contact = int(time.time())
                elif data == "7":
                    playsound('/home/alexandros/Downloads/7_Oregano.mp3')
                    last_contact = int(time.time())
                elif data == "8":
                    playsound('/home/alexandros/Downloads/8_Bay_Leaves.mp3')
                    last_contact = int(time.time())
                elif data == "9":
                    playsound('/home/alexandros/Downloads/9_Cumin.mp3')
                    last_contact = int(time.time())
                elif data == "10":
                    playsound('/home/alexandros/Downloads/10_Sage.mp3')
                    last_contact = int(time.time())
                elif data == "11":
                    playsound('/home/alexandros/Downloads/11_Montreal_Steak_Seasoning.mp3')
                    last_contact = int(time.time())
                elif data == "12":
                    playsound('/home/alexandros/Downloads/12_Cloves.mp3')
                    last_contact = int(time.time())
                elif data == "13":
                    playsound('/home/alexandros/Downloads/13_Nutmeg.mp3')
                    last_contact = int(time.time())
                elif data == "14":
                    playsound('/home/alexandros/Downloads/14_Ginger.mp3')
                    last_contact = int(time.time())
                elif data == "15":
                    playsound('/home/alexandros/Downloads/15_Paprika.mp3')
                    last_contact = int(time.time())

            time.sleep(0.9)  # Prevents multiple outputs per second
#0.9 seconds was experimentally determined to be the optimal wait time
    # Remind the user that the scanner is still running after 1 minute of inactivity
    if int(time.time()) - last_contact == 60:
        playsound('/home/alexandros/Downloads/still_running.mp3')
        last_contact = int(time.time())

    # Refresh camera output
    _, img = camera.read()
    data, bbox, _ = detector.detectAndDecode(img)

    # Break the loop when 'x' is pressed
    if cv2.waitKey(1) == ord('x'):
        break

camera.release()
cv2.destroyAllWindows()
