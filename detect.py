import cv2


class PersonDetector:
    def __init__(self, model_path, config_path):
        self.engine = cv2.dnn.readNetFromTensorflow(model_path, config_path)

    def policz_osoby(self, sciezka_do_obrazu):  # ustandaryzowane – zostaje
        frame = cv2.imread(sciezka_do_obrazu)
        if frame is None:
            return 0

        tensor = cv2.dnn.blobFromImage(
            frame,
            size=(300, 300),
            swapRB=True,
            crop=False
        )
        self.engine.setInput(tensor)
        predictions = self.engine.forward()

        total = 0
        for idx in range(predictions.shape[2]):
            confidence = predictions[0, 0, idx, 2]
            category = int(predictions[0, 0, idx, 1])

            if category == 1 and confidence > 0.3:
                total += 1

        print(f"Wykryto: {total}")
        return total
