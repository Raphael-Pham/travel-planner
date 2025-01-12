# Travel Planner App

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction
The Travel Planner App is a web application designed to help users plan and manage their trips. Users can create trips, add transportation details, and share trips with other users.

## Features
- User registration and authentication
- Create and manage trips
- Add transportation details to trips
- Share trips with multiple users
- Responsive design

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/travel-planner.git
    ```
2. Navigate to the project directory:
    ```bash
    cd travel-planner
    ```
3. Create a virtual environment:
    ```bash
    python3 -m venv venv
    ```
4. Activate the virtual environment:
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
5. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
6. Apply the migrations:
    ```bash
    python manage.py migrate
    ```
7. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```
8. Run the development server:
    ```bash
    python manage.py runserver
    ```

## Usage
1. Open your web browser and navigate to `http://127.0.0.1:8000/`.
2. Register a new account or log in with an existing account.
3. Create a new trip and add transportation details.
4. Share the trip with other users.

## Contributing
Contributions are welcome! Please follow these steps to contribute:
1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature/your-feature-name
    ```
3. Make your changes and commit them:
    ```bash
    git commit -m 'Add some feature'
    ```
4. Push to the branch:
    ```bash
    git push origin feature/your-feature-name
    ```
5. Open a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For any questions or suggestions, please contact:
- Your Name - raphaelpham14@gmail.com (mailto:your.email@example.com)
- GitHub: Raphael-Pham (https://github.com/raphael-pham)