import asyncio
from contract_generator import ContractGenerator
import os
from dotenv import load_dotenv
import sys
import traceback

async def main():
    try:
        # Load environment variables
        load_dotenv()
        
        # Check if API key is set
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            print("Error: GOOGLE_API_KEY not found in .env file")
            sys.exit(1)
            
        print("Initializing contract generator...")
        generator = ContractGenerator()
        
        # Example data for service agreement
        form_data = {
            "service_provider": "Digital Solutions Corp",
            "client": "Global Enterprises Ltd",
            "service_description": "Website development and maintenance",
            "scope": "Full-stack development of e-commerce platform",
            "payment_terms": "$5,000 per month",
            "term": "12 months",
            "additional_terms": "24/7 support included, monthly progress reports"
        }
        
        print("\nGenerating Service Agreement...")
        result = await generator.generate_contract("service_agreement", form_data)
        
        print("\nGenerated Contract:")
        print("=" * 80)
        print(result["contract"])
        print("=" * 80)
        
        print("\nMetadata:")
        print(f"Contract Type: {result['metadata']['contract_type']}")
        print(f"Generated At: {result['metadata']['generated_at']}")
        print(f"Model: {result['metadata']['model']}")
        
    except Exception as e:
        print(f"\nError: {str(e)}")
        print(traceback.format_exc())
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main()) 