#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
print(pd.__version__)


# In[2]:


import pandas as pd
import numpy as np
a1=np.array([10,42,63,49,25])
s1=pd.Series(a1)
print(s1)


# In[3]:


import pandas as pd
import numpy as np
a1=np.array([10,42,63,49,25])
s1=pd.Series(a1)
df = s1.to_frame().reset_index()
print(df)


# In[4]:


import seaborn as sns
print("Datasets available in seaborn:\n",sns.get_dataset_names())
mpg=sns.load_dataset('mpg')
print("*****Dataset mpg loaded:*****\n",mpg)


# In[5]:


import seaborn as sns
mpg=sns.load_dataset('mpg')
print(mpg['origin'].unique())


# In[7]:


import seaborn as sns
mpg=sns.load_dataset('mpg')
print(mpg[mpg['origin']=='usa'])


# In[ ]:




