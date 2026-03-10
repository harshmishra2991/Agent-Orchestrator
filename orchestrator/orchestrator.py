from concurrent.futures import ThreadPoolExecutor, as_completed, TimeoutError
import time
class Orchestrator:
    def __init__(self,steps):
        self.steps = steps
        self.execution_trace = []
    def run_parallel(self, agents, context, timeout = 3):
        results = []

        with ThreadPoolExecutor() as executor:
            futures = {}
            for agent in agents:
                start_time = time.time()
                future = executor.submit(agent, context)
                futures[future] = (agent.__name__,start_time)
                
            try:
                for future in as_completed(futures, timeout= timeout):
                    agent_name, start_time = futures[future]
                    result = future.result()
                    end_time = time.time()
                    duration_ms = int((end_time - start_time) * 1000)
                    results.append(result)

                    self.execution_trace.append({
                        "agent": result["provider"],
                        "status": result["status"],
                        "duration_ms": duration_ms
                    })
            except TimeoutError:
                print("global timeout reached")

            for future, (agent_name, start_time) in futures.items():
                if not future.done():
                    duration_ms = int((time.time() - start_time) * 1000)
                    results.append({
                        "status": "failure",
                        "provider": agent_name,
                        "price":None,
                        "reason": "timeout"
                    })
                    self.execution_trace.append({
                        "agent": agent_name,
                        "status": "timeout",
                        "duration_ms": duration_ms
                    })

        return results
    
    def run(self, initial_context):
        context = initial_context

        for agent in self.steps:

            if isinstance(agent, list):
                parallel_results = self.run_parallel(agent, context)
                context = context.copy()
                context['provider_results'] = parallel_results

                self.execution_trace.append({
                    "agent": "parallel providers",
                    "status": "completed"
                })
                continue
             
            start_time = time.time()
            result = agent(context)
            end_time = time.time()
            duration_ms = int((end_time - start_time) * 1000)


            self.execution_trace.append({
                "agent": agent.__name__,
                "status": result["status"],
                "duration_ms": duration_ms
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
            "message": result.get("message"),
            "trace" : self.execution_trace
        }        
    
   
        
                    

