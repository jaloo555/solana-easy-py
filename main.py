import requests
import json
from rpc.boosted_client import BoostedClient

if __name__ == "__main__":
    # Sample usage
    URL = "https://api.mainnet-beta.solana.com"
    solClient = BoostedClient(URL)
    print(solClient.getEpochProgress())