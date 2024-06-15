# Facial Recognition Web App with Streamlit and DeepFace

This repository contains the code for a web application that performs facial recognition using the DeepFace library. The app is built with Streamlit and allows users to scan through image folders to find all images matching a reference image. Users can specify the reference folder, the folder containing images to be scanned, and the output folder where matching images will be saved.

## Features
- **User-Friendly Interface:** Simple and intuitive interface built with Streamlit.
- **Facial Recognition:** Uses DeepFace for robust facial recognition capabilities.
- **Folder Browsing:** Easily browse and select reference, input, and output folders.
- **Progress Monitoring:** Visual progress bar to track the scanning process.
- **Control:** Start and stop the scan with a single click.

## How to Use

### Prerequisites
- Python 3.7 or higher

### Installation
1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/facial_recognition_app.git
    cd facial_recognition_app
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate    # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

### Running the App
1. **Start the Streamlit app:**
    ```sh
    streamlit run app.py
    ```

2. **Use the sidebar to input paths for the reference folder, images folder, and output folder.**

3. **Click the 'Start Scan' button to begin the facial recognition process.**

## File Structure
- `app.py`: Main Streamlit application.
- `utils.py`: Utility functions for image loading and facial recognition.
- `requirements.txt`: List of dependencies.
- `reference_images/`: Folder to store reference images.
- `image_files/`: Folder to store images to be scanned.
- `output/`: Folder to store output results.

## Dependencies
- Streamlit
- DeepFace
- Pandas
- OpenCV-Python-Headless
- tf-keras

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements
Special thanks to the developers of Streamlit and DeepFace for providing powerful tools for building AI applications.

---

### Contact
For any questions or suggestions, please feel free to contact me at fletlajn@gmail.com.
