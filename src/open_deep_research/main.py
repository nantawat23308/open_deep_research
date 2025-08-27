from open_deep_research.deep_researcher import deep_researcher
import asyncio


async def main():
    # Example usage:
    result = await deep_researcher.ainvoke(input={"messages": [{"type": "human", "content": "I would like a detailed analysis of the Saint Seiya franchise (anime/manga). The analysis should be structured around the different classes of armor (Cloths, Scales, Surplices, God Robes, etc.), such as Bronze Saints, Silver Saints, Gold Saints, Marina Generals, Specters, God Warriors, etc. For each significant character within these categories, provide details on their power level, signature techniques, key appearances/story arcs, and final outcome/fate within the series."}]})
    print(result["final_report"])

if __name__ == "__main__":
    asyncio.run(main())