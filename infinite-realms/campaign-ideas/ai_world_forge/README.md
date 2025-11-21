# AI World-Forge for TTRPGs

This project is an automated pipeline that uses a team of AI crews, powered by CrewAI, to expand a simple `world-building-spec.md` file into a complete, database-ready Dungeons & Dragons campaign world.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd <your-repo-name>
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1.  **Create a `.env` file:**
    Copy the example environment file `.env.example` to a new file named `.env`.
    ```bash
    cp .env.example .env
    ```

2.  **Add your API keys:**
    Open the `.env` file and add your API keys for OpenRouter and Google Gemini. You can also specify the OpenRouter model you wish to use.

    ```
    OPENROUTER_API_KEY="your_openrouter_api_key"
    GEMINI_API_KEY="your_gemini_api_key"
    OPENROUTER_MODEL_NAME="mistralai/mixtral-8x7b-instruct"
    ```

## Usage

To run the AI World-Forge, execute the `main.py` script from your terminal, providing the path to your world-building specification file as an argument.

```bash
python main.py path/to/your/spec.md
```

The script will then process the input file and print the final, compiled campaign world to the console.
