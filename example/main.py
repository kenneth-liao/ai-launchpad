from langgraph_sdk import get_client
from langgraph.types import Command, RunnableConfig
from dotenv import load_dotenv
from typing import Any
load_dotenv()


# This can be a local or remote deployment URL, but it must point to a Langgraph Server
langgraph_api = "http://localhost:2024"

# Initialize the client that will handle all API requests to the Langgraph Server
client = get_client(url=langgraph_api)


async def main():
    """Main function to run the frontend."""
    user_id = "kenny"
    thread = await client.threads.create(
        if_exists="do_nothing",
        metadata={
            "user_id": user_id,
        }
    )

    print(thread)

    # Search for threads
    # threads = await client.threads.search(
    #     metadata={
    #         "user_id": user_id,
    #     }
    # )

    # print(threads)

    response = await client.runs.wait(
        thread_id=thread["thread_id"],
        assistant_id="ConfigAgent",
        input={"messages": ["What's the user's name?"]},
        config=RunnableConfig(configurable={"user": {
            "user_id": user_id,
            "name": "Kenny",
        }}),
    )

    print(response)


if __name__ == "__main__":
    import asyncio
    import nest_asyncio
    nest_asyncio.apply()
    asyncio.run(main())