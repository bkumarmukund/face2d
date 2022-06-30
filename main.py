from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os 
from flask import send_file
from flask import make_response
from waitress import serve


app = Flask(__name__)

@app.route('/')
def upload_f():
   return render_template('upload.html')

@app.route('/2dswap/', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['face']
      f.save('face.jpg')
      
      f = request.files['body']
      f.save('body.jpg')
      
      
      #face swapcase
      import cv2
      from face_swap import swap_faces

      # Read images
      body = cv2.imread("body.jpg")
      face = cv2.imread("face.jpg")

      # Swap faces
      result = swap_faces(body, face)


      #save results
      cv2.imwrite('result.jpg', result)
      
      return send_file('result.jpg', mimetype='image')

#if __name__ == '__main__':
#    app.run(host='127.0.0.1', port='7777', debug = True)
serve(app,host='127.0.0.1', port='7777')


