"""
Core functionality for BANANA-AI.
"""

class BananaAI:
    """Main class for BANANA-AI functionality."""
    
    def __init__(self):
        """Initialize the BananaAI instance."""
        self.version = "0.1.0"
    
    def get_version(self):
        """Get the current version of BANANA-AI."""
        return self.version
    
    def square(self, number):
        """Calculate the square of a number.
        
        Args:
            number (int): The number to square.
            
        Returns:
            int: The square of the input number.
        """
        return number * number 