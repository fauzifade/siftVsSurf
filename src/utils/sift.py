import cv2

class SiftDetector:
    def __init__(self):
        # Menggunakan xfeatures2d untuk kompatibilitas OpenCV lama (SURF)
        self.detector = cv2.xfeatures2d.SIFT_create()

    def process_image(self, image_path):
        img = cv2.imread(image_path, 0) # Load Grayscale
        if img is None:
            return None, None, None
        kp, des = self.detector.detectAndCompute(img, None)
        return img, kp, des

    # --- [BARU] FUNGSI VISUALISASI KEYPOINTS ---
    def visualize_keypoints(self, img, kp):
        """Menggambar lingkaran di lokasi keypoints."""
        # Gunakan bendera DRAW_RICH_KEYPOINTS agar lingkaran menunjukkan ukuran dan orientasi
        img_kp = cv2.drawKeypoints(img, kp, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        return img_kp

    # --- [BARU] FUNGSI VISUALISASI MATCHING (STATIC) ---
    @staticmethod
    def visualize_matches(img1, kp1, img2, kp2, good_matches, N=50):
        """Menggambar garis antara N pencocokan terbaik."""
        # Urutkan dulu berdasarkan jarak terdekat
        good_matches = sorted(good_matches, key=lambda x: x.distance)
        
        # Gambar N pencocokan teratas saja biar tidak ruwet
        img_matches = cv2.drawMatches(img1, kp1, img2, kp2, good_matches[:N], None,
                                      flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)
        return img_matches