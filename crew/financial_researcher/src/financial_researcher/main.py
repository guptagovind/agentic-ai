#!/usr/bin/env python
import os

from crewai.events.listeners.tracing.utils import set_suppress_tracing_messages

from financial_researcher.crew import ResearchCrew

os.makedirs("output", exist_ok=True)


def run():
    """
    Run the financial researcher crew.
    """
    set_suppress_tracing_messages(True)
    inputs = {"company": "Newgen Software Technologies Ltd."}
    result = ResearchCrew().crew().kickoff(inputs=inputs)
    print(result.raw)
    print("\n\nReport has been saved to output/report.md")
    return result


if __name__ == "__main__":
    run()
