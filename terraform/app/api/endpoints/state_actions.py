# 5, 8 9
from fastapi import APIRouter, HTTPException
router = APIRouter()

@router.post("/get_terraform_output")
def getTerraformOutput(config_path: str) -> bool:
    try:
        result = True
        return {"success": result}
    except Exception as e:
        raise HTTPException(status_code=500)
