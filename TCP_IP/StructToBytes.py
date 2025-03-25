import struct

# 구조체 형식 문자열 정의 (예: 정수, 문자열, 부동 소수점)
format_string = 'i4sf'  # i: 정수, 4s: 4바이트 문자열, f: 부동 소수점

# 구조체 데이터
data = (123, b'abcd', 3.14)

# 데이터 패킹
packed_data = struct.pack(format_string, *data)
print(f"패킹된 데이터: {packed_data} {len(packed_data)}")

# 패킹된 데이터 언패킹
unpacked_data = struct.unpack(format_string, packed_data)
print(f"언패킹된 데이터: {unpacked_data} {len(unpacked_data)}")

