def aggregator(context):
    results = context["provider_results"]

    succeesful = []
    failed = []

    for r in results:
        if r['status'] == "success":
            succeesful.append(r)
        else:
            failed.append(r)

    new_context = context.copy()

    if len(succeesful) == 0:
        return{
            "status" : "failure",
            "context": new_context,
            "message": "All providers failed. Please try again later"
            }

    min_price = succeesful[0]["price"] 

    for r in succeesful:
        if r['price'] < min_price:
            min_price = r['price']

    best_options = []

    for r in succeesful:
        if r['price'] == min_price:
            best_options.append(r)

    new_context['best_options'] = best_options
    new_context['successful_count'] = len(succeesful)
    new_context['failed_count'] = len(failed)

    failed_provider_names = []

    for r in failed:
        failed_provider_names.append(r['provider'])

    new_context['failed_providers'] = failed_provider_names

    return{
        "status": "success",
        "context": new_context,
        "message": None
    }  


                