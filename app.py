from flask import Flask, request, jsonify
from app_config import SERVICES
import logging

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

services = {}


@app.route('/services/add', methods=['POST'])
def add_service():
    """
        Adds a new service to the registry.
        Request format: JSON with 'name' (string) and 'url' (reference to the implementation)
        Response:
            - Success: JSON with a message, status code 200
            - Failure: JSON with an error message, status code 400 (Bad Request) or 409 (Conflict)
    """
    service_data = request.json
    service_name = service_data.get('name')

    if not service_name:
        return jsonify({'error': 'Service name is required'}), 400

    if service_name in services:
        return jsonify({'error': f'Service {service_name} already exists'}), 409

    services[service_name] = service_data.get('url')
    print(services)
    return jsonify({'message': f'Service {service_name} added'}), 200


# Endpoint to remove a service
@app.route('/services/<service_name>', methods=['DELETE'])
def remove_service(service_name):
    """
       Removes a service from the registry.
       Request format: Service name included in the URL path
       Response:
           - Success: JSON with a message, status code 200
           - Failure: JSON with an error message, status code 404 (Not Found)
    """

    if service_name in services:
        del services[service_name]
        print(services)
        return jsonify({'message': f'Service {service_name} removed'}), 200
    return jsonify({'error': 'Service not found'}), 404


# Endpoint to list all available services
@app.route('/services', methods=['GET'])
def list_services():
    """
        Lists all available services in the registry.
        Request format: None (GET request)
        Response:
            - Success: JSON with a list of services, status code 200
            - Failure: JSON with an error message, status code 500 (Internal Server Error)
    """
    try:
        available_services = list(services.keys())
        return jsonify({'services': available_services}), 200
    except Exception as e:
        return jsonify({'error': 'Failed to retrieve services', 'details': str(e)}), 500


@app.route('/analyze', methods=['POST'])
def analyze_text():
    """
       Analyzes text using the specified text analysis service.

       Expects a POST request with a JSON payload containing:
       - 'service': The name of the text analysis service to use.
       - 'text': The text to be analyzed.

       Returns:
       - A JSON response with the analysis result, status code 200 on success.
       - An error message with status code 400 if 'service' or 'text' is missing,
         or if an error occurs during the execution of the service.
       - An error message with status code 404 if the specified service is not found.

       Example Request:
           POST /analyze
           {
               "service": "sentiment_analysis",
               "text": "I love sunny days!"
           }
    """
    data = request.json

    service_name = data.get('service')
    text = data.get('text')

    if not service_name:
        return jsonify({'error': 'Service name is missing.'}), 400

    if not text:
        return jsonify({'error': 'Text is missing.'}), 400

    if service_name in services:
        function = SERVICES[service_name]
        try:
            result = function(text)
        except Exception as e:
            logging.error('Error at %s', exc_info=e)
            return jsonify({'error': 'Invalid text! Only strings should be passed to the text input.'}), 400
    else:
        return jsonify({'error': f'Service "{service_name}" not found.'}), 404

    return jsonify({'result': result}), 200


if __name__ == '__main__':
    app.run()
