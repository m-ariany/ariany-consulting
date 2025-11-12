import os
import json
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize OpenAI client
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set")

client = OpenAI(api_key=api_key)

# System prompts for the two clients
with open('prompts/writer-prompt.txt', 'r') as file:
    Writer_SYSTEM_PROMPT = file.read()

with open('prompts/evaluator-prompt.txt', 'r') as file:
    Evaluator_SYSTEM_PROMPT = file.read()


def writer_do(prompt: str) -> str:
    """
    Client 1: Generates content based on the given prompt.
    
    Args:
        prompt: The prompt or feedback to generate content from
        
    Returns:
        The generated content string
    """
    try:
        response = client.chat.completions.create(
            model="gpt-5",
            messages=[
                {"role": "developer", "content": Writer_SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ],
            reasoning_effort="high",
        )
        return response.choices[0].message.content
    except Exception as e:
        raise Exception(f"Error generating content: {str(e)}")


def evaluator_do(content: str) -> dict:
    """
    Client 2: Evaluates content and returns JSON with summary and score.
    
    Args:
        content: The content to evaluate
        
    Returns:
        Dictionary with 'summary' and 'score' keys
        
    Raises:
        Exception: If API call fails or JSON parsing fails
    """
    try:
        response = client.chat.completions.create(
            model="gpt-5",
            messages=[
                {"role": "developer", "content": Evaluator_SYSTEM_PROMPT},
                {"role": "user", "content": content}
            ],
            reasoning_effort="high",
            response_format={"type": "json_object"}
        )
        
        response_text = response.choices[0].message.content
        
        # Parse JSON response
        try:
            result = json.loads(response_text)
        except json.JSONDecodeError:
            # Try to extract JSON from response if it's wrapped in text
            import re
            json_match = re.search(r'\{[^{}]*"summary"[^{}]*"score"[^{}]*\}', response_text, re.DOTALL)
            if json_match:
                result = json.loads(json_match.group())
            else:
                raise Exception(f"Failed to parse JSON from response: {response_text}")
        
        # Validate required keys
        if "summary" not in result or "score" not in result:
            raise Exception(f"Response missing required keys. Got: {result}")
        
        # Ensure score is numeric
        result["score"] = float(result["score"])
        
        return result
    except Exception as e:
        raise Exception(f"Error evaluating content: {str(e)}")


def format_markdown(content: str) -> str:
    """
    Formats content into markdown using a lighter model.
    
    Args:
        content: The content to format
        
    Returns:
        Formatted markdown string
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-nano",
            messages=[
                {"role": "developer", "content": "You are a markdown formatter. Format the given content into well-structured markdown with proper headings, paragraphs, lists, and emphasis. Ensure the markdown is clean and properly formatted. REMEBER: You are not allowed to change the content of the original text, you are only allowed to format it into markdown."},
                {"role": "user", "content": f"Format the following content into markdown. Do not change the content of the original text, you are only allowed to format it into markdown.\n\n{content}"}
            ],
            temperature=0.1
        )
        return response.choices[0].message.content
    except Exception as e:
        raise Exception(f"Error formatting markdown: {str(e)}")


def workflow(initial_prompt: str, max_iterations: int = 2) -> dict:
    """
    Main workflow that orchestrates the two-client interaction.
    
    Args:
        initial_prompt: The initial prompt for content generation
        max_iterations: Maximum number of back-and-forth iterations (default: 2)
        
    Returns:
        Dictionary with final content, summary, score, and iteration count
    """
    current_prompt = initial_prompt
    iteration = 0
        
    while iteration < max_iterations:
        iteration += 1
        print(f"--- Iteration {iteration} ---")

        # Writer: Generate content
        print("Writer: Generating content...")
        try:
            generated_content = writer_do(current_prompt)
        except Exception as e:
            print(f"Error in Writer: {e}")
            raise
        
        # Evaluator: Evaluate content
        print("Evaluator: Evaluating content...")
        try:
            evaluation = evaluator_do(generated_content)
            score = evaluation["score"]
            summary = evaluation["summary"]
            
            print(f"Score: {score}")
            
            # Check if score meets threshold
            if score >= 90:
                print(f"✓ Score {score} meets threshold (>= 90). Workflow complete!")
                return {
                    "content": generated_content,
                    "summary": summary,
                    "score": score,
                    "iterations": iteration,
                    "status": "success"
                }
            
            # If score < 90 and we have iterations left, send summary back to Client 1
            if iteration < max_iterations:
                print(f"Score {score} is below threshold. Sending feedback to Client 1 for rework...\n")
                current_prompt = f"Based on this feedback, please improve your content: {summary}"
            else:
                print(f"Maximum iterations ({max_iterations}) reached. Workflow complete.")
                return {
                    "content": generated_content,
                    "summary": summary,
                    "score": score,
                    "iterations": iteration,
                    "status": "max_iterations_reached"
                }
                
        except Exception as e:
            print(f"Error in Evaluator: {e}")
            raise
    
    # This should not be reached, but included for safety
    return {
        "content": generated_content,
        "summary": summary,
        "score": score,
        "iterations": iteration,
        "status": "completed"
    }


if __name__ == "__main__":
    
    with open('article.txt', 'r') as file:
        initial_prompt = file.read()
    
    try:
        result = workflow(initial_prompt, max_iterations=2)
        
        print("\n=== Final Result ===")
        print(f"Status: {result['status']}")
        print(f"Iterations: {result['iterations']}")
        print(f"Final Score: {result['score']}")
        with open('raw_output.md', 'w', encoding='utf-8') as file:
            file.write(result["content"])
        
        # If workflow succeeded, format and save to file
        # if result['status'] == "success":
        #     print("\n=== Formatting Content ===")
        #     try:
        #         formatted_content = format_markdown(result['content'])
                
        #         # Save to file
        #         output_filename = "formatted_output.md"
        #         with open(output_filename, 'w', encoding='utf-8') as f:
        #             f.write(formatted_content)
                
        #         print(f"✓ Formatted content saved to {output_filename}")
        #     except Exception as e:
        #         print(f"Error formatting/saving content: {e}")
        #         raise
        
    except Exception as e:
        print(f"\nWorkflow failed with error: {e}")
        raise

