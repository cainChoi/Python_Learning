import numpy as np

def second_largest_argmax(arr):
    """넘파이 배열에서 두 번째로 큰 숫자의 인덱스를 argmax로 구합니다."""

    if len(arr) < 2:
        return None  # 배열의 길이가 2보다 작으면 None 반환

    arr_copy = arr.copy() # 원본 배열을 복사합니다.
    sorted_arr = np.sort(arr_copy) # 복사한 배열을 정렬합니다.
    second_largest = sorted_arr[-2] # 정렬된 배열에서 두 번째로 큰 숫자

    # 원본 배열에서 두 번째로 큰 숫자의 인덱스를 찾습니다.
    second_largest_indices = np.where(arr == second_largest)[0]

    return second_largest_indices[0] if len(second_largest_indices) > 0 else None
