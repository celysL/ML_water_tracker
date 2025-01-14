import cv2

def main():
    cap = cv2.VideoCapture(0)  # Open the default camera
    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    while True:
        ret, frame = cap.read()  # Capture frame-by-frame
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        cv2.imshow('Frame', frame)  # Display the resulting frame

        if cv2.waitKey(1) == ord('q'):  # Press 'q' to quit
            break

    cap.release()  # When everything done, release the capture
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
