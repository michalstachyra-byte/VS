from flask import Flask, request, jsonify
import requests
from detect import PersonDetector

app = Flask(__name__)
core = PersonDetector(
    'frozen_inference_graph.pb',
    'ssd_mobilenet_v2_coco_2018_03_29.pbtxt'
)


@app.route('/licznik_dysk', methods=['GET'])
def licznik_dysk():
    image_path = request.args.get('image_path', 'test.jpg') 
    val = core.policz_osoby(image_path)
    return jsonify({'persons_detected': val})  


@app.route('/licznik_url', methods=['GET'])
def licznik_url():
    url = request.args.get('url') 
    if not url:
        return jsonify({'error': 'Brak url'}), 400

    tmp_name = "temp_pic.jpg"
    try:
        r = requests.get(url, timeout=10)
        with open(tmp_name, 'wb') as h:
            h.write(r.content)

        score = core.policz_osoby(tmp_name)
        return jsonify({'Liczba wykrytych osob': score})
    except Exception as err:
        return jsonify({'error': str(err)}), 500


if __name__ == '__main__':
    app.run(debug=True)
