# Mini-prototipo-de-reconhecimento-de-rosto-em-python

## Tecnologias ultilizadas
- [Python 3](https://www.python.org/)  
- [OpenCV](https://opencv.org/) – captura e manipulação de vídeo  
- [face_recognition](https://github.com/ageitgey/face_recognition) – extração de características e reconhecimento  
- [NumPy](https://numpy.org/) – operações matemáticas

---

## Instalação

## -1
Se você ultiliza Windows:
Instale [CMake](https://cmake.org/download/) e o [Visual Studio Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)

Ao abrir o instalador, selecione: Desktop development with C++

Reinicie o PC e verifique executado:
```bash
cmake --version
```
## -3
```bash
pip install -r requirements.txt
```
## -3.1
Caso a instalação da biblioteca "face_recognition" não funcione faça isso:
```bash
pip install cmake
pip install dlib
pip install face_recognition
```
## -3
Rode o comando para instalar os modelos do face_recognition
```bash
pip install wheel setuptools pip --upgrade
pip install git+https://github.com/ageitgey/face_recognition_models --verbos
```
## -4
```bash
python Reconhecimento.py
```
