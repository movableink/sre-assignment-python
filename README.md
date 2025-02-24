# GeoIP Service

A Python-based service that provides geographical information for IP addresses using the Movable Ink GeoIP API.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/movableink/sre-assignment-python.git
cd sre-assignment-python
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

The service requires the following environment variables:

- `API_URL`: The base URL for the Movable Ink GeoIP API (default: http://localhost:8000). A production URL will be provided by Movable Ink.
- `API_TOKEN`: Your API token for authentication with the Movable Ink GeoIP API. This is required for production use.
- `PORT`: The port number for the service (default: 3000)

Example configuration:
```bash
export API_URL="https://geoip.movableink.com"
export API_TOKEN="your-token-here"
export PORT=3000  # optional
```

## Running the Service

Start the service (don't forget to set your environment variables before starting):
```bash
python run.py
```

The service will be available at `http://localhost:3000`.

## API Endpoints

### GET /lookup/:ip

Returns geographical information for the specified IP address.

Example request:
```bash
curl http://localhost:3000/lookup/8.8.8.8
```

Example successful response:
```json
{
  "ip": "8.8.8.8",
  "location": "United States",
  "postal_code": "",
  "network_name": "AS15169 GOOGLE",
  "domain": "Google",
  "latitude": 37.751,
  "longitude": -97.822
}
```

Example error response (500 Internal Server Error):
```json
{
  "error": "API request failed: <error details>"
}
```

## Testing

### IP Address Testing Script

The repository includes a bash script (`test-ips.sh`) that tests the service with a list of IP addresses from `test_ips.txt`. If test_ips.txt is not available you can create your own file and enter an ip address per line for testing. For the assignment the test_ips.txt file will be provided by Movable Ink.

To run the tests:

1. Make sure the service is running in one terminal:
```bash
python run.py
```

2. In another terminal, run the test script:
```bash
./test-ips.sh
```

The script will:
- Process each IP address in `test_ips.txt`
- Show progress every 100 requests
- Display a summary including:
  - Total number of requests
  - Total time taken
  - Average requests per second
  - Distribution of HTTP status codes

## Project Structure

- `src/`: Main package directory
  - `__init__.py`: Package initialization
  - `config.py`: Configuration management
  - `geoip.py`: GeoIP service implementation
  - `server.py`: Flask server and route definitions
- `run.py`: Application entry point
- `requirements.txt`: Python dependencies
- `test-ips.sh`: Testing script

## License

This project is proprietary and confidential to Movable Ink.
