## Code Profiling

#### Time Consumption

Load the line profiler:
`%load_ext line_profiler`

Run the line profiler on 'convert_units' function
`%lprun -f convert_units convert_units(heroes, hts, wts)`

#### Memory Consumption

Load the memory profiler:
`%load_ext memory_profiler`

Run the memory profiler
`from bmi_lists import calc_bmi_lists`
`%mprun -f calc_bmi_lists calc_bmi_lists(sample_indices, hts, wts)`

