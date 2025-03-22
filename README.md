# Symmetric Encryption App

## Overview

This project is a web application built using Django (backend) and React (frontend) that provides symmetric encryption and decryption functionalities. The application supports multiple encryption algorithms, including **DES3 (Triple DES)**, **OTP (One-Time Pad)**, and **AES (Advanced Encryption Standard)**. It is designed to be a user-friendly tool for securely encrypting and decrypting sensitive data.

## Features

- **Symmetric Encryption Algorithms**:
  - **DES3 (Triple DES)**: A symmetric-key block cipher that applies the DES algorithm three times to each data block.
  - **OTP (One-Time Pad)**: An encryption technique that requires a one-time pre-shared key of the same length as the message.
  - **AES (Advanced Encryption Standard)**: A widely used symmetric encryption algorithm that supports key lengths of 128, 192, and 256 bits.

- **User-Friendly Interface**:
  - A React-based frontend for seamless interaction with the encryption and decryption processes.
  - Easy-to-use forms for inputting text, selecting encryption algorithms, and providing keys.

- **Secure Key Management**:
  - Users can input their own encryption keys for enhanced security.
  - Keys are not stored on the server, ensuring data privacy.

- **Cross-Platform Compatibility**:
  - The app is accessible via any modern web browser.

## Technologies Used

- **Backend**:
  - **Django**: A high-level Python web framework for building secure and scalable web applications.
  - **Cryptography Libraries**: Python libraries such as `pycryptodome` or `cryptography` for implementing DES3, OTP, and AES encryption algorithms.

- **Frontend**:
  - **React**: A JavaScript library for building interactive and responsive user interfaces.
  - **Axios**: For making HTTP requests to the Django backend.

- **Other Tools**:
  - **Django REST Framework (DRF)**: For building RESTful APIs to handle encryption and decryption requests.
  - **Webpack/Babel**: For bundling and transpiling React code.

## Installation

### Prerequisites

- Python 3.8 or higher
- Node.js and npm (for React)
- PostgreSQL (or any other database supported by Django)

### Backend Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/symmetric-encryption-app.git
   cd symmetric-encryption-app/backend
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   - Update the `DATABASES` configuration in `settings.py` with your database credentials.
   - Run migrations:
     ```bash
     python manage.py migrate
     ```

5. Start the Django development server:
   ```bash
   python manage.py runserver
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd ../frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the React development server:
   ```bash
   npm start
   ```

4. The app should now be running on `http://localhost:3000`.

## Usage

1. Open the app in your browser.
2. Select the encryption algorithm (DES3, OTP, or AES) from the dropdown menu.
3. Enter the text you want to encrypt or decrypt.
4. Provide the encryption key (ensure it meets the requirements for the selected algorithm).
5. Click the "Encrypt" or "Decrypt" button to process the data.
6. View the result in the output field.

## API Endpoints

The Django backend exposes the following REST API endpoints:

- **POST `/api/encrypt/`**:
  - Request Body:
    ```json
    {
      "algorithm": "DES3",  // or "OTP", "AES"
      "text": "Your plaintext here",
      "key": "Your encryption key here"
    }
    ```
  - Response:
    ```json
    {
      "encrypted_text": "Encrypted output here"
    }
    ```

- **POST `/api/decrypt/`**:
  - Request Body:
    ```json
    {
      "algorithm": "DES3",  // or "OTP", "AES"
      "encrypted_text": "Your encrypted text here",
      "key": "Your decryption key here"
    }
    ```
  - Response:
    ```json
    {
      "decrypted_text": "Decrypted output here"
    }
    ```

## Encryption Algorithms

### DES3 (Triple DES)
- **Key Length**: 168 bits (3 × 56-bit DES keys).
- **Block Size**: 64 bits.
- **Security**: Provides stronger security than DES by applying the DES algorithm three times.

### OTP (One-Time Pad)
- **Key Length**: Must be at least as long as the plaintext.
- **Security**: Provides perfect secrecy if the key is truly random and used only once.

### AES (Advanced Encryption Standard)
- **Key Length**: 128, 192, or 256 bits.
- **Block Size**: 128 bits.
- **Security**: Highly secure and widely used in modern applications.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push to the branch.
4. Submit a pull request with a detailed description of your changes.


## Acknowledgments

- Thanks to the Django and React communities for their excellent documentation and resources.
- Special thanks to the developers of the cryptography libraries used in this project.

## Contact

For questions or feedback, please reach out to yohannesmengistie634@gmail.com.

