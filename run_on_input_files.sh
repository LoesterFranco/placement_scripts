cd $(dirname $0)
input_files=$(ls input_files)

for input_file in $input_files; do
    input_file_path="input_files/$input_file"

    if [ ! -d "sol_files" ]; then
        mkdir sol_files
    fi

    if [ ! -d "output_images" ]; then
        mkdir output_images
    fi

    IFS='.' read -r -a prefix <<< "$input_file"
    
    kl_sol_file_path="sol_files/${prefix}_kl.json"
    fm_sol_file_path="sol_files/${prefix}_fm.json"


    kl_img_file_path="output_images/${prefix}_kl.png"
    fm_img_file_path="output_images/${prefix}_fm.png"



    java -jar place.jar $input_file_path $kl_sol_file_path kl
    java -jar place.jar $input_file_path $fm_sol_file_path fm

    python3 placement_visualization/visualize_placement.py $input_file_path $kl_sol_file_path 100 $kl_img_file_path
    python3 placement_visualization/visualize_placement.py $input_file_path $fm_sol_file_path 100 $fm_img_file_path

done