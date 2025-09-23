from datetime import datetime

class TimeUtils:
    @staticmethod
    def get_current_time() -> str:
        # Returns current time as a string, similar to C++ ctime()
        return datetime.now().strftime("%a %b %d %H:%M:%S %Y")
