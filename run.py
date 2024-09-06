from app import app
import os

if __name__ == '__main__':
    port = os.getenv('PORT',5000)
    app.run(debug=True,port=port)