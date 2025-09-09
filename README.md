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
Instale o Visual [Studio Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
Ao abrir o instalador, selecione:
Desktop development with C++
Isso instala o compilador MSVC, que o dlib precisa.
Reinicie o PC e verifique executado:
```bash
cmake --version
```
## -3
```bash
pip install -r requirements.txt
```
## -3.1
Caso a instalaçãod da biblioteca "face_recognition" não funcione instale manualmente as dependencias dela antes:
```bash
pip install cmake
pip install dlib
pip install face_recognition
```
## -4
```bash
python Reconhecimento.py
```
