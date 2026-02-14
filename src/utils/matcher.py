import cv2
import numpy as np

class FeatureMatcher:
    def __init__(self):
        self.bf_l2 = cv2.BFMatcher(cv2.NORM_L2, crossCheck=False)
        self.bf_hamming = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=False)

    def match(self, des1, des2):
        if des1 is None or des2 is None or len(des1) < 2 or len(des2) < 2:
            return []

        if des1.dtype == np.float32:
            matches = self.bf_l2.knnMatch(des1, des2, k=2)
        else:
            matches = self.bf_hamming.knnMatch(des1, des2, k=2)

        good_matches = []
        ratio_thresh = 0.75
        for match in matches:
            if len(match) == 2:
                m, n = match
                if m.distance < ratio_thresh * n.distance:
                    good_matches.append(m)
        
        return good_matches