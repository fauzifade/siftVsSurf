import cv2
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))

from utitouch .gitignorels.sift import SiftDetector
from utils.matcher import FeatureMatcher

try:
    from utils.surf import SurfDetector
    SURF_AVAILABLE = True
except (ImportError, AttributeError):
    SURF_AVAILABLE = False
    print("PERINGATAN: SURF tidak bisa di-load. Pastikan kamu di environment '(surf)'.")

IMG_1 = "dataset/101_1.tif" 
IMG_2 = "dataset/101_2.tif"
OUTPUT_DIR = "output"

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def generate_images(detector_class, algo_name, file1, file2):
    print(f"\n[{algo_name}] Sedang membuat visualisasi...")
    
    try:
        detector = detector_class()
        matcher = FeatureMatcher()
    except Exception as e:
        print(f"  Gagal inisialisasi {algo_name}: {e}")
        return

    img1, kp1, des1 = detector.process_image(file1)
    img2, kp2, des2 = detector.process_image(file2)

    if img1 is None or img2 is None:
        print(f"  Error: Gambar tidak ditemukan di {file1} atau {file2}")
        return

    try:
        vis_kp = detector.visualize_keypoints(img1, kp1)
        filename_kp = f"{algo_name}_Keypoints.jpg"
        cv2.imwrite(os.path.join(OUTPUT_DIR, filename_kp), vis_kp)
        print(f"  -> Tersimpan: {filename_kp}")
    except AttributeError:
        print("  -> Gagal: Method 'visualize_keypoints' belum ada di utils.")

    try:
        matches = matcher.match(des1, des2)
        
        vis_match = detector.visualize_matches(img1, kp1, img2, kp2, matches, N=50)
        filename_match = f"{algo_name}_Matches.jpg"
        cv2.imwrite(os.path.join(OUTPUT_DIR, filename_match), vis_match)
        print(f"  -> Tersimpan: {filename_match}")
    except AttributeError:
        print("  -> Gagal: Method 'visualize_matches' belum ada di utils.")

if __name__ == "__main__":
    generate_images(SiftDetector, "SIFT", IMG_1, IMG_2)

    if SURF_AVAILABLE:
        generate_images(SurfDetector, "SURF", IMG_1, IMG_2)
    else:
        print("\nSKIP: Visualisasi SURF dilewati karena modul tidak tersedia.")