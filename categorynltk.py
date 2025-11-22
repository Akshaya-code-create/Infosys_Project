"""NLP-based Transaction Categorization"""
import re

ALL_CATEGORIES = [
    "Food & Dining", "Groceries", "Transportation", "Shopping",
    "Entertainment", "Utilities", "Healthcare", "Rent & Housing",
    "Education", "Travel", "Personal Care", "Income", "Other"
]

CATEGORY_KEYWORDS = {
    "Food & Dining": ["restaurant", "food", "dining", "lunch", "dinner", "breakfast", 
                      "cafe", "coffee", "pizza", "burger", "mcdonald", "kfc", "domino", "starbucks"],
    "Groceries": ["grocery", "dmart", "reliance", "big bazaar", "supermarket", "vegetables", "fruits"],
    "Transportation": ["uber", "ola", "taxi", "cab", "auto", "petrol", "diesel", "parking", "metro"],
    "Shopping": ["amazon", "flipkart", "myntra", "shopping", "mall", "clothes", "electronics"],
    "Entertainment": ["movie", "netflix", "spotify", "game", "pvr", "inox", "cinema"],
    "Utilities": ["electricity", "water", "internet", "wifi", "phone", "recharge", "gas bill"],
    "Healthcare": ["doctor", "hospital", "pharmacy", "medicine", "medical", "clinic"],
    "Rent & Housing": ["rent", "lease", "apartment", "flat", "maintenance"],
    "Education": ["school", "college", "course", "book", "tuition", "fees"],
    "Travel": ["hotel", "flight", "vacation", "trip", "travel"],
    "Personal Care": ["salon", "gym", "spa", "fitness"],
    "Income": ["salary", "income", "payment", "bonus", "freelance"]
}

def categorize_expense(description, transaction_type="Expense"):
    if transaction_type and transaction_type.lower() == "income":
        return "Income"
    
    desc_lower = description.lower()
    for category, keywords in CATEGORY_KEYWORDS.items():
        if category == "Income":
            continue
        for keyword in keywords:
            if keyword in desc_lower:
                return category
    return "Other"
