# Insight DevOps Engineering Systems Puzzle-Matilda Wysocki

# My process:
1. Followed prompt instructions to download dependencies and see what the issue was
2. Check if the port used for the program is open
3. Note that ports don’t match between docker files, the docket logs say it is serving on port 5000
4. Check docker logs on database
5. Tried starting flask manually by running app.py, but the user wasn’t found in the data base, which was called from os.environ
6. Look on stack overflow and see that the error may be the app name added to the database
7. Found article demonstrating how to configure nginx, had to reverse the position of ports numbers from “80:8080” to “8080:80”
8. URL for success then broke when adding to database
9. Changed flask port to 5001
10. Tried changing conf file server_name to “0.0.0.0”
11. Removed the 5001 specification in the yml file
12. Removed the redundant host definition in the conf file
13. Flask code seems to come from all the right places
14. Specify port for database to query it
15. Previous query failed, so must correct for it
16. Check connection to database server in logs, find a 404 error
17. Curl to find an invalid length of startup packet
18. Check data type of returned list, as well as the initial result of the query itself
19. Convert each entry to another data type(dictionaries in this case), since lists cannot be rendered by flask directly, and sqlalchemy query results need to be translated themselves
20. Check back in the logs to see if the 404 error is still there
