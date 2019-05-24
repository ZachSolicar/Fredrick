from Client import *

import datetime
import discord
import os

def main():
	@client.event
	async def on_message(msg):
		server_id = client.get_guild(463678175009046539)
		
		if msg.content.find(".hi") != -1:
			await msg.channel.send("Hello, World!")
		if msg.content.find(".Status") != -1:
			await msg.channel.send(f"""Members: {server_id.member_count}""")
		if msg.content.find(".datetime") != -1:
			await msg.channel.send(f"""Today's date is {datetime.datetime.now()}""")
		if msg.content.find(".warn") != -1:
			cmd = msg.content
			command = cmd.split(' ')
			await msg.channel.send(f""":white_check_mark: {command[1]} has been warned""")
		if msg.content.find(".ping") != -1:
			await msg.channel.send("PONG!")

	@client.event
	async def on_ready():
		print("Successfully logged in")

	client.run(token)

if __name__ == '__main__':
	os.system("title FredRick - DiscordBot")
	main()