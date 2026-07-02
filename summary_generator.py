from ollama import chat

def summarize_contract(text):

    response = chat(
        model='phi4',
        messages=[
            {
                'role':'user',
                'content':f'''
                Analyze this contract.

                Give:
                1 Risks
                2 Fees
                3 Deadlines
                4 Summary

                {text}
                '''
            }
        ]
    )

    return response["message"]["content"]
