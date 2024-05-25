import requests
from flask import Flask, request

app = Flask(__name__)

# Discord webhook URL
discord_webhook_url = "https://discord.com/api/webhooks/1221194569832464514/hlJ9f6X4ZLp4amLtO_yNoIgfPekVrIomZ7CREIMCfoNGKB7wWSlx9u93gwjmCcF76W8K"

# Function to send webhook notification to Discord
def send_discord_webhook(message):
    data = {
        "content": message
    }
    requests.post(discord_webhook_url, json=data)

# Route to receive webhook from Roblox
@app.route('/webhook/roblox/gamepass', methods=['POST'])
def roblox_gamepass_webhook():
    data = request.json

    # Check if the purchase event is for a specific gamepass
    target_gamepass_id = "757047218"  # Replace with the ID of your gamepass
    if data.get('purchaseType') == 'GamePass' and data.get('productId') == target_gamepass_id:
        username = data.get('username')
        gamepass_name = data.get('gamePassName')
        message = f"User {username} has purchased the specific gamepass: {gamepass_name}"
        
        # Send the webhook notification to Discord
        send_discord_webhook(message)
    
    return "Webhook received successfully"

if __name__ == '__main__':
    app.run(debug=True)
