#!/usr/bin/python3
from jinja2 import Environment, FileSystemLoader

env = Environment(loader = FileSystemLoader("codegen"))
template_lut = env.get_template("vcompress-LUT.cpp.j2")
template_file = env.get_template("mipp_LUT.cpp.j2")


def generate_lut(entries, simdwidth, words_per_simd):
    lut = [[0 for j in range(0, simdwidth)] for i in range(0, entries)]

    elem_bytes = simdwidth // words_per_simd
    
    for i in range(0, entries):
        mask = i
        j = 0
        
        for k in range(0, words_per_simd):
            for b in range(0, elem_bytes):
                lut[i][j + b] = k * elem_bytes + b
                
            if mask & 1 == 1:
                j += elem_bytes
            mask >>= 1

        for k in range(j, simdwidth):
            lut[i][k] = -1
            
    return lut

def generate_luts(filename, simdname, simdwidth, entrydef, lut_params_list):

    (entrytype, entrybytes) = entrydef
    
    all_luts = []
    for entries, simd_words in lut_params_list:

        elem_bits = (simdwidth // simd_words) * entrybytes * 8
        
        lut = template_lut.render(
            lutname = f"vcompress_LUT{elem_bits}x{simd_words}_{simdname}",
            entries = entries,
            simdwidth = simdwidth,
	    entrytype = entrytype,
            lut = generate_lut(entries, simdwidth, simd_words)
        )

        all_luts += [lut]

    all_content = template_file.render(
        luts = all_luts,
    )
        
    with open(filename, 'w+') as file:
        file.write(all_content)
        
        

def generate_AVX_luts(filename, simdname):
    
    
    pass
	
generate_luts("src/mipp_SSE_LUT.cpp",  "SSE",  16, ("int8_t", 1),  [(4, 2), (16, 4), (256, 8), (65536, 16)])
generate_luts("src/mipp_NEON_LUT.cpp", "NEON", 16, ("int8_t", 1),  [(4, 2), (16, 4), (256, 8), (65536, 16)])

generate_luts("src/mipp_AVX_LUT.cpp",  "AVX",  8, ("int32_t", 4), [(256, 8)])
