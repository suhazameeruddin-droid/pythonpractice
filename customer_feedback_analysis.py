def calculate_positive_feedback(ratings):
    if not ratings:
        return "No ratings available."
    
    positive = sum(1 for r in ratings if r >= 4)
    percentage = (positive / len(ratings)) * 100
    return f"Positive Feedback: {round(percentage, 2)}%"

# Example input
ratings = [5, 4, 3, 5, 2, 4, 1, 5]

# Output
print(calculate_positive_feedback(ratings))
