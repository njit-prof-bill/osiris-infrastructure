# 5, 8 9
from fastapi import APIRouter
router = APIRouter()

@router.post("/unlock_terraform_state")
def unlockTerraformState(config_path: str) -> bool:
    try:
        result = True
        return {"success": result}
    except Exception as e:
        raise HTTPException(status_code=500)

