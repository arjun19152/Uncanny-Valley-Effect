from human import *

def solve_humanoid():
    gaze_x, gaze_y, bxs, bys, bxe, bye = 100, 100, 50, 50, 150, 150

    humanoid_images_mouth = (0.0, -0.13, 0.21, 0.07)
    humanoid_images_eye = (0.0, 0.018, 0.29, 0.075)
    humanoid_images_nose = (0.0, -0.055, 0.2, 0.055)
    humanoid_images_forehead = (0.0, 0.1, 0.25, 0.066)

    normalised_humanoid_images_mouth = (normalize_coordinate(humanoid_images_mouth[0]), normalize_coordinate(humanoid_images_mouth[1]), humanoid_images_mouth[2], humanoid_images_mouth[3])
    normalised_humanoid_images_eye = (normalize_coordinate(humanoid_images_eye[0]), normalize_coordinate(humanoid_images_eye[1]), humanoid_images_eye[2], humanoid_images_eye[3])
    normalised_humanoid_images_nose = (normalize_coordinate(humanoid_images_nose[0]), normalize_coordinate(humanoid_images_nose[1]), humanoid_images_nose[2], humanoid_images_nose[3])
    normalised_humanoid_images_forehead = (normalize_coordinate(humanoid_images_forehead[0]), normalize_coordinate(humanoid_images_forehead[1]), humanoid_images_forehead[2], humanoid_images_forehead[3])

    bounds_humanoid_image_mouth = get_bounds(normalised_humanoid_images_mouth[0], normalised_humanoid_images_mouth[1], normalised_humanoid_images_mouth[2], normalised_humanoid_images_mouth[3])
    bounds_humanoid_image_eye = get_bounds(normalised_humanoid_images_eye[0], normalised_humanoid_images_eye[1], normalised_humanoid_images_eye[2], normalised_humanoid_images_eye[3])
    bounds_humanoid_image_nose = get_bounds(normalised_humanoid_images_nose[0], normalised_humanoid_images_nose[1], normalised_humanoid_images_nose[2], normalised_humanoid_images_nose[3])
    bounds_humanoid_image_forehead = get_bounds(normalised_humanoid_images_forehead[0], normalised_humanoid_images_forehead[1], normalised_humanoid_images_forehead[2], normalised_humanoid_images_forehead[3])


    gazeData = pd.read_csv(os.getcwd()+"\\"+"GazeCollection.csv")
    gazeData.rename(columns = {"Unnamed: 0": "Image"}, inplace = True)


    humanoid_8_mouth_count = 0
    humanoid_8_eyes_count = 0
    humanoid_8_nose_count = 0
    humanoid_8_forehead_count = 0
    humanoid_8_other_count = 0
    humanoid_32_mouth_count = 0
    humanoid_32_eyes_count = 0
    humanoid_32_nose_count = 0
    humanoid_32_forehead_count = 0
    humanoid_32_other_count = 0
    humanoid_mouth_count = 0
    humanoid_eyes_count = 0
    humanoid_nose_count = 0
    humanoid_forehead_count = 0
    humanoid_other_count = 0

    humanoidROIdataCSV = pd.read_csv('humanoidROIData.csv')
    
    humanoid_name = ["63", "64", "65", "71", "74" "76", "66", "67", "77", "79", "58", "61", "69", "72"]

    humanoid_pre=["matched-8","matched-32","matched-c"]
    for image in gazeData["Image"]:
        path_ = ""
        isHumanoid = image[-2::] in humanoid_name
        if isHumanoid:
            path_ = "C:\\Users\\Varun\\Downloads\\behaviour_analysis-20230704T062824Z-001\\behaviour_analysis\\roi_images\\screenshots_HUMANOID"
            imager = mpimg.imread(path_+"\\"+image+".jpg")
            ysz = imager.shape[0]
            xsz = imager.shape[1]
            imagenm = image + ".jpg"
            coords = humanoidROIdataCSV.loc[humanoidROIdataCSV['file_name'] == imagenm, 'coords']
            coords = list(coords)
            coords = ast.literal_eval(coords[0])
            other_coords = coords[4][0][0], coords[4][0][1], coords[4][1][0], coords[4][1][1]
            scaled_humanoid_image_mouth = coords[3][0][0], coords[3][0][1], coords[3][1][0], coords[3][1][1]
            scaled_humanoid_image_eyes = coords[1][0][0], coords[1][0][1], coords[1][1][0], coords[1][1][1]
            scaled_humanoid_image_nose = coords[2][0][0], coords[2][0][1], coords[2][1][0], coords[2][1][1]
            scaled_humanoid_image_forehead = coords[0][0][0], coords[0][0][1], coords[0][1][0], coords[0][1][1]
            gaze = gazeData.loc[gazeData['Image'] == image]
            gaze_x = gaze["Gaze_X"].values
            gaze_x = list(map(float, gaze_x[0][1:-1:].split(", ")))
            gaze_y = gaze["Gaze_Y"].values
            gaze_y = list(map(float, gaze_y[0][1:-1:].split(", ")))
            for i in range(0, len(gaze_x)):
                x, y = normalize_coordinateXY(gaze_x[i], gaze_y[i])
                x, y = rescaleXY(x, y, xsz, ysz)
                if (image[0:len(humanoid_pre[0]):] == humanoid_pre[0]):
                    if(is_inside(x, y, *other_coords)):
                        humanoid_8_other_count = humanoid_8_other_count + 1
                        if (is_inside(x, y, *scaled_humanoid_image_eyes)):
                            humanoid_8_eyes_count+=1
                        elif (is_inside(x, y, *scaled_humanoid_image_nose)):
                            humanoid_8_nose_count+=1
                        elif (is_inside(x, y, *scaled_humanoid_image_mouth)):
                            humanoid_8_mouth_count+=1
                        elif (is_inside(x, y, *scaled_humanoid_image_forehead)):
                            humanoid_8_forehead_count+=1
                elif (image[0:len(humanoid_pre[1]):] == humanoid_pre[1]):
                    if(is_inside(x, y, *other_coords)):
                        humanoid_32_other_count = humanoid_32_other_count + 1
                        if (is_inside(x, y, *scaled_humanoid_image_eyes)):
                            humanoid_32_eyes_count+=1
                        elif (is_inside(x, y, *scaled_humanoid_image_nose)):
                            humanoid_32_nose_count+=1
                        elif (is_inside(x, y, *scaled_humanoid_image_mouth)):
                            humanoid_32_mouth_count+=1
                        elif (is_inside(x, y, *scaled_humanoid_image_forehead)):
                            humanoid_32_forehead_count+=1
                elif (image[0:len(humanoid_pre[2]):] == humanoid_pre[2]):
                    if(is_inside(x, y, *other_coords)):
                        humanoid_other_count = humanoid_other_count + 1
                        if (is_inside(x, y, *scaled_humanoid_image_eyes)):
                            humanoid_eyes_count+=1
                        elif (is_inside(x, y, *scaled_humanoid_image_nose)):
                            humanoid_nose_count+=1
                        elif (is_inside(x, y, *scaled_humanoid_image_mouth)):
                            humanoid_mouth_count+=1
                        elif (is_inside(x, y, *scaled_humanoid_image_forehead)):
                            humanoid_forehead_count+=1


    humanoid_other_count = humanoid_other_count - (humanoid_eyes_count + humanoid_nose_count + humanoid_mouth_count + humanoid_forehead_count)
    total = humanoid_eyes_count + humanoid_nose_count + humanoid_mouth_count + humanoid_forehead_count + humanoid_other_count

    humanoid_eyes_count/=total
    humanoid_nose_count/=total
    humanoid_mouth_count/=total
    humanoid_forehead_count/=total
    humanoid_other_count/=total

    humanoid_8_other_count = humanoid_8_other_count - (humanoid_8_eyes_count + humanoid_8_nose_count + humanoid_8_mouth_count + humanoid_8_forehead_count)
    total = humanoid_8_eyes_count + humanoid_8_nose_count + humanoid_8_mouth_count + humanoid_8_forehead_count + humanoid_8_other_count

    humanoid_8_eyes_count/=total
    humanoid_8_nose_count/=total
    humanoid_8_mouth_count/=total
    humanoid_8_forehead_count/=total
    humanoid_8_other_count/=total

    humanoid_32_other_count = humanoid_32_other_count - (humanoid_32_eyes_count + humanoid_32_nose_count + humanoid_32_mouth_count + humanoid_32_forehead_count)
    total = humanoid_32_eyes_count + humanoid_32_nose_count + humanoid_32_mouth_count + humanoid_32_forehead_count + humanoid_32_other_count

    humanoid_32_eyes_count/=total
    humanoid_32_nose_count/=total
    humanoid_32_mouth_count/=total
    humanoid_32_forehead_count/=total
    humanoid_32_other_count/=total

    return ([humanoid_eyes_count, humanoid_nose_count, humanoid_mouth_count, humanoid_forehead_count, humanoid_other_count], [humanoid_8_eyes_count, humanoid_8_nose_count, humanoid_8_mouth_count, humanoid_8_forehead_count, humanoid_8_other_count], [humanoid_32_eyes_count, humanoid_32_nose_count, humanoid_32_mouth_count, humanoid_32_forehead_count, humanoid_32_other_count])

def plot_humanoid():
    allData = solve_humanoid()
    
    Legend = ["8", "32", "c"]
    X_labels = ["Eyes", "Nose", "Mouth", "Forehead", "Other"]
    X_axis = np.arange(len(X_labels))
    

    ListLow = allData[1]
    ListRafd = allData[0]
    ListHigh = allData[2]

    
    plt.bar(X_axis - 0.2, ListLow, 0.2, label = '8')
    plt.bar(X_axis + 0.0, ListHigh, 0.2, label = '32')
    plt.bar(X_axis + 0.2, ListRafd, 0.2, label = 'c')
    plt.title("Humanoid ROI Summary")
    plt.xticks(X_axis, X_labels)
    plt.legend(Legend)
    plt.show()

if __name__ == "__main__":
    plot_humanoid()