import os

from jinja2 import Environment, FileSystemLoader

from configs import path_define
from configs.dump_config import DumpConfig
from configs.git_deploy_config import GitDeployConfig
from utils.unidata_util import UnidataDB

target_px = 12

dump_configs = [
    DumpConfig(
        'ark-pixel-monospaced',
        'ark-pixel-monospaced/ark-pixel-12px-monospaced-zh_cn.otf',
    ),
    DumpConfig(
        'ark-pixel-old',
        'ark-pixel-old/ark-pixel-12px-zh_cn.otf',
    ),
    DumpConfig(
        'Cubic-11',
        'Cubic-11/Cubic_11_1.013_R.ttf',
        offset_xy=(-1, 0),
    ),
    DumpConfig(
        'Galmuri-11',
        'Galmuri/Galmuri11.ttf',
    ),
]

font_config = (12, 10, 6, 8)

unidata_db = UnidataDB(os.path.join(path_define.unidata_dir, 'Blocks.txt'))

template_env = Environment(loader=FileSystemLoader(path_define.templates_dir))

git_deploy_configs = [GitDeployConfig(
    'git@github.com:TakWolf/fusion-pixel-font.git',
    'github',
    'gh-pages',
)]
