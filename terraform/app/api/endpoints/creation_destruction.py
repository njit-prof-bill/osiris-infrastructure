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


@router.post("/unlock_terraform_state")
def unlockTerraformState(config_path: str) -> bool:
    try:
        result = True
        return {"success": result}
    except Exception as e:
        raise HTTPException(status_code=500)


@router.post("/import_terraform_resource")
def importTerraformResource(resource_id: str, config_path: str, resource_name: str) -> bool:
    try:
        result = True
        return {"success": result}
    except Exception as e:
        raise HTTPException(status_code=500)