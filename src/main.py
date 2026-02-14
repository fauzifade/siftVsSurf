import sys
import os
import glob
import time

sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))

from utils.sift import SiftDetector as MyDetector
# from utils.surf import SurfDetector as MyDetector 

from utils.matcher import FeatureMatcher

def main():
    dataset_path = "dataset" 
    
    # Variabel ini hanya untuk label print, karena matcher.py kamu otomatis Brute Force
    USE_FLANN = False 
    
    files = glob.glob(os.path.join(dataset_path, "*.tif"))
    files.sort()
    
    if not files:
        print("Dataset kosong!")
        return

    detector = MyDetector()
    matcher = FeatureMatcher()
    
    algo_name = "SIFT" if "Sift" in MyDetector.__name__ else "SURF"
    match_name = "FLANN" if USE_FLANN else "Brute Force"

    # 1. Build Database
    print(f"[{algo_name} - {match_name}]")
    print(f"Mengekstrak fitur dari {len(files)} gambar...")
    
    database = {}
    for file_path in files:
        _, _, des = detector.process_image(file_path)
        if des is not None:
            database[file_path] = des
    
    # 2. Matching & Recap
    print(f"\n--- REKAPITULASI KESALAHAN ({algo_name} + {match_name}) ---")
    print(f"{'QUERY':<12} | {'HASIL SALAH':<12} | {'SKOR':<5} | {'WAKTU (s)':<10}")
    print("-" * 55)

    wrong_count = 0
    total = 0
    total_search_time = 0 

    for query_path in files:
        query_filename = os.path.basename(query_path)
        query_id = query_filename.split('_')[0]
        query_des = database.get(query_path)
        
        if query_des is None: continue
        
        best_score = -1
        best_match_file = "None"
        
        start_time = time.time()
        
        for db_path, db_des in database.items():
            if db_path == query_path: continue
            
            # --- PERBAIKAN DI SINI ---
            # Menghapus parameter use_flann karena menyebabkan error
            matches = matcher.match(query_des, db_des)
            
            if len(matches) > best_score:
                best_score = len(matches)
                best_match_file = db_path
        
        exec_time = time.time() - start_time
        total_search_time += exec_time
        
        if best_match_file != "None":
            result_filename = os.path.basename(best_match_file)
            result_id = result_filename.split('_')[0]
            is_correct = (query_id == result_id)
            
            if not is_correct:
                print(f"{query_filename:<12} | {result_filename:<12} | {best_score:<5} | {exec_time:.4f}s")
                wrong_count += 1
        
        total += 1

    # 3. Hasil Akhir
    avg_time = total_search_time / total if total > 0 else 0
    accuracy = ((total - wrong_count) / total) * 100 if total > 0 else 0
    
    print("-" * 55)
    print(f"ALGORITMA       : {algo_name}")
    print(f"METODE MATCHING : {match_name}")
    print(f"TOTAL UJI       : {total}")
    print(f"TOTAL SALAH     : {wrong_count}")
    print(f"AKURASI         : {accuracy:.2f}%")
    print(f"RATA-RATA WAKTU : {avg_time:.4f} detik/query")
    print("-" * 55)

if __name__ == "__main__":
    main()