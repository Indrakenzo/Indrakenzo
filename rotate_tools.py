import random
import re

# Daftar seluruh senjatamu. Sistem akan mengacak dan mengambil 4 setiap hari.
all_tools = [
    "![Unity](https://img.shields.io/badge/Unity-100000?style=for-the-badge&logo=unity&logoColor=white)",
    "![C#](https://img.shields.io/badge/C%23-239120?style=for-the-badge&logo=c-sharp&logoColor=white)",
    "![Flutter](https://img.shields.io/badge/Flutter-02569B?style=for-the-badge&logo=flutter&logoColor=white)",
    "![Dart](https://img.shields.io/badge/Dart-0175C2?style=for-the-badge&logo=dart&logoColor=white)",
    "![C++](https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white)",
    "![Unreal Engine](https://img.shields.io/badge/Unreal_Engine-313131?style=for-the-badge&logo=unrealengine&logoColor=white)"
]

random.shuffle(all_tools)
selected_tools = " ".join(all_tools[:4]) # Menampilkan 4 badge secara acak

with open("README.md", "r", encoding="utf-8") as file:
    readme = file.read()

# Mencari dan menimpa bagian di antara tag START_TOOLS dan END_TOOLS
readme = re.sub(
    r'<!-- START_TOOLS -->.*<!-- END_TOOLS -->', 
    f'<!-- START_TOOLS -->\n{selected_tools}\n<!-- END_TOOLS -->', 
    readme, 
    flags=re.DOTALL
)

with open("README.md", "w", encoding="utf-8") as file:
    file.write(readme)
