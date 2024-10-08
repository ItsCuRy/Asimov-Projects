import cv2 
import mediapipe as mp
import pyautogui 

pyautogui.FAILSAFE = False

#Lendo a camera e inicializando a solucao
cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)

#Coletar tamanho da tela 
tela_w, tela_h = pyautogui.size()

#Coletar especificacoes da nossa camera
_, frame = cam.read()
frame_h, frame_w, _ = frame.shape

#loop principal 
while True:
    _,img = cam.read()
    img = cv2.flip(img,1)
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


    results = face_mesh.process(rgb_img)
    landmark_points = results.multi_face_landmarks

    #checar se os landmarks existem
    if landmark_points:
        landmarks = landmark_points[0].landmark

        #pontos necessarios
        iris_and_mouth = [landmarks[145],landmarks[159],landmarks[14],landmarks[13]]

        #checa se boca esta aberta 
        boca_distancia = iris_and_mouth[-2].y - iris_and_mouth[-1].y
        #print(boca_distancia)
        if boca_distancia > 0.105: 
            #ignorar o codigo de mouse
            pass 
        else:
            #iterar sobre landmarks da iris
            #mouse na iris rodando 
            for id, landmark in enumerate(iris_and_mouth[0:2]):
                #adaptar o x,y
                if id == 0:
                    x = int(landmark.x * frame_w) 
                    y = int(landmark.y * frame_h)
                    pyautogui.moveTo(x,y)
            pass
            





        for lm in iris_and_mouth:
            x = int(lm.x * frame_w)
            y = int(lm.y * frame_h)
            cv2.circle(img,(x,y),4,(255,255,0))



    cv2.imshow('Visao', img)


    if cv2.waitKey(20) & 0xFF==ord('q'):
        break
#final do codigo 