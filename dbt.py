import subprocess

# Define the dbt project directory
dbt_project_dir = "folderdbt"

# Run dbt models
def run_dbt_models():
  subprocess.run(["dbt", "run"], cwd=dbt_project_dir)

# Compile dbt models (optional)
def compile_dbt_models():
  subprocess.run(["dbt", "compile"], cwd=dbt_project_dir)

# Test dbt models (optional)
def test_dbt_models():
  subprocess.run(["dbt", "test"], cwd=dbt_project_dir)

# Example usage
run_dbt_models()  # Run all models in the project
compile_dbt_models() 
test_dbt_models() 
