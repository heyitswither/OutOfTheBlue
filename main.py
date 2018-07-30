import socket
from player import Player

def is_connected():
    try:
        socket.create_connection(("1.1.1.1", 80))
        return True
    except OSError:
        pass
    return False

def main():
    player = Player()
    player.add_song("mr blue sky")
    while len(player.queue) < 1:
        pass
    player.add_song("aerosmith angel")
    player.start()
    while player.looping and player.queue:
        pass

if __name__ == "__main__":
    main()
