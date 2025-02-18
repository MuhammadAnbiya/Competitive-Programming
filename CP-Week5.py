from datetime import datetime

def count_letters_in_date_range(filename, start_date, end_date):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        count = 0

        for line in lines:
            date, _ = line.strip().split(',', 1)
            current_date = datetime.strptime(date, "%Y-%m-%d")
            if start_date <= current_date <= end_date:
                count += 1
        
        return count
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {e}"


filename = input().strip()
start_date = input().strip()
end_date = input().strip()

result = count_letters_in_date_range(filename, start_date, end_date)
print(result)
