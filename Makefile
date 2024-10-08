DC = docker-compose
STORAGES_FILE = docker_compose/mongodb.yaml
MONGODB_EXPRESS_FILE = docker_compose/mongodb_express.yaml
MONGODB_BACKUP_FILE = docker_compose/mongodb_backup.yaml
KAFKA_FILE = docker_compose/kafka.yaml
APP_FILE = docker_compose/app.yaml
EXEC = docker exec -it
LOGS = docker logs
ENV_FILE = --env-file .env
APP_CONTAINER = app
DB_CONTAINER = ppostgres
INTO_BASH = /bin/bash
ENTER_POSTGRES_CONTAINER = psql -U postgres -d auth


.PHONY: app
app:
	${DC} -f ${APP_FILE} -f ${STORAGES_FILE} -f ${MONGODB_EXPRESS_FILE} -f ${MONGODB_BACKUP_FILE} -f ${KAFKA_FILE} ${ENV_FILE} up -d

.PHONY: mongo_backup
mongo_backup:
	${DC} -f ${MONGODB_BACKUP_FILE} ${ENV_FILE} up -d

.PHONY: app-logs
app-logs:
	${LOGS} ${APP_CONTAINER} -f

.PHONY: app-down
app-down:
	${DC} -f ${APP_FILE} -f ${STORAGES_FILE} -f ${MONGODB_EXPRESS_FILE} -f ${MONGODB_BACKUP_FILE} -f ${KAFKA_FILE} down

.PHONY: appbash
appbash:
	${EXEC} ${APP_CONTAINER} ${INTO_BASH}

.PHONY: dbbash
dbbash:
	${EXEC} ${DB_CONTAINER} ${ENTER_POSTGRES_CONTAINER}

.PHONY: runtest
runtest:
	${EXEC} ${APP_CONTAINER} pytest
