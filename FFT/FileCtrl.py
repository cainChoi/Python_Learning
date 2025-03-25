import csv
import numpy as np

def read_csv_file(file_path):
    """
    CSV 파일을 읽어 내용을 리스트 형태로 반환합니다.

    Args:
        file_path (str): 읽을 CSV 파일의 경로

    Returns:
        list: CSV 파일의 내용을 담은 리스트 (각 행은 리스트로 표현)
              파일을 읽는 데 실패하면 빈 리스트를 반환합니다.
    """
    data = []
    frequencies = []
    voltages = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                frequencies.append(float(row[0])) #첫번째 열의 주파수 데이터를 float형식으로 저장
                voltages.append(float(row[1]))  
    except FileNotFoundError:
        print(f"오류: '{file_path}' 파일을 찾을 수 없습니다.")
    except Exception as e:
        print(f"오류: 파일을 읽는 동안 오류가 발생했습니다: {e}")
    return np.array(frequencies), np.array(voltages)
