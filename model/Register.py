from password_strength import PasswordPolicy
from email_validator import validate_email, EmailNotValidError

def validatePasswordStrength(pwd):
        policy = PasswordPolicy.from_names(
        length=8,  # min length: 8
        uppercase=1,  # need min. 2 uppercase letters
        numbers=2,  # need min. 2 digits
        special=1,  # need min. 2 special characters
      )

        return len(policy.test(pwd))==0

def ensurePasswordsAreEqual(psw, repeat_psw):

    return psw == repeat_psw

def emailValidator(email):
    try:
        # Check that the email address is valid.
        validation = validate_email(email)

        # Take the normalized form of the email address
        # for all logic beyond this point (especially
        # before going to a database query where equality
        # may not take into account Unicode normalization).
        email = validation.email
    except EmailNotValidError as e:
        # Email is not valid.
        # The exception message is human-readable.
        print(str(e))
        return False

    return True

