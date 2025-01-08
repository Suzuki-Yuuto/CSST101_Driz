import re

def evaluate(statement, values):
    # Replace variables in the statement with their corresponding values
    for var, val in values.items():
        statement = re.sub(r'\b' + re.escape(var) + r'\b', str(val), statement)
    
    # Replace logical operators with Python's equivalents
    statement = statement.replace('AND', 'and').replace('OR', 'or').replace('NOT', 'not')
    
    # Evaluate the modified statement
    try:
        return eval(statement)
    except Exception as e:
        return f"Error evaluating statement: {e}"