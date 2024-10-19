import os

from discord.ext import commands  # Corrected import
import discord
from web3 import Web3
from sklearn.linear_model import LinearRegression  # Example: Replace with your chosen model
from nft_utils import (  # Import all NFT management functions
    mint_nft,
    list_nfts,
    buy_nft,
    sell_nft,
    transfer_nft,
)

# Bot setup
intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Web3 setup with your Infura Project URL (moved outside function for efficiency)
infura_url = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"  # Replace with your Infura project ID
web3 = Web3(Web3.HTTPProvider(infura_url))

# Check Web3 connection (moved outside function for efficiency)
if web3.isConnected():
    print("Connected to Ethereum mainnet")
else:
    print("Failed to connect to Ethereum mainnet")


# Bot event for when it's ready
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


# 8-ball game command (rest of the code remains the same)

# Machine learning demo command for price prediction (replace with your model)
@bot.command(name='predict')
async def predict_price(ctx, current_price: float, price_change: float):
    # Replace with your trained model and data
    model = your_trained_model
    X_train = your_training_data_X
    y_train = your_training_data_y
    model.fit(X_train, y_train)
    next_price = model.predict(np.array([[current_price + price_change]]))[0]
    await ctx.send(f" The predicted price is {next_price:.2f}")


# NFT management commands
@bot.command(name='mint')
async def mint_nft(ctx, name: str, description: str, image_url: str):
    await mint_nft(ctx, name, description, image_url)

@bot.command(name='list')
async def list_nfts(ctx):
    await list_nfts(ctx)

@bot.command(name='buy')
async def buy_nft(ctx, nft_id: int):
    await buy_nft(ctx, nft_id)

@bot.command(name='sell')
async def sell_nft(ctx, nft_id: int, price: float):
    await sell_nft(ctx, nft_id, price)

@bot.command(name='transfer')
async def transfer_nft(ctx, nft_id: int, recipient_address: str):
    await transfer_nft(ctx, nft_id, recipient_address)


# Run the bot using the token from environment variables
bot.run(os.getenv('DISCORD_TOKEN'))  # Make sure your bot token is set as an environment variable