# Skin Disease ChatBot using ChainLit

## Overview
This project implements a Skin Disease ChatBot using ChainLit, designed to provide answers related to various skin conditions. The bot uses a JSON-based knowledge base to handle user queries and deliver accurate responses.

## Features
- **Interactive Chat Interface**: Built using ChainLit for a seamless user experience.
- **Skin Disease Knowledge Base**: A comprehensive JSON dataset containing questions and answers about common skin conditions.
- **Scalable Design**: Easily extendable to include more diseases and questions.
- **Simple Deployment**: Easy to set up and run locally or on a cloud platform.

## Requirements
### Prerequisites
- Python 3.8+
- Virtual environment setup (optional but recommended)

### Dependencies
Install the required dependencies by running:
```bash
pip install -r requirements.txt
```
The `requirements.txt` should include:
```text
chainlit
jsonschema  # For validating JSON schema if needed
```

## Getting Started
### 1. Clone the Repository
```bash
git clone <repository_url>
cd skin-disease-chatbot
```

### 2. Setup the JSON Knowledge Base
Ensure the `knowledge_base.json` file is in the root directory. An example format:
```json
{
  "Acne": {
    "What is acne?": "Acne is a skin condition that occurs when hair follicles are clogged with oil and dead skin cells.",
    "How can acne be treated?": "Treatments include topical medications, oral drugs, and lifestyle changes."
  },
  "Eczema": {
    "What is eczema?": "Eczema is a condition that makes your skin red and itchy.",
    "How to manage eczema?": "Management includes moisturizing, avoiding triggers, and using prescribed treatments."
  }
}
```

### 3. Run the Application
Launch the chatbot using the ChainLit CLI:
```bash
chainlit run app.py
```

### 4. Access the ChatBot
Open the provided URL (default: `http://localhost:8000`) in your web browser to interact with the chatbot.

## Project Structure
```
skin-disease-chatbot/
├── app.py                 # Main application logic
├── knowledge_base.json    # JSON file with Q&A data
├── requirements.txt       # Dependencies
├── README.md              # Project documentation
```

## How It Works
1. **User Interaction**: Users enter questions related to skin diseases.
2. **JSON Querying**: The application searches the JSON knowledge base for a matching question.
3. **Response Delivery**: The chatbot responds with the corresponding answer or a default fallback message.

## Extending the Project
### Adding New Data
1. Open `knowledge_base.json`.
2. Add a new disease or question-answer pair:
```json
"New Disease": {
  "What is this disease?": "Description of the disease.",
  "How is it treated?": "Treatment methods."
}
```
3. Save the file and restart the chatbot.

### Enhancing Features
- **Natural Language Processing**: Use NLP techniques to allow fuzzy matching for user queries.
- **Database Integration**: Replace the JSON file with a database for scalability.
- **User Authentication**: Add user accounts for personalized experiences.

## Contributing
Contributions are welcome! Please fork the repository, make changes, and submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments
- **ChainLit**: For the user-friendly chatbot framework.
- **Contributors**: Thanks to everyone who helped build this project.

## Contact
For any queries or suggestions, please contact [Your Name] at [your.email@example.com].
