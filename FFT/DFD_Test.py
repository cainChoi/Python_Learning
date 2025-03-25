from FileCtrl import read_csv_file
from pathlib import Path
import os
import FFT_Test as FFT
import matplotlib.pyplot as plt
import numpy as np
from SecondMax import second_largest_argmax as sla
import FindPeak as fp

current_path = os.path.abspath(__file__)

# 사용 예시
#current_dir = Path.cwd()
file_path = os.path.dirname(current_path) + '\sample1.txt' #combined path
freqs, amps = read_csv_file(file_path)

fft_Freqs, fft_Mags = FFT.fft_analysis(freqs, amps)
fft_Freqs_zero, fft_Mags_zero = FFT.fft_analysis_zeropadding(freqs, amps, 100)
print("주파수 배열 (Hz):", fft_Freqs)

print(fft_Freqs[sla(fft_Mags)])
print(fft_Freqs_zero[sla(fft_Mags_zero)])
findIdx = fp.FindPeak(fft_Mags_zero)
print(f"%3f KHz"%(fft_Freqs_zero[findIdx] / 1000))

# plt.figure(figsize=(10, 5))
# plt.plot(fft_Freqs, fft_Mags)
# plt.xlabel("Frequency (Hz)")
# plt.ylabel("Magnitude")
# plt.title("FFT Analysis")
# plt.grid(True)
# plt.show()

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(fft_Freqs, fft_Mags)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title("FFT Analysis (No Padding)")
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(fft_Freqs_zero, fft_Mags_zero)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title("FFT Analysis (Zero Padding)")
plt.grid(True)

plt.tight_layout()
plt.show()