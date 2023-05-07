import csv
import pandas as pd

def calculate_iou(box1, box2):
    x1, y1, w1, h1 = box1
    x2, y2, w2, h2 = box2

    x_intersection = max(0, min(x1 + w1, x2 + w2) - max(x1, x2))
    y_intersection = max(0, min(y1 + h1, y2 + h2) - max(y1, y2))
    intersection_area = x_intersection * y_intersection

    box1_area = w1 * h1
    box2_area = w2 * h2
    union_area = box1_area + box2_area - intersection_area

    iou = intersection_area / union_area if union_area > 0 else 0
    return iou

def IntersectionOverUnion():
    detected_df = pd.read_csv('src/IOU/detected_cells.csv')
    real_df = pd.read_csv('archive/annotations.csv')

    iou_values = []

    for image in detected_df['image'].unique():

        detected_cells = detected_df[detected_df['image'] == image]
        real_cells = real_df[real_df['image'] == image]
        
        print("Valores para a imagem: " + str(image))

        for label in detected_cells['label'].unique():
            print("     Com a label: " + str(label))

            detected_cells_label = detected_cells[detected_cells['label'] == label]
            real_cells_label = real_cells[real_cells['label'] == label]
            
            correct_values = 0

            for _, detected_row in detected_cells_label.iterrows():
                for _, real_row in real_cells_label.iterrows():

                    box1 = (detected_row['xmin'], detected_row['ymin'], 
                            detected_row['xmax'] - detected_row['xmin'], detected_row['ymax'] - detected_row['ymin'])

                    box2 = (real_row['xmin'], real_row['ymin'], 
                            real_row['xmax'] - real_row['xmin'], real_row['ymax'] - real_row['ymin'])

                    iou = calculate_iou(box1, box2)

                    if iou >= 0.5:
                        correct_values += 1

                    print("           Valor Encontrado: " + str(iou))

                    iou_values.append(iou)
            
        print('                 Valores corretos: ' + str(correct_values))
        print('\n')
    
    return iou_values