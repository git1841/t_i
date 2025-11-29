import pkg_resources

packages = [
    'fastapi', 'uvicorn', 'pydantic', 'pydantic-core',
    'annotated-types', 'typing-extensions', 'markdown',
    'python-frontmatter', 'python-multipart', 'instagrapi',
    'requests', 'pycryptodome'
]

print("Versions installées sur votre PC local:")
print("=" * 50)

for package in packages:
    try:
        version = pkg_resources.get_distribution(package).version
        print(f"✅ {package:20} : {version}")
    except pkg_resources.DistributionNotFound:
        print(f"❌ {package:20} : NON INSTALLÉ")