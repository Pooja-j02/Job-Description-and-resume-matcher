import os

# Basic settings for Flask
# class Config:
#     # Flask app settings
#     SECRET_KEY = os.urandom(24)  # Used for session cookies and security
#     UPLOAD_FOLDER = 'uploads/'  # Folder where uploaded files will be stored
#     ALLOWED_EXTENSIONS = {'pdf', 'docx', 'txt'}  # Allowed file extensions
#     MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # Max file size limit (16 MB)
#     DEBUG = True  # Set to False in production
#     HOST = '127.0.0.1'  # Localhost binding
#     PORT = 5000  # Port to run the Flask app on

class Config:
    UPLOAD_FOLDER = 'uploads/'
    HOST = '127.0.0.1'
    PORT = 5000
    DEBUG = True


# For production, you can add configurations for security or scaling, but the above are the most basic settings.
