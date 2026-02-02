def parser(context):
    user_input = context.get("user_input", "").lower()
    result = {
        "status": None,
        "context": None,
        "message": None
    }


    if "paris" not in user_input:
        result["status"] = "needs_clarification"
        result["message"] = "Please provide destination"
        return result
    if "flight" not in user_input: 
        result["status"] = "needs_clarification"
        result["message"] = "Please provide travel mode"
        return result
    if "friday" not in user_input: 
        result["status"] = "needs_clarification"
        result["message"] = "Please provide travel date"
        return result
    
    new_context = context.copy()
    new_context["destination"] = "paris"
    new_context["travel_mode"] ="flight"
    new_context["travel_date"] = "friday"

    result["status"] = "success"
    result["context"] = new_context

    return result