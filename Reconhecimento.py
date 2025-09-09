import cv2
import face_recognition
import numpy as np

#lista de embeddings já cadastrados
embeddings_cadastrados = []
ids_cadastrados = []
proximo_id = 1

#inicia a captura de vídeo
webcam = cv2.VideoCapture(0)

#verifica se existe webcam em loop
while True:
    ret, frame = webcam.read()
    if not ret:
        break

    #conversão para RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Localiza rostos
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):
        # Compara com rostos cadastrados
        matches = face_recognition.compare_faces(embeddings_cadastrados, face_encoding, tolerance=0.6)
        face_distances = face_recognition.face_distance(embeddings_cadastrados, face_encoding)

        if True in matches:
            best_match_index = np.argmin(face_distances)
            face_id = ids_cadastrados[best_match_index]
        else:
            #cadastro de novo rosto
            face_id = proximo_id
            proximo_id += 1
            embeddings_cadastrados.append(face_encoding)
            ids_cadastrados.append(face_id)

        #desenha na tela
        top, right, bottom, left = face_location
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, f"ID {face_id}", (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    #exibe o frame com os reconhecimentos
    cv2.imshow("Reconhecimento com ID", frame)

    if cv2.waitKey(5) == 27:  # ESC para sair
        break

#desativa webcam e fecha a janela
webcam.release()
cv2.destroyAllWindows()
