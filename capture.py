import cv2
import os
import time

def capture_image():
    # Initialize the camera
    camera = cv2.VideoCapture(0)  # Use 0 for the default camera

    if not camera.isOpened():
        print("Error: Camera could not be opened.")
        return None

    # Allow the camera to warm up
    time.sleep(2)

    # Capture an image
    ret, frame = camera.read()

    if not ret:
        print("Error: Could not read frame.")
        return None

    # Define the file name and path
    file_name = "sample.jpg"
    file_path = os.path.join(os.getcwd(), file_name)  # Get the full file path

    # Save the captured image
    cv2.imwrite(file_path, frame)
    print(f"Image captured and saved as '{file_name}'.")

    # Print the full path of the saved file
    print(f"File path: {file_path}")

    # Release the camera
    camera.release()

    return file_path

if __name__ == "__main__":
    # Capture the image and get the file path
    image_path = capture_image()
    if image_path:
        print(f"The image is saved at: {image_path}")
