"""Basic Video Processing methods."""
import os
import cv2


# Replace ID1 and ID2 with your IDs.
ID1 = '308345891'
ID2 = '987654321'

INPUT_VIDEO = 'atrium.avi'
GRAYSCALE_VIDEO = f'{ID1}_{ID2}_atrium_grayscale.avi'
BLACK_AND_WHITE_VIDEO = f'{ID1}_{ID2}_atrium_black_and_white.avi'
SOBEL_VIDEO = f'{ID1}_{ID2}_atrium_sobel.avi'


def get_video_parameters(capture: cv2.VideoCapture) -> dict:
    """Get an OpenCV capture object and extract its parameters.
    Args:
        capture: cv2.VideoCapture object. The input video's VideoCapture.
    Returns:
        parameters: dict. A dictionary of parameters names to their values.
    """
    fourcc = int(capture.get(cv2.CAP_PROP_FOURCC))
    fps = int(capture.get(cv2.CAP_PROP_FPS))
    height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    parameters = {"fourcc": fourcc, "fps": fps, "height": height, "width": width}
    return parameters


def convert_video_to_grayscale(input_video_path: str,
                               output_video_path: str) -> None:
    """Convert the video in the input path to grayscale.

    Use VideoCapture from OpenCV to open the video and read its
    parameters using the capture's get method.
    Open an output video using OpenCV's VideoWriter.
    Iterate over the frames. For each frame, convert it to gray scale,
    and save the frame to the new video.
    Make sure to close all relevant captures and to destroy all windows.

    Args:
        input_video_path: str. Path to input video.
        output_video_path: str. Path to output video.

    Additional References:
    (1) What are fourcc parameters:
    https://docs.microsoft.com/en-us/windows/win32/medfound/video-fourccs

    """
    """INSERT YOUR CODE HERE."""
    cap = cv2.VideoCapture(input_video_path)
    if cap.isOpened()== False:
        print("Error open video file")
        exit(-1)
    param = get_video_parameters(cap)
    out = cv2.VideoWriter(output_video_path, fourcc=param["fourcc"], fps=param["fps"], frameSize=(param["width"],
                                                                                                  param["height"]), isColor=False)
    while True:
        ret, frame = cap.read()
        if ret:
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            out.write(gray_frame)
        else:
            break
    cap.release()
    out.release()

def convert_video_to_black_and_white(input_video_path: str,
                                     output_video_path: str) -> None:
    """Convert the video in the input path to black and white.

    Use VideoCapture from OpenCV to open the video and read its
    parameters using the capture's get method.
    Open an output video using OpenCV's VideoWriter.
    Iterate over the frames. For each frame, first convert it to gray scale,
    then use OpenCV's THRESH_OTSU to slice the gray color values to
    black (0) and white (1) and finally convert the frame format back to RGB.
    Save the frame to the new video.
    Make sure to close all relevant captures and to destroy all windows.

    Args:
        input_video_path: str. Path to input video.
        output_video_path: str. Path to output video.

    Additional References:
    (1) What are fourcc parameters:
    https://docs.microsoft.com/en-us/windows/win32/medfound/video-fourccs

    """
    """INSERT YOUR CODE HERE."""
    cap = cv2.VideoCapture(input_video_path)
    if cap.isOpened()== False:
        print("Error open video file")
        exit(-1)
    param = get_video_parameters(cap)
    out = cv2.VideoWriter(output_video_path, fourcc=param["fourcc"], fps=param["fps"], frameSize=(param["width"],
                                                                                                  param["height"]), isColor=False)
    while True:
        ret, frame = cap.read()
        if ret:
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray_frame, (3, 3), 0)
            ret3, binary_frame = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            out.write(binary_frame)
        else:
            break
    cap.release()
    out.release()



def convert_video_to_sobel(input_video_path: str,
                           output_video_path: str) -> None:
    """Convert the video in the input path to sobel map.

    Use VideoCapture from OpenCV to open the video and read its
    parameters using the capture's get method.
    Open an output video using OpenCV's VideoWriter.
    Iterate over the frames. For each frame, first convert it to gray scale,
    then use OpenCV's THRESH_OTSU to slice the gray color values to
    black (0) and white (1) and finally convert the frame format back to RGB.
    Save the frame to the new video.
    Make sure to close all relevant captures and to destroy all windows.

    Args:
        input_video_path: str. Path to input video.
        output_video_path: str. Path to output video.

    Additional References:
    (1) What are fourcc parameters:
    https://docs.microsoft.com/en-us/windows/win32/medfound/video-fourccs

    """
    """INSERT YOUR CODE HERE.
        REMOVE THE pass KEYWORD AND IMPLEMENT YOUR OWN CODE.
        """
    pass


def main():
    convert_video_to_grayscale(INPUT_VIDEO, GRAYSCALE_VIDEO)
    convert_video_to_black_and_white(INPUT_VIDEO, BLACK_AND_WHITE_VIDEO)
    convert_video_to_sobel(INPUT_VIDEO, SOBEL_VIDEO)


if __name__ == "__main__":
    main()
