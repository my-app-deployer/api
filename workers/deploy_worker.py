"""
GET DEPLOYS
FOREACH DEPLOYS
	FOREACH ROUTINE
		FOREACH COMMAND
			IF COMMAND not in RUNNING_COMMANDS AND DEPLOY is SYNCHRONOUS
				FOREACH SERVER IN DEPLOY
					ping server.ip?command=COMMAND&ping_back=API_URL
			ELSE_IF DEPLOY NOT SYNCHRONOUS
				ping server.ip?command=COMMAND&ping_back=API_URL
"""