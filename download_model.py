from huggingface_hub import snapshot_download

# TinyLlama for modest machines (CPU/8-12GB RAM)
repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
local_dir = "./models/tinyllama-1.1b-chat"

print(f"Downloading {repo_id} to {local_dir}...")
snapshot_download(
    repo_id, 
    local_dir=local_dir, 
    local_dir_use_symlinks=False
)
print(f"✅ Downloaded successfully to: {local_dir}")
