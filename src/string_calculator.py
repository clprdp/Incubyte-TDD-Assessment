class StringCalculator:
    
    def add(self, numbers: str) -> int:
        if numbers == "":
            return 0
        
        if numbers.startswith("//"):
            lines = numbers.split('\n', 1)
            delimiter_line = lines[0]
            numbers_part = lines[1] if len(lines) > 1 else ""
            delimiter = delimiter_line[2:]
            numbers = numbers_part.replace(delimiter, ',')
        
        numbers = numbers.replace('\n', ',')
        number_list = numbers.split(',')
        
        negative_numbers = [num for num in number_list if num.startswith('-') and num != '-']
        if negative_numbers:
            message = "negative numbers not allowed " + ", ".join(negative_numbers)
            raise ValueError(message)
        
        # Filter out numbers bigger than 1000
        valid_numbers = [int(num) for num in number_list if int(num) <= 1000]
        return sum(valid_numbers)