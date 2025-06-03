class Utiles:
    @staticmethod
    def validar_email(email):
        return "@" in email and "." in email.split("@")[1]
        
print(Utiles.validar_email("test@example.com"))  # True
