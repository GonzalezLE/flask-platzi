import firebase_admin
from firebase_admin import credentials,firestore


key = {
    "type": "service_account",
    "project_id": "platzi-py-b3d83",
    "private_key_id": "09ba49d1135b6056718952f30c30259f295b133b",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCdm24OJSIiicDx\n335/Evc6XDGcPAGdZX23RieTZcLGse7UTjTntq0PYp3L0Qt8BzovBSXENLeKpSnU\nSoDEXqB9M0vLcX5DpaSRAvgkHBUXhoHQa+QyisaKG5xMy6HbxlUvZXkTTvuhzgEE\n5CYTH/XyM7zukThBL2sYjJSrkuI1wqVXGO9traOr+doN/j8bTLNFC7LkkE6C/gAP\nLY1nxFVYT71CBS2yax4ecPVgOfklDqiJiiUZ+JXzitEmzuCSr+0tJJwLC4pCj/YF\nW9YkY8zU/Fm0PH9UoAO/NPwRVIgGIbHxwJy2dWm3MdTyrGC+hvIU2WU6k6CrMcbE\nnll1ugd9AgMBAAECggEABOzwyBK4rzakkoqRuVFI67MqPmqRAa/EeYqrkvYzsPeq\nR0qjFE4dDiWJWUTRDzu/QZfvbGMvYe8JJcrRnRF4rOECWzsn9IpD4IpPYfraB+Ww\nFJOX9U0T/l31iQrg0JhcB4KsLC0kPRQjQQQLp+kFoTT6ZcRLwJxwRDtPLCYyLqGN\nmHMFFS38NBcTI5WOUSR6dAeTrwI94MD8kaqpZ5mj26mX8AklGfzE1L33qbmAvn+u\n89soO7i+xWfBXEMJOV2GTsJQVYBcJo6mf79P8KojyJqvBeovUiB8n9//cRHFnP3n\nNF9W0UR4wQKxpINCoHUdcswu3zl6jZyJwYbZ9frIkQKBgQDRyFV/PFeeYuR3dbIC\nFKgDfd+ruGXLyxpVwiH5FjAxmPGOSGXH2LjQ1Pay+lqg5Ru1NQXb6U6eiQaZr7T+\n50f+VrBoOVvLH+2OAfcwsXYVrdrDsSr+5TmJ4DT6ndglFIXXw0NWYb6dL0bONXsE\n/hdZY9tZ3iorQgv5mPuay7MOWQKBgQDAVGug/0TkDLMSpOBnxLycN1Nk3M6Nl84A\na645UG1l5E72wVNDC4VpXeBIpO4ORsUggk/SFwXbEPU8m8cZLWfuora6H3frbwcu\nx9vs94MQXXbVfphGFqPQjEh7JCHe++sc6Z1PlnGCn1w00ElmyT0CFu0Ln1zXdDf7\ns0HRFGJFxQKBgCCIE5IWlnPOXCWWT9N4xpE8DNqBTu/qgBv6bfBFm5WlZRgua/Iw\nzoA79kHNBw7aWJCiN1Vh+bol/6sHj2bUENsFMHgJJQ371ofmECIx8uDrw/gC2msK\nuwCBj1Wp8qHVa+gItMGJiNixQyapLnmYuaA4FwT5qcpphJfhPGtF2W+JAoGAGRvs\nYTxyVgOCbXCxC1sX9J0UehqJrNqgvlVQjZL+dUr1NCnRIPOkGzlySomduqdqnO/m\nU9tFnG/+VEdSGuteoj0D9hCdq1L3cRgOkkVOCxjopr68SooyIMvvuoPhGCdzbnbh\nXr6ZWyBK/Woj6xNir58mm1nW2RoHJQkmEpHCsrECgYBlDVv/6J9fcYORKkowbhtd\nIZlPdKLKaHuYuIurPCbkqgrPESp/PuDYIXXydrwUKb1SDOrDuIsj34kFsSooi5qv\nQ9lvnoCgj5hro7aLLpxsD3c6jjdY69yeUO41Kulo922O5wFOEG9XJCIEPKIBJpWG\nhPBkGIABZIpp/hxRoH9OBg==\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-7whav@platzi-py-b3d83.iam.gserviceaccount.com",
    "client_id": "112771958500894480684",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-7whav%40platzi-py-b3d83.iam.gserviceaccount.com"
}


cred = credentials.Certificate(key)
firebase_admin.initialize_app(cred)


db:firestore = firestore.client()


def get_users():
    return db.collection('users').get()


def get_todos(user_id):
    
    return db.collection('users').document(user_id).collection('todos').get()






