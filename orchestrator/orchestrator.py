from concurrent.futures import ThreadPoolExecutor, as_completed, TimeoutError
class Orchestrator:
    def __init__(self,steps):
        self.steps = steps
        self.execution_trace = []

    def run(self, initial_context):
        context = initial_context

        for agent in self.steps:
            result = agent(context)

            self.execution_trace.append({
                "agent": agent.__name__,
                "status": result["status"]
                })   
            
            if result["status"] == "success":
                context = result["context"]
            elif result["status"] == "needs_clarification":
                return {
                    "status": "needs_clarification",
                    "message": result["message"],
                    "trace":self.execution_trace
                }
            else:
                return{
                    "status": "failed",
                    "context": context,
                    "trace": self.execution_trace
                }
        return{
            "status" : "success",
            "context" : context,
            "trace" : self.execution_trace
        }        
    
    def run_parallel(self, agents, context, timeout = 3):
        results = []

        with ThreadPoolExecutor() as executor:
            futures = {}
            for agent in agents:
                future = executor.submit(agent, context)
                futures[future] = agent.__name__
                
            try:
                for future in as_completed(futures, timeout= timeout):
                    result = future.result()
                    results.append(result)
            except TimeoutError:
                print("global timeout reached")

            for future, agent_name in futures.items():
                if not future.done():
                    results.append({
                        "status": "failure",
                        "provider": agent_name,
                        "price":None,
                        "reason": "timeout"
                    })

        return results
        
                    

