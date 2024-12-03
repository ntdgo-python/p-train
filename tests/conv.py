import os
from PIL import Image
import multiprocessing
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from ultralytics import YOLO

# Set input and output directories
input_dir = "Z:\\AI Project\\현대제철 과제 준비\\특수강 대형 절단후 강 길이 측정\\현대제철 이미지"
output_dir = "Z:\\AI Project\\현대제철 과제 준비\\특수강 대형 절단후 강 길이 측정\\Images"

def process_batch(files_batch):
    """
    Process a batch of files: convert images and save them as JPEG.
    """
    for input_file, output_file in files_batch:
        if os.path.exists(output_file):
            continue
        try:
            with Image.open(input_file) as img:
                # Convert and save as JPEG
                if img.mode in ('RGBA', 'LA'):
                    img = img.convert('RGB')  # Remove alpha channel
                img.save(output_file, 'JPEG', quality=100)
        except Exception as e:
            print(f"Could not convert {input_file}: {str(e)}")

def is_image_file(filename):
    """
    Check if a file is an image based on its extension.
    """
    valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff', '.webp')
    return filename.lower().endswith(valid_extensions)

def prepare_file_list(input_path, output_path):
    """
    Prepare a list of image files for processing, including their corresponding output paths.
    """
    file_list = []
    for root, dirs, files in os.walk(input_path):
        # Create corresponding output subdirectory
        rel_path = os.path.relpath(root, input_path)
        curr_output_dir = os.path.join(output_path, rel_path)
        if not os.path.exists(curr_output_dir):
            os.makedirs(curr_output_dir)
        
        for file in files:
            if is_image_file(file):
                input_file = os.path.join(root, file)
                output_file = os.path.join(curr_output_dir, os.path.splitext(file)[0] + '.jpg')
                file_list.append((input_file, output_file))
    return file_list

def convert_images(input_path, output_path, batch_size=500, num_workers=None):
    """
    Convert images to JPEG format using multiprocessing for efficiency.
    """
    # Prepare the list of files to process
    file_list = prepare_file_list(input_path, output_path)
    print(f"Found {len(file_list)} files to process")
    # Split files into batches
    batches = [file_list[i:i + batch_size] for i in range(0, len(file_list), batch_size)]
    print(f"Split into {len(batches)} batches")
    # Use multiprocessing to process batches
    with ThreadPoolExecutor(max_workers=200) as executor:
        executor.map(process_batch, batches)

if __name__ == "__main__":
    # Set batch size and number of workers
    batch_size = 500
    num_workers = multiprocessing.cpu_count() + 25 # Use all available CPU cores
    print(f"Using {num_workers} workers")
    # Run the conversion
    convert_images(input_dir, output_dir, batch_size=batch_size, num_workers=num_workers)
