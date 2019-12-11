
# Stanford CoreNLP

**Not stanfordnlp!!**

1. `stanford-corenlp`的gitpage主页：https://stanfordnlp.github.io/CoreNLP/
2. `stanford-corenlp`的github仓库地址：https://github.com/stanfordnlp/CoreNLP
3. `stanford-corenlp`的软件组件介绍：https://nlp.stanford.edu/software/


我们从上述链接可以发现stanfordnlp的主要组成部分：`Core`、`Projects`、`Archive`
这些软件基本组合进`stanford-corenlp`，成为其组成部分，使用方法也比较多，大的区分为：
1. 直接使用对应组件的package，写java代码进行调用
2. 以`stanford-corenlp`服务的方式进行调用

- `Command line usage` 通过命令行使用
*[source](https://stanfordnlp.github.io/CoreNLP/cmdline.html)*

```dos
java -mx1g -cp "*" edu.stanford.nlp.naturalli.OpenIE    # 从标准输入获取输入，输出到标准输出
java -mx1g -cp "*" edu.stanford.nlp.naturalli.OpenIE  /path/to/file1  /path/to/file2    # 指定输入与输出路径
```

- `Stanford CoreNLP API` 通过`java programmatic API`
*[source](https://stanfordnlp.github.io/CoreNLP/api.html)*

>The backbone of the CoreNLP package is formed by two classes: Annotation and Annotator. Annotations are the data structure which hold the results of annotators. Annotations are basically maps, from keys to bits of the annotation, such as the parse, the part-of-speech tags, or named entity tags. Annotators are a lot like functions, except that they operate over Annotations instead of Objects. They do things like tokenize, parse, or NER tag sentences. Annotators and Annotations are integrated by AnnotationPipelines, which create sequences of generic Annotators. Stanford CoreNLP inherits from the AnnotationPipeline class, and is customized with NLP Annotators.
```java
import edu.stanford.nlp.pipeline.*;
import java.util.*;

public class BasicPipelineExample {

    public static void main(String[] args) {

        // creates a StanfordCoreNLP object, with POS tagging, lemmatization, NER, parsing, and coreference resolution
        Properties props = new Properties();
        props.setProperty("annotators", "tokenize, ssplit, pos, lemma, ner, parse, dcoref");
        StanfordCoreNLP pipeline = new StanfordCoreNLP(props);

        // read some text in the text variable
        String text = "...";

        // create an empty Annotation just with the given text
        Annotation document = new Annotation(text);

        // run all Annotators on this text
        pipeline.annotate(document);

    }

}
```

- `CoreNLP server` 通过web service运行`stanford-corenlp`（`python` or other）

*这种一般以服务的方式运行，通过其他语言的wrapper调用[source](https://stanfordnlp.github.io/CoreNLP/other-languages.html)*

启动
*[source](https://stanfordnlp.github.io/CoreNLP/corenlp-server.html)*
```shell
# Run the server using all jars in the current directory (e.g., the CoreNLP home directory)
java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000
```

```python
# python wrapper：https://github.com/Lynten/stanford-corenlp/blob/master/stanfordcorenlp/corenlp.py
# Simple usage
from stanfordcorenlp import StanfordCoreNLP

nlp = StanfordCoreNLP(r'G:\JavaLibraries\stanford-corenlp-full-2018-02-27')

sentence = 'Guangdong University of Foreign Studies is located in Guangzhou.'
print 'Tokenize:', nlp.word_tokenize(sentence)
print 'Part of Speech:', nlp.pos_tag(sentence)
print 'Named Entities:', nlp.ner(sentence)
print 'Constituency Parsing:', nlp.parse(sentence)
print 'Dependency Parsing:', nlp.dependency_parse(sentence)

nlp.close() # Do not forget to close! The backend server will consume a lot memery.
```

## 1. Stanford Named Entity Recognizer (NER)

参考：https://nlp.stanford.edu/software/CRF-NER.html

>Stanford NER is also known as CRFClassifier. The software provides a general implementation of (arbitrary order) linear chain Conditional Random Field (CRF) sequence models. That is, by training your own models on labeled data, you can actually use this code to build sequence models for NER or any other task. (CRF models were pioneered by [Lafferty, McCallum, and Pereira (2001)](http://www.cis.upenn.edu/~pereira/papers/crf.pdf); see [Sutton and McCallum (2006)](http://people.cs.umass.edu/~mccallum/papers/crf-tutorial.pdf) or [Sutton and McCallum (2010)](http://arxiv.org/pdf/1011.4088v1) for more comprehensible introductions.)

## 2. Stanford OpenIE

参考：https://nlp.stanford.edu/software/openie.html

```java
//https://github.com/stanfordnlp/CoreNLP/blob/master/src/edu/stanford/nlp/naturalli/OpenIEDemo.java
public static void main(String[] args) throws Exception {
    // Create the Stanford CoreNLP pipeline
    Properties props = PropertiesUtils.asProperties(
            "annotators", "tokenize,ssplit,pos,lemma,depparse,natlog,openie"
    );
    StanfordCoreNLP pipeline = new StanfordCoreNLP(props);

    // Annotate an example document.
    String text;
    if (args.length > 0) {
      text = IOUtils.slurpFile(args[0]);
    } else {
      text = "Obama was born in Hawaii. He is our president.";
    }
    Annotation doc = new Annotation(text);
    pipeline.annotate(doc);
```


## 学习参考

- Python中使用Stanford CoreNLP：https://blog.csdn.net/qq_35203425/article/details/80451243