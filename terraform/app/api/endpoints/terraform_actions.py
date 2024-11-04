# 6, 7, 10
from fastapi import APIRouter, HTTPException
router = APIRouter()

@router.post("/lock_terraform_state")
def lockTerraformState(config_path: str) -> bool:
    try:
        result = True
        return {"success": result}
    except Exception as e:
        raise HTTPException(status_code=500)
