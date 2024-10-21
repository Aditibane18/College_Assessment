K_Base = {
    "Is the computer powering on?": {
        "Yes": {
            "Is there a beeping sound?": {
                "Yes": "Check the RAM and CPU",
                "No": {
                    "Is the display showing any output?": {
                        "Yes": "Check the display connections and settings",
                        "No": "Check the power supply and motherboard"
                    }
                }
            }
        },
        "No": "Check the power supply and cables"
    }
}
def troubleshoot(tree):
    if isinstance(tree, dict):
        question = list(tree.keys())[0]
        answer = input(f"{question} (Yes/No): ").strip().capitalize()
        if answer in tree[question]:
            return troubleshoot(tree[question][answer])
        else:
            return "Invalid input. Please enter 'Yes' or 'No'."
    else:
        return tree
if __name__ == "__main__":
    print("Computer Troubleshooting Guide:")
    result = troubleshoot(K_Base)
    print(f"Result: {result}")
