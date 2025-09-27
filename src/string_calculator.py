class StringCalculator:
    """String Calculator implementation following TDD approach"""
    
    def add(self, numbers: str) -> int:
        """Add method that takes a string of numbers and returns their sum"""
        if numbers == "":
            return 0