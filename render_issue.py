#!/usr/bin/env python3
import argparse
import json

from project_registry import (
    build_task,
    canonical_repository,
    load_registry,
    projects_by_id,
)


def render_issue(
    project,
    objective,
    priority=50,
    acceptance=None,
    target_repository=None,
):
    task = build_task(project, objective, target_repository=target_repository)
    envelope = {
        "process": task["process"],
        "repository": task["repository"],
        "objective": task["objective"],
        "priority": priority,
        "contracts": [],
        "context_refs": task["context_refs"],
        "acceptance": acceptance or [],
        "blocked_by": [],
        "capabilities": [],
    }
    body = (
        "<!-- ai-os-task:v1 -->\n"
        "```json\n"
        + json.dumps(envelope, ensure_ascii=False, indent=2, sort_keys=True)
        + "\n```\n\n"
        + f"Project: {project['name']}\n"
        + f"Project ID: {project['project_id']}\n"
        + f"Canonical repository: {canonical_repository(project)}\n"
        + f"Target repository: {task['repository']}\n"
    )
    title = f"[AIOS][{project['project_id']}] {objective.strip()}"
    return {"title": title, "body": body, "task_envelope": envelope}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--registry", default="projects.json")
    parser.add_argument("--project-id", required=True)
    parser.add_argument("--objective", required=True)
    parser.add_argument("--priority", type=int, default=50)
    parser.add_argument("--acceptance", action="append", default=[])
    parser.add_argument("--target-repository")
    args = parser.parse_args()

    projects = projects_by_id(load_registry(args.registry))
    project = projects[args.project_id]
    print(json.dumps(
        render_issue(
            project,
            args.objective,
            args.priority,
            args.acceptance,
            target_repository=args.target_repository,
        ),
        ensure_ascii=False,
        indent=2,
        sort_keys=True,
    ))


if __name__ == "__main__":
    main()
