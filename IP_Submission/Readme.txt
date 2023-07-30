
Aproach Used:

1) Collected data of participants. (Data of 26 participants in this case)
2) Filtered the visual images used in the experiment to obtain only the facial region. This hugely reduces the region of non-interest.
3) Created ROI for Forehead, eye, nose and mouth (ONLY eyes and mouth in case of robots) in the filtered out images.
4) The mask for obtaining the facial region was generated only using BSF images and the same mask for each BSF images was applied onto the corresponding LSF and HSF images.
5) Similarly, the ROI was defined using teh BSF images and then applied onto the corresponding LSF and HSF images.
6) Gaze points falling outside of the ROIs were counted as "Others".
7) Gaze Points falling in Others Category = Total Gaze Points in the filtered facial region - ( Gaze Points in forehead roi + Gaze Points in eye roi + Gaze Points in nose roi+ Gaze Points in mouth roi )

###############################################################################################################################################
The folder contains following files and folders:
 
0) DLIB_Face_Filtering.py : This code utilizes the DLIB library (198 landmark variant) to create a mask to filter out other regions of the image other
than the face and then filter is adjusted according to the facial features in each image. 

1) ROI_Images_human : This folder contains the final filtered and ROI generated images of humans, on which the final
analysis have been performed.

2) ROI_images_humanoid_2 : This folder contains the final filtered and ROI generated images of humanoid, on which the final
analysis have been performed.

3) ROI generation: This code helps to generate the ROI on BSF images of humanoid and humans and then apply the same ROIs on the corresponding HSF and LSF images.

4) Manual_ROI_generation : This python file was used to individually define ROI for eyes and mouth for robotic images, Here on the image the user has to drag and make a rectangle over the interested region and press "C" to see the defined ROI. On the output screen the user obtains the top_left coordinate and bottom right coordinate of the defined rectangle.

5) robotic.py : This python code was used for calculating the count of gaze points falling in each ROI region (Eye and mouth) of 
in every robotic/mechanical image and to finally plot the normalized bar plot.

6) human.py : This python code was used for calculating the count of gaze points falling in each ROI region (Forehead. Eye, Nose, Mouth) of 
in every human image and to finally plot the normalized bar plot.

7) humanoid.py : This python code was used for calculating the count of gaze points falling in each ROI region (Forehead. Eye, Nose, Mouth)  of 
in every humanoid image and to finally plot the normalized bar plot.

8) robotROIData.csv : CSV file contains the coordinates of top_left_coordinate and bottom_right_coordinate of each ROI that has been defined.
9) humanoidROIData.csv : CSV file contains the coordinates of top_left_coordinate and bottom_right_coordinate of each ROI that has been defined.
10) humanROIData.csv : CSV file contains the coordinates of top_left_coordinate and bottom_right_coordinate of each ROI that has been defined.


