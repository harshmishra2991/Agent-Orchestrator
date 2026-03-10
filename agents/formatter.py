def formatter(context):
    best_options = context["best_options"]
    successful_count = context["successful_count"]
    failed_count = context["failed_count"]
    message = f"I found {successful_count} flight option(s).\n\n"

    message += "Best flight options:\n"

    for option in best_options:
        provider = option["provider"]
        price = option["price"]

        message += f"- {provider} : ${price}\n"

    if failed_count > 0:
        message += f"\n Note: {failed_count} provider(s) did not respond"

    new_context = context.copy()

    return {
        "status": "success",
        "context": new_context,
        "message": message
    }        