# -*- coding: utf-8 -*-
import xbmcgui

# Import the common settings
from resources.lib.settings import log


#########################
# Main
#########################
if __name__ == '__main__':

    msg = 'The Recap Addon has been removed from the Official Repo'
    msg2 = 'Recap is now located in the robwebset repository.'
    msg3 = 'See the forum for more information'
    makeRequest = xbmcgui.Dialog().ok('Recap Has Moved', msg, msg2, msg3)