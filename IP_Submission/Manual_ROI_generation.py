import cv2

## Function to Obtain the coordinates from the drawn rectangle.
def drag_rectangle(event, x, y, flags, param):
    global drawing, ix, iy, roi_coords

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        roi_coords = [(ix, iy), (x, y)]


if __name__ == "__main__":
    image_path = "C://Users//Admin//PycharmProjects//ROI_generation_on_Mechanical_Images//Mechanical_Normal Images//matched-c43.jpeg"  # Replace this with the path to your image

    # Load the image
    image = cv2.imread(image_path)
    cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
    clone = image.copy()

    # Initialize variables
    drawing = False
    roi_coords = []

    # Create a window and set the callback function
    cv2.namedWindow("Image")
    cv2.setMouseCallback("Image", drag_rectangle)

    while True:
        cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
        cv2.imshow("Image", image)
        key = cv2.waitKey(1) & 0xFF

        # Press 'r' to reset the ROI selection
        if key == ord("r"):
            image = clone.copy()
            roi_coords = []

        # Press 'c' to confirm the ROI selection
        elif key == ord("c") and len(roi_coords) == 2:
            break

        # Draw the rectangle while dragging the mouse
        if drawing and len(roi_coords) == 1:
            image = clone.copy()
            cv2.rectangle(image, roi_coords[0], (ix, iy), (0, 255, 0), 2)

    # Display the final image with the ROI
    print(roi_coords[0])
    print(roi_coords[1])
    cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
    cv2.rectangle(image, roi_coords[0], roi_coords[1], (0, 255, 0), 1)
    cv2.imshow("Image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Print the ROI coordinates
    if len(roi_coords) == 2:
        print("ROI Coordinates (Top-Left, Bottom-Right):", roi_coords)
