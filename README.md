# Delta Lake Data Bricks

- Sign Up with your Google 
- [My Databricks](https://dbc-c59e6aef-de8a.cloud.databricks.com/?o=7474649364858640)


## Quick Start 

- New -> Notebook

```python
spark
```

![img.png](img.png)

```python
df = spark.createDataFrame(
    [{"Google": "Colab", "Spark": "Scala"}, {"Google": "Dataproc", "Spark": "Python"}]
)
df.show()

```

![img_1.png](img_1.png)