import os
import cv2

# 원본 이미지 폴더 경로와 저장할 폴더 경로
input_folder = '/path/to/your/image_folder'
output_folder = '/path/to/your/output_folder'

# 출력 폴더가 없으면 생성
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 폴더 내의 모든 파일을 확인하여 이미지 형식을 JPG로 변환
for filename in os.listdir(input_folder):
    if filename.endswith(('.png', '.jpeg', '.bmp', '.tiff', '.gif')):  # 변환할 이미지 확장자들
        # 파일 경로
        file_path = os.path.join(input_folder, filename)
        
        # 이미지 열기
        img = cv2.imread(file_path)
        
        # 파일명에서 확장자를 제외한 이름
        name, ext = os.path.splitext(filename)
        
        # JPG 파일로 저장
        output_file = os.path.join(output_folder, name + '.jpg')
        cv2.imwrite(output_file, img)
        
print("변환 완료!")
