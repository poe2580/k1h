from PIL import Image

# 빈 이미지 생성 함수
def create_empty_images(width, height):
    # RGB 모드의 빈 이미지 생성 (흰색 배경)
    return Image.new("RGB", (width, height), (255, 255, 255))

# 특정 픽셀 채우기 함수
def fill_pixel(image, x, y, color):
    pixels = image.load()  # 픽셀 데이터 접근
    pixels[x, y] = color   # 특정 좌표의 픽셀 색상 변경

# 이미지 파일로 저장 함수
def save_image_as_file(image, filename):
    # 이미지를 PNG 형식으로 저장
    image.save(filename, "PNG")

# 사용 예시
image = create_empty_images(200, 300)
fill_pixel(image, 20, 30, (0, 0, 0))  # (20, 30) 좌표에 검은색 (#000000) 채우기
save_image_as_file(image, "output_image.png")