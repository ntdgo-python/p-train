import cv2
import numpy as np

img = cv2.imread(
    "C:/Users/ThanhDat/AppData/Local/label-studio/label-studio/media/upload/12/13bf200f-2024-10-31_20h09m31s809ms_Job1_Fail.bmp"
)
label = [
    {
        "transcription": "64850",
        "points": [[955, 784], [1283, 892], [1249, 995], [921, 887]],
    },
    {
        "transcription": "6103",
        "points": [[1046, 677], [1270, 751], [1236, 854], [1012, 780]],
    },
]

for i in label:
    first_point = tuple(map(int, i["points"][0]))
    cv2.circle(img, first_point, radius=5, color=(0, 0, 255), thickness=-1)
    cv2.polylines(img, [np.array(i["points"])], True, (0, 0, 255), 2)
    cv2.putText(
        img,
        i["transcription"],
        (i["points"][0][0], i["points"][0][1]),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        (0, 0, 255),
        2,
    )

cv2.imwrite("img.png", img)


import torch

free, total = torch.cuda.mem_get_info()
print(f"Free: {free/1024**3:.2f} GB, Total: {total/1024**3:.2f} GB")
