https://paddlepaddle.github.io/PaddleX/latest/en/installation/paddlepaddle_install.html
https://paddlepaddle.github.io/PaddleX/latest/en/installation/installation.html
https://paddlepaddle.github.io/PaddleX/latest/en/module_usage/tutorials/ocr_modules/text_detection.html
https://paddlepaddle.github.io/PaddleX/latest/en/module_usage/tutorials/ocr_modules/text_recognition.html

 python -m pip install paddlepaddle-gpu==3.0.0b2 -i https://www.paddlepaddle.org.cn/packages/stable/cu123/
python -m pip install paddlepaddle==3.0.0b2 -i https://www.paddlepaddle.org.cn/packages/stable/cpu/
pip install https://paddle-model-ecology.bj.bcebos.com/paddlex/whl/paddlex-3.0.0b2-py3-none-any.whl

mkdir dataset
curl -o ./dataset/ocr_det_dataset_examples.tar https://paddle-model-ecology.bj.bcebos.com/paddlex/data/ocr_det_dataset_examples.tar
tar -xf ./dataset/ocr_det_dataset_examples.tar -C ./dataset/

python PaddleX/main.py -c PaddleX/paddlex/configs/text_detection/PP-OCRv4_server_det.yaml -o Global.mode=train -o Global.dataset_dir=dataset/ocr_det_dataset_examplesaa



pip install paddlepaddle-gpu==3.0.0b1 -i https://www.paddlepaddle.org.cn/packages/stable/cu118/

# Training Detection Model
python ./PaddleOCR/tools/train.py -c ./dataset/det.yml

# Training Classification Model
python ./PaddleOCR/tools/train.py -c ./dataset/cls.yml

# Training Recognizer Model
python ./PaddleOCR/tools/train.py -c ./dataset/rec.yml
python ./PaddleOCR/tools/train.py -c ./dataset/rec_new.yml

# Conversion of Detection Trained Weights to Inference
python ./PaddleOCR/tools/export_model.py -c ./dataset/det.yml -o Global.pretrained_model="./output/det_ppocr_v4/best_accuracy" Global.save_inference_dir=./inference/det_inference/

# Conversion of Classification Trained weights to Inference
python ./PaddleOCR/tools/export_model.py -c ./dataset/cls.yml -o Global.pretrained_model=./output/cls/best_accuracy Global.save_inference_dir=./inference/cls_inference/

# Conversion of Recognizer Trained weights to Inference
python ./PaddleOCR/tools/export_model.py -c ./dataset/rec.yml -o Global.pretrained_model=./output/rec_ppocr_v4/best_accuracy Global.save_inference_dir=./inference/rec_inference/
python ./PaddleOCR/tools/export_model.py -c ./dataset/rec_new.yml -o Global.pretrained_model=./output/rec_new/best_accuracy Global.save_inference_dir=./inference/rec_inference_v2/
