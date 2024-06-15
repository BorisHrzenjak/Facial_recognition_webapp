import os
from deepface import DeepFace
import cv2

def load_images_from_folder(folder):
    images = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(('jpg', 'jpeg', 'png')):
                images.append(os.path.join(root, file))
    return images

def find_facial_matches(reference_img_path, images_folder, output_folder, update_progress):
    reference_img = cv2.imread(reference_img_path)
    images = load_images_from_folder(images_folder)
    matched_images = []

    total_images = len(images)
    for idx, img_path in enumerate(images):
        img = cv2.imread(img_path)
        result = DeepFace.verify(img, reference_img, enforce_detection=False)
        if result['verified']:
            matched_images.append(img_path)
            output_path = os.path.join(output_folder, os.path.basename(img_path))
            cv2.imwrite(output_path, img)
        update_progress((idx + 1) / total_images)

    return matched_images
