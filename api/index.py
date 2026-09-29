from __future__ import annotations

from pathlib import Path
from typing import Any

from fastapi import FastAPI, HTTPException

from project_registry import build_task, load_registry, projects_by_id
from render_issue import render_issue

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REGISTRY = ROOT / "projects.json"

app = FastAPI(title="ai-os-projects HTTP API", version="1")


def _projects() -> dict[str, dict[str, Any]]:
    return projects_by_id(load_registry(str(DEFAULT_REGISTRY)))


@app.get("/api/health")
def health() -> dict[str, Any]:
    return {"ok": True, "service": "ai-os-projects"}


@app.get("/api/projects")
def list_projects() -> dict[str, Any]:
    return {"projects": list(_projects().values())}


@app.post("/api/projects/resolve")
def resolve_project(payload: dict[str, Any]) -> dict[str, Any]:
    try:
        projects = _projects()
        project_id = payload.get("project_id")
        if project_id:
            return projects[str(project_id)]
        query = str(payload["query"]).casefold()
        matches = [
            p for p in projects.values()
            if query in p["project_id"].casefold()
            or query in p["name"].casefold()
            or query in p["repository"].casefold()
        ]
        if len(matches) != 1:
            raise ValueError(f"expected exactly one project match, got {len(matches)}")
        return matches[0]
    except (KeyError, TypeError, ValueError, OSError) as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@app.post("/api/projects/task")
def project_task(payload: dict[str, Any]) -> dict[str, Any]:
    try:
        project = _projects()[str(payload["project_id"])]
        objective = str(payload["objective"])
        task = build_task(project, objective)
        issue = render_issue(
            project,
            objective,
            int(payload.get("priority", 50)),
            payload.get("acceptance", []),
        )
        return {
            "schema": "ai-os-projects-http:v1",
            "project": project,
            "task": task,
            "issue": issue,
        }
    except (KeyError, TypeError, ValueError, OSError) as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
