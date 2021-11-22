AIMMS spelling wordlist
================================

A spelling_wordlist.txt file is shipped with the sphinx-aimms-theme, and can be used when running a spell checker.

Importing the spelling wordlist in the conf.py
-

To use this file, you may add the following line to your conf.py file:

``` python
# Getting the spelling word list from the sphinx-aimms-theme
spelling_word_list_filename = os.path.join(os.path.dirname(sphinx_aimms_theme.__file__),"spelling_wordlist.txt")

```

Calling the spellchecker on your docs
-

To call the spellchecker, instead of `make html` you may run `make spelling` or
```
python3 -msphinx -b spelling . _build/spelling
```
Please refer to [sphinxcontrib-spelling extension documentation](https://sphinxcontrib-spelling.readthedocs.io/en/latest/)

Note about adding several wordlist files
-

``` python
# Getting the spelling word list from the sphinx-aimms-theme and adding a personal file. Those 2 files will be merged.
spelling_word_list_filename = ["my_wordlist_file.txt",os.path.join(os.path.dirname(sphinx_aimms_theme.__file__),"spelling_wordlist.txt")]

```
