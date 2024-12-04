## LICENSE
[LICENSE](LICENSE)


## Prerequisites

Make sure you have the following installed on your machine:

- Python 3.x
- `pip` (comes with Python installation)

## Installation

Follow these steps to set up and run the Flask application:

1. **Clone the Repository**: Open your terminal or command prompt, and run:

    ```bash
    git clone https://github.com/your-username/your-repo.git
    ```

2. **Navigate to the Project Directory**:

    ```bash
    cd your-repo
    ```

3. **Create a Virtual Environment**:
    - For Linux/Mac:

        ```bash
        python3 -m venv venv
        ```

    - For Windows:

        ```bash
        python -m venv venv
        ```

4. **Activate the Virtual Environment**:
    - For Linux/Mac:

        ```bash
        source venv/bin/activate
        ```

    - For Windows:

        ```bash
        venv\Scripts\activate
        ```

5. **Install Dependencies**:

    After activating the virtual environment, install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

    *(Make sure you have a `requirements.txt` file in your project directory that lists your Flask app's dependencies.)*

## Usage

To run the Flask application, execute the following command:
Before that make sure you have gemini api key then save the key to .env as:  ```GOOGLE_API_KEY =<api_key>```

```bash
python app.py
```

The application will be available at http://127.0.0.1:5000/. You can visit this URL in your web browser to access the app.
