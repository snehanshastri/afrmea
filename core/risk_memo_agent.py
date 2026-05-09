import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-3-flash-preview")


def generate_risk_memo(evaluation_result):

    prompt = f"""
You are a financial analyst working at a bank.

Analyze the following company financial evaluation data and generate a professional internal risk memo.

DATA:
{evaluation_result}

The memo should include:
- Overall Risk Level
- Key Financial Observations
- Risk Factors Identified
- Suggested Actions

Keep it concise, formal, and professional.
"""

    response = model.generate_content(prompt)

    return response.text