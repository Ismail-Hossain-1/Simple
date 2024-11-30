from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
import google.generativeai as genai
import os
# Load environment variables from .env file
load_dotenv()


genai.configure(api_key=os.environ["GOOGLE_API_KEY"])


# Initialize Flask app
app = Flask(__name__)

# Enable CORS for specific origin
CORS(app)
model = genai.GenerativeModel('gemini-1.5-flash')


@app.route('/')
def hello_world():
    
    return 'Hello, World!'
@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    msg= data['text']
    language = data['langName']
    print("input :",language)
    prompt=f"""
            Your are a multilingual expert capable of translating from any language to any language. See the example input and output which are given for multiple language , but you will response in  {language}: 
            if the input is a single word, for example- 
            
            example 1(single word):
            
             input -"word"
             output:
                    meaning: शब्द
                    definition: भाषा का वह अंश जो विचार, भावना, या सूचना को व्यक्त करने के लिए प्रयुक्त होता है। यह एक या अधिक वर्णों से मिलकर बनता है और इसका कोई निश्चित अर्थ होता है। शब्द का उपयोग लिखित या मौखिक रूप में किया जा सकता है।
                    
            if the input contains many words or sentences first, translate the text in {language} and summarize it in two lines, 
            for example-
            
            example 2(multiple words or sentence):
            
            input: "A word of warning is offered to the 
                beginning student of philosophy. The beginner may despair over diverse definitions. 
                Students who come from a scientific background frequently expect concise, clear, and universally accepted definitions. 
                This will not be true in philosophy and it is not universally true concerning all issues in any science or non-scientific study or discipline.
                The diversity of opinion in philosophy becomes a source of embarrassment for the beginner when asked to explain to parents or
                unknowing friends just what a course in philosophy is all about. It might be expected that one of the oldest 
                disciplines or subjects in academia should achieve some uniformity or opinion, but this is not the case." 
                
            
            Output:
                Translation: "दर्शनशास्त्र के आरंभिक विद्यार्थी को चेतावनी का एक शब्द दिया जाता है। शुरुआत करने वाले को विविध परिभाषाओं से निराशा हो सकती है। 
                        जो छात्र वैज्ञानिक पृष्ठभूमि से आते हैं वे अक्सर संक्षिप्त, स्पष्ट और सार्वभौमिक रूप से स्वीकृत परिभाषाओं की अपेक्षा करते हैं।
                        यह दर्शनशास्त्र में सत्य नहीं होगा और यह किसी भी विज्ञान या गैर-वैज्ञानिक अध्ययन या अनुशासन के सभी मुद्दों के संबंध में
                        सार्वभौमिक रूप से सत्य नहीं है। दर्शनशास्त्र में विचारों की विविधता शुरुआती लोगों के लिए शर्मिंदगी का कारण बन जाती है 
                        जब माता-पिता या अनजाने दोस्तों को यह समझाने के लिए कहा जाता है कि दर्शनशास्त्र में पाठ्यक्रम क्या है। यह उम्मीद की जा सकती है कि शिक्षा जगत के सबसे पुराने विषयों या विषयों में से एक को कुछ एकरूपता या राय हासिल करनी चाहिए, लेकिन ऐसा नहीं है।"
                
                Summarization: "दर्शनशास्त्र के विद्यार्थी को परिभाषाओं की विविधता से निराशा हो सकती है,
                                खासकर जब वे स्पष्ट और सार्वभौमिक परिभाषाओं की उम्मीद करते हैं। यह विषय अपने विचारों की 
                                विविधता के कारण शुरुआती लोगों के लिए भ्रम और असुविधा का कारण बनता है।"
            
            example 3(single word):
             
             input: "territory"
             output:
                meaning: "territorio"
                definition: ""Territorio" es un área de tierra que está bajo el control o la posesión de una persona, grupo, país o entidad. También puede referirse a una zona de influencia o jurisdicción, o al espacio que ocupa un ser vivo"
             
            example 4(multiple word or sentence): 
             input: "The sun is shining in the sky and everyone is enjoying the good weather."
             output:
                translation: "El sol brilla en el cielo y todos disfrutan del buen clima."
                summarization: "El sol brilla y la gente disfruta del buen clima."
            example 5:
                input: "天気"
                output: 
                    meaning: "погода"
                    definigion: "Погода" — это состояние атмосферы в определённый момент времени, включая температуру, влажность, ветер и осадки."
            example 6(for multiple words on sentence):
                input: "図書館で静かに本を読んでいます。"
                output:
                    tranalation: "Я тихо читаю книгу в библиотеке."
                    summarization: "Я читаю книгу в библиотеке."
                
                
        the actual INPUT: {msg}
                
     """
    
    response = model.generate_content(prompt)
    respns= str(response.text.replace("```", "").replace("{", "").replace("}", "").strip(""))
    print(respns)
    return  jsonify({"translation": respns})

if __name__ == '__main__':
    # Run the app on port 8080
    app.run(debug=True, port=5000)
