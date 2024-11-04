# 5, 8 9
from fastapi import APIRouter, HTTPException
router = APIRouter()

@router.post("/refresh_terraform_state")
def refreshTerraformState(config_path: str) -> bool:
    try:
        result = True
        return {"success": result}
    except Exception as e:
        raise HTTPException(status_code=500)

@router.post("/get_terraform_output")
def getTerraformOutput(config_path: str) -> bool:
    try:
        result = True
        return {"success": result}
    except Exception as e:
        raise HTTPException(status_code=500)


@router.post("/unlock_terraform_state")
def unlockTerraformState(config_path: str) -> bool:
    try:
        result = True
        return {"success": result}
    except Exception as e:
        raise HTTPException(status_code=500)

