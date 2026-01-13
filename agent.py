import ollama
import re
import platform

class ArtefactAgent:
    def __init__(self, model_name: str = "phi3"):
        self.model_name = model_name

    def _calculator_tool(self, expression: str) -> str:
        """Core tool for mathematical precision."""
        try:
            # Clean expression: keep only numbers and operators
            clean_expr = re.sub(r'[^0-9+\-*/().]', '', expression)
            if not any(op in clean_expr for op in "+-*/"):
                return "Error: No operators found for calculation."
            return str(eval(clean_expr))
        except Exception:
            return "Math Error: Could not process expression."

    def _classify_intent(self, question: str) -> str:
        """Determines if the question is MATH, or GENERAL."""
        prompt = (
            f"Question: '{question}'\n"
            "Classify into ONLY ONE category:\n"
            "- MATH: If it's a calculation.\n"
            "- GENERAL: If it's a general question.\n"
            "Answer ONLY with the category name."
        )
        try:
            res = ollama.chat(model=self.model_name, messages=[{'role': 'user', 'content': prompt}])
            return res['message']['content'].strip().upper()
        except:
            return "GENERAL"

    def run(self):
        print(f"\n{'='*50}")
        print("   ARTEFACT AI AGENT   ")
        print(f"{'='*50}")
        print("Capabilities: Calculator | Knowledge")
        print("Type 'exit' to quit.\n")

        while True:
            user_input = input("USER > ").strip()
            if user_input.lower() in ['exit', 'quit']: break
            if not user_input: continue

            category = self._classify_intent(user_input)

            if "MATH" in category:
                print("DEBUG: [Routing to Calculator]")
                p_extract = f"Extract ONLY the numbers and operators from: '{user_input}'. Ex: 2+2"
                expr = ollama.chat(model=self.model_name, messages=[{'role': 'user', 'content': p_extract}])['message']['content'].strip()
                result = self._calculator_tool(expr)
                print(f"AGENT (Math) > The result is {result}")
            else:
                print("DEBUG: [Routing to General Knowledge]")
                response = ollama.chat(model=self.model_name, messages=[{'role': 'user', 'content': user_input}])
                print(f"AGENT > {response['message']['content']}")
            
            print("-" * 50)

if __name__ == "__main__":
    ArtefactAgent().run()