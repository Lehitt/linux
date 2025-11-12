from flask import Flask
import mysql.connector

app=Flask(__name__)

@app.route('/')
def home():
    conn = mysql.connector.connect(
        host="localhost",
        user="exampleuser",
        password="new_strong_password",
        database="exampledb"
    )
    cursor = conn.cursor()

    cursor.execute("SELECT 'Hello from MySQL!'")
    result = cursor.fetchone()

    cursor.execute("SELECT NOW()")
    current_time = cursor.fetchone()

    cursor.close()
    conn.close()



    return f"""
        <html>
    <head>
        <style>
            body {{
                background-color: #7F00FF;  
                color: #000000;             
                font-family: Arial, sans-serif;
                text-align: center;
                padding-top: 50px;
            }}
            h1 {{
                color: #000000;  
            }}
            p {{
                color: #000000;  
            }}
        </style>
    </head>
    <body>
  
    
    <h1>{result[0]}</h1>
    <h2>{current_time[0]}</h2>
    </body>
    </html>

    """
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)