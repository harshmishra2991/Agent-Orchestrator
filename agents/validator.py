def validator(context):
   
    result = {
        "status": None,
        "context": None,
        "message": None
    }

    if 'destination' not in context:
        result["status"] = "needs_clarification"
        result["message"] = "destination missing"
        return result
    if 'travel_mode' not in context:
        result["status"] = "needs_clarification"
        result["message"] = "travel mode is missing"
        return result
    if 'travel_date' not in context:
        result["status"] = "needs_clarification"
        result["message"] = "travel_date is missing" 
        return result 

    result["status"] = "success"
    result["context"] = context.copy()

    return result          