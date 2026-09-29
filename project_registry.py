#!/usr/bin/env python3
import argparse
import json
from pathlib import Path


def load_registry(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if data.get("schema") != "ai-os-project-registry:v1":
        raise ValueError("unsupported registry schema")
    return data


def projects_by_id(data):
    result = {}
    for project in data.get("projects", []):
        project_id = project.get("project_id")
        if not project_id:
            raise ValueError("project missing project_id")
        if project_id in result:
            raise ValueError(f"duplicate project_id: {project_id}")
        result[project_id] = project
    return result


def build_task(project, objective):
    if not objective.strip():
        raise ValueError("objective must not be empty")
    if not project.get("repository") or not project.get("process"):
        raise ValueError("project missing repository or process")
    refs = []
    for ref in project.get("refs", []):
        path = ref.get("path")
        if not path:
            raise ValueError("project ref missing path")
        refs.append(f"path:{path}")
    return {
        "schema": "ai-os-task:v1",
        "process": project["process"],
        "repository": project["repository"],
        "objective": objective.strip(),
        "context_refs": refs,
        "project": {
            "project_id": project["project_id"],
            "name": project["name"],
        },
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--registry", default="projects.json")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("list")
    get_p = sub.add_parser("get")
    get_p.add_argument("--project-id", required=True)
    find_p = sub.add_parser("find")
    find_p.add_argument("--query", required=True)
    task_p = sub.add_parser("task")
    task_p.add_argument("--project-id", required=True)
    task_p.add_argument("--objective", required=True)
    args = parser.parse_args()

    data = load_registry(args.registry)
    projects = projects_by_id(data)

    if args.command == "list":
        output = list(projects.values())
    elif args.command == "get":
        output = projects[args.project_id]
    elif args.command == "find":
        q = args.query.casefold()
        output = [
            p for p in projects.values()
            if q in p["project_id"].casefold()
            or q in p["name"].casefold()
            or q in p["repository"].casefold()
        ]
    else:
        output = build_task(projects[args.project_id], args.objective)

    print(json.dumps(output, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
