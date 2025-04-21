import sys
import urllib.parse
from PySide2.QtWidgets import QApplication, QFileDialog
from packager import run_packager

def main():
    print("[LAUNCHER] Starting script...")

    if len(sys.argv) < 2:
        print("[ERROR] No arguments passed.")
        input("Press Enter to exit...")
        return

    url_data = sys.argv[1]
    print(f"[LAUNCHER] Received URL data: {url_data}")

    if "ids=" in url_data:
        parsed = urllib.parse.urlparse(url_data)
        query = urllib.parse.parse_qs(parsed.query)
        ids = query.get("ids", [])
        if ids:
            shot_ids = ids[-1].split(",")
            print(f"[LAUNCHER] Shot IDs: {shot_ids}")

            # Create the QApplication instance before using QFileDialog
            app = QApplication(sys.argv)

            # Ask for folder only once
            folder = QFileDialog.getExistingDirectory(None, "Select Destination Folder")
            if not folder:
                print("[LAUNCHER] ❌ Cancelled by user")
                input("Press Enter to exit...")
                return

            success_ids = []
            for shot_id in shot_ids:
                try:
                    # Now passing both shot_id and folder to run_packager
                    run_packager(int(shot_id), folder)
                    success_ids.append(shot_id)
                    print(f"[LAUNCHER] ✅ Success: Shot {shot_id}")
                except Exception as e:
                    print(f"[LAUNCHER] ❌ Failed: Shot {shot_id} | Reason: {e}")

            print(f"\n[LAUNCHER] Packager finished.")
            print(f"  ✅ Successful: {', '.join(success_ids)}")
            print(f"  ❌ Failed: {', '.join(set(shot_ids) - set(success_ids))}" if len(success_ids) != len(
                shot_ids) else "")

        else:
            print("[ERROR] No valid 'ids' found.")
    else:
        print("[ERROR] 'ids=' not found in URL")

    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
