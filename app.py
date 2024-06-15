import streamlit as st
import os
from utils import find_facial_matches

def main():
    st.title('Facial Recognition App')

    st.sidebar.header('Folders')
    reference_folder = st.sidebar.text_input('Reference Folder')
    images_folder = st.sidebar.text_input('Images Folder')
    output_folder = st.sidebar.text_input('Output Folder')

    if st.sidebar.button('Start Scan'):
        if not reference_folder or not images_folder or not output_folder:
            st.error('Please provide all folder paths.')
        else:
            start_scan(reference_folder, images_folder, output_folder)

def start_scan(reference_folder, images_folder, output_folder):
    reference_images = os.listdir(reference_folder)
    if not reference_images:
        st.error('No reference images found.')
        return

    reference_img_path = os.path.join(reference_folder, reference_images[0])

    progress_bar = st.progress(0)
    status_text = st.empty()

    def update_progress(progress):
        progress_bar.progress(progress)
        status_text.text(f'Scan progress: {progress * 100:.2f}%')

    matched_images = find_facial_matches(reference_img_path, images_folder, output_folder, update_progress)

    st.success(f'Scan completed. Found {len(matched_images)} matching images.')

    if st.button('Stop Scan'):
        st.stop()

if __name__ == '__main__':
    main()
