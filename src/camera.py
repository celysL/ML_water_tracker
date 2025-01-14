import cv2

class Camera:
    def __init__(self, video_source=0):
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)

        # Set resolution to 640x480 or another suitable resolution
        self.vid.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    def get_frame(self):
        if self.vid and self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (False, None)

    def release(self):
        """Release the camera resource."""
        if self.vid and self.vid.isOpened():
            self.vid.release()  # Properly release the camera
            self.vid = None  # Ensure the object is reset

    def __del__(self):
        """Destructor to release resources if not already done."""
        self.release()
