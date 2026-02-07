Import("env")
import os
import shutil

def post_program_action(source, target, env):
    print("=" * 50)
    print("Post-build script started...")
    print("=" * 50)
    build_dir = os.path.join('.pio', 'build', 'pico2w')
    src_file = os.path.join(build_dir, 'firmware.uf2')
    dst_file = 'ulisp-picocalc-pico2w.uf2'
    print(f"Looking for: {src_file}")
    if os.path.exists(src_file):
        shutil.copyfile(src_file, dst_file)
        print(f'Successfully renamed {src_file} to {dst_file}')
    else:
        print(f"Error: {src_file} not found!")
    print("=" * 50)

env.AddPostAction("buildprog", post_program_action)
