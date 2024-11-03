#1,2,3,4
from fastapi import APIRouter, HTTPException
router = APIRouter()

@router.post("/apply_terraform")
def applyTerraform(config_path: str, var_file: str = None):
    try:
        result = True
        return {"success": result}
    except Exception as e:
        raise HTTPException(status_code=500)
    

@router.post("/destroy_terraform")
def destroyTerraform(config_path: str, var_file: str = None):
    try:
        result = True
        return {"success": result}
    except Exception as e:
        raise HTTPException(status_code=500)

