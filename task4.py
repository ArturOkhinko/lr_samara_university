def get_sale_count(names_medications):
    sales_count = {}
    for medication in names_medications:
        update_sales_count(medication, sales_count)
        
    return sales_count

def update_sales_count(medication, sales_count):
    medication_is_empty = medication in sales_count
    if medication_is_empty:
        sales_count[medication] = sales_count[medication] + 1
        return
    sales_count[medication] = 1


names_medications = [
    "оземпик", "семавик", "оземпик", "квинсент", "квинсент", "семавик",
    "квинсент", "оземпик", "семавик", "квинсент", "семавик", "семавик",
    "оземпик", "семавик", "оземпик", "квинсент", "квинсент", "семавик",
    "квинсент", "оземпик", "семавик", "квинсент", "семавик", "семавик",
    "оземпик", "семавик", "оземпик", "квинсент", "квинсент", "семавик",
    "квинсент", "оземпик", "семавик", "квинсент", "семавик", "семавик",
    "оземпик", "семавик", "оземпик", "квинсент", "квинсент", "семавик",
    "квинсент", "оземпик", "семавик", "квинсент", "семавик", "семавик",
    "оземпик", "семавик", "оземпик", "квинсент", "квинсент", "семавик",
    "квинсент", "оземпик", "семавик", "квинсент", "семавик", "семавик"
]

get_sale_count(names_medications)