import sys
import time

print("\033[42m[SUCCESS] cs2.exe found!\033[0m")
print("Initializing inject sequence...")

for i in range(101):
    time.sleep(0.03)
    bar = '█' * (i // 5) + '░' * (20 - (i // 5))
    sys.stdout.write(f"\rInjecting main.dll: [{bar}] {i}%")
    sys.stdout.flush()

print("\n[32m[DONE] Successfully injected into cs2.exe!\033[0m")
