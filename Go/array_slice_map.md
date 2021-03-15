---
title: Array Slice Map
date: 2021-03-11 20:01:00
categories:
- Go
tags:
- Go
---

# array slice and map

## array

1. 数组变量的类型包括数组长度和每个元素的类型。只有这两部分都相同的数组，才是类型相同的数组，才能相互赋值。赋值只是数组中的值是一样的，数组的地址并不发生变化

```go
	var array1 [5]string
	array2 := [5]string{"Red", "Blue", "Green", "Yellow", "Pink"}
	array1 = array2
	for index :=0; index < len(array2); index++ {
		fmt.Printf("Value1=%X, value2=%X\n", &array1[index], &array2[index])
	}

```

## slice

切片（Slice）是有3个字段的数据结构，3个字段：指向底层数组的指针，切片访问的元素的个数（长度）和切片允许增长到的元素个数（即容量）

### 切片的创建

1. `make` 和 切片字面量

- 使用 `make` 可以指定长度和容量创建切片
- 使用切片字面量初始化切片

```go

```

2. nil 和 空切片

- `nil` 切片

## map