import csv
import pandas as pd

def calculate_iou(box1, box2):
    x1, y1, w1, h1 = box1
    x2, y2, w2, h2 = box2

    x_intersection = max(0, min(x1 + w1, x2 + w2) - max(x1, x2))
    y_intersection = max(0, min(y1 + h1, y2 + h2) - max(y1, y2))
    intersection_area = x_intersection * y_intersection

    # Calculate the area of union rectangle
    box1_area = w1 * h1
    box2_area = w2 * h2
    union_area = box1_area + box2_area - intersection_area

    iou = intersection_area / union_area if union_area > 0 else 0
    return iou

detected_df = pd.read_csv('detected_cells.csv')
real_df = pd.read_csv('real_cells.csv')

detected_groups = detected_df.groupby('image')
real_groups = real_df.groupby('image')

iou_values = []

for image_name, detected_group in detected_groups:
    if image_name in real_groups.groups:
        real_group = real_groups.get_group(image_name)

        for _, detected_row in detected_group.iterrows():
            for _, real_row in real_group.iterrows():

                # Extract bounding box coordinates
                box1 = (detected_row['xmin'], detected_row['ymin'], 
                        detected_row['xmax'] - detected_row['xmin'], detected_row['ymax'] - detected_row['ymin'])

                box2 = (real_row['xmin'], real_row['ymin'], 
                        real_row['xmax'] - real_row['xmin'], real_row['ymax'] - real_row['ymin'])

                # Calculate IOU
                iou = calculate_iou(box1, box2)

                # Add the IOU value to a list
                iou_values.append(iou)