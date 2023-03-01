echo "Création de l'environnement virtuel"
python3.10 -m venv venv
source venv/bin/activate

echo "Installation des dépendances"
python -m pip install -r requirements.txt

echo "Téléchargement des modèles"
mkdir -p modeles/detection && cd modeles/detection
wget https://github.com/OlafenwaMoses/ImageAI/releases/download/3.0.0-pretrained/retinanet_resnet50_fpn_coco-eeacb38b.pth
wget https://github.com/OlafenwaMoses/ImageAI/releases/download/3.0.0-pretrained/yolov3.pt
wget https://github.com/OlafenwaMoses/ImageAI/releases/download/3.0.0-pretrained/tiny-yolov3.pt

mkdir ../classification && cd ../classification
wget https://github.com/OlafenwaMoses/ImageAI/releases/download/3.0.0-pretrained/mobilenet_v2-b0353104.pth
wget https://github.com/OlafenwaMoses/ImageAI/releases/download/3.0.0-pretrained/resnet50-19c8e357.pth
wget https://github.com/OlafenwaMoses/ImageAI/releases/download/3.0.0-pretrained/inception_v3_google-1a9a5a14.pth
wget https://github.com/OlafenwaMoses/ImageAI/releases/download/3.0.0-pretrained/densenet121-a639ec97.pth




