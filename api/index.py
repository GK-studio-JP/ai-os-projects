from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from fastapi import FastAPI, Header, HTTPException

from project_registry import (
    build_task,
    load_registry,
    project_matches,
    projects_by_id,
)
from render_issue import render_issue

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REGISTRY = ROOT / "projects.json"

app = FastAPI(title="ai-os-projects HTTP API", version="2")


def _authorize(authorization: str | None) -> None:
    token = os.getenv("AIOS_SERVICE_TOKEN")
    if not token:
        raise HTTPException(status_code=503, detail="AIOS_SERVICE_TOKEN is not configured")
    if authorization != f"Bearer {token}":
        raise HTTPException(status_code=401, detail="unauthorized")


def _projects() -> dict[str, dict[str, Any]]:
    return projects_by_id(load_registry(str(DEFAULT_REGISTRY)))


@app.get("/api/health")
def health() -> dict[str, Any]:
    return {"ok": True, "service": "ai-os-projects"}


@app.get("/api/projects")
def list_projects(
    authorization: str | None = Header(default=None),
) -> dict[str, Any]:
    _authorize(authorization)
    return {"projects": list(_projects().values())}


@app.post("/api/projects/resolve")
def resolve_project(
    payload: dict[str, Any],
    authorization: str | None = Header(default=None),
) -> dict[str, Any]:
    _authorize(authorization)
    try:
        projects = _projects()
        project_id = payload.get("project_id")
        if project_id:
            return projects[str(project_id)]
        query = str(payload["query"])
        matches = [p for p in projects.values() if project_matches(p, query)]
        if len(matches) != 1:
            raise ValueError(f"expected exactly one project match, got {len(matches)}")
        return matches[0]
    except (KeyError, TypeError, ValueError, OSError) as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@app.post("/api/projects/task")
def project_task(
    payload: dict[str, Any],
    authorization: str | None = Header(default=None),
) -> dict[str, Any]:
    _authorize(authorization)
    try:
        project = _projects()[str(payload["project_id"])]
        objective = str(payload["objective"])
        target_repository = payload.get("target_repository")
        task = build_task(
            project,
            objective,
            target_repository=target_repository,
        )
        issue = render_issue(
            project,
            objective,
            int(payload.get("priority", 50)),
            payload.get("acceptance", []),
            target_repository=target_repository,
        )
        return {
            "schema": "ai-os-projects-http:v2",
            "project": project,
            "task": task,
            "issue": issue,
        }
    except (KeyError, TypeError, ValueError, OSError) as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
