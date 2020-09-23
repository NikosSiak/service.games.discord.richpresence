import xbmc
import discordIPC
import time

CLIENT_ID = '750797452453478629'

if __name__ == "__main__":
    monitor = xbmc.Monitor()
    player = xbmc.Player()
    discord = discordIPC.DiscordIPC(CLIENT_ID)

    while True:
        monitor.waitForAbort(5)
        if monitor.abortRequested():
            discord.close()
            break
        
        if player.isPlayingGame():
            data = player.getGameInfoTag()
            activity = {
                'assets': {'large_image': 'kodi', 'large_text': 'Kodi'},
                'state': data.getTitle(),
                'details': data.getCaption(),
                'timestamps': {'start': time.time()}
            }
            discord.update_activity(activity)
        else:
            # close discord if it's connected 
            pass
