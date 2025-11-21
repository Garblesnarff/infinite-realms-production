import argparse
import os
from dotenv import load_dotenv
from utils import load_markdown_file
from llm_config import get_gemini_llm, get_openrouter_llm
from crews import WorldForgeCrew

def main():
    load_dotenv()

    parser = argparse.ArgumentParser(description="AI World-Forge for TTRPGs")
    parser.add_argument("spec_file", type=str, help="Path to the world-building-spec.md file.")
    args = parser.parse_args()

    print("Initializing LLMs...")
    gemini_llm = get_gemini_llm()
    openrouter_llm_configs = {
        "Lore Scribes Crew": "mistralai/mixtral-8x7b-instruct", 
        "Faction Dynamics Crew": "moonshotai/kimi-k2", 
        "Character Forge Crew": "mistralai/mixtral-8x7b-instruct", 
        "World Architects Crew": "mistralai/mixtral-8x7b-instruct", 
        "Causality Engine Crew": "deepseek/deepseek-chat-v3.1",
        "World-Forge Crew": "openai/gpt-oss-120b"
    }

    print(f"Loading specification file from: {args.spec_file}")
    try:
        markdown_content = load_markdown_file(args.spec_file)
    except Exception as e:
        print(e)
        return

    print("Initializing the World-Forge master crew...")
    world_forge = WorldForgeCrew(markdown_content, gemini_llm, openrouter_llm_configs)

    print("Kicking off the world-building process... This may take a while.")
    final_campaign_world = world_forge.run()

    print("\n\n--- AI World-Forge Process Complete ---")
    print("\n--- Final Campaign World ---")
    print(final_campaign_world)

    # Save the output to a file
    output_dir = os.path.dirname(args.spec_file)
    input_filename_base = os.path.splitext(os.path.basename(args.spec_file))[0]
    output_filename = f"{input_filename_base}_output.md"
    output_file_path = os.path.join(output_dir, output_filename)

    try:
        with open(output_file_path, "w") as f:
            f.write(final_campaign_world)
        print(f"\n--- Final campaign world saved to: {output_file_path} ---")
    except Exception as e:
        print(f"Error saving output to file: {e}")

if __name__ == "__main__":
    main()
