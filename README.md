 # 1. Statement of the problem
 
 When studying phase transitions, it is very common to perform constant volume optimizations (CVOLOPTS) for those volumes where a soft phonon mode (negative frequency) was observed.
 
 In these type of runs, both the optimised volume and energy are desired to be extracted from these oputputs. 
 
 # 2. What is the `CVOLOPTS` program ? 
 
 `CVOLOPTS` is a program that extracts the the optimised energy and volume from a constant volume optimization (``CVOLOPT`` calculation) on [CRYSTAL](http://www.crystal.unito.it/index.php). 
 
 
 # 3. Files needed for running `CVOLOPTS`
 
 You don't need CRYSTAL to run `CVOLOPTS`, only the output files from a constant volume optimization calculation:
 
 ```
 OPTGEOM
 CVOLOPT
 END 
 ```
 The name of this output has to end as `*.out`

 # 4. Test

Under the `Test` folder, you will find 16 constant volume optimization outputs `*.out` for Calcite I.
If you run the program, you will obtain the following table:

![Data flow](https://github.com/DavidCdeB/CVOLOPTS/blob/master/Images_for_README_md/data.png)

 
