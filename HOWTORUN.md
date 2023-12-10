# Disability Detection Django App

This Django web application allows users to upload images and detects disabilities based on a pre-trained model.

## Installation

1. Clone the repository:

    ```bash
    cd DisabilityDetection
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:
        ```bash
        venv\Scripts\activate
        ```

    - On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1. Navigate to the project directory:

    ```bash
    cd DisabilityDetection
    ```

2. Run the Django development server:

    ```bash
    python manage.py runserver
    ```

3. Access the application in your web browser at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Admin Login

- **Username:** admin
- **Password:** 1234

## Additional Notes

- Ensure you have the necessary permissions to access the directory for uploading images.
- The project assumes a pre-trained model is saved and located at the specified path.
- Adjust paths and configurations according to your project structure and requirements.
