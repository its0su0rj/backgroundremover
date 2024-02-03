import rembg
from PIL import Image
import streamlit as st
import os
import base64

def remove_background(input_image_content, output_image_path):
    output_image = rembg.remove(input_image_content)

    with open(output_image_path, "wb") as f:
        f.write(output_image)

def main():
    st.title("Image Background Remover App")

    uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

        # Create a temporary directory to store the output image
        output_image_dir = "output_images"
        os.makedirs(output_image_dir, exist_ok=True)
        output_image_path = os.path.join(output_image_dir, "output_image.png")

        remove_background(uploaded_file.read(), output_image_path)  # Pass the file content

        # Display the output image
        st.image(output_image_path, caption="Background Removed Image", use_column_width=True)

        # Provide a download link for the output image
        st.markdown(get_binary_file_downloader_html(output_image_path, 'Background Removed Image'), unsafe_allow_html=True)

def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
    return href

if __name__ == "__main__":
    main()
