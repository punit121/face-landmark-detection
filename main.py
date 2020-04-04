# import the necessary packages
import numpy as np
import cv2
import argparse
import dlib
import imutils
import argparse

 
facial_features_cordinates = {}

# define a dictionary that maps the indexes of the facial
# landmarks to specific face regions
FACIAL_LANDMARKS_INDEXES = dict([
    ("Mouth", (48, 68)),
    ("Right_Eyebrow", (17, 22)),
    ("Left_Eyebrow", (22, 27)),
    ("Right_Eye", (36, 42)),
    ("Left_Eye", (42, 48)),
    ("Nose", (27, 35)),
    ("Jaw", (0, 17))
])


def shape_to_numpy_array(shape, dtype="int"):
    # initialize the list of (x, y)-coordinates
    coordinates = np.zeros((68, 2), dtype=dtype)

    # loop over the 68 facial landmarks and convert them
    # to a 2-tuple of (x, y)-coordinates
    for i in range(0, 68):
        coordinates[i] = (shape.part(i).x, shape.part(i).y)

    # return the list of (x, y)-coordinates
    return coordinates


def visualize_facial_landmarks(image, shape, colors=None, alpha=0.75):
    # create two copies of the input image -- one for the
    # overlay and one for the final output image
    overlay = image.copy()
    output = image.copy()

    # if the colors list is None, initialize it with a unique
    # color for each facial landmark region
    if colors is None:
        colors = [(19, 199, 109), (79, 76, 240), (230, 159, 23),
                  (168, 100, 168), (158, 163, 32),
                  (163, 38, 32), (180, 42, 220)]

    # loop over the facial landmark regions individually
    for (i, name) in enumerate(FACIAL_LANDMARKS_INDEXES.keys()):
        # grab the (x, y)-coordinates associated with the
        # face landmark
        (j, k) = FACIAL_LANDMARKS_INDEXES[name]
        pts = shape[j:k]
        facial_features_cordinates[name] = pts

        

    ##Draw Jawline
    jaw=facial_features_cordinates["Jaw"]
    for l in range(1, len(jaw)):
            ptA = tuple(jaw[l - 1])
            ptB = tuple(jaw[l])
            cv2.line(overlay, ptA, ptB, colors[i], 2)
    
    
    # apply the transparent overlay
    cv2.addWeighted(overlay, alpha, output, 1 - alpha, 0, output)

    # return the output image
    print(facial_features_cordinates)
    image_feature_data={"image_feature_data":facial_features_cordinates}
    fname="landmarks_features.txt"
    np.set_printoptions(threshold=np.inf, linewidth=np.inf)  # turn off summarization, line-wrapping
    with open(fname, 'w') as f:
        f.write(str(image_feature_data))
    return output


def face_detection(rects):   
    # loop over the face detections
    for (i, rect) in enumerate(rects):
        # determine the facial landmarks for the face region, then
        # convert the landmark (x, y)-coordinates to a NumPy array
        shape = predictor(gray, rect)
        shape = shape_to_numpy_array(shape)

        output = visualize_facial_landmarks(image, shape)
        cv2.imwrite("outImage.png", output)
        cv2.waitKey(0)
        
        
if __name__=="__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True,help="path to input image")
    args = vars(ap.parse_args())
    # initialize dlib's face detector
    detector = dlib.get_frontal_face_detector()
    p = "shape_predictor_68_face_landmarks.dat"

    predictor = dlib.shape_predictor(p)

    # load the input image, resize it, and convert it to grayscale
    image = cv2.imread(args["image"])
    image = imutils.resize(image, width=500)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # detect faces in the grayscale image
    rects = detector(gray, 1)
    
    face_detection(rects)
    