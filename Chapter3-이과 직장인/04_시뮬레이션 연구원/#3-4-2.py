try:
    import ross as rs
    module_status = "Ross module imported successfully."
except ImportError as e:
    module_status = f"Error importing Ross module: {str(e)}"
 
module_status  # 모듈 설치 성공 여부 출력
