from langchain.schema import HumanMessage, SystemMessage,AIMessage
chat(
        [
            SystemMessage(content="you are am international chef that helps who specialize in making sandwiches"),
            HumanMessage(content="I dont like tomatoes, what elses can make me a sandwich? Gove a 2 line recipie.")

        ]
        )
