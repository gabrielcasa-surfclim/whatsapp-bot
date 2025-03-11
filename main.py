from flask import Flask, request, send_from_directory
from twilio.twiml.messaging_response import MessagingResponse
import os

app = Flask(__name__)

# Rota do webhook do WhatsApp
@app.route("/webhook", methods=["POST"])
def webhook():
    incoming_msg = request.values.get("Body", "").lower()
    resp = MessagingResponse()
    msg = resp.message()
    
    if "oi" in incoming_msg:
        response_text = "Oi! Como posso te ajudar hoje?"
    else:
        response_text = "Desculpe, não entendi. Tente dizer 'Oi'!"
    
    msg.body(response_text)
    return str(resp)

# Rota para servir arquivos estáticos (incluindo o HTML do Twilio)
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory(os.getcwd(), filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
