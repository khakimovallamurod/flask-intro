from flask import Flask, request

app = Flask(__name__)

usd = 12737 # 1 USD = 12 737 UZS

@app.route('/api/to-usd/', methods=['GET'])
def to_usd():
    """
    Convert to USD

    Returns:
        json: Converted amounts
    
    Note:
        request data will be like this:
            /api/to-usd?amount=1000
        
        response will be like this:
            {
                "amount": 1000,
                "currency": "UZS",
                "converted": 88.7,
                "convertedCurrency": "USD"
            }
    """
    

@app.route('/api/to-uzs', methods=['GET'])
def to_uzs():
    """
    Convert to UZS

    Returns:
        json: Converted amount
    
    Note:
        request data will be like this:
            /api/to-uzs?amount=1000
        
        response will be like this:
            {
                "amount": 1000,
                "currency": "USD",
                "converted": 1138070,
                "convertedCurrency": "UZS"
            }
    """
    return 
if __name__ == '__main__':
    app.run(port=8080, debug=True)    

