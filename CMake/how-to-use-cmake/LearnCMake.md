```cmake
cmake_minimum_required(VERSION 3.14)
project(My_project VERSION 1.1.0)
```
# Set variables
- By default, anything is a string
```cmake
set(MY_VARIABLE "This is a variable.")
```

# Print message
```cmake
message(STATUS ${MY_VARIABLE})
set(My_bool "This is a string")
```
# Control flow
```cmake
if(NOT ${My_bool})
    message(STATUS "This is true case")
elseif()
else()
    message(STATUS "This is false case")
endif()
```

# for and while loop
```cmake
foreach(idx RANGE 100)
    
endforeach()

while(my_value LESS 50)

endwhile()
```
# STREQUAL
```cmake
include_directories()
```

# Adding targets & subdirectories

```cmake
add_executable()
add_library()
add_subdirectory()
```


# Cmake internal variables
```cmake
message(STATUS "This is cmake module path: " ${CMAKE_MODULE_PATH})
message(STATUS ${CMAKE_CURRENT_SOURCE_DIR})
message(STATUS "proj is " ${PROJECT_NAME})
message(STATUS "proj name is " ${PROJECT_VERSION})
```

# Adding include directories
> To use additional headers located in separate directories
> include xxx for all targets
```cmake
include_directories()
```

# include xxx only for the specificed target
```cmake
target_include_directories()
```

# Add pre-processors
```cmake
add_definitions()
```

# Set target properties
```cmake
set_target_properties()
```

# Linking libraries
```cmake
target_link_libraries()
```

- Option
`option()`

- File simliar to io to operate file
```cmake
file(WRITE xxx.txt "this is a test to write\n")
file(APPEND xxx/xxx.txt "This is a test to append")
file(READ <filename> <variable>)
``` 

- String: manipulate the string 
`string()`

- math command that performs arithmetic
`math(EXPR My_sum "1+1")`


- List: manipulate the lists
`list()`

## Functions 
> functions run in differ scope with parent function
```cmake
function(doubleIt VALUE)
    math(EXPR RESULT "${VALUE} * 2")
    set(VALUE RESULT PARENT_SCOPE)
endfunction()
```
- an arbitary number of arguments
```cmake
function(doubleEach)
    foreach(ARG ${ARGN})
        math(EXPR N "${ARG} * 2")
        message(STATUS "${N})
    endforeach()
endfunction()
```
## macro/endmacro
> macro set all variables in the caller's scope
```cmake
macro(doubleIt VALUE)
    math(EXPR RESULT "${VALUE} * 2")
endmacro()
```
## Run options
- -P option runs the given script, but doesn't generate a build pipeline
`cmake -P hello.txt`

- -D option defines the variable
`cmake -DNAME=xxxx -P hello.txt`

## Including Other Scripts
> cmake variables are defined at file scope. 
`include`command executes another CMake script. Use the variable `CMAKE_MODULE_PATH` as a search path.

> `add_subdirectory`command creates a new scope. Use it to add another CMake-based subproject, such as a library or executable, to the calling project. 
> None of the variables defined in the subproject's script will pollute the parent's scope.

## add_custom_command 
> 可在目标编译链接之前/编译链接之后执行 command
```cmake
add_custom_command(TARGET test_elf PRE_LINK
COMMAND
cp ${CMAKE_BINARY_DIR}/cfg/start.o ${CMAKE_BINARY_DIR}/. && 
cp ${CMAKE_SOURCE_DIR}/target/imx6_gcc/imx6.ld ${CMAKE_BINARY_DIR}/.
)

COMMAND ${CMAKE_COMMAND} -E copy_if_different xxx_src xxx_dst
```
## Tips:
- The difference of `include` and `include_directories()`: include to include 

ref: https://preshing.com/20170522/learn-cmakes-scripting-language-in-15-minutes/

https://cmake.org/cmake-tutorial/

https://www.jianshu.com/p/aaa19816f7ad