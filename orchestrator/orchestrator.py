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

