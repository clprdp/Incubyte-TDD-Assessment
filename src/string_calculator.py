class StringCalculator:
    
    def add(self, numbers: str) -> int:
        """Add method that takes a string of numbers and returns their sum"""
        if numbers == "":
            return 0
        
        numbers = numbers.replace('\n', ',')
        number_list = numbers.split(',')
        return sum(int(num) for num in number_list)