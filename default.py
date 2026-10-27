"""TMDbHelper Sync - Floppy (Installer): the add-on that brings in the sync provider
(script.module.tmdbhelper.sync.floppy, a module Kodi's repository browser doesn't list).
Opening it offers the two steps to set the sync up."""
import xbmc
import xbmcgui

SYNC = "script.module.tmdbhelper.sync.floppy"
TMDBHELPER = "plugin.video.themoviedb.helper"
HEADING = "TMDbHelper Sync - Floppy"


def main():
    options = [
        ("Set up Floppy sync", "Your Floppy address and API token. Left empty, the Floppy add-on's are used.",
         "Addon.OpenSettings({})".format(SYNC)),
        ("TMDbHelper settings", "Choose Floppy for history and progress, watchlist and scrobbling.",
         "Addon.OpenSettings({})".format(TMDBHELPER)),
    ]
    items = []
    for label, help_text, _ in options:
        item = xbmcgui.ListItem(label, help_text, offscreen=True)
        items.append(item)
    choice = xbmcgui.Dialog().select(HEADING, items, useDetails=True)
    if choice >= 0:
        xbmc.executebuiltin(options[choice][2])


if __name__ == "__main__":
    main()
