from sklearn.metrics import roc_curve, roc_auc_score
import numpy as np
import matplotlib.pyplot as plt

lang = 'xho'
for r in range(1, 10):
    file_english = open(f'./outputs/Outputs/output{r}.txt', 'r')
    file_other = open(f'./Outputsmiddle/Outputsmiddle/output{r}.txt', 'r')

    english = file_english.readlines()
    english = np.array([float(i) for i in english])

    other = file_other.readlines()
    other = np.array([float(i) for i in other])

    y_true = np.append(np.zeros(english.size), np.ones(other.size))
    y_pred = np.append(english, other)

    roc = roc_curve(y_true, y_pred)
    auc = roc_auc_score(y_true, y_pred)

    ax = plt.subplot(3, 3, r)
    ax.plot(roc[0], roc[1])
    ax.set_title(f"r={r}, auc={round(auc,2)}")
    ax.set_xlabel("1 - specificity")
    ax.set_ylabel("sensitivity")

plt.tight_layout()
plt.show()
