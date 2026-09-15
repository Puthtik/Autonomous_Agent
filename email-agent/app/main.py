from agent import run_agent
from tools import send_email

def human_approval(tool_call): # This function is the part that human involved

    arguments = tool_call.function.arguments

    print("\n")
    print("=" * 50)
    print("HUMAN APPROVAL REQUIRED")
    print("=" * 50)

    print(f"Tool: {tool_call.function.name}")
    print(f"To: {arguments['to']}")
    print(f"Subject: {arguments['subject']}")
    print(f"Body: {arguments['body']}")

    print("=" * 50)

    answer = input(
        "Do you approve sending this email? [y/n]: "
    )

    return answer.lower() == "y"

def main():

    user_request = input(
        "What email should the agent send?\n> "
    )

    # -------------------------
    # 1. Agent
    # -------------------------

    response = run_agent(user_request)

    # -------------------------
    # 2. Agent requests tool
    # -------------------------

    if not response.message.tool_calls:

        print("\nAgent:")
        print(response.message.content)

        return

    # -------------------------
    # 3. Human approval
    # -------------------------

    for tool_call in response.message.tool_calls:

        print("\nAgent requested a tool call.")

        approved = human_approval(tool_call)

        # -------------------------
        # 4. Reject
        # -------------------------

        if not approved:

            print("\nHuman rejected the action.")

            return

        # -------------------------
        # 5. Execute real tool
        # -------------------------

        if tool_call.function.name == "send_email":

            arguments = tool_call.function.arguments

            result = send_email(
                to=arguments["to"],
                subject=arguments["subject"],
                body=arguments["body"],
            )

            print("\nTOOL RESULT")
            print(result)

if __name__ == "__main__":
    main()