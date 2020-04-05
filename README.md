## Face Landmarks Recognition 

![My Face](output/outImage_punit.png)

### About
This is a python script which uses opencv, dlib, and imutils to extract the 68 facial landmark co-ordinates  and draw the jaw line from it as output. 

### Dependencies 
`pip install numpy opencv-python dlib imutils`

### Run
`python main.py --image "input/punit.jpeg"`

#### facial landmark coordinates

```
{'facial_features_cordinates': [{'Mouth': array([[210, 142],
       [215, 141],
       [219, 141],
       [222, 141],
       [226, 140],
       [231, 140],
       [236, 140],
       [232, 144],
       [227, 146],
       [223, 147],
       [220, 147],
       [215, 146],
       [212, 143],
       [219, 142],
       [223, 142],
       [226, 142],
       [234, 140],
       [226, 143],
       [223, 144],
       [219, 144]]), 'Right_Eyebrow': array([[197, 117],
       [201, 113],
       [206, 113],
       [212, 113],
       [217, 114]]), 'Left_Eyebrow': array([[222, 114],
       [227, 112],
       [234, 111],
       [240, 111],
       [245, 114]]), 'Right_Eye': array([[203, 120],
       [206, 119],
       [210, 118],
       [213, 119],
       [210, 120],
       [206, 121]]), 'Left_Eye': array([[229, 118],
       [232, 117],
       [236, 117],
       [239, 118],
       [236, 119],
       [232, 119]]), 'Nose': array([[220, 118],
       [220, 123],
       [220, 127],
       [221, 132],
       [215, 135],
       [218, 136],
       [222, 137],
       [225, 135]]), 'Jaw': array([[194, 119],
       [196, 126],
       [197, 133],
       [199, 139],
       [201, 146],
       [205, 151],
       [210, 155],
       [217, 158],
       [224, 159],
       [232, 157],
       [239, 154],
       [244, 149],
       [249, 144],
       [252, 137],
       [252, 129],
       [252, 122],
       [252, 114]])}]}
```


