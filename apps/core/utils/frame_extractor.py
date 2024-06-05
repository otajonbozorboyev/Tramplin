import cv2
import os


def extract_frame_from_5th_minute(video_path, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Get the frames per second (fps) and calculate frame index for the 5th minute
    fps = cap.get(cv2.CAP_PROP_FPS)
    start_frame = int(5 * 60 * fps)  # 5 minutes * 60 seconds * fps

    # Set the video capture object to the starting frame
    cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

    # Read and save the frame from the 5th minute to the output folder
    ret, frame = cap.read()
    if ret:
        frame_path = os.path.join(output_folder, "frame_from_5th_minute.png")
        cv2.imwrite(frame_path, frame)

    # Release the video capture object
    cap.release()

# if __name__ == "__main__":
#     video_path = "3012709714450.mp4"
#     output_folder = "images"
#     extract_frame_from_5th_minute(video_path, output_folder)
