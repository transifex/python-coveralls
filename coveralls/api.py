import json
from six import StringIO
import requests
import logging


def post(url, repo_token, service_number, service_job_id, service_name, git, source_files, parallel):
    json_file = build_file(repo_token, service_number, service_job_id, service_name, git, source_files, parallel)
    return requests.post(url, files={'json_file': json_file})


def build_file(repo_token, service_number, service_job_id, service_name, git, source_files, parallel):
    content = {
        'service_number': service_number,
        'service_job_id': service_job_id,
        'service_name': service_name,
        'git': git,
        'source_files': source_files,
    }
    if repo_token:
        content['repo_token'] = repo_token
    if parallel:
        content['parallel'] = True
    logger = logging.getLogger('coveralls')
    logger.info("JSON payload: %r", content.keys())
    logger.info("build num: %s", content['service_number'])
    logger.info("job id: %s", content['service_job_id'])
    return StringIO(json.dumps(content))
