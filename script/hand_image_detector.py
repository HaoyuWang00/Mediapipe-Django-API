import cv2
import mediapipe as mp
import os

# import sys

def hand_detection(image_path):
  mp_drawing = mp.solutions.drawing_utils
  mp_hands = mp.solutions.hands

  # For static images:
  hands = mp_hands.Hands(
      static_image_mode=True,
      max_num_hands=2,
      min_detection_confidence=0.5)
  # Read an image, flip it around y-axis for correct handedness output (see
  # above).
  idx = 0
  image = cv2.flip(image_path, 1)
  # Convert the BGR image to RGB before processing.
  results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

  # Print handedness and draw hand landmarks on the image.
  print('Handedness:', results.multi_handedness)
  if not results.multi_hand_landmarks:
    print("WARNING: This image has no hand(s)!!!")
  else:
    image_hight, image_width, _ = image.shape
    annotated_image = image.copy()
    for hand_landmarks in results.multi_hand_landmarks:
      print('hand_landmarks:', hand_landmarks)
      print(
          f'Index finger tip coordinates: (',
          f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width}, '
          f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_hight})'
      )
      mp_drawing.draw_landmarks(
          annotated_image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    
    output_relative_path = '/tmp/annotated_image/' + str(idx) + '.png'
    cv2.imwrite(output_relative_path, cv2.flip(annotated_image, 1))
  hands.close()

  return cv2.flip(annotated_image, 1)