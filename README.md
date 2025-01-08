# Product Review Video Script Generator

This Python script automatically generates video scripts for products based on their Amazon reviews. It processes product data and reviews to create engaging 1-minute video scripts using OpenAI's GPT models.

## Features

- Processes multiple products and their reviews from a JSON file
- Summarizes product reviews using GPT-4
- Generates engaging 1-minute video scripts using GPT-3.5-turbo
- Saves all generated scripts to a JSON file

## Prerequisites

- Python 3.6 or higher
- OpenAI API key

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
```

2. Install the required dependencies:
```bash
pip install openai python-dotenv
```

3. Create a `.env` file in the project root and add your OpenAI API key:
```plaintext
OPENAI_API_KEY=your_api_key_here
```

## Input Data Format

The script expects a JSON file named `bestsellers_with_reviews.json` with the following structure:
```json
[
{
"items": [
{
"title": "Product Name",
"url": "Product URL",
"amazon_reviews": [
{
"review_title": "Review Title",
"review_star_rating": "5",
"review_comment": "Review Text"
}
]
}
]
}
]
```

## Output

The script generates a `video_scripts.json` file containing:
- Product name
- Buying link
- Generated video script

## Usage

Run the script using:
bash
python scriptcreator.py


## Error Handling

The script includes error handling for:
- File reading/writing operations
- API calls to OpenAI
- Data processing

## Contributing

Feel free to submit issues and enhancement requests!

## License

MIT License

Copyright (c) 2024

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
