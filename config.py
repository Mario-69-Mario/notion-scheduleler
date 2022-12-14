import os
import enum

#config stuff 
Weekly = 'Weekly'
Every_work_day = 'Every work day'
Bi_weekly = "Bi-weekly"
Monthly = 'Monthly'

logfile = 'scheduleler.log'
tokenHeartbeat = 'NOTION_TOKEN_heartbeat'
tokenActions = 'NOTION_TOKEN'
#tokenReports = 'NOTION_TOKEN_reports'

def NotionHeader(token : str):
    return { 'Authorization': 'Bearer ' + str(os.getenv(token)) ,
                'Content-Type': 'application/json',
                'Notion-Version': '2022-06-28'
                }

    #return True


# NotionHeader_heartbeat = { 'Authorization': 'Bearer ' + str(os.getenv('NOTION_TOKEN_heartbeat')) ,
#                 'Content-Type': 'application/json',
#                 'Notion-Version': '2022-06-28'
#                 }


actions_database_id = "cbf1a5a1dae148dbabac74a98f5534c0"
heartbeat_database_id = "6a6b13d5d7ae49daa0b8bb4a54e5af18"
reports_database_id = 'a38dd709d4a44e61b5df461f1c08eaa5'
NotionAPIDatabases =  'https://api.notion.com/v1/databases/'
NotionAPIPages = 'https://api.notion.com/v1/pages/'
NotionAPICommnets = 'https://api.notion.com/v1/comments/'
NotionAPIBlocks = 'https://api.notion.com/v1/blocks/{0}/children'

# end config stuff 
