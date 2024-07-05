create_network:
	docker network create pattern_d_network

build_app_image:
	docker build -t pattern_d .

build_test_image:
	docker build -t pattern_d_test .

run_app:
	docker compose -f .//docker//local//docker-compose.yml up -d

stop_app:
	docker compose -f .//docker//local//docker-compose.yml down --remove-orphans

follow_app_log:
	docker logs -f pattern_d

start_database:
	docker compose -f .//docker//local//docker-compose-postgres.yml run postgres