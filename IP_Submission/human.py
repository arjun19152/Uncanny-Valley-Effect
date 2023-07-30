import pandas as pd
import os
import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt
import ast
import cv2

# given a rectangle, check if a point is inside it
def is_inside(gaze_x, gaze_y, bxs, bys, bxe, bye):
    if gaze_x >= bxs and gaze_x <= bxe and gaze_y >= bys and gaze_y <= bye:
        return True
    else:
        return False

# function to convert size from center anchor and position to x and y bounds
def get_bounds(center_x, center_y, width, height):
    bxs = center_x - width/2
    bys = center_y - height/2
    bxe = center_x + width/2
    bye = center_y + height/2
    return (bxs, bys, bxe, bye)

def normalize_coordinate(val):
    return (val+1)/2

# normalize the coordinate
def normalize_coordinateXY(x, y):
    return (x+1)/2, (y+1)/2

def rescale(bxs, bys, bxe, bye, image_width, image_height):
    return bxs*image_width, bys*image_height, bxe*image_width, bye*image_height

def rescaleXY(x, y, image_width, image_height):
    return x*image_width, y*image_height


def solve_human():
    gaze_x, gaze_y, bxs, bys, bxe, bye = 100, 100, 50, 50, 150, 150

    human_images_mouth = (0.0, -0.028, 0.12, 0.04)
    human_images_eye = (0.008, 0.053, 0.18, 0.035)
    human_images_nose = (0.0, 0.013, 0.1, 0.036)
    human_images_forehead = (0.008, 0.1, 0.17, 0.045)

    normalised_human_images_mouth = (normalize_coordinate(human_images_mouth[0]), normalize_coordinate(human_images_mouth[1]), human_images_mouth[2], human_images_mouth[3])
    normalised_human_images_eye = (normalize_coordinate(human_images_eye[0]), normalize_coordinate(human_images_eye[1]), human_images_eye[2], human_images_eye[3])
    normalised_human_images_nose = (normalize_coordinate(human_images_nose[0]), normalize_coordinate(human_images_nose[1]), human_images_nose[2], human_images_nose[3])
    normalised_human_images_forehead = (normalize_coordinate(human_images_forehead[0]), normalize_coordinate(human_images_forehead[1]), human_images_forehead[2], human_images_forehead[3])

    bounds_human_image_mouth = get_bounds(normalised_human_images_mouth[0], normalised_human_images_mouth[1], normalised_human_images_mouth[2], normalised_human_images_mouth[3])
    bounds_human_image_eye = get_bounds(normalised_human_images_eye[0], normalised_human_images_eye[1], normalised_human_images_eye[2], normalised_human_images_eye[3])
    bounds_human_image_nose = get_bounds(normalised_human_images_nose[0], normalised_human_images_nose[1], normalised_human_images_nose[2], normalised_human_images_nose[3])
    bounds_human_image_forehead = get_bounds(normalised_human_images_forehead[0], normalised_human_images_forehead[1], normalised_human_images_forehead[2], normalised_human_images_forehead[3])

    gazeData = pd.read_csv(os.getcwd()+"\\"+"GazeCollection.csv")
    gazeData.rename(columns = {"Unnamed: 0": "Image"}, inplace = True)

    human_8_mouth_count = 0
    human_8_eyes_count = 0
    human_8_nose_count = 0
    human_8_forehead_count = 0
    human_8_other_count = 0
    human_32_mouth_count = 0
    human_32_eyes_count = 0
    human_32_nose_count = 0
    human_32_forehead_count = 0
    human_32_other_count = 0
    human_mouth_count = 0
    human_eyes_count = 0
    human_nose_count = 0
    human_forehead_count = 0
    human_other_count = 0

    humanROIdataCSV = pd.read_csv('humanROIData.csv')

    human_pre=["matched-8","matched-32","matched-Ra"]
    for image in gazeData["Image"]:
        path_ = ""
        isHuman = "Caucasian" in image
        if isHuman:
            path_ = "C:\\Users\\Varun\\Downloads\\behaviour_analysis-20230704T062824Z-001\\behaviour_analysis\\roi_images\\screenshots_HUMAN"
            imager = mpimg.imread(path_+"\\"+image+".jpg")
            ysz = imager.shape[0]
            xsz = imager.shape[1]
            imagenm = image + ".jpg"
            coords = humanROIdataCSV.loc[humanROIdataCSV['file_name'] == imagenm, 'coords']
            coords = list(coords)
            coords = ast.literal_eval(coords[0])
            eye_top_left = (coords[1][0][0], coords[1][0][1])
            eye_bottom_right = (coords[1][1][0], coords[1][1][1])
            other_coords = coords[4][0][0], coords[4][0][1], coords[4][1][0], coords[4][1][1]
            scaled_human_image_mouth = coords[3][0][0], coords[3][0][1], coords[3][1][0], coords[3][1][1]
            scaled_human_image_eyes = coords[1][0][0], coords[1][0][1], coords[1][1][0], coords[1][1][1]
            scaled_human_image_nose = coords[2][0][0], coords[2][0][1], coords[2][1][0], coords[2][1][1]
            scaled_human_image_forehead = coords[0][0][0], coords[0][0][1], coords[0][1][0], coords[0][1][1]
            gaze = gazeData.loc[gazeData['Image'] == image]
            gaze_x = gaze["Gaze_X"].values
            gaze_x = list(map(float, gaze_x[0][1:-1:].split(", ")))
            gaze_y = gaze["Gaze_Y"].values
            gaze_y = list(map(float, gaze_y[0][1:-1:].split(", ")))
            for i in range(0, len(gaze_x)):
                x, y = normalize_coordinateXY(gaze_x[i], gaze_y[i])
                x, y = rescaleXY(x, y, xsz, ysz)
                if (image[0:len(human_pre[0]):] == human_pre[0]):
                    if(is_inside(x, y, *other_coords)):
                        human_8_other_count = human_8_other_count + 1
                        if (is_inside(x, y, *scaled_human_image_eyes)):
                            human_8_eyes_count+=1
                        elif (is_inside(x, y, *scaled_human_image_nose)):
                            human_8_nose_count+=1
                        elif (is_inside(x, y, *scaled_human_image_mouth)):
                            human_8_mouth_count+=1
                        elif (is_inside(x, y, *scaled_human_image_forehead)):
                            human_8_forehead_count+=1
                elif (image[0:len(human_pre[1]):] == human_pre[1]):
                    if(is_inside(x, y, *other_coords)):
                        human_32_other_count = human_32_other_count + 1
                        if (is_inside(x, y, *scaled_human_image_eyes)):
                            human_32_eyes_count+=1
                        elif (is_inside(x, y, *scaled_human_image_nose)):
                            human_32_nose_count+=1
                        elif (is_inside(x, y, *scaled_human_image_mouth)):
                            human_32_mouth_count+=1
                        elif (is_inside(x, y, *scaled_human_image_forehead)):
                            human_32_forehead_count+=1
                elif (image[0:len(human_pre[2]):] == human_pre[2]):
                    if(is_inside(x, y, *other_coords)):
                        human_other_count = human_other_count + 1
                        if (is_inside(x, y, *scaled_human_image_eyes)):
                            human_eyes_count+=1
                        elif (is_inside(x, y, *scaled_human_image_nose)):
                            human_nose_count+=1
                        elif (is_inside(x, y, *scaled_human_image_mouth)):
                            human_mouth_count+=1
                        elif (is_inside(x, y, *scaled_human_image_forehead)):
                            human_forehead_count+=1

    human_other_count = human_other_count - (human_eyes_count + human_nose_count + human_mouth_count + human_forehead_count)
    total = human_eyes_count + human_nose_count + human_mouth_count + human_forehead_count + human_other_count
    human_eyes_count/=total
    human_nose_count/=total
    human_mouth_count/=total
    human_forehead_count/=total
    human_other_count/=total

    human_8_other_count = human_8_other_count - (human_8_eyes_count + human_8_nose_count + human_8_mouth_count + human_8_forehead_count)
    total = human_8_eyes_count + human_8_nose_count + human_8_mouth_count + human_8_forehead_count + human_8_other_count
    human_8_eyes_count/=total
    human_8_nose_count/=total
    human_8_mouth_count/=total
    human_8_forehead_count/=total
    human_8_other_count/=total

    human_32_other_count = human_32_other_count - (human_32_eyes_count + human_32_nose_count + human_32_mouth_count + human_32_forehead_count)
    total = human_32_eyes_count + human_32_nose_count + human_32_mouth_count + human_32_forehead_count + human_32_other_count
    human_32_eyes_count/=total
    human_32_nose_count/=total
    human_32_mouth_count/=total
    human_32_forehead_count/=total
    human_32_other_count/=total

    return ([human_eyes_count, human_forehead_count, human_mouth_count, human_nose_count, human_other_count], [human_8_eyes_count, human_8_forehead_count, human_8_mouth_count, human_8_nose_count, human_8_other_count], [human_32_eyes_count, human_32_forehead_count, human_32_mouth_count, human_32_nose_count, human_32_other_count])

def plot_human():
    allData = solve_human()
    Legend = ["8", "32", "Rafd"]
    X_labels = ["Eyes", "Forehead", "Mouth", "Nose", "Other"]
    X_axis = np.arange(len(X_labels))
    ListLow = allData[1]
    ListRafd = allData[0]
    ListHigh = allData[2]
    plt.bar(X_axis - 0.2, ListLow, 0.2, label = '8')
    plt.bar(X_axis + 0.0, ListHigh, 0.2, label = '32')
    plt.bar(X_axis + 0.2, ListRafd, 0.2, label = 'Rafd')
    plt.title("Human ROI Summary")
    plt.xticks(X_axis, X_labels)
    plt.legend(Legend)
    plt.show()


if __name__ == '__main__':
    plot_human()