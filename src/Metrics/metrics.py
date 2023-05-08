import pandas as pd
import numpy as np
from sklearn.metrics import precision_recall_fscore_support
from IOU import intersection_over_union as IOU

# TO DO
# AINDA NÃO CONSEGUI IMPLEMENTAR AS MÉTRICAS, MAS CONTINUO LENDO SOBRE

def calculate_iou(gt_row, pred_row):
    gt_bbox = [gt_row['xmin'], gt_row['ymin'], gt_row['xmax'], gt_row['ymax']]
    pred_bbox = [pred_row['xmin'], pred_row['ymin'], pred_row['xmax'], pred_row['ymax']]

    iou = IOU.calculate_iou(gt_bbox, pred_bbox)
    return iou

def getMetrics():
    df = pd.read_csv('src/IOU/detected_cells.csv')

    ground_truth_labels = ['rbc', 'wbc']

    tp = 0
    fp = 0
    fn = 0

    iou_threshold = 0.5

    for label in ground_truth_labels:
        pred_rows = df[df['label'] == label]

        num_pred_objects = len(pred_rows)

        gt_rows = df[df['label'] == label].reset_index()

        iou_matrix = np.zeros((len(gt_rows), len(pred_rows)))
        for i, gt_row in gt_rows.iterrows():
            for j, pred_row in pred_rows.iterrows():
                iou_matrix[i,j] = calculate_iou(gt_row, pred_row)

        matched_pairs = []
        
        while True:
            i, j = np.unravel_index(iou_matrix.argmax(), iou_matrix.shape)
            if iou_matrix[i,j] < iou_threshold:
                break
            matched_pairs.append((i, j))
            iou_matrix[i,:] = -1
            iou_matrix[:,j] = -1

        if len(matched_pairs) == 0:
            iou_matrix = np.zeros((0, 0))
        else:
            iou_matrix = iou_matrix[:len(matched_pairs), :len(pred_rows)]

        num_tp = len(matched_pairs)
        num_fp = num_pred_objects - num_tp
        num_fn = len(gt_rows) - num_tp

        tp += num_tp
        fp += num_fp
        fn += num_fn

    precision, recall, f1, _ = precision_recall_fscore_support([1] * tp + [0] * fp, [1] * tp + [0] * fn, average='binary')

    print("Precision:", precision)
    print("Recall:", recall)
    print("F1 score:", f1)