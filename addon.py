import xbmcgui
import xbmcplugin

def build_menu():
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url='plugin://plugin.video.redecanais/?action=filmes', listitem=xbmcgui.ListItem('Filmes'), isFolder=True)
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url='plugin://plugin.video.redecanais/?action=desenhos', listitem=xbmcgui.ListItem('Desenhos'), isFolder=True)
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url='plugin://plugin.video.redecanais/?action=series', listitem=xbmcgui.ListItem('SÃ©ries'), isFolder=True)
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url='plugin://plugin.video.redecanais/?action=tvaberta', listitem=xbmcgui.ListItem('TV Aberta'), isFolder=True)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

def show_filmes_page():
    # Adicione a lÃ³gica para exibir a pÃ¡gina de filmes

def show_desenhos_page():
    # Adicione a lÃ³gica para exibir a pÃ¡gina de desenhos

def show_series_page():
    # Adicione a lÃ³gica para exibir a pÃ¡gina de sÃ©ries

def show_tvaberta_page():
    # Adicione a lÃ³gica para exibir a pÃ¡gina de TV aberta

def main():
    action = xbmcplugin.getSetting(int(sys.argv[1]), 'action')

    if action == "filmes":
        show_filmes_page(https://redecanais.la/browse-filmes-videos-1-date.html)
    elif action == "desenhos":
        show_desenhos_page(https://redecanais.la/browse-desenhos-videos-1-date.html)
    elif action == "series":
        show_series_page(https://redecanais.la/browse-series-videos-1-date.html)
    elif action == "tvaberta":
        show_tvaberta_page(https://redecanaistv.zip/)
    else:
        build_menu()

if __name__ == '__main__':
    main() 
