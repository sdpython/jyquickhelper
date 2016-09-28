

.. blogpost::
    :title: Issue with raphael.js in a notebook.
    :keywords: 
    :date: 2016-09-28
    :categories: javascript, notebook
    
    I spent a couple of hours to understand why I could not 
    use `morris.js <http://morrisjs.github.io/morris.js/>`_ in a notebook
    which was recommended as one of the most simple javascript libraries to use.
    I ran into issues because it depends on 
    `raphael.js <http://dmitrybaranovskiy.github.io/raphael/>`_ which also
    depends on `evejs <http://evejs.com/>`_.
    I discovered that if I did not solve that issue myself, I was
    was able to use `raphael.js <http://dmitrybaranovskiy.github.io/raphael/>`_
    in a notebook without noticing it 
    (see `treant-js <http://www.xavierdupre.fr/app/jupytalk/helpsphinx/notebooks/jsonly_treant.html#jsonlytreantrst>`_).
    You will find to do so in
    :ref:`notebookgraphjsrst`.
