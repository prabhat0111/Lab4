class CricketMatch:
    def __init__(self, location, team1, team2, timing):
        self.location = location
        self.team1 = team1
        self.team2 = team2
        self.timing = timing

class CricketMatchDatabase:
    def __init__(self, matches):
        self.matches = matches

    def search_by_team(self, team_name):
        team_matches = []
        for match in self.matches:
            if team_name in (match.team1, match.team2):
                team_matches.append(match)
        return team_matches

    def search_by_location(self, location):
        location_matches = []
        for match in self.matches:
            if match.location == location:
                location_matches.append(match)
        return location_matches

    def search_by_timing(self, timing):
        timing_matches = []
        for match in self.matches:
            if timing in match.timing:
                timing_matches.append(match)
        return timing_matches

def main():
    matches = [
        CricketMatch("Mumbai", "India", "Sri Lanka", "DAY"),
        CricketMatch("Delhi", "England", "Australia", "DAY-NIGHT"),
        CricketMatch("Chennai", "India", "South Africa", "DAY"),
        CricketMatch("Indore", "England", "Sri Lanka", "DAY-NIGHT"),
        CricketMatch("Mohali", "Australia", "South Africa", "DAY-NIGHT"),
        CricketMatch("Delhi", "India", "Australia", "DAY"),
    ]

    match_database = CricketMatchDatabase(matches)

    while True:
        print("\nSearch Options:")
        print("1. List of all matches of a Team")
        print("2. List of matches on a Location")
        print("3. List of matches based on timing")
        print("4. Quit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            team_name = input("Enter the team name: ")
            team_matches = match_database.search_by_team(team_name)
            print("Matches involving", team_name)
            for match in team_matches:
                print(f"{match.team1} vs {match.team2} at {match.location}, Timing: {match.timing}")

        elif choice == 2:
            location = input("Enter the location: ")
            location_matches = match_database.search_by_location(location)
            print("Matches at", location)
            for match in location_matches:
                print(f"{match.team1} vs {match.team2}, Timing: {match.timing}")

        elif choice == 3:
            timing = input("Enter the timing: ")
            timing_matches = match_database.search_by_timing(timing)
            print("Matches with timing", timing)
            for match in timing_matches:
                print(f"{match.team1} vs {match.team2} at {match.location}")

        elif choice == 4:
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()