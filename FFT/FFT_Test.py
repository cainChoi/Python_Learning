import numpy as np

def fft_analysis(frequency, voltage):
    """
    주파수-전압 데이터에 대해 FFT 분석을 수행하고 주파수 배열을 반환합니다.

    Args:
        frequency (numpy.ndarray): 주파수 데이터 배열 (MHz)
        voltage (numpy.ndarray): 전압 데이터 배열 (V)

    Returns:
        tuple: (주파수 배열 (Hz), FFT 결과의 크기 배열)
    """

    # 샘플링 간격 계산 (주파수 데이터 간의 차이)
    sampling_rate = (frequency[1] - frequency[0]) * 1e6 # MHz -> Hz

    # FFT 수행
    fft_result = np.fft.fft(voltage)
    fft_magnitude = np.abs(fft_result)  # 크기 계산

    # 주파수 배열 생성
    frequencies = np.fft.fftfreq(len(voltage), 1 / sampling_rate)
    frequencies = frequencies[:len(voltage) // 2] #양의 주파수영역만 추출

    fft_magnitude = fft_magnitude[:len(voltage) // 2] #양의 주파수영역만 추출

    return frequencies, fft_magnitude

def fft_analysis_zeropadding(frequency, voltage, padding_factor=2):
    """제로 패딩을 적용한 FFT 분석을 수행합니다."""

    sampling_rate = (frequency[1] - frequency[0]) * 1e6
    fft_result = np.fft.fft(voltage, n=len(voltage) * padding_factor) #제로 패딩 적용
    fft_magnitude = np.abs(fft_result)

    freqs = np.fft.fftfreq(len(fft_result), 1 / sampling_rate)
    freqs = freqs[:len(fft_result) // 2]
    fft_magnitude = fft_magnitude[:len(fft_result) // 2]
    return freqs, fft_magnitude