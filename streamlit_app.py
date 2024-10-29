import streamlit as st
import asyncio
import os
import json
import base64

from computer_use_demo.loop import sampling_loop, APIProvider
from computer_use_demo.tools import ToolResult
from anthropic.types.beta import BetaMessage, BetaMessageParam
from anthropic import APIResponse

# Define the Streamlit app layout and functionality
def main():
    st.title("Claude Computer Use Demo")
    st.write("A modern, high-end, professional interface for interacting with Claude.")

    # Set up your Anthropic API key and model
    api_key = os.getenv("ANTHROPIC_API_KEY", "YOUR_API_KEY_HERE")
    if api_key == "YOUR_API_KEY_HERE":
        st.error("Please set your API key in the ANTHROPIC_API_KEY environment variable.")
        return
    provider = APIProvider.ANTHROPIC

    # User input section
    instruction = st.text_input("Enter your instruction:", "Save an image of a cat to the desktop.")

    if st.button("Run"):
        st.write(f"Starting Claude 'Computer Use' with instruction: '{instruction}'")

        # Set up the initial messages
        messages: list[BetaMessageParam] = [
            {
                "role": "user",
                "content": instruction,
            }
        ]

        # Define callbacks
        def output_callback(content_block):
            if isinstance(content_block, dict) and content_block.get("type") == "text":
                st.write("Assistant:", content_block.get("text"))

        def tool_output_callback(result: ToolResult, tool_use_id: str):
            if result.output:
                st.write(f"> Tool Output [{tool_use_id}]:", result.output)
            if result.error:
                st.write(f"!!! Tool Error [{tool_use_id}]:", result.error)
            if result.base64_image:
                # Save the image to a file if needed
                os.makedirs("screenshots", exist_ok=True)
                image_data = result.base64_image
                with open(f"screenshots/screenshot_{tool_use_id}.png", "wb") as f:
                    f.write(base64.b64decode(image_data))
                st.image(f"screenshots/screenshot_{tool_use_id}.png", caption=f"Screenshot {tool_use_id}")

        def api_response_callback(response: APIResponse[BetaMessage]):
            st.write(
                "\n---------------\nAPI Response:\n",
                json.dumps(json.loads(response.text)["content"], indent=4),  # type: ignore
                "\n",
            )

        # Run the sampling loop
        asyncio.run(sampling_loop(
            model="claude-3-5-sonnet-20241022",
            provider=provider,
            system_prompt_suffix="",
            messages=messages,
            output_callback=output_callback,
            tool_output_callback=tool_output_callback,
            api_response_callback=api_response_callback,
            api_key=api_key,
            only_n_most_recent_images=10,
            max_tokens=4096,
        ))

if __name__ == "__main__":
    main()
