from sklearn.metrics import roc_curve, roc_auc_score
import numpy as np
import matplotlib.pyplot as plt

file = "testr2.txt"
file_labels = "./syscalls/snd-cert/snd-cert.1.labels"

outputs = open(file, "r")
labels = [int(i) for i in open(file_labels, "r").readlines()]
outputs = outputs.readlines()

matching_detectors = np.zeros(len(outputs))
for i, output in enumerate(outputs):
    values = np.array(output.split(), dtype=float)
    matching_detectors[i] = np.mean(values)

roc = roc_curve(labels, matching_detectors)
auc = roc_auc_score(labels, matching_detectors)

ax = plt.subplot(1, 1, 1)
ax.plot(roc[0], roc[1])
ax.set_title(f"r={2}, auc={round(auc,2)}")
ax.set_xlabel("1 - specificity")
ax.set_ylabel("sensitivity")

plt.show()