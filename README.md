# Budget Calculator

This project is a budget calculator that uses OpenAI's GPT model to generate a budget based on the type of project specified by the user.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables. Create a `.env` file in the root directory and add your OpenAI API key:
   ```
   OPENAI_KEY=your_openai_api_key
   ```

## Usage

Run the `budget_calculator.py` script to generate a budget for a specific project type:

```bash
python budget_calculator.py
```

You will be prompted to enter the project type (e.g., 'pos for restaurant'). The script will then call the GPT model to generate a budget and display the response.

## Dependencies

- openai
- python-dotenv

## License

This project is licensed under the MIT License.
