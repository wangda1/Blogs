---
title: java
date: 2019-12-10 10:06:42
categories:
- Java
tags:
- Java
---

# java.util package

## 查找数据结构

使用Hash的`HashTable`、`HashMap`都具有很高效的查找效率

- `java.util.HashMap`
- `java.util.HashTable`

```java
HashTable<String, Double> class_prob = new HashTable<String, Double>();
HashTable<Map<String, Double>, Double> class_term_prob = new HashTable<Map<String, Double>, Double>();
class_prob.put(classname, Double.valueOf(args[1])/file_total);
prob = class_prob.getOrDefault(classname, defaultValue: 0.0);

Map<String,String> map = new HashMap<String, String>();
map.put(classname,term);
class_term_prob.put(map, (count+1)/(class_term_total.get(classname)+class_term_num.get(classname)));
```

- `java.util.Map`

```java
for(String word:words){
    Map<String,String> map = new HashMap<String, String>();
    map.put(classname, word);
    result += Math.log(class_term_prob.getOrDefault(map,1.0/(class_term_total.get(classname)+class_term_num.get(classname))));
}
```