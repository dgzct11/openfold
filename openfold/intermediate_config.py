import ml_collections as mlc

def get_intermediate_config( 
                save_blocks=[],
                save_all_blocks=False,
                save_prefix="pair_reps", 
                save_dir="intermediate_outputs", 
                generate_final_outputs=True
        ):
    if save_all_blocks:
        save_blocks = range(48)
    return mlc.ConfigDict({
        "save_blocks": save_blocks,
        "save_prefix": save_prefix,
        "save_dir": save_dir,
        "generate_final_outputs": generate_final_outputs,
    })



