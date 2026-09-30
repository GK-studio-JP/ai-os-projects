#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

REGISTRY_SCHEMAS = {"ai-os-project-registry:v1", "ai-os-project-registry:v2"}


def load_registry(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if data.get("schema") not in REGISTRY_SCHEMAS:
        raise ValueError("unsupported registry schema")
    return data


def project_repositories(project):
    repositories = project.get("repositories")
    if repositories is None:
        repository = project.get("repository")
        if not isinstance(repository, str) or not repository.strip():
            raise ValueError("project missing repository")
        return [repository]

    if (
        not isinstance(repositories, list)
        or not repositories
        or any(not isinstance(item, str) or not item.strip() for item in repositories)
    ):
        raise ValueError("project repositories must be a non-empty string list")

    result = []
    for repository in repositories:
        if repository not in result:
            result.append(repository)

    canonical = project.get("canonical_repository")
    if not isinstance(canonical, str) or not canonical.strip():
        raise ValueError("multi-repo project missing canonical_repository")
    if canonical not in result:
        raise ValueError("canonical_repository must be included in repositories")
    return result


def canonical_repository(project):
    value = project.get("canonical_repository") or project.get("repository")
    if not isinstance(value, str) or not value.strip():
        raise ValueError("project missing canonical repository")
    return value


def validate_project(project):
    for key in ("project_id", "name", "process"):
        value = project.get(key)
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"project missing {key}")

    repositories = project_repositories(project)
    canonical = canonical_repository(project)
    if canonical not in repositories:
        raise ValueError("canonical repository is not registered")

    for ref in project.get("refs", []):
        if not isinstance(ref, dict):
            raise ValueError("project ref must be an object")
        path = ref.get("path")
        if not isinstance(path, str) or not path.strip():
            raise ValueError("project ref missing path")
        ref_repository = ref.get("repository")
        if ref_repository is not None and ref_repository not in repositories:
            raise ValueError(f"project ref repository is not registered: {ref_repository}")


def projects_by_id(data):
    result = {}
    for project in data.get("projects", []):
        validate_project(project)
        project_id = project["project_id"]
        if project_id in result:
            raise ValueError(f"duplicate project_id: {project_id}")
        result[project_id] = project
    return result


def _context_ref(project, ref):
    path = ref["path"]
    repositories = project_repositories(project)
    if len(repositories) == 1 and not project.get("canonical_repository"):
        return f"path:{path}"

    repository = ref.get("repository") or canonical_repository(project)
    if repository not in repositories:
        raise ValueError(f"project ref repository is not registered: {repository}")
    return f"repo:{repository}:path:{path}"


def build_task(project, objective, target_repository=None):
    if not isinstance(objective, str) or not objective.strip():
        raise ValueError("objective must not be empty")

    repositories = project_repositories(project)
    target = target_repository or canonical_repository(project)
    if target not in repositories:
        raise ValueError(f"target repository is not registered for project: {target}")

    refs = [_context_ref(project, ref) for ref in project.get("refs", [])]
    return {
        "schema": "ai-os-task:v1",
        "process": project["process"],
        "repository": target,
        "objective": objective.strip(),
        "context_refs": refs,
        "project": {
            "project_id": project["project_id"],
            "name": project["name"],
            "canonical_repository": canonical_repository(project),
            "repositories": repositories,
        },
    }


def project_matches(project, query):
    q = query.casefold()
    values = [project["project_id"], project["name"], *project_repositories(project)]
    return any(q in value.casefold() for value in values)


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
    task_p.add_argument("--target-repository")
    args = parser.parse_args()

    data = load_registry(args.registry)
    projects = projects_by_id(data)

    if args.command == "list":
        output = list(projects.values())
    elif args.command == "get":
        output = projects[args.project_id]
    elif args.command == "find":
        output = [p for p in projects.values() if project_matches(p, args.query)]
    else:
        output = build_task(
            projects[args.project_id],
            args.objective,
            target_repository=args.target_repository,
        )

    print(json.dumps(output, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
