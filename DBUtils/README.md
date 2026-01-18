# DB Utils

DataBricks Utils

- credentials: DatabricksCredentialUtils -> Utilities for interacting with credentials within notebooks
- data: DataUtils -> Utilities for understanding and interacting with datasets (EXPERIMENTAL)
- fs: DbfsUtils -> Manipulates the Databricks filesystem (DBFS) from the console
- jobs: JobsUtils -> Utilities for leveraging jobs features
- library: LibraryUtils -> Utilities for session isolated libraries
- meta: MetaUtils -> Methods to hook into the compiler (EXPERIMENTAL)
- notebook: NotebookUtils -> Utilities for the control flow of a notebook (EXPERIMENTAL)
- preview: Preview -> Utilities under preview category
- secrets: SecretUtils -> Provides utilities for leveraging secrets within notebooks
- widgets: WidgetsUtils -> Methods to create and get bound value of input widgets inside notebooks

### List Files
- Option 1 - python calls
```python
dbutils.fs.ls('/')
dbutils.fs.ls('dbfs:/databricks-datasets')
```
- Option 2 - magic commands

```shell
%fs ls /
%fs ls dbfs:/databricks-datasets
```
