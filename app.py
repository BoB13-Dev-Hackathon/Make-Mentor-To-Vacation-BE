from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = 'test_key'

MODEL_ID = 'test_key'

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    prompt = data.get('prompt', '')

    try:
        response = openai.Completion.create(
            model=MODEL_ID,
            prompt=prompt,
            max_tokens=150,
            temperature=0.7
        )
        model_response = response['choices'][0]['text'].strip()
        return jsonify({'response': model_response})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
