# IBM_AUTOGRADER

#### NOTE: 
The model could not be uploaded on Github directly due to file size restrictions, hence the model has been uploaded with tokenizers in drive link below<br>
[T_5 Autograder Model](https://drive.google.com/drive/folders/1r2P0PzB5u2a4xhI4hFaa_l0RZRYw5sb-?usp=sharing)


## File Structure

```
.
├── LICENSE
├── README.md
├── autograder/ -> Django app for endpoints
├── IBM -> Project configurations
├── manage.py
└── requirements.txt
```


## Technology Stack

#### Backend
- Django 3.0+ (Python 3.6+)
- Django REST Framework (3.10+)
- PyTorch (1.9.0)
- Numpy
- NLTK
- Spacy
- Tenserflow

## Build Instructions

#### Backend
```bash
  pip3 install -r requirements.txt
  python3 manage.py makemigrations
  python3 manage.py migrate
  python3 manage.py runserver
```
Addidionally, one may require to install [Rust Compiler](https://static.rust-lang.org/rustup/dist/x86_64-pc-windows-msvc/rustup-init.exe) for one of the dependency fpr Windows and certain versions of pip

## Developers         
1. Harsh Vartak (60004180028)
2. Kanishk Shah (60004180042)
3. Govind Thakur (60004180024)
4. Manali Maniyar (60004180048)
5. Naman Dangi (60004180056)
6. Onkar Thorat (60004180067)
