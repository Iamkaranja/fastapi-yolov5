#! /bin/bash

echo "Setting up..."

cat << EOF > install.sh
echo "Installing Yolov5..."
git clone https://github.com/ultralytics/yolov5
EOF
bash install.sh >> /dev/null
if [ -d "yolov5" ]; then
    echo "[+] \033[32m File \"yolov5\" downloaded successfully."
fi
rm -r install.sh
sleep 1


cat << EOF > requirements.txt
fastapi
uvicorn
python-multipart
pillow
aiofiles
tqdm
matplotlib
seaborn
pandas
opencv-python-headless
requests
torch
torchvision
nest-asyncio 
pyngrok
EOF


for i in $(cat requirements.txt); do echo "\033[1;32m [*] Dowloading packages from requirements.txt"; pip install $i >> /dev/null; echo "\033[32m [+] Download Complete"; done