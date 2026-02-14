# SIFT vs SURF: Comparative Analysis of Feature Matching

## 📌 Overview

This project provides a comprehensive comparison between two popular feature detection algorithms: SIFT (Scale-Invariant Feature Transform) and SURF (Speeded Up Robust Features).
The system evaluates the performance of these algorithms on a specific dataset based on:

1. Accuracy: Percentage of correct image matches.
2. Computation Time: Average processing time per query.
3. Robustness: Ability to handle geometric transformations.


## 📂 Project Structure


```python
siftVsSurf
├── dataset/                    # Input images (.tif)
├── utils/                      # Helper modules
│   ├── matcher.py              # Feature matching logic
│   ├── sift.py                 # SIFT detector wrapper
│   └── surf.py                 # SURF detector wrapper
├── hasil_visualisasi/          # Output folder for generated images
├── main.py                     # Main script for statistical evaluation
├── image.py                    # Script to visualize keypoints & matches
└── requirements.txt            # Python dependencies (Crucial versions)
```

## 🛠️ Installation & Setup 
This project relies on OpenCV 3.4.2.17 to access the non-free SURF algorithm (which was removed in later versions due to patent issues). Follow these steps strictly.
### 1. Clone the Repository


```python
git clone [https://github.com/fauzifade/siftVsSurf.git](https://github.com/fauzifade/siftVsSurf.git)
cd siftVsSurf
```

### 2. Set up a Virtual Environment

It is highly recommended to use a virtual environment to avoid conflicts with other OpenCV versions on your system.
1. Linux/MacOS:



```python
python3 -m venv vs
source vs/bin/activate
```

2. Windows:


```python
python -m venv vs
vs\Scripts\activate
```

### 3. Install Dependencies
Install the required libraries, including the specific legacy version of OpenCV.



```python
pip install -r requirements.txt

```

# 🚀 How to Use
## A. Statistical Evaluation (Accuracy & Speed)
Run main.py to process the entire dataset and generate a performance report. It will calculate accuracy and log any mismatch errors.



```python
python main.py
```

Sample Output:


```python
[SIFT - Brute Force]
Mengekstrak fitur dari 80 gambar...

--- REKAPITULASI KESALAHAN (SIFT + Brute Force) ---
QUERY        | HASIL SALAH  | SKOR  | WAKTU (s) 
-------------------------------------------------------
106_7.tif    | 107_2.tif    | 77    | 2.6233s
109_8.tif    | 108_2.tif    | 60    | 1.6457s
-------------------------------------------------------
ALGORITMA       : SIFT
METODE MATCHING : Brute Force
TOTAL UJI       : 80
TOTAL SALAH     : 2
AKURASI         : 97.50%
RATA-RATA WAKTU : 3.7566 detik/query
-------------------------------------------------------
```

## B. Visualizing Matches
Run image.py to generate visual outputs (Keypoints and Matching Lines) between two sample images. The results will be saved in the hasil_visualisasi/ folder.



```python
python image.py
```

# ⚙️ Configuration
To switch between SIFT and SURF, or to change the dataset path, you need to modify the main.py or image.py file slightly:
In main.py:



```python
# --- SELECT DETECTOR ---
# Uncomment the one you want to use:
# from utils.sift import SiftDetector as MyDetector  <-- Use this for SIFT
from utils.surf import SurfDetector as MyDetector    <-- Use this for SURF
```


```python

```

| Algorithm | Method | Avg Time (s) | Accuracy | Notes |
|---|---|---|---|---|
| SIFT | Brute Force | ~0.15s | High | Very robust to rotation |
| SURF | Bruce Force | ~0.08s | Medium | Faster but less accurate on specific textures |


# ⚠️ Troubleshooting
*Error: module 'cv2' has no attribute 'xfeatures2d'*
Cause: You are using a newer version of OpenCV where SURF is removed.

Fix: Uninstall your current OpenCV and install the version from requirements.txt:




```python
pip uninstall opencv-python opencv-contrib-python
pip install opencv-contrib-python==3.4.2.17
```
