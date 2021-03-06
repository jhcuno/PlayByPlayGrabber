import urllib.request
from bs4 import BeautifulSoup


def espn_url_generator(game_number_start, game_number_end):
    """
    This method creates a dictionary of urls that link to ESPN's play-by-play results.
    :param game_number_start: Integer that represents the game to start creating urls for.
    :param game_number_end: Integer that represents the game to stop creating urls for (inclusive).
    :return: dictionary with the list of game urls.
    """
    url_root = "http://www.espn.com/nfl/playbyplay?gameId="
    list_of_urls = {}
    current_game_number = game_number_start
    while current_game_number <= game_number_end:
        url = url_root + str(current_game_number)
        list_of_urls[current_game_number] = url
        current_game_number += 1
    return list_of_urls


def espn_retrieve_pbps(list_of_urls):
    box_score_root = "http://www.espn.com/nfl/boxscore?gameId="
    for key in list_of_urls:
        espn_scrap_single_game_pbp(list_of_urls.get(key), str(key))
    return


def espn_scrap_single_game_pbp(url_to_scrap, file_to_save_to):
    """
    This method takes a single url representing an ESPN play-by-play page and extracts the necessary text from the
    webpage.  The results will be saved to a text file with the name given by param file_to_save_to.
    :param url_to_scrap: String that represents the webpage containing the games play-by-play
    :param file_to_save_to: String representing the name of the file to save the play-by-play to (do not include ".txt")
    :return:
    """
    url = url_to_scrap
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, "lxml")
    file = open(file_to_save_to + ".txt", "w")
    # file.write(url_to_scrap)
    # for play in soup.find_all(class_="post-play"):
    for play in soup.find_all(True, {'class': ["post-play", "team-logo imageLoaded"]}):
        print(play.get_text())
        file.write(play.get_text())
    file.close()
    return


# scrap_single_game_pbp("http://www.espn.com/nfl/playbyplay?gameId=400874484", "400874484")
# test
# espn_retrieve_pbps(espn_url_generator(400874484, 400874490))


def fox_url_generator(game_number_start, game_number_end):
    """
    This method creates a dictionary of urls that link to ESPN's play-by-play results.
    :param game_number_start: Integer that represents the game to start creating urls for.
    :param game_number_end: Integer that represents the game to stop creating urls for (inclusive).
    :return: dictionary with the list of game urls.
    """
    url_root = "http://www.foxsports.com/nfl/play-by-play?id="
    list_of_urls = {}
    current_game_number = game_number_start
    while current_game_number <= game_number_end:
        url = url_root + str(current_game_number)
        list_of_urls[current_game_number] = url
        current_game_number += 1
    return list_of_urls


def fox_retrieve_pbps(list_of_urls):
    for key in list_of_urls:
        fox_scrap_single_game_pbp(list_of_urls.get(key), str(key))
    return


def fox_scrap_single_game_pbp(url_to_scrap, file_to_save_to):
    """
    This method takes a single url representing an ESPN play-by-play page and extracts the necessary text from the
    webpage.  The results will be saved to a text file with the name given by param file_to_save_to.
    :param url_to_scrap: String that represents the webpage containing the games play-by-play
    :param file_to_save_to: String representing the name of the file to save the play-by-play to (do not include ".txt")
    :return:
    """
    teams = []
    team_locaitons = []
    url = url_to_scrap
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, "lxml")
    file = open(file_to_save_to + ".txt", "w")

    for team in soup.find_all(class_='wisbb_bsName'):
        teams.append(team.get_text())
    for location in soup.find_all(class_='wisbb_bsLocation'):
        team_locaitons.append(location.get_text())

    file.write("home team: " + team_locaitons[1] + ' ' + teams[1] + '\n')
    file.write("away team: " + team_locaitons[0] + ' ' + teams[0] + '\n')

    for play in soup.find_all(True, {'class': ["wisbb_bsPbpPlay", "wisbb_bsPbpTeamFullName"]}):
        print(play.get_text())
        file.write(play.get_text())
    file.close()
    return

fox_retrieve_pbps(fox_url_generator(7691, 7692))
