class User:
    # Precondition: Password must be at least 8 characters long
    def set_password(self, password: str):
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long!")
        print("Password set successfully")


class AdminUser(User):
    # LSP-compliant: Weakens the precondition
    # Now allows passwords with at least 6 characters
    def set_password(self, password: str):
        if len(password) < 6:
            raise ValueError("Password must be at least 6 characters long!")
        print("Password set successfully")


if __name__ == "__main__":
    user: User = AdminUser()
    user.set_password("Admin1")  # Works fine: AdminUser allows shorter passwords
