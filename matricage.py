import json

files = ("RetinaNet.json", "YOLOv3.json", "TinyYOLOv3.json")

all = {}
for file in files:
    with open(file, mode="r", encoding="utf-8") as f:
        all[file] = json.load(f)

allkw = set()
for file in files:
    for img in all[file]:
        for kw in all[file][img]:
            if kw not in allkw:
                allkw.add(kw)

allkw = list(allkw)
allkw.sort()

with open("kwlist.json", mode="w", encoding="utf-8") as f:
    json.dump(allkw, f, indent=2, ensure_ascii=False)

with open("kwlist.txt", mode="w", encoding="utf-8") as f:
    f.write("\n".join(allkw))


import numpy as np

def get_vector(img):
    return np.array([sum(img[kw]) if kw in img else 0 for kw in allkw])

def get_matrix():
    return np.array([get_vector(img) for file in all.values() for img in file.values()])

from scipy import sparse
sparse.save_npz("matrix.npz", sparse.csr_matrix(get_matrix()))

